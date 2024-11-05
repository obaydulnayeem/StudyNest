from django.shortcuts import render, redirect
from .models import *
from apps.account.models.profile_models import Profile
from apps.account.models.education_models import *
from apps.admin_panel.models import *
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from django.db.models import Q
from collections import Counter
from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from apps.notifications.models import Notification
from .templatetags.semester_year_filters import semester_converter
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Department
from utils.permissions import *


def show_all_universities(request):
    university_type_id = request.GET.get('type')
    search_query = request.GET.get('search', '')  # Get the search query
    
    universities = University.objects.all().order_by('name')
    
    total_universities = universities.count()
    
    if university_type_id:
        universities = universities.filter(university_type_id=university_type_id)
    
    if search_query:
        universities = universities.filter(
            Q(name__icontains=search_query) |
            Q(acronym__icontains=search_query)
            )  # Filter by search query
    
    university_types = UniversityType.objects.all()
    
    num_public_general = University.objects.filter(university_type=1).count()
    num_public_autonomous = University.objects.filter(university_type=3).count()
    num_science_and_technology = University.objects.filter(university_type=4).count()
    num_engineering = University.objects.filter(university_type=5).count()
    num_agricultural = University.objects.filter(university_type=6).count()
    num_specialized = University.objects.filter(university_type=7).count()
    num_off_campus = University.objects.filter(university_type=8).count()
    num_affiliate_institutes = University.objects.filter(university_type=9).count()
    num_specialized_textile = University.objects.filter(university_type=10).count()
    num_private_general = University.objects.filter(university_type=11).count()
    num_private_science_and_technology = University.objects.filter(university_type=12).count()
    num_private_specialized = University.objects.filter(university_type=13).count()
    num_international = University.objects.filter(university_type=14).count()
    num_proposed = University.objects.filter(university_type=15).count()
    
    # total_public_general = University.objects.filter(university_type=).count()
    
    return render(request, 'university/show_all_universities.html', {
        'universities': universities,
        'university_types': university_types,
        'selected_university_type': university_type_id,
        'search_query': search_query, # Pass the search query back to the template
        
        'num_public_general': num_public_general,
        'num_public_autonomous': num_public_autonomous,
        'num_science_and_technology': num_science_and_technology,
        'num_engineering': num_engineering,
        'num_agricultural': num_agricultural,
        'num_specialized': num_specialized,
        'num_off_campus': num_off_campus,
        'num_affiliate_institutes': num_affiliate_institutes,
        'num_specialized_textile': num_specialized_textile,
        'num_private_general': num_private_general,
        'num_private_science_and_technology': num_private_science_and_technology,
        'num_private_specialized': num_private_specialized,
        'num_international': num_international,
        'num_proposed': num_proposed,
        
        'total_universities': total_universities,
    })


def show_university(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    department = Department.objects.filter(university=university).first()
    
    faculty_id = request.GET.get('faculty')
    search_query = request.GET.get('search', '')

    if faculty_id:
        departments = Department.objects.filter(university=university, faculty_id=faculty_id).order_by('name')
    else:
        departments = Department.objects.filter(university=university).order_by('name')

    if search_query:
        departments = departments.filter(name__icontains=search_query)
        
    department_with_all_info = departments.annotate(
        # Add your annotations here if needed
    )
    
    

    faculties = Faculty.objects.filter(university=university).order_by('name')
    schools = School.objects.filter(university=university).order_by('name')
    institutes = Institute.objects.filter(university=university).order_by('name')
    centers = Center.objects.filter(university=university).order_by('name')
    departments = Department.objects.filter(university=university).order_by('name')
    disciplines = Discipline.objects.filter(university=university).order_by('name')
    
    
    total_faculties = faculties.count()
    total_institutes = institutes.count()
    total_schools = School.objects.filter(university=university).count()
    total_centers = Center.objects.filter(university=university).count()    
    total_departments = Department.objects.filter(university=university).count()
    total_disciplines = Discipline.objects.filter(university=university).count()
    
    
    total_resources = (
        ResourcesQuestion.objects.filter(university=university).count() +
        ResourcesBook.objects.filter(university=university).count() +
        ResourcesNote.objects.filter(university=university).count() +
        ResourcesLecture.objects.filter(university=university).count()
    )

    bu = University.objects.get(name='University of Barishal')
    cse_bu = Department.objects.get(university=bu, name='Department of Computer Science and Engineering')

    questions_cse_bu = ResourcesQuestion.objects.filter(department=cse_bu).count()
    books_cse_bu = ResourcesBook.objects.filter(department=cse_bu).count()
    notes_cse_bu = ResourcesNote.objects.filter(department=cse_bu).count()
    lectures_cse_bu = ResourcesLecture.objects.filter(department=cse_bu).count()
    
    total_cse_bu = questions_cse_bu + books_cse_bu + notes_cse_bu + lectures_cse_bu

    university_moderator = Profile.objects.filter(
    Q(edu_university__university=university) &
    Q(moderator_type='University Moderator') &
    Q(moderator_info__is_running=True)
)
    
    # Annotate with duration (time since approved_final_at)
    university_moderator = university_moderator.annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    
    # departmental_moderator = Profile.objects.filter(edu_university__department = department, moderator_type = 'Departmental Moderator')
    departmental_moderator = Profile.objects.filter(
    edu_university__department=department,
    moderator_type='Departmental Moderator'
)
    

    context = {
        'university': university,
        'department_with_all_info': department_with_all_info,
        'faculties': faculties,
        'schools': schools,
        'centers': centers,
        'institutes': institutes,
        'departments': departments,
        'disciplines': disciplines,
        'selected_faculty': int(faculty_id) if faculty_id else None,
        'search_query': search_query,
        
        'total_faculties': total_faculties,
        'total_institutes': total_institutes,
        'total_schools': total_schools,
        'total_centers': total_centers,
        'total_departments': total_departments,
        'total_disciplines': total_disciplines,
        'total_resources': total_resources,
        
        'bu': bu,
        'cse_bu': cse_bu,
        'questions_cse_bu': questions_cse_bu,
        'books_cse_bu': books_cse_bu,
        'notes_cse_bu': notes_cse_bu,
        'lectures_cse_bu': lectures_cse_bu,
        'total_cse_bu': total_cse_bu,
        
        'university_moderator': university_moderator,
        'departmental_moderator': departmental_moderator,
    }
    return render(request, 'university/show_university.html', context)


def show_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    university = faculty.university
    
    departments = Department.objects.filter(faculty=faculty).order_by('name')
    disciplines = Discipline.objects.filter(faculty=faculty).order_by('name')
    institutes = Institute.objects.filter(faculty=faculty).order_by('name')
    
    context = {
        'university': university,
        'faculty': faculty,
        'departments': departments,
        'disciplines': disciplines,
        'institutes': institutes,
    }
    
    return render(request, 'university/show_faculty.html', context)



def show_institute(request, institute_id):
    institute = get_object_or_404(Institute, pk=institute_id)
    university = institute.university
    
    departments = Department.objects.filter(institute=institute).order_by('name')
    # institutes = Institute.objects.filter(institute=institute).order_by('name')
    
    # department_system = department.system
    
    courses = institute.course_set.all()
    # print(department_system)
    total_semester_or_year = institute.total_semester_or_year
    
    #  Handle the case where total_semester_or_year is None
    if total_semester_or_year is None:
        total_semester_or_year = 8  # or any other default value that makes sense in your context
    
    
    bu = University.objects.get(name='University of Barishal')
    cse_bu = Department.objects.get(university=bu, name='Department of Computer Science and Engineering')

    questions_cse_bu = ResourcesQuestion.objects.filter(department=cse_bu).count()
    books_cse_bu = ResourcesBook.objects.filter(department=cse_bu).count()
    notes_cse_bu = ResourcesNote.objects.filter(department=cse_bu).count()
    lectures_cse_bu = ResourcesLecture.objects.filter(department=cse_bu).count()
    
    total_cse_bu = questions_cse_bu + books_cse_bu + notes_cse_bu + lectures_cse_bu 

    university_moderator = Profile.objects.filter(
    Q(edu_university__university=university) &
    Q(moderator_type='University Moderator') &
    Q(moderator_info__is_running=True)
)
    
    # Annotate with duration (time since approved_final_at)
    university_moderator = university_moderator.annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )


#     departmental_moderator = Profile.objects.filter(
#     Q(edu_university__department=department) &
#     Q(moderator_type='Departmental Moderator') &
#     Q(moderator_info__is_running=True)
# )
    
    # departmental_moderator = departmental_moderator.annotate(
    #     duration_departmental_moderator=ExpressionWrapper(
    #         now() - F('moderator_info__approved_final_at'),
    #         output_field=DurationField()
    #     )
    # )
    
#     batch_moderator = Profile.objects.filter(
#     Q(edu_university__department=department) &
#     Q(moderator_type='Batch Moderator') &
#     Q(moderator_info__is_running=True)
# )
    
    # batch_moderator = batch_moderator.annotate(
    #     duration_batch_moderator=ExpressionWrapper(
    #         now() - F('moderator_info__approved_final_at'),
    #         output_field=DurationField()
    #     )
    # )
    
    
    # discipline_id = None

    # # Assuming department_id is passed in the URL, for example: /department/1/
    # if 'department_id' in request.resolver_match.kwargs:
    #     department_id = request.resolver_match.kwargs['department_id']

    # TOTAL COURSES - SEMESTER WISE==========================
    courses_sem1 = Course.objects.filter(institute = institute_id, semester='1st').count()
    
    courses_sem2 = Course.objects.filter(institute = institute_id, semester='2nd').count()
    
    courses_sem3 = Course.objects.filter(institute = institute_id, semester='3rd').count()
    
    courses_sem4 = Course.objects.filter(institute = institute_id, semester='4th').count()
    
    courses_sem5 = Course.objects.filter(institute = institute_id, semester='5th').count()
    
    courses_sem6 = Course.objects.filter(institute = institute_id, semester='6th').count()
    
    courses_sem7 = Course.objects.filter(institute = institute_id, semester='7th').count()
    
    courses_sem8 = Course.objects.filter(institute = institute_id, semester='8th').count()
    
    total_courses_s = Course.objects.filter(institute = institute_id).count()
    
    # TOTAL CREDITS SEMESTER WISE===============================
    credits_sem1 = Course.objects.filter(institute = institute_id, semester='1st').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem2 = Course.objects.filter(institute = institute_id, semester='2nd').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem3 = Course.objects.filter(institute = institute_id, semester='3rd').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem4 = Course.objects.filter(institute = institute_id, semester='4th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem5 = Course.objects.filter(institute = institute_id, semester='5th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem6 = Course.objects.filter(institute = institute_id, semester='6th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem7 = Course.objects.filter(institute = institute_id, semester='7th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem8 = Course.objects.filter(institute = institute_id, semester='8th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0

    total_credits_s = credits_sem1 + credits_sem2 + credits_sem3 + credits_sem4 + credits_sem5 + credits_sem6 + credits_sem7 + credits_sem8
   
   
    # TOTAL HOURS SEMESTER WISE===============================
    hours_sem1 = Course.objects.filter(institute = institute_id, semester='1st').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem2 = Course.objects.filter(institute = institute_id, semester='2nd').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem3 = Course.objects.filter(institute = institute_id, semester='3rd').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem4 = Course.objects.filter(institute = institute_id, semester='4th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem5 = Course.objects.filter(institute = institute_id, semester='5th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem6 = Course.objects.filter(institute = institute_id, semester='6th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem7 = Course.objects.filter(institute = institute_id, semester='7th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem8 = Course.objects.filter(institute = institute_id, semester='8th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    total_hours_s = hours_sem1 + hours_sem2 + hours_sem3 + hours_sem4 + hours_sem5 + hours_sem6 + hours_sem7 + hours_sem8
    
    # TOTAL RESOURCES SEMESTER WISE===============================
    total_resources_sem1 = ResourcesQuestion.objects.filter(institute = institute_id, semester='1st').count() + ResourcesBook.objects.filter(institute = institute_id, semester='1st').count() + ResourcesLecture.objects.filter(institute = institute_id, semester='1st').count() + ResourcesNote.objects.filter(institute = institute_id, semester='1st').count()
    
    total_resources_sem2 = ResourcesQuestion.objects.filter(institute = institute_id, semester='2nd').count() + ResourcesBook.objects.filter(institute = institute_id, semester='2nd').count() + ResourcesLecture.objects.filter(institute = institute_id, semester='2nd').count() + ResourcesNote.objects.filter(institute = institute_id, semester='2nd').count()
    
    total_resources_sem3 = ResourcesQuestion.objects.filter(institute = institute_id, semester='3rd').count() + ResourcesBook.objects.filter(institute = institute_id, semester='3rd').count() + ResourcesLecture.objects.filter(institute = institute_id, semester='3rd').count() + ResourcesNote.objects.filter(institute = institute_id, semester='3rd').count()
    
    total_resources_sem4 = ResourcesQuestion.objects.filter(institute = institute_id, semester='4th').count() + ResourcesBook.objects.filter(institute = institute_id, semester='4th').count() + ResourcesLecture.objects.filter(institute = institute_id, semester='4th').count() + ResourcesNote.objects.filter(institute = institute_id, semester='4th').count()
    
    total_resources_sem5 = ResourcesQuestion.objects.filter(institute = institute_id, semester='5th').count() + ResourcesBook.objects.filter(institute = institute_id, semester='5th').count() + ResourcesLecture.objects.filter(institute = institute_id, semester='5th').count() + ResourcesNote.objects.filter(institute = institute_id, semester='5th').count()
    
    total_resources_sem6 = ResourcesQuestion.objects.filter(institute = institute_id, semester=6).count() + ResourcesBook.objects.filter(institute = institute_id, semester=6).count() + ResourcesLecture.objects.filter(institute = institute_id, semester=6).count() + ResourcesNote.objects.filter(institute = institute_id, semester=6).count()
    
    total_resources_sem7 = ResourcesQuestion.objects.filter(institute = institute_id, semester=7).count() + ResourcesBook.objects.filter(institute = institute_id, semester=7).count() + ResourcesLecture.objects.filter(institute = institute_id, semester=7).count() + ResourcesNote.objects.filter(institute = institute_id, semester=7).count()
    
    total_resources_sem8 = ResourcesQuestion.objects.filter(institute = institute_id, semester=8).count() + ResourcesBook.objects.filter(institute = institute_id, semester=8).count() + ResourcesLecture.objects.filter(institute = institute_id, semester=8).count() + ResourcesNote.objects.filter(institute = institute_id, semester=8).count()
    
    total_resources_all_sem = total_resources_sem1 + total_resources_sem2 + total_resources_sem3 + total_resources_sem4 + total_resources_sem5 + total_resources_sem6 + total_resources_sem7 + total_resources_sem8
    
    context = {
        'university': university,
        'departments': departments,
        'institute': institute,
        'courses': courses,
        'total_semester_or_year': range(1, total_semester_or_year + 1),
        # 'total_semester_or_year': total_semester_or_year,
        
        'bu': bu,
        'cse_bu': cse_bu,
        'questions_cse_bu': questions_cse_bu,
        'books_cse_bu': books_cse_bu,
        'notes_cse_bu': notes_cse_bu,
        'lectures_cse_bu': lectures_cse_bu,
        'total_cse_bu': total_cse_bu,
        'university_moderator': university_moderator,
        # 'departmental_moderator': departmental_moderator,
        # 'batch_moderator': batch_moderator,
        
        
        'total_courses_s': total_courses_s,

        'courses_sem1': courses_sem1,
        'courses_sem2': courses_sem2,
        'courses_sem3': courses_sem3,
        'courses_sem4': courses_sem4,
        'courses_sem5': courses_sem5,
        'courses_sem6': courses_sem6,
        'courses_sem7': courses_sem7,
        'courses_sem8': courses_sem8,
        
        'credits_sem1': credits_sem1,
        'credits_sem2': credits_sem2,
        'credits_sem3': credits_sem3,
        'credits_sem4': credits_sem4,
        'credits_sem5': credits_sem5,
        'credits_sem6': credits_sem6,
        'credits_sem7': credits_sem7,
        'credits_sem8': credits_sem8,
        
        'hours_sem1': hours_sem1,
        'hours_sem2': hours_sem2,
        'hours_sem3': hours_sem3,
        'hours_sem4': hours_sem4,
        'hours_sem5': hours_sem5,
        'hours_sem6': hours_sem6,
        'hours_sem7': hours_sem7,
        'hours_sem8': hours_sem8,
        
        'total_credits_s': total_credits_s,
        'total_hours_s': total_hours_s,
        
        'total_resources_sem1': total_resources_sem1,
        'total_resources_sem2': total_resources_sem2,
        'total_resources_sem3': total_resources_sem3,
        'total_resources_sem4': total_resources_sem4,
        'total_resources_sem5': total_resources_sem5,
        'total_resources_sem6': total_resources_sem6,
        'total_resources_sem7': total_resources_sem7,
        'total_resources_sem8': total_resources_sem8,
        'total_resources_all_sem': total_resources_all_sem,
    }
    
    return render(request, 'university/show_institute.html', context)


def show_school(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    university = school.university
    
    departments = Department.objects.filter(school=school).order_by('name')
    disciplines = Discipline.objects.filter(school=school).order_by('name')
    # institutes = Institute.objects.filter(institute=institute).order_by('name')
    
    context = {
        'university': university,
        'school': school,
        # 'schools': schools,
        # 'institute': institute,
        'departments': departments,
        'disciplines': disciplines,
    }
    
    return render(request, 'university/show_school.html', context)


def show_center(request, center_id):
    center = get_object_or_404(Center, pk=center_id)
    university = center.university
    
    departments = Department.objects.filter(center=center).order_by('name')
    disciplines = Discipline.objects.filter(center=center).order_by('name')
    # institutes = Institute.objects.filter(institute=institute).order_by('name')
    
    context = {
        'university': university,
        'center': center,
        # 'schools': schools,
        # 'institute': institute,
        'departments': departments,
        'disciplines': disciplines,
    }
    
    return render(request, 'university/show_center.html', context)


def show_department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    university = department.university
    
    # department_system = department.system
    
    courses = department.course_set.all()
    # print(department_system)
    total_semester_or_year = department.total_semester_or_year
    
    #  Handle the case where total_semester_or_year is None
    if total_semester_or_year is None:
        total_semester_or_year = 8  # or any other default value that makes sense in your context
    
    
    bu = University.objects.get(name='University of Barishal')
    cse_bu = Department.objects.get(university=bu, name='Department of Computer Science and Engineering')

    questions_cse_bu = ResourcesQuestion.objects.filter(department=cse_bu).count()
    books_cse_bu = ResourcesBook.objects.filter(department=cse_bu).count()
    notes_cse_bu = ResourcesNote.objects.filter(department=cse_bu).count()
    lectures_cse_bu = ResourcesLecture.objects.filter(department=cse_bu).count()
    
    total_cse_bu = questions_cse_bu + books_cse_bu + notes_cse_bu + lectures_cse_bu 

    university_moderator = Profile.objects.filter(
    Q(edu_university__university=university) &
    Q(moderator_type='University Moderator') &
    Q(moderator_info__is_running=True)
)
    
    # Annotate with duration (time since approved_final_at)
    university_moderator = university_moderator.annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )


    departmental_moderator = Profile.objects.filter(
    Q(edu_university__department=department) &
    Q(moderator_type='Departmental Moderator') &
    Q(moderator_info__is_running=True)
)
    
    departmental_moderator = departmental_moderator.annotate(
        duration_departmental_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    batch_moderator = Profile.objects.filter(
    Q(edu_university__department=department) &
    Q(moderator_type='Batch Moderator') &
    Q(moderator_info__is_running=True)
)
    
    batch_moderator = batch_moderator.annotate(
        duration_batch_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    
    department_id = None

    # Assuming department_id is passed in the URL, for example: /department/1/
    if 'department_id' in request.resolver_match.kwargs:
        department_id = request.resolver_match.kwargs['department_id']

    # TOTAL COURSES - SEMESTER WISE==========================
    courses_sem1 = Course.objects.filter(department = department_id, semester='1st').count()
    
    courses_sem2 = Course.objects.filter(department = department_id, semester='2nd').count()
    
    courses_sem3 = Course.objects.filter(department = department_id, semester='3rd').count()
    
    courses_sem4 = Course.objects.filter(department = department_id, semester='4th').count()
    
    courses_sem5 = Course.objects.filter(department = department_id, semester='5th').count()
    
    courses_sem6 = Course.objects.filter(department = department_id, semester='6th').count()
    
    courses_sem7 = Course.objects.filter(department = department_id, semester='7th').count()
    
    courses_sem8 = Course.objects.filter(department = department_id, semester='8th').count()
    
    total_courses_s = Course.objects.filter(department = department_id).count()
    
    # TOTAL CREDITS SEMESTER WISE===============================
    credits_sem1 = Course.objects.filter(department = department_id, semester='1st').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem2 = Course.objects.filter(department = department_id, semester='2nd').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem3 = Course.objects.filter(department = department_id, semester='3rd').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem4 = Course.objects.filter(department = department_id, semester='4th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem5 = Course.objects.filter(department = department_id, semester='5th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem6 = Course.objects.filter(department = department_id, semester='6th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem7 = Course.objects.filter(department = department_id, semester='7th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem8 = Course.objects.filter(department = department_id, semester='8th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0

    total_credits_s = credits_sem1 + credits_sem2 + credits_sem3 + credits_sem4 + credits_sem5 + credits_sem6 + credits_sem7 + credits_sem8
   
   
    # TOTAL HOURS SEMESTER WISE===============================
    hours_sem1 = Course.objects.filter(department = department_id, semester='1st').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem2 = Course.objects.filter(department = department_id, semester='2nd').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem3 = Course.objects.filter(department = department_id, semester='3rd').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem4 = Course.objects.filter(department = department_id, semester='4th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem5 = Course.objects.filter(department = department_id, semester='5th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem6 = Course.objects.filter(department = department_id, semester='6th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem7 = Course.objects.filter(department = department_id, semester='7th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem8 = Course.objects.filter(department = department_id, semester='8th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    total_hours_s = hours_sem1 + hours_sem2 + hours_sem3 + hours_sem4 + hours_sem5 + hours_sem6 + hours_sem7 + hours_sem8
    
    # TOTAL RESOURCES SEMESTER WISE===============================
    total_resources_sem1 = ResourcesQuestion.objects.filter(department = department_id, semester='1st').count() + ResourcesBook.objects.filter(department = department_id, semester='1st').count() + ResourcesLecture.objects.filter(department = department_id, semester='1st').count() + ResourcesNote.objects.filter(department = department_id, semester='1st').count()
    
    total_resources_sem2 = ResourcesQuestion.objects.filter(department = department_id, semester='2nd').count() + ResourcesBook.objects.filter(department = department_id, semester='2nd').count() + ResourcesLecture.objects.filter(department = department_id, semester='2nd').count() + ResourcesNote.objects.filter(department = department_id, semester='2nd').count()
    
    total_resources_sem3 = ResourcesQuestion.objects.filter(department = department_id, semester='3rd').count() + ResourcesBook.objects.filter(department = department_id, semester='3rd').count() + ResourcesLecture.objects.filter(department = department_id, semester='3rd').count() + ResourcesNote.objects.filter(department = department_id, semester='3rd').count()
    
    total_resources_sem4 = ResourcesQuestion.objects.filter(department = department_id, semester='4th').count() + ResourcesBook.objects.filter(department = department_id, semester='4th').count() + ResourcesLecture.objects.filter(department = department_id, semester='4th').count() + ResourcesNote.objects.filter(department = department_id, semester='4th').count()
    
    total_resources_sem5 = ResourcesQuestion.objects.filter(department = department_id, semester='5th').count() + ResourcesBook.objects.filter(department = department_id, semester='5th').count() + ResourcesLecture.objects.filter(department = department_id, semester='5th').count() + ResourcesNote.objects.filter(department = department_id, semester='5th').count()
    
    total_resources_sem6 = ResourcesQuestion.objects.filter(department = department_id, semester='6th').count() + ResourcesBook.objects.filter(department = department_id, semester='6th').count() + ResourcesLecture.objects.filter(department = department_id, semester='6th').count() + ResourcesNote.objects.filter(department = department_id, semester='6th').count()
    
    total_resources_sem7 = ResourcesQuestion.objects.filter(department = department_id, semester='7th').count() + ResourcesBook.objects.filter(department = department_id, semester='7th').count() + ResourcesLecture.objects.filter(department = department_id, semester='7th').count() + ResourcesNote.objects.filter(department = department_id, semester='7th').count()
    
    total_resources_sem8 = ResourcesQuestion.objects.filter(department = department_id, semester='8th').count() + ResourcesBook.objects.filter(department = department_id, semester='8th').count() + ResourcesLecture.objects.filter(department = department_id, semester='8th').count() + ResourcesNote.objects.filter(department = department_id, semester='8th').count()
    
    total_resources_all_sem = total_resources_sem1 + total_resources_sem2 + total_resources_sem3 + total_resources_sem4 + total_resources_sem5 + total_resources_sem6 + total_resources_sem7 + total_resources_sem8
   
    
    for course in courses:
        common_courses = course.common_courses.all()
        # Reset counters for each common course
        common_question_count = 0
        common_note_count = 0
        common_book_count = 0
        common_lecture_count = 0
        
        for common_course in common_courses:
            common_question_count += ResourcesQuestion.objects.filter(common_courses=common_course).count()
            common_note_count += ResourcesNote.objects.filter(common_courses=common_course).count()
            common_book_count += ResourcesBook.objects.filter(common_courses=common_course).count()
            common_lecture_count += ResourcesLecture.objects.filter(common_courses=common_course).count()

        semester = course.semester
        # print('xxx:',semester)
        if semester == '1st':
            total_resources_sem1 += common_question_count + common_note_count + common_book_count + common_lecture_count
        elif semester == '2nd':
            total_resources_sem2 += common_question_count + common_note_count + common_book_count + common_lecture_count
        elif semester == '3rd':
            total_resources_sem3 += common_question_count + common_note_count + common_book_count + common_lecture_count
        elif semester == '4th':
            total_resources_sem4 += common_question_count + common_note_count + common_book_count + common_lecture_count
        elif semester == '5th':
            total_resources_sem5 += common_question_count + common_note_count + common_book_count + common_lecture_count
        elif semester == '6th':
            total_resources_sem6 += common_question_count + common_note_count + common_book_count + common_lecture_count
        elif semester == '7th':
            total_resources_sem7 += common_question_count + common_note_count + common_book_count + common_lecture_count
        elif semester == '8th':
            total_resources_sem8 += common_question_count + common_note_count + common_book_count + common_lecture_count

        # Combine with main course resources
        total_resources_all_sem += common_question_count + common_note_count + common_book_count + common_lecture_count
    
    context = {
        'university': university,
        'department': department,
        'courses': courses,
        'total_semester_or_year': range(1, total_semester_or_year + 1),
        # 'total_semester_or_year': total_semester_or_year,
        
        'bu': bu,
        'cse_bu': cse_bu,
        'questions_cse_bu': questions_cse_bu,
        'books_cse_bu': books_cse_bu,
        'notes_cse_bu': notes_cse_bu,
        'lectures_cse_bu': lectures_cse_bu,
        'total_cse_bu': total_cse_bu,
        'university_moderator': university_moderator,
        'departmental_moderator': departmental_moderator,
        'batch_moderator': batch_moderator,
        
        'total_courses_s': total_courses_s,

        'courses_sem1': courses_sem1,
        'courses_sem2': courses_sem2,
        'courses_sem3': courses_sem3,
        'courses_sem4': courses_sem4,
        'courses_sem5': courses_sem5,
        'courses_sem6': courses_sem6,
        'courses_sem7': courses_sem7,
        'courses_sem8': courses_sem8,
        
        'credits_sem1': credits_sem1,
        'credits_sem2': credits_sem2,
        'credits_sem3': credits_sem3,
        'credits_sem4': credits_sem4,
        'credits_sem5': credits_sem5,
        'credits_sem6': credits_sem6,
        'credits_sem7': credits_sem7,
        'credits_sem8': credits_sem8,
        
        'hours_sem1': hours_sem1,
        'hours_sem2': hours_sem2,
        'hours_sem3': hours_sem3,
        'hours_sem4': hours_sem4,
        'hours_sem5': hours_sem5,
        'hours_sem6': hours_sem6,
        'hours_sem7': hours_sem7,
        'hours_sem8': hours_sem8,
        
        'total_credits_s': total_credits_s,
        'total_hours_s': total_hours_s,
        
        'total_resources_sem1': total_resources_sem1,
        'total_resources_sem2': total_resources_sem2,
        'total_resources_sem3': total_resources_sem3,
        'total_resources_sem4': total_resources_sem4,
        'total_resources_sem5': total_resources_sem5,
        'total_resources_sem6': total_resources_sem6,
        'total_resources_sem7': total_resources_sem7,
        'total_resources_sem8': total_resources_sem8,
        'total_resources_all_sem': total_resources_all_sem,
    }
    
    return render(request, 'department/show_department.html', context)


def show_discipline(request, discipline_id):
    discipline = get_object_or_404(Discipline, pk=discipline_id)
    university = discipline.university
    
    # department_system = department.system
    
    courses = discipline.course_set.all()
    # print(department_system)
    total_semester_or_year = discipline.total_semester_or_year
    
    #  Handle the case where total_semester_or_year is None
    if total_semester_or_year is None:
        total_semester_or_year = 8  # or any other default value that makes sense in your context
    
    
    bu = University.objects.get(name='University of Barishal')
    cse_bu = Department.objects.get(university=bu, name='Department of Computer Science and Engineering')

    questions_cse_bu = ResourcesQuestion.objects.filter(department=cse_bu).count()
    books_cse_bu = ResourcesBook.objects.filter(department=cse_bu).count()
    notes_cse_bu = ResourcesNote.objects.filter(department=cse_bu).count()
    lectures_cse_bu = ResourcesLecture.objects.filter(department=cse_bu).count()
    
    total_cse_bu = questions_cse_bu + books_cse_bu + notes_cse_bu + lectures_cse_bu 

    university_moderator = Profile.objects.filter(
    Q(edu_university__university=university) &
    Q(moderator_type='University Moderator') &
    Q(moderator_info__is_running=True)
)
    
    # Annotate with duration (time since approved_final_at)
    university_moderator = university_moderator.annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )


#     departmental_moderator = Profile.objects.filter(
#     Q(edu_university__department=department) &
#     Q(moderator_type='Departmental Moderator') &
#     Q(moderator_info__is_running=True)
# )
    
    # departmental_moderator = departmental_moderator.annotate(
    #     duration_departmental_moderator=ExpressionWrapper(
    #         now() - F('moderator_info__approved_final_at'),
    #         output_field=DurationField()
    #     )
    # )
    
#     batch_moderator = Profile.objects.filter(
#     Q(edu_university__department=department) &
#     Q(moderator_type='Batch Moderator') &
#     Q(moderator_info__is_running=True)
# )
    
    # batch_moderator = batch_moderator.annotate(
    #     duration_batch_moderator=ExpressionWrapper(
    #         now() - F('moderator_info__approved_final_at'),
    #         output_field=DurationField()
    #     )
    # )
    
    
    # discipline_id = None

    # # Assuming department_id is passed in the URL, for example: /department/1/
    # if 'department_id' in request.resolver_match.kwargs:
    #     department_id = request.resolver_match.kwargs['department_id']

    # TOTAL COURSES - SEMESTER WISE==========================
    courses_sem1 = Course.objects.filter(discipline = discipline_id, semester='1st').count()
    
    courses_sem2 = Course.objects.filter(discipline = discipline_id, semester='2nd').count()
    
    courses_sem3 = Course.objects.filter(discipline = discipline_id, semester='3rd').count()
    
    courses_sem4 = Course.objects.filter(discipline = discipline_id, semester='4th').count()
    
    courses_sem5 = Course.objects.filter(discipline = discipline_id, semester='5th').count()
    
    courses_sem6 = Course.objects.filter(discipline = discipline_id, semester='6th').count()
    
    courses_sem7 = Course.objects.filter(discipline = discipline_id, semester='7th').count()
    
    courses_sem8 = Course.objects.filter(discipline = discipline_id, semester='8th').count()
    
    total_courses_s = Course.objects.filter(discipline = discipline_id).count()
    
    # TOTAL CREDITS SEMESTER WISE===============================
    credits_sem1 = Course.objects.filter(discipline = discipline_id, semester='1st').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem2 = Course.objects.filter(discipline = discipline_id, semester='2nd').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem3 = Course.objects.filter(discipline = discipline_id, semester='3rd').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem4 = Course.objects.filter(discipline = discipline_id, semester='4th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem5 = Course.objects.filter(discipline = discipline_id, semester='5th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem6 = Course.objects.filter(discipline = discipline_id, semester='6th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem7 = Course.objects.filter(discipline = discipline_id, semester='7th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
    credits_sem8 = Course.objects.filter(discipline = discipline_id, semester='8th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0

    total_credits_s = credits_sem1 + credits_sem2 + credits_sem3 + credits_sem4 + credits_sem5 + credits_sem6 + credits_sem7 + credits_sem8
   
   
    # TOTAL HOURS SEMESTER WISE===============================
    hours_sem1 = Course.objects.filter(discipline = discipline_id, semester='1st').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem2 = Course.objects.filter(discipline = discipline_id, semester='2nd').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem3 = Course.objects.filter(discipline = discipline_id, semester='3rd').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem4 = Course.objects.filter(discipline = discipline_id, semester='4th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem5 = Course.objects.filter(discipline = discipline_id, semester='5th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem6 = Course.objects.filter(discipline = discipline_id, semester='6th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem7 = Course.objects.filter(discipline = discipline_id, semester='7th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    hours_sem8 = Course.objects.filter(discipline = discipline_id, semester='8th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
    total_hours_s = hours_sem1 + hours_sem2 + hours_sem3 + hours_sem4 + hours_sem5 + hours_sem6 + hours_sem7 + hours_sem8
    
    # TOTAL RESOURCES SEMESTER WISE===============================
    total_resources_sem1 = ResourcesQuestion.objects.filter(discipline = discipline_id, semester='1st').count() + ResourcesBook.objects.filter(discipline = discipline_id, semester='1st').count() + ResourcesLecture.objects.filter(discipline = discipline_id, semester='1st').count() + ResourcesNote.objects.filter(discipline = discipline_id, semester='1st').count()
    
    total_resources_sem2 = ResourcesQuestion.objects.filter(discipline = discipline_id, semester='2nd').count() + ResourcesBook.objects.filter(discipline = discipline_id, semester='2nd').count() + ResourcesLecture.objects.filter(discipline = discipline_id, semester='2nd').count() + ResourcesNote.objects.filter(discipline = discipline_id, semester='2nd').count()
    
    total_resources_sem3 = ResourcesQuestion.objects.filter(discipline = discipline_id, semester='3rd').count() + ResourcesBook.objects.filter(discipline = discipline_id, semester='3rd').count() + ResourcesLecture.objects.filter(discipline = discipline_id, semester='3rd').count() + ResourcesNote.objects.filter(discipline = discipline_id, semester='3rd').count()
    
    total_resources_sem4 = ResourcesQuestion.objects.filter(discipline = discipline_id, semester='4th').count() + ResourcesBook.objects.filter(discipline = discipline_id, semester='4th').count() + ResourcesLecture.objects.filter(discipline = discipline_id, semester='4th').count() + ResourcesNote.objects.filter(discipline = discipline_id, semester='4th').count()
    
    total_resources_sem5 = ResourcesQuestion.objects.filter(discipline = discipline_id, semester='5th').count() + ResourcesBook.objects.filter(discipline = discipline_id, semester='5th').count() + ResourcesLecture.objects.filter(discipline = discipline_id, semester='5th').count() + ResourcesNote.objects.filter(discipline = discipline_id, semester='5th').count()
    
    total_resources_sem6 = ResourcesQuestion.objects.filter(discipline = discipline_id, semester=6).count() + ResourcesBook.objects.filter(discipline = discipline_id, semester=6).count() + ResourcesLecture.objects.filter(discipline = discipline_id, semester=6).count() + ResourcesNote.objects.filter(discipline = discipline_id, semester=6).count()
    
    total_resources_sem7 = ResourcesQuestion.objects.filter(discipline = discipline_id, semester=7).count() + ResourcesBook.objects.filter(discipline = discipline_id, semester=7).count() + ResourcesLecture.objects.filter(discipline = discipline_id, semester=7).count() + ResourcesNote.objects.filter(discipline = discipline_id, semester=7).count()
    
    total_resources_sem8 = ResourcesQuestion.objects.filter(discipline = discipline_id, semester=8).count() + ResourcesBook.objects.filter(discipline = discipline_id, semester=8).count() + ResourcesLecture.objects.filter(discipline = discipline_id, semester=8).count() + ResourcesNote.objects.filter(discipline = discipline_id, semester=8).count()
    
    total_resources_all_sem = total_resources_sem1 + total_resources_sem2 + total_resources_sem3 + total_resources_sem4 + total_resources_sem5 + total_resources_sem6 + total_resources_sem7 + total_resources_sem8
    
    
    context = {
        'university': university,
        # 'discipline': discipline,
        'discipline': discipline,
        'courses': courses,
        'total_semester_or_year': range(1, total_semester_or_year + 1),
        # 'total_semester_or_year': total_semester_or_year,
        
        'bu': bu,
        'cse_bu': cse_bu,
        'questions_cse_bu': questions_cse_bu,
        'books_cse_bu': books_cse_bu,
        'notes_cse_bu': notes_cse_bu,
        'lectures_cse_bu': lectures_cse_bu,
        'total_cse_bu': total_cse_bu,
        'university_moderator': university_moderator,
        # 'departmental_moderator': departmental_moderator,
        # 'batch_moderator': batch_moderator,
        
        
                'total_courses_s': total_courses_s,

        'courses_sem1': courses_sem1,
        'courses_sem2': courses_sem2,
        'courses_sem3': courses_sem3,
        'courses_sem4': courses_sem4,
        'courses_sem5': courses_sem5,
        'courses_sem6': courses_sem6,
        'courses_sem7': courses_sem7,
        'courses_sem8': courses_sem8,
        
        'credits_sem1': credits_sem1,
        'credits_sem2': credits_sem2,
        'credits_sem3': credits_sem3,
        'credits_sem4': credits_sem4,
        'credits_sem5': credits_sem5,
        'credits_sem6': credits_sem6,
        'credits_sem7': credits_sem7,
        'credits_sem8': credits_sem8,
        
        'hours_sem1': hours_sem1,
        'hours_sem2': hours_sem2,
        'hours_sem3': hours_sem3,
        'hours_sem4': hours_sem4,
        'hours_sem5': hours_sem5,
        'hours_sem6': hours_sem6,
        'hours_sem7': hours_sem7,
        'hours_sem8': hours_sem8,
        
        'total_credits_s': total_credits_s,
        'total_hours_s': total_hours_s,
        
        'total_resources_sem1': total_resources_sem1,
        'total_resources_sem2': total_resources_sem2,
        'total_resources_sem3': total_resources_sem3,
        'total_resources_sem4': total_resources_sem4,
        'total_resources_sem5': total_resources_sem5,
        'total_resources_sem6': total_resources_sem6,
        'total_resources_sem7': total_resources_sem7,
        'total_resources_sem8': total_resources_sem8,
        'total_resources_all_sem': total_resources_all_sem,
    }
    
    return render(request, 'university/show_discipline.html', context)


# def show_course(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     university = course.university
#     department = course.department
#     discipline = course.discipline
    
#     # total_resourses_course = question_count + note_count + book_count + lecture_count
    
#     # Retrieve the main course resources count
#     question_count = ResourcesQuestion.objects.filter(course=course).count()
#     note_count = ResourcesNote.objects.filter(course=course).count()
#     book_count = ResourcesBook.objects.filter(course=course).count()
#     lecture_count = ResourcesLecture.objects.filter(course=course).count()

#     # Retrieve common courses associated with the course
#     common_courses = course.common_courses.all()

#     # Initialize variables for common course resource counts
#     common_question_count = 0
#     common_note_count = 0
#     common_book_count = 0
#     common_lecture_count = 0

#     # Iterate over each common course and count resources
#     for common_course in common_courses:
#         common_question_count += ResourcesQuestion.objects.filter(common_courses=common_course).count()
#         common_note_count += ResourcesNote.objects.filter(common_courses=common_course).count()
#         common_book_count += ResourcesBook.objects.filter(common_courses=common_course).count()
#         common_lecture_count += ResourcesLecture.objects.filter(common_courses=common_course).count()

#     # Combine main course counts with common course counts
#     question_count = question_count + common_question_count
#     note_count = note_count + common_note_count
#     book_count = book_count + common_book_count
#     lecture_count = lecture_count + common_lecture_count

#     # Calculate total resources count (for both main and common courses)
#     total_resourses_course = question_count + note_count + book_count + lecture_count

#     syllabus = course.syllabus
    
#     university_moderator = Profile.objects.filter(
#     Q(edu_university__university=university) &
#     Q(moderator_type='University Moderator') &
#     Q(moderator_info__is_running=True)
# )
    
#     # Annotate with duration (time since approved_final_at)
#     university_moderator = university_moderator.annotate(
#         duration_university_moderator=ExpressionWrapper(
#             now() - F('moderator_info__approved_final_at'),
#             output_field=DurationField()
#         )
#     )
    
#     departmental_moderator = Profile.objects.filter(
#     Q(edu_university__department=department) &
#     Q(moderator_type='Departmental Moderator') &
#     Q(moderator_info__is_running=True)
# )
    
#     departmental_moderator = departmental_moderator.annotate(
#         duration_departmental_moderator=ExpressionWrapper(
#             now() - F('moderator_info__approved_final_at'),
#             output_field=DurationField()
#         )
#     )
    
#     batch_moderator = Profile.objects.filter(
#     Q(edu_university__department=department) &
#     Q(moderator_type='Batch Moderator') &
#     Q(moderator_info__is_running=True)
# )
    
#     batch_moderator = batch_moderator.annotate(
#         duration_batch_moderator=ExpressionWrapper(
#             now() - F('moderator_info__approved_final_at'),
#             output_field=DurationField()
#         )
#     )
    
    
#     # serializer = CourseModelSerializer(course)
#     # json_data = JSONRenderer().render(serializer.data)
    
#     # return HttpResponse(json_data, content_type='application/json')
    
    
#     bu = University.objects.get(name='University of Barishal')
#     cse_bu = Department.objects.get(university=bu, name='Department of Computer Science and Engineering')

#     questions_cse_bu = ResourcesQuestion.objects.filter(department=cse_bu).count()
#     books_cse_bu = ResourcesBook.objects.filter(department=cse_bu).count()
#     notes_cse_bu = ResourcesNote.objects.filter(department=cse_bu).count()
#     lectures_cse_bu = ResourcesLecture.objects.filter(department=cse_bu).count()
    
#     total_cse_bu = questions_cse_bu + books_cse_bu + notes_cse_bu + lectures_cse_bu 
    
#     context = {
#         'course': course,
#         'university': university,
#         'department': department,
#         'discipline': discipline,
#         'question_count': question_count,
#         'note_count': note_count,
#         'book_count': book_count,
#         'lecture_count': lecture_count,
#         'total_resourses_course': total_resourses_course,
#         'syllabus': syllabus,
#         'university_moderator': university_moderator,
#         'departmental_moderator': departmental_moderator,
#         'batch_moderator': batch_moderator,
        
#         'bu': bu,
#         'cse_bu': cse_bu,
#         'questions_cse_bu': questions_cse_bu,
#         'books_cse_bu': books_cse_bu,
#         'notes_cse_bu': notes_cse_bu,
#         'lectures_cse_bu': lectures_cse_bu,
#         'total_cse_bu': total_cse_bu,
#     }
    
#     return render(request, 'show_course.html', context)


def show_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    university = course.university
    department = course.department
    discipline = course.discipline

    # Retrieve the main course resources and their counts
    question_ids = set(ResourcesQuestion.objects.filter(course=course).values_list('id', flat=True))
    note_ids = set(ResourcesNote.objects.filter(course=course).values_list('id', flat=True))
    book_ids = set(ResourcesBook.objects.filter(course=course).values_list('id', flat=True))
    lecture_ids = set(ResourcesLecture.objects.filter(course=course).values_list('id', flat=True))

    # Retrieve common courses associated with the course
    common_courses = course.common_courses.all()

    # Iterate over each common course and add resources that haven't been counted yet
    for common_course in common_courses:
        # For questions
        common_question_ids = set(ResourcesQuestion.objects.filter(common_courses=common_course).values_list('id', flat=True))
        question_ids.update(common_question_ids.difference(question_ids))

        # For notes
        common_note_ids = set(ResourcesNote.objects.filter(common_courses=common_course).values_list('id', flat=True))
        note_ids.update(common_note_ids.difference(note_ids))

        # For books
        common_book_ids = set(ResourcesBook.objects.filter(common_courses=common_course).values_list('id', flat=True))
        book_ids.update(common_book_ids.difference(book_ids))

        # For lectures
        common_lecture_ids = set(ResourcesLecture.objects.filter(common_courses=common_course).values_list('id', flat=True))
        lecture_ids.update(common_lecture_ids.difference(lecture_ids))

    # Calculate the final counts
    question_count = len(question_ids)
    note_count = len(note_ids)
    book_count = len(book_ids)
    lecture_count = len(lecture_ids)

    # Calculate total resources count
    total_resourses_course = question_count + note_count + book_count + lecture_count

    # Additional logic for syllabus and moderators
    syllabus = course.syllabus

    university_moderator = Profile.objects.filter(
        Q(edu_university__university=university) &
        Q(moderator_type='University Moderator') &
        Q(moderator_info__is_running=True)
    ).annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )

    departmental_moderator = Profile.objects.filter(
        Q(edu_university__department=department) &
        Q(moderator_type='Departmental Moderator') &
        Q(moderator_info__is_running=True)
    ).annotate(
        duration_departmental_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )

    batch_moderator = Profile.objects.filter(
        Q(edu_university__department=department) &
        Q(moderator_type='Batch Moderator') &
        Q(moderator_info__is_running=True)
    ).annotate(
        duration_batch_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )

    # Example for Barishal University CSE department
    bu = University.objects.get(name='University of Barishal')
    cse_bu = Department.objects.get(university=bu, name='Department of Computer Science and Engineering')

    questions_cse_bu = ResourcesQuestion.objects.filter(department=cse_bu).count()
    books_cse_bu = ResourcesBook.objects.filter(department=cse_bu).count()
    notes_cse_bu = ResourcesNote.objects.filter(department=cse_bu).count()
    lectures_cse_bu = ResourcesLecture.objects.filter(department=cse_bu).count()

    total_cse_bu = questions_cse_bu + books_cse_bu + notes_cse_bu + lectures_cse_bu

    context = {
        'course': course,
        'university': university,
        'department': department,
        'discipline': discipline,
        'question_count': question_count,
        'note_count': note_count,
        'book_count': book_count,
        'lecture_count': lecture_count,
        'total_resourses_course': total_resourses_course,
        'syllabus': syllabus,
        'university_moderator': university_moderator,
        'departmental_moderator': departmental_moderator,
        'batch_moderator': batch_moderator,
        'bu': bu,
        'cse_bu': cse_bu,
        'questions_cse_bu': questions_cse_bu,
        'books_cse_bu': books_cse_bu,
        'notes_cse_bu': notes_cse_bu,
        'lectures_cse_bu': lectures_cse_bu,
        'total_cse_bu': total_cse_bu,
    }

    return render(request, 'show_course.html', context)



def my_department_s(request, university_id, department_id):
    university = get_object_or_404(University, pk=university_id)
    department = get_object_or_404(Department, pk=department_id, university=university)
    
    # department_system = department.system
    
    courses = department.course_set.all()
    # print(department_system)
    total_semester_or_year = department.total_semester_or_year
    
    #  Handle the case where total_semester_or_year is None
    if total_semester_or_year is None:
        total_semester_or_year = 8  # or any other default value that makes sense in your context
    
    
    bu = University.objects.get(name='University of Barishal')
    cse_bu = Department.objects.get(university=bu, name='Department of Computer Science and Engineering')

    questions_cse_bu = ResourcesQuestion.objects.filter(department=cse_bu).count()
    books_cse_bu = ResourcesBook.objects.filter(department=cse_bu).count()
    notes_cse_bu = ResourcesNote.objects.filter(department=cse_bu).count()
    lectures_cse_bu = ResourcesLecture.objects.filter(department=cse_bu).count()
    
    total_cse_bu = questions_cse_bu + books_cse_bu + notes_cse_bu + lectures_cse_bu 

    university_moderator = Profile.objects.filter(
    Q(edu_university__university=university) &
    Q(moderator_type='University Moderator') &
    Q(moderator_info__is_running=True)
)
    
    # Annotate with duration (time since approved_final_at)
    university_moderator = university_moderator.annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )


    departmental_moderator = Profile.objects.filter(
    Q(edu_university__department=department) &
    Q(moderator_type='Departmental Moderator') &
    Q(moderator_info__is_running=True)
)
    
    departmental_moderator = departmental_moderator.annotate(
        duration_departmental_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    batch_moderator = Profile.objects.filter(
    Q(edu_university__department=department) &
    Q(moderator_type='Batch Moderator') &
    Q(moderator_info__is_running=True)
)
    
    batch_moderator = batch_moderator.annotate(
        duration_batch_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    context = {
        'department': department,
        'university': university,
        'courses': courses,
        'total_semester_or_year': range(1, total_semester_or_year + 1),
        # 'total_semester_or_year': total_semester_or_year,
        
        'bu': bu,
        'cse_bu': cse_bu,
        'questions_cse_bu': questions_cse_bu,
        'books_cse_bu': books_cse_bu,
        'notes_cse_bu': notes_cse_bu,
        'lectures_cse_bu': lectures_cse_bu,
        'total_cse_bu': total_cse_bu,
        'university_moderator': university_moderator,
        'departmental_moderator': departmental_moderator,
        'batch_moderator': batch_moderator,
    }
    
    return render(request, 'department/my_department_s.html', context)


def university_list(request):
    university_type_id = request.GET.get('type')
    search_query = request.GET.get('search', '')  # Get the search query
    
    universities = University.objects.all().order_by('name')
    
    if university_type_id:
        universities = universities.filter(university_type_id=university_type_id)
    
    if search_query:
        universities = universities.filter(name__icontains=search_query)  # Filter by search query
    
    university_types = UniversityType.objects.all()
    
    # total_public_general = University.objects.filter(university_type=).count()
    
    return render(request, 'university/university_list.html', {
        'universities': universities,
        'university_types': university_types,
        'selected_university_type': university_type_id,
        'search_query': search_query, # Pass the search query back to the template
        
        # 'total_public_general': total_public_general,
    })



def university_info(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    department = Department.objects.filter(university=university).first()
    
    faculty_id = request.GET.get('faculty')
    search_query = request.GET.get('search', '')

    if faculty_id:
        departments = Department.objects.filter(university=university, faculty_id=faculty_id).order_by('name')
    else:
        departments = Department.objects.filter(university=university).order_by('name')

    if search_query:
        departments = departments.filter(name__icontains=search_query)

    department_with_all_info = departments.annotate(
        # Add your annotations here if needed
    )

    faculties = Faculty.objects.filter(university=university).order_by('name')
    
    total_faculties = faculties.count()
    total_departments = Department.objects.filter(university=university).count()
    
    total_resources = (
        ResourcesQuestion.objects.filter(university=university).count() +
        ResourcesBook.objects.filter(university=university).count() +
        ResourcesNote.objects.filter(university=university).count() +
        ResourcesLecture.objects.filter(university=university).count()
    )

    bu = University.objects.get(name='University of Barishal')
    cse_bu = Department.objects.get(university=bu, name='Department of Computer Science and Engineering')

    questions_cse_bu = ResourcesQuestion.objects.filter(department=cse_bu).count()
    books_cse_bu = ResourcesBook.objects.filter(department=cse_bu).count()
    notes_cse_bu = ResourcesNote.objects.filter(department=cse_bu).count()
    lectures_cse_bu = ResourcesLecture.objects.filter(department=cse_bu).count()
    
    total_cse_bu = questions_cse_bu + books_cse_bu + notes_cse_bu + lectures_cse_bu

    # Update the query to use the correct field path
    # moderators = ModeratorRequest.objects.filter(
    #     profile__edu_university__university=university,
    #     is_running=True
    # )
    
    # university_moderator = Profile.objects.filter(edu_university__university = university, moderator_type = 'University Moderator', moderator_info__is_running = True)
    
    university_moderator = Profile.objects.filter(
    Q(edu_university__university=university) &
    Q(moderator_type='University Moderator') &
    Q(moderator_info__is_running=True)
)
    
    # Annotate with duration (time since approved_final_at)
    university_moderator = university_moderator.annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    
    # departmental_moderator = Profile.objects.filter(edu_university__department = department, moderator_type = 'Departmental Moderator')
    departmental_moderator = Profile.objects.filter(
    edu_university__department=department,
    moderator_type='Departmental Moderator'
)

    context = {
        'university': university,
        'department_with_all_info': department_with_all_info,
        'faculties': faculties,
        'selected_faculty': int(faculty_id) if faculty_id else None,
        'search_query': search_query,
        
        'total_faculties': total_faculties,
        'total_departments': total_departments,
        'total_resources': total_resources,
        
        'bu': bu,
        'cse_bu': cse_bu,
        'questions_cse_bu': questions_cse_bu,
        'books_cse_bu': books_cse_bu,
        'notes_cse_bu': notes_cse_bu,
        'lectures_cse_bu': lectures_cse_bu,
        'total_cse_bu': total_cse_bu,
        
        'university_moderator': university_moderator,
        'departmental_moderator': departmental_moderator,
    }
    return render(request, 'university/university_info.html', context)




@require_POST
def update_department_order(request):
    new_order = request.POST.getlist('order[]')
    # Update the database with the new order
    # Example:
    # for index, department_id in enumerate(new_order, start=1):
    #     Department.objects.filter(id=department_id).update(order=index)
    return JsonResponse({'success': True})


from django.contrib import messages
  

from django.db.models import F, ExpressionWrapper, DurationField
from django.utils.timezone import now
@login_required
def my_resources_s(request, x_id, semester):
    if request.user.profile.edu_university.department:
        department = get_object_or_404(Department, pk=x_id)
        university = department.university
        courses = Course.objects.filter(department=department, semester=semester_converter(semester))
    else:
        department = None
    
    if request.user.profile.edu_university.discipline:
        discipline = get_object_or_404(Discipline, pk=x_id)
        university = discipline.university
        courses = Course.objects.filter(discipline=discipline, semester=semester_converter(semester))
    else:
        discipline = None
    
    course_data = []
    
    question_count = 0
    note_count = 0
    lecture_count = 0
    book_count = 0
    
    course_semester = ''
    
    for course in courses:
        question_count = ResourcesQuestion.objects.filter(course=course).count()
        
        note_count = ResourcesNote.objects.filter(course=course).count()
        
        lecture_count = ResourcesLecture.objects.filter(course=course).count()
        
        book_count = ResourcesBook.objects.filter(course=course).count()
        
        course_data.append({'course': course, 'question_count': question_count, 'note_count': note_count, 'lecture_count': lecture_count, 'book_count': book_count})
        course_semester = course.semester
    
    university_moderator = Profile.objects.filter(
    Q(edu_university__university=university) &
    Q(moderator_type='University Moderator') &
    Q(moderator_info__is_running=True)
)
    
    # Annotate with duration (time since approved_final_at)
    university_moderator = university_moderator.annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    if request.user.profile.edu_university.department:  
        departmental_moderator = Profile.objects.filter(
        Q(edu_university__department=department) &
        Q(moderator_type='Departmental Moderator') &
        Q(moderator_info__is_running=True)
    )
    
        departmental_moderator = departmental_moderator.annotate(
            duration_departmental_moderator=ExpressionWrapper(
                now() - F('moderator_info__approved_final_at'),
                output_field=DurationField()
            )
        )
    else:
        departmental_moderator = None
    
    batch_moderator = Profile.objects.filter(
    (Q(edu_university__department=department)) &
    Q(moderator_type='Batch Moderator') &
    Q(moderator_info__is_running=True)
)

    
    batch_moderator = batch_moderator.annotate(
        duration_batch_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    context = {
        'department': department,
        'discipline': discipline,
        'university': university,
        'semester': semester,
        'courses': courses,
        # 'question_count': question_count,
        'course_data': course_data,
        'note_count': note_count,
        'lecture_count': lecture_count,
        'book_count': book_count,
        'university_moderator': university_moderator,
        'departmental_moderator': departmental_moderator,
        'batch_moderator': batch_moderator,
        
        'course_semester': course_semester,
    }

    return render(request, 'resources/my_resources_s.html', context)



from apps.account.models.profile_models import CoinTransaction
@login_required
def add_coin_transaction(profile, activity, coins):
    # print('hiiiiiiiiiiiii')
    """Add a coin transaction for a profile based on activity."""
    if activity not in [choice[0] for choice in CoinTransaction.ACTIVITY_CHOICES]:
        raise ValueError("Invalid activity type.")

    if coins <= 0:
        raise ValueError("Coins must be greater than zero.")

    # Create a new coin transaction
    CoinTransaction.objects.create(
        profile=profile,
        activity=activity,
        coins=coins
    )

    # Update the user's total coins
    # profile.total_coins = profile.calculate_total_coins()  # Ensure total_coins is updated correctly
    profile.total_coins = profile.total_coins + coins
    profile.save()


# QUESTION ================================================
@user_passes_test(has_resources_upload_permission, login_url='home')
def add_question(request):
    user = request.user
    uploader = request.user.profile.fullname or request.user
    edu_university = EduUniversity.objects.get(profile=user.profile)
    leaderboard_url = reverse('leaderboard')
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, user=user)
        
        if form.is_valid():
            question = form.save(commit=False)  # Save the form but don't commit yet
            profile = Profile.objects.get(user=request.user)

            # Set additional fields
            question.uploaded_by = profile
            question.university = edu_university.university
            question.faculty = edu_university.faculty
            question.institute = edu_university.institute
            question.school = edu_university.school
            question.center = edu_university.center
            question.department = edu_university.department
            question.discipline = edu_university.discipline
            
            question.save()  # Save the question object to get the ID

            # Add coins for the activity
            add_coin_transaction(profile, 'add_question', 30)

            # Display success message
            messages.success(request, mark_safe(
                f"প্রিয় <strong>{uploader}</strong>!, প্রশ্নটি আপলোড করার জন্য আপনি <strong>30টি Onebyzero Coin</strong> পেয়েছেন! "
                f"এই মুহুর্তে আপনার মোট কয়েনঃ <strong>{profile.total_coins}</strong>টি। নিঃসন্দেহে আপনার এ অবদান থেকে অসংখ্য শিক্ষার্থী "
                f"বছরের পর বছর উপকৃত হবে। সহযোগিতার এ ধারা অব্যহত রাখুন!</a>।"
                f"<a href='{leaderboard_url}' class='btn btn-secondary btn-sm mt-1'>Your Contribution Ranking</a>"
            ))

            # Create a notification for the user
            Notification.objects.create(
                user=request.user,
                type='add_question',
                message=mark_safe(
                    f"অভিনন্দন! 1টি প্রশ্ন আপলোড করার জন্য আপনি 30টি Onebyzero Coin পেয়েছেন! "
                    f"এই মুহুর্তে আপনার মোট কয়েনঃ {profile.total_coins}টি। "
                    f"নিঃসন্দেহে আপনার এ অবদান থেকে অসংখ্য শিক্ষার্থী উপকৃত হবে।"
                ),
                additional_id_one=question.course.id,
            )

            # Redirect to the view questions page
            return redirect('view_questions', course_id=question.course.id)
        else:
            print(form.errors)
    else:
        form = QuestionForm(user=user)

    return render(request, 'resources/questions/add_question.html', {
        'form': form,
        'uploader': uploader,
        'user': user,
        'is_add_question': True,
    })



def edit_question(request, question_id):
    question = get_object_or_404(ResourcesQuestion, pk=question_id)
    
    # Check if the user has permission to edit the question
    if not has_resources_edit_permission(request.user, question):
        messages.success(request, "Sorry, you do not have permission to edit this question.")
        return redirect('view_questions', course_id=question.course.id)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save()
            messages.success(request, "Successfully updated the question!")
            return redirect('view_questions', course_id=question.course.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'resources/questions/edit_question.html', {'form': form, 'question': question})



def delete_question(request, question_id):
    question = get_object_or_404(ResourcesQuestion, pk=question_id)
    
    if not has_resources_delete_permission(request.user, question):
        messages.success(request, "Sorry, you do not have permission to delete this question.")
        return redirect('view_questions', course_id=question.course.id)
    
    question.delete()
    course_id = question.course.id
    
    uploader_profile = Profile.objects.get(user=question.uploaded_by.user)
    uploader_profile.total_coins -= 30
    uploader_profile.save()
    
    messages.success(request, mark_safe(f"প্রশ্নটি ডিলেট করা হয়েছে এবং একই সাথে এর আপলোডার {uploader_profile.fullname} এর টোটাল Onebyzero Coin থেকে এই প্রশ্নের জন্য পাওয়া <strong>30টি Coin</strong> নেগেটিভ করা হয়েছে!"))
    
    return redirect('view_questions', course_id=course_id)

# @user_passes_test(is_verified, login_url='/study/error/department/access-denied/')

# def view_questions(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)

#     questions = ResourcesQuestion.objects.filter(course=course).order_by('-upload_time')

#     # Retrieve the IDs of questions already displayed
#     displayed_question_ids = questions.values_list('id', flat=True)

#     # Retrieve common courses for the course
#     common_courses = course.common_courses.all()

#     # Retrieve questions for each common course, excluding already displayed questions
#     common_course_questions = {}
#     total_common_course_questions = 0  # To keep track of the total number of common course questions

#     for common_course in common_courses:
#         # Filter questions for the common course that are not already displayed
#         questions_for_common_course = ResourcesQuestion.objects.filter(
#             common_courses=common_course
#         ).exclude(id__in=displayed_question_ids).order_by('-upload_time')

#         # Store the questions for each common course
#         common_course_questions[common_course] = questions_for_common_course
#         # Add the count of questions for this common course to the total
#         total_common_course_questions += questions_for_common_course.count()

# # Calculate the total number of questions
#     total_questions = questions.count() + total_common_course_questions

    
#     session_filter = request.GET.get('session')
#     exam_name_filter = request.GET.get('exam_name')

#     if session_filter:
#         questions = questions.filter(session=session_filter)

#     if exam_name_filter:
#         questions = questions.filter(exam_name__icontains=exam_name_filter)

#     users_with_question_count = (
#         ResourcesQuestion.objects
#         .filter(course=course)
#         .values('uploaded_by', 'uploaded_by__user', 'uploaded_by__fullname', 'uploaded_by__nickname', 'uploaded_by__profile_image')
#         .annotate(question_count=Count('uploaded_by__fullname'))
#     )

#     user_profile = None
#     if request.user.is_authenticated:
#         # If the user is authenticated, retrieve their profile
#         user_profile = get_object_or_404(Profile, user=request.user)
    
#     university = course.university
#     department = course.department

#     context = {
#         'questions': questions,
#         'course': course,
#         'users_with_question_count': users_with_question_count,
        
#         'common_courses': common_courses,
#         'common_course_questions': common_course_questions,
        
#         'user_profile': user_profile,
#         'total_questions': total_questions,
#         'university': university,
#         'department': department,
#     }
#     return render(request, 'resources/questions/view_questions.html', context)


def view_questions(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    # Retrieve questions for the course and order them by upload time
    questions = ResourcesQuestion.objects.filter(course=course).order_by('-upload_time')

    # Create a set to store the displayed question IDs
    displayed_question_ids = set(questions.values_list('id', flat=True))

    # Retrieve common courses for the course
    common_courses = course.common_courses.all()

    # Dictionary to store questions from common courses
    common_course_questions = {}
    total_common_course_questions = 0  # To keep track of the total number of common course questions

    for common_course in common_courses:
        # Filter questions for the common course that are not already displayed
        questions_for_common_course = ResourcesQuestion.objects.filter(
            common_courses=common_course
        ).exclude(id__in=displayed_question_ids).order_by('-upload_time')

        # Store the questions for each common course
        common_course_questions[common_course] = questions_for_common_course
        
        # Add the IDs of these questions to the displayed_question_ids set to avoid duplicates
        displayed_question_ids.update(questions_for_common_course.values_list('id', flat=True))
        
        # Add the count of questions for this common course to the total
        total_common_course_questions += questions_for_common_course.count()

    # Calculate the total number of questions
    total_questions = questions.count() + total_common_course_questions

    # Apply session and exam name filters if provided
    session_filter = request.GET.get('session')
    exam_name_filter = request.GET.get('exam_name')

    if session_filter:
        questions = questions.filter(session=session_filter)

    if exam_name_filter:
        questions = questions.filter(exam_name__icontains=exam_name_filter)

    # Get users who have uploaded questions and count their uploads
    users_with_question_count = (
        ResourcesQuestion.objects
        .filter(course=course)
        .values('uploaded_by', 'uploaded_by__user', 'uploaded_by__fullname', 'uploaded_by__nickname', 'uploaded_by__profile_image')
        .annotate(question_count=Count('uploaded_by__fullname'))
    )

    # Get the user's profile if authenticated
    user_profile = None
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)

    university = course.university
    department = course.department

    # Pass context to template
    context = {
        'questions': questions,
        'course': course,
        'users_with_question_count': users_with_question_count,
        
        'common_courses': common_courses,
        'common_course_questions': common_course_questions,
        
        'user_profile': user_profile,
        'total_questions': total_questions,
        'university': university,
        'department': department,
    }
    
    return render(request, 'resources/questions/view_questions.html', context)


def share_question(request, question_id):
    # Retrieve the question with the specified ID or handle appropriately
    question = get_object_or_404(ResourcesQuestion, pk=question_id)
    # You can pass the question to a template and render it for viewing
    return render(request, 'resources/questions/share_question.html', {'question': question})

# NOTES=================================================

@user_passes_test(has_resources_upload_permission, login_url='home')
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        uploader = request.user.profile.fullname or request.user
        leaderboard_url = reverse('leaderboard')
        
        if form.is_valid():
            note = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            edu_university = EduUniversity.objects.get(profile=profile)
            note.uploaded_by = profile
            note.university = edu_university.university
            note.faculty = edu_university.faculty
            note.institute = edu_university.institute
            note.center = edu_university.center
            note.department = edu_university.department
            note.discipline = edu_university.discipline
            note.save()  # Save the question with the uploaded_by information
            # print('dfdsfdsfs', question)

            add_coin_transaction(profile, 'add_note', 50)
            
            messages.success(request, mark_safe(
                f"প্রিয় <strong>{uploader}</strong>!, নোটটি আপলোড করার জন্য আপনি <strong>50টি Onebyzero Coin</strong> পেয়েছেন! এই মুহুর্তে আপনার মোট কয়েনঃ <strong>{profile.total_coins}</strong>টি। নিঃসন্দেহে আপনার এ অবদান থেকে অসংখ্য শিক্ষার্থী বছরের পর বছর উপকৃত হবে। সহযোগিতার এ ধারা অব্যহত রাখুন!</a>।"
                f"<a href='{leaderboard_url}' class='btn btn-secondary btn-sm mt-1'>Your Contribution Ranking</a>"
                ))
            
            Notification.objects.create(
            user = request.user,
            type='add_note',
            # notification_type = 1
            message = mark_safe(
                f"অভিনন্দন! 1টি নোট আপলোড করার জন্য আপনি 50টি Onebyzero Coin পেয়েছেন! এই মুহুর্তে আপনার মোট কয়েনঃ {profile.total_coins}টি। নিঃসন্দেহে আপনার এ অবদান থেকে অসংখ্য শিক্ষার্থী বছরের পর বছর উপকৃত হবে। সহযোগিতার এ ধারা অব্যহত রাখুন!"
                ),
            additional_id_one = note.course.id
        )

            return redirect('view_notes', course_id=note.course.id)
        # else:
            # print(form.errors)
    else:
        form = NoteForm()
    return render(request, 'resources/notes/add_note.html', {'form': form, 'is_add_note': True})

def edit_note(request, note_id):
    note = get_object_or_404(ResourcesNote, pk=note_id)
    
    if not has_resources_edit_permission(request.user, note):
        messages.success(request, "Sorry, you don't have permission to edit this note.")
        return redirect('view_notes', course_id=note.course.id)
        
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.save()
            messages.success(request, "Successfully updated the note!")
            return redirect('view_notes', course_id=note.course.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'resources/notes/edit_note.html', {'form': form, 'note': note})


# def view_notes(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     notes = ResourcesNote.objects.filter(course=course).order_by('-upload_time')
        
#     # total_notes = ResourcesNote.objects.filter(course=course).count()
    
#     # Retrieve the IDs of questions already displayed
#     displayed_notes_ids = notes.values_list('id', flat=True)

#     # Retrieve common courses for the course
#     common_courses = course.common_courses.all()

#     # Retrieve questions for each common course, excluding already displayed questions
#     common_course_notes = {}
#     total_common_course_notes = 0  # To keep track of the total number of common course questions
    
#     for common_course in common_courses:
#         # Filter questions for the common course that are not already displayed
#         notes_for_common_course = ResourcesNote.objects.filter(
#             common_courses=common_course
#         ).exclude(id__in=displayed_notes_ids).order_by('-upload_time')

#         # Store the questions for each common course
#         common_course_notes[common_course] = notes_for_common_course
#         # Add the count of questions for this common course to the total
#         total_common_course_notes += notes_for_common_course.count()

# # Calculate the total number of questions
#     total_notes = notes.count() + total_common_course_notes
    
#     session_filter = request.GET.get('session')

#     if session_filter:
#         notes = notes.filter(session=session_filter)

#     users_with_note_count = (
#     ResourcesNote.objects
#     .filter(course=course)
#     .values('uploaded_by', 'uploaded_by__user', 'uploaded_by__fullname', 'uploaded_by__nickname', 'uploaded_by__profile_image')
#     .annotate(note_count=Count('uploaded_by__fullname'))
# )

#     user_profile = None
#     if request.user.is_authenticated:
#         # If the user is authenticated, retrieve their profile
#         user_profile = get_object_or_404(Profile, user=request.user)
    
#     university = course.university
#     department = course.department
    
#     context = {
#         'notes': notes,
#         'course': course,
#         'users_with_note_count': users_with_note_count,
#         'user_profile': user_profile,
#         'total_notes': total_notes,
#         'university': university,
#         'department': department,
        
#         'common_course_notes': common_course_notes,
#         'total_common_course_notes': total_common_course_notes,
#         'common_courses': common_courses,
#     }
    
#     return render(request, 'resources/notes/view_notes.html', context)


def view_notes(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    # Retrieve notes for the course and order them by upload time
    notes = ResourcesNote.objects.filter(course=course).order_by('-upload_time')

    # Create a set to store the displayed note IDs
    displayed_note_ids = set(notes.values_list('id', flat=True))

    # Retrieve common courses for the course
    common_courses = course.common_courses.all()

    # Dictionary to store notes from common courses
    common_course_notes = {}
    total_common_course_notes = 0  # To keep track of the total number of common course notes

    for common_course in common_courses:
        # Filter notes for the common course that are not already displayed
        notes_for_common_course = ResourcesNote.objects.filter(
            common_courses=common_course
        ).exclude(id__in=displayed_note_ids).order_by('-upload_time')

        # Store the notes for each common course
        common_course_notes[common_course] = notes_for_common_course
        
        # Add the IDs of these notes to the displayed_note_ids set to avoid duplicates
        displayed_note_ids.update(notes_for_common_course.values_list('id', flat=True))
        
        # Add the count of notes for this common course to the total
        total_common_course_notes += notes_for_common_course.count()

    # Calculate the total number of notes
    total_notes = notes.count() + total_common_course_notes

    # Apply session filter if it exists
    session_filter = request.GET.get('session')
    if session_filter:
        notes = notes.filter(session=session_filter)

    # Get users who have uploaded notes and count their uploads
    users_with_note_count = (
        ResourcesNote.objects
        .filter(course=course)
        .values('uploaded_by', 'uploaded_by__user', 'uploaded_by__fullname', 'uploaded_by__nickname', 'uploaded_by__profile_image')
        .annotate(note_count=Count('uploaded_by__fullname'))
    )

    # Get the user's profile if authenticated
    user_profile = None
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)

    university = course.university
    department = course.department

    # Pass context to the template
    context = {
        'notes': notes,
        'course': course,
        'users_with_note_count': users_with_note_count,
        
        'common_courses': common_courses,
        'common_course_notes': common_course_notes,
        
        'user_profile': user_profile,
        'total_notes': total_notes,
        'university': university,
        'department': department,
        'total_common_course_notes': total_common_course_notes,
    }

    return render(request, 'resources/notes/view_notes.html', context)


def delete_note(request, note_id):
    note = get_object_or_404(ResourcesNote, pk=note_id)
    
    if not has_resources_delete_permission(request.user, note):
        messages.success(request, "Sorry, you don't have permission to delete this note.")
        return redirect('view_notes', course_id=note.course.id)
    
    note.delete()
    course_id = note.course.id
    
    uploader_profile = Profile.objects.get(user=note.uploaded_by.user)
    uploader_profile.total_coins -= 50
    uploader_profile.save()
    
    messages.success(request, mark_safe(f"নোটটি ডিলেট করা হয়েছে এবং একই সাথে এর আপলোডার {uploader_profile.fullname} এর টোটাল Onebyzero Coin থেকে এই নোটের জন্য পাওয়া <strong>50টি Coin</strong> নেগেটিভ করা হয়েছে!"))
    
    return redirect('view_notes', course_id=course_id)

# BOOKS =================================================
@user_passes_test(has_resources_upload_permission, login_url='home')
def add_book(request):
    if request.method == 'POST':
        uploader = request.user.profile.nickname or request.user
        
        form = BookForm(request.POST, request.FILES)
        
        leaderboard_url = reverse('leaderboard')
        
        if form.is_valid():
            book = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            edu_university = EduUniversity.objects.get(profile=profile)
            book.uploaded_by = profile
            book.university = edu_university.university
            book.faculty = edu_university.faculty
            book.institute = edu_university.institute
            book.school = edu_university.school
            book.center = edu_university.center
            book.department = edu_university.department
            book.discipline = edu_university.discipline
            book.save()
            
            add_coin_transaction(profile, 'add_book', 20)
            
            messages.success(request, mark_safe(
                f"প্রিয় <strong>{uploader}</strong>!, বইটি আপলোড করার জন্য আপনি <strong>20টি Onebyzero Coin</strong> পেয়েছেন! এই মুহুর্তে আপনার মোট কয়েনঃ <strong>{profile.total_coins}</strong>টি। নিঃসন্দেহে আপনার এ অবদান থেকে অসংখ্য শিক্ষার্থী বছরের পর বছর উপকৃত হবে। সহযোগিতার এ ধারা অব্যহত রাখুন!</a>।"
                f"<a href='{leaderboard_url}' class='btn btn-secondary btn-sm mt-1'>Your Contribution Ranking</a>"
                ))
            
            Notification.objects.create(
            user = request.user,
            type='add_book',
            # notification_type = 1
            message = mark_safe(
                f"অভিনন্দন! 1টি বই আপলোড করার জন্য আপনি 20টি Onebyzero Coin পেয়েছেন! এই মুহুর্তে আপনার মোট কয়েনঃ {profile.total_coins}টি। নিঃসন্দেহে আপনার এ অবদান থেকে অসংখ্য শিক্ষার্থী বছরের পর বছর উপকৃত হবে। সহযোগিতার এ ধারা অব্যহত রাখুন!"
                ),
            additional_id_one = book.course.id
        )
            
            # messages.success(request, mark_safe("Dear <strong>" + str(uploader) + "</strong>, Thank you for uploading the book! Your contribution will undoubtedly benefit the students for years of years. Keep up the great work by continuing your contributions!"))
            
            return redirect('view_books', course_id=book.course.id)
        else:
            print(form.errors)

    else:
        form = BookForm()
    return render(request, 'resources/books/add_book.html', {'form': form, 'is_add_book': True})



# def view_books(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     books = ResourcesBook.objects.filter(course=course).order_by('-upload_time')
        
#     # total_books = ResourcesBook.objects.filter(course=course).count()
    
#     # Retrieve the IDs of questions already displayed
#     displayed_book_ids = books.values_list('id', flat=True)

#     # Retrieve common courses for the course
#     common_courses = course.common_courses.all()

#     # Retrieve questions for each common course, excluding already displayed questions
#     common_course_books = {}
#     total_common_course_books = 0  # To keep track of the total number of common course questions
    
#     for common_course in common_courses:
#         # Filter questions for the common course that are not already displayed
#         books_for_common_course = ResourcesBook.objects.filter(
#             common_courses=common_course
#         ).exclude(id__in=displayed_book_ids).order_by('-upload_time')

#         # Store the questions for each common course
#         common_course_books[common_course] = books_for_common_course
#         # Add the count of questions for this common course to the total
#         total_common_course_books += books_for_common_course.count()

# # Calculate the total number of questions
#     total_books = books.count() + total_common_course_books

#     users_with_book_count = (
#     ResourcesBook.objects
#     .filter(course=course)
#     .values('uploaded_by', 'uploaded_by__user', 'uploaded_by__fullname', 'uploaded_by__nickname', 'uploaded_by__profile_image')
#     .annotate(book_count=Count('uploaded_by__fullname'))
# )

    
#     user_profile = None
#     if request.user.is_authenticated:
#         # If the user is authenticated, retrieve their profile
#         user_profile = get_object_or_404(Profile, user=request.user)
    
#     university = course.university
#     department = course.department
    
#     context = {
#         'books': books,
#         'course': course,
#         'users_with_book_count': users_with_book_count,
#         'user_profile': user_profile,
#         'total_books': total_books,
#         'university': university,
#         'department': department,
#         'common_course_books': common_course_books,
#         'total_common_course_books': total_common_course_books,
#     }
#     return render(request, 'resources/books/view_books.html', context)


from django.shortcuts import render, get_object_or_404
from django.db.models import Count

def view_books(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    # Retrieve books for the course and order them by upload time
    books = ResourcesBook.objects.filter(course=course).order_by('-upload_time')

    # Create a set to store the displayed book IDs
    displayed_book_ids = set(books.values_list('id', flat=True))

    # Retrieve common courses for the course
    common_courses = course.common_courses.all()

    # Dictionary to store books from common courses
    common_course_books = {}
    total_common_course_books = 0  # To keep track of the total number of common course books

    for common_course in common_courses:
        # Filter books for the common course that are not already displayed
        books_for_common_course = ResourcesBook.objects.filter(
            common_courses=common_course
        ).exclude(id__in=displayed_book_ids).order_by('-upload_time')

        # Store the books for each common course
        common_course_books[common_course] = books_for_common_course
        
        # Add the IDs of these books to the displayed_book_ids set to avoid duplicates
        displayed_book_ids.update(books_for_common_course.values_list('id', flat=True))
        
        # Add the count of books for this common course to the total
        total_common_course_books += books_for_common_course.count()

    # Calculate the total number of books
    total_books = books.count() + total_common_course_books

    # Get users who have uploaded books and count their uploads
    users_with_book_count = (
        ResourcesBook.objects
        .filter(course=course)
        .values('uploaded_by', 'uploaded_by__user', 'uploaded_by__fullname', 'uploaded_by__nickname', 'uploaded_by__profile_image')
        .annotate(book_count=Count('uploaded_by__fullname'))
    )

    # Get the user's profile if authenticated
    user_profile = None
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)

    university = course.university
    department = course.department

    # Pass context to template
    context = {
        'books': books,
        'course': course,
        'users_with_book_count': users_with_book_count,
        
        'common_courses': common_courses,
        'common_course_books': common_course_books,
        
        'user_profile': user_profile,
        'total_books': total_books,
        'university': university,
        'department': department,
        'total_common_course_books': total_common_course_books,
    }
    
    return render(request, 'resources/books/view_books.html', context)


def edit_book(request, book_id):
    book = get_object_or_404(ResourcesBook, pk=book_id)
    
    if not has_resources_edit_permission(request.user, book):
        messages.success(request, "Sorry, you do not have permission to edit this book.")
        return redirect('view_books', course_id=book.course.id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            book = form.save()
            messages.success(request, "Successfully updated the book!")
            return redirect('view_books', course_id=book.course.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'resources/books/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(ResourcesBook, pk=book_id)
    
    if not has_resources_delete_permission(request.user, book):
        messages.success(request, "Sorry, you do not have permission to delete this book.")
        return redirect('view_books', course_id=book.course.id)
        
    book.delete()
    course_id = book.course.id
    
    uploader_profile = Profile.objects.get(user=book.uploaded_by.user)
    uploader_profile.total_coins -= 20
    uploader_profile.save()
    
    messages.success(request, mark_safe(f"বইটি ডিলেট করা হয়েছে এবং একই সাথে এর আপলোডার {uploader_profile.fullname} এর টোটাল Onebyzero Coin থেকে এই বইয়ের জন্য পাওয়া <strong>20টি Coin</strong> নেগেটিভ করা হয়েছে!"))
    
    return redirect('view_books', course_id=course_id)


# LECTURE SLIDES =================================================
@user_passes_test(has_resources_upload_permission, login_url='home')
def add_lecture(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        uploader = request.user.profile.fullname or request.user
        leaderboard_url = reverse('leaderboard')
        
        if form.is_valid():
            lecture = form.save(commit=False) # Create the question object but don't save it yet
            profile = Profile.objects.get(user=request.user)
            edu_university = EduUniversity.objects.get(profile=profile)
            lecture.uploaded_by = profile
            lecture.university = edu_university.university
            lecture.faculty = edu_university.faculty
            lecture.institute = edu_university.institute
            lecture.school = edu_university.school
            lecture.center = edu_university.center
            lecture.department = edu_university.department
            lecture.discipline = edu_university.discipline
            # lecture.faculty = profile.faculty
            lecture.save()  # Save the question with the uploaded_by information
            # print('dfdsfdsfs', question)

            add_coin_transaction(profile, 'add_lecture', 10)
            
            messages.success(request, mark_safe(
                f"প্রিয় <strong>{uploader}</strong>!, লেকচার স্লাইডটি আপলোড করার জন্য আপনি <strong>10টি Onebyzero Coin</strong> পেয়েছেন! এই মুহুর্তে আপনার মোট কয়েনঃ <strong>{profile.total_coins}</strong>টি। নিঃসন্দেহে আপনার এ অবদান থেকে অসংখ্য শিক্ষার্থী বছরের পর বছর উপকৃত হবে। সহযোগিতার এ ধারা অব্যহত রাখুন!</a>।"
                f"<a href='{leaderboard_url}' class='btn btn-secondary btn-sm mt-1'>Your Contribution Ranking</a>"
                ))
            
            Notification.objects.create(
            user = request.user,
            type='add_lecture',
            # notification_type = 1
            message = mark_safe(
                f"অভিনন্দন! 1টি লেকচার স্লাইড আপলোড করার জন্য আপনি 10টি Onebyzero Coin পেয়েছেন! এই মুহুর্তে আপনার মোট কয়েনঃ {profile.total_coins}টি। নিঃসন্দেহে আপনার এ অবদান থেকে অসংখ্য শিক্ষার্থী বছরের পর বছর উপকৃত হবে। সহযোগিতার এ ধারা অব্যহত রাখুন!"
                ),
            additional_id_one = lecture.course.id,
        )

            return redirect('view_lectures', course_id=lecture.course.id)
        # else:
            # print(form.errors)
    else:
        form = LectureForm()
    return render(request, 'resources/lectures/add_lecture.html', {'form': form, 'is_add_lecture': True})

# @user_passes_test(is_verified, login_url='/study/error/department/access-denied/')



def view_lectures(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    # Retrieve lectures for the course and order them by upload time
    lectures = ResourcesLecture.objects.filter(course=course).order_by('-upload_time')
    
    # Create a set to store the displayed lecture IDs
    displayed_lectures_ids = set(lectures.values_list('id', flat=True))

    # Retrieve common courses for the course
    common_courses = course.common_courses.all()

    # Dictionary to store lectures from common courses
    common_course_lectures = {}
    total_common_course_lectures = 0  # To keep track of the total number of common course lectures

    for common_course in common_courses:
        # Filter lectures for the common course that are not already displayed
        lectures_for_common_course = ResourcesLecture.objects.filter(
            common_courses=common_course
        ).exclude(id__in=displayed_lectures_ids).order_by('-upload_time')

        # Store the lectures for each common course
        common_course_lectures[common_course] = lectures_for_common_course
        
        # Add the IDs of these lectures to the displayed_lectures_ids set to avoid duplicates
        displayed_lectures_ids.update(lectures_for_common_course.values_list('id', flat=True))
        
        # Add the count of lectures for this common course to the total
        total_common_course_lectures += lectures_for_common_course.count()

    # Calculate the total number of lectures
    total_lectures = lectures.count() + total_common_course_lectures

    # Apply session filter if provided
    session_filter = request.GET.get('session')
    if session_filter:
        lectures = lectures.filter(session=session_filter)

    # Get users who have uploaded lectures and count their uploads
    users_with_lecture_count = (
        ResourcesLecture.objects
        .filter(course=course)
        .values('uploaded_by', 'uploaded_by__user', 'uploaded_by__fullname', 'uploaded_by__nickname', 'uploaded_by__profile_image')
        .annotate(lecture_count=Count('uploaded_by__fullname'))
    )

    # Get the user's profile if authenticated
    user_profile = None
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user=request.user)

    university = course.university
    department = course.department

    # Pass context to template
    context = {
        'lectures': lectures,
        'course': course,
        'users_with_lecture_count': users_with_lecture_count,
        'user_profile': user_profile,
        'total_lectures': total_lectures,
        'university': university,
        'department': department,
        'common_course_lectures': common_course_lectures,
        'total_common_course_lectures': total_common_course_lectures,
        'common_courses': common_courses,
    }
    
    return render(request, 'resources/lectures/view_lectures.html', context)


def edit_lecture(request, lecture_id):
    lecture = get_object_or_404(ResourcesLecture, pk=lecture_id)
    
    if not has_resources_edit_permission(request.user, lecture):
        messages.success(request, "Sorry, you don't have permission to edit this lecture slide!")
        return redirect('view_lectures', course_id=lecture.course.id)
    
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES, instance=lecture)
        if form.is_valid():
            lecture = form.save()
            messages.success(request, "Successfully updated the lecture slide!")
            return redirect('view_lectures', course_id=lecture.course.id)
    else:
        form = LectureForm(instance=lecture)
    return render(request, 'resources/lectures/edit_lecture.html', {'form': form, 'lecture': lecture})

def delete_lecture(request, lecture_id):
    lecture = get_object_or_404(ResourcesLecture, pk=lecture_id)
    
    if not has_resources_delete_permission(request.user, lecture):
        messages.success(request, "Sorry, you don't have permission to delete this lecture slide!")
        return redirect('view_lectures', course_id=lecture.course.id)
    
    lecture.delete()
    course_id = lecture.course.id
    
    uploader_profile = Profile.objects.get(user=lecture.uploaded_by.user)
    uploader_profile.total_coins -= 10
    uploader_profile.save()
    
    messages.success(request, mark_safe(f"লেকচার স্লাইডটি ডিলেট করা হয়েছে এবং একই সাথে এর আপলোডার {uploader_profile.fullname} এর টোটাল Onebyzero Coin থেকে এই স্লাইডের জন্য পাওয়া <strong>10টি Coin</strong> নেগেটিভ করা হয়েছে!"))
    
    return redirect('view_lectures', course_id=course_id)


# from .serializers import CourseModelSerializer
# from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# @user_passes_test(is_verified, login_url='/study/error/department/access-denied/')
def view_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    university = course.university
    department = course.department
    
    question_count = ResourcesQuestion.objects.filter(course=course).count()
    note_count = ResourcesNote.objects.filter(course=course).count()
    book_count = ResourcesBook.objects.filter(course=course).count()
    lecture_count = ResourcesLecture.objects.filter(course=course).count()
    
    total_resourses_course = question_count + note_count + book_count + lecture_count
    
    syllabus = course.syllabus
    
    
    university_moderator = Profile.objects.filter(
    Q(edu_university__university=university) &
    Q(moderator_type='University Moderator') &
    Q(moderator_info__is_running=True)
)
    
    # Annotate with duration (time since approved_final_at)
    university_moderator = university_moderator.annotate(
        duration_university_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    departmental_moderator = Profile.objects.filter(
    Q(edu_university__department=department) &
    Q(moderator_type='Departmental Moderator') &
    Q(moderator_info__is_running=True)
)
    
    departmental_moderator = departmental_moderator.annotate(
        duration_departmental_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    batch_moderator = Profile.objects.filter(
    Q(edu_university__department=department) &
    Q(moderator_type='Batch Moderator') &
    Q(moderator_info__is_running=True)
)
    
    batch_moderator = batch_moderator.annotate(
        duration_batch_moderator=ExpressionWrapper(
            now() - F('moderator_info__approved_final_at'),
            output_field=DurationField()
        )
    )
    
    
    # serializer = CourseModelSerializer(course)
    # json_data = JSONRenderer().render(serializer.data)
    
    # return HttpResponse(json_data, content_type='application/json')
    
    context = {
        'course': course,
        'university': university,
        'department': department,
        'question_count': question_count,
        'note_count': note_count,
        'book_count': book_count,
        'lecture_count': lecture_count,
        'total_resourses_course': total_resourses_course,
        'syllabus': syllabus,
        'university_moderator': university_moderator,
        'departmental_moderator': departmental_moderator,
        'batch_moderator': batch_moderator,
    }
    
    return render(request, 'view_course.html', context)


def increment_love_count(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        question = get_object_or_404(ResourcesQuestion, pk=question_id)
        question.love_count += 1
        question.save()
        return JsonResponse({'love_count': question.love_count})

# # AJAX
# def load_departments(request):
#     university_id = request.GET.get('university_id')
#     departments = Department.objects.filter(university_id=university_id).all()
#     return render(request, 'department_dropdown_list_options.html', {'departments': departments})
#     # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    
# def load_courses(request):
#     university_id = request.GET.get('university_id')
#     department_id = request.GET.get('department_id')
#     semester = request.GET.get('semester')
#     year = request.GET.get('year')
#     courses = Course.objects.filter(university_id=university_id, department_id = department_id, year = year, semester = semester).all()
#     return render(request, 'course_dropdown_list_options.html', {'courses': courses})

# def load_teachers(request):
#     university_id = request.GET.get('university_id')
#     department_id = request.GET.get('department_id')
#     teachers = Teacher.objects.filter(university_id=university_id, department_id = department_id).all()
#     print(teachers)
#     return render(request, 'teachers_dropdown_list_options.html', {'teachers': teachers})

@login_required
def submit_feedback(request, question_id):
    question = get_object_or_404(ResourcesQuestion, pk=question_id)
    exam_name = question.exam_name
    session = question.session
    course_name = question.course.title
    department_name = question.course.department.name
    university_name = question.course.department.university.name
    
    if request.method == 'POST':
        
        if question_id:  # Check if question_id is not an empty string
            feedback_text = request.POST.get('feedback')
            question = get_object_or_404(ResourcesQuestion, pk=question_id)
            question.feedback = feedback_text
            question.save()
        return HttpResponseRedirect(reverse('view_questions', args=[question.course.id]))

    
    # return HttpResponseRedirect(reverse('success_feedback'))
    
    return render(request, 'feedbacks/submit_feedback.html', {
        'question_id': question_id,
        'exam_name': exam_name,
        'session': session,
        'course_name': course_name,
        'department_name': department_name,
        'university_name': university_name
    })


def success_feedback(request):
    # Your logic for the success feedback view
    return render(request, 'feedbacks/success_feedback.html')

def view_feedback(request):
    feedbacks = ResourcesQuestion.objects.all() # Fetch all feedbacks (adjust as needed)
    return render(request, 'feedbacks/view_feedbacks.html', {'feedbacks': feedbacks})



from django.db.models import Q
from django.db.models import Sum
from django.db.models import Count, ExpressionWrapper, F, IntegerField, Subquery, OuterRef, Value
from django.db.models import Count, ExpressionWrapper, F, IntegerField, Subquery, OuterRef
from django.db.models.functions import Coalesce
from django.db.models import F, OuterRef, Subquery

@login_required
def leaderboard(request):
    # Exclude the profile with the specific email
    excluded_email = 'teams.onebyzeroedu@gmail.com'
    
    # Subquery to get the university and department from EduUniversity
    edu_university_subquery = EduUniversity.objects.filter(
        profile=OuterRef('pk')
    ).values('university__name', 'department__name')[:1]
    
    # Query all profiles, excluding the one with the specified email
    profiles_queryset = Profile.objects.exclude(
        user__email=excluded_email
    ).annotate(
        username=F('user__username'),
        user_fullname=F('fullname'),
        user_image=F('profile_image'),
        total_coins_annotated=F('total_coins'),
        university_name=Subquery(edu_university_subquery.values('university__name')),
        department_name=Subquery(edu_university_subquery.values('department__name')),
    ).values(
        'id', 'username', 'user_fullname', 'user_image', 'total_coins_annotated', 'university_name', 'department_name'
    ).order_by('-total_coins_annotated')
    
    # Get the current logged-in user's profile
    user_profile = request.user.profile
    user_total_coins = user_profile.total_coins
    
    # Find the user's rank in the leaderboard
    users_with_all_info = list(profiles_queryset)  # Convert queryset to list
    user_rank = None
    for rank, profile in enumerate(users_with_all_info, start=1):
        if profile['id'] == user_profile.id:
            user_rank = rank
            break

    # Limit to top 50 users
    top_50_users = users_with_all_info[:50]
    
    # Get all resource uploads, ordered by upload_time
   # Get all resource uploads, ordered by upload_time, limited to top 50
    # recent_uploads = sorted(
    #     list(ResourcesQuestion.objects.all()) +
    #     list(ResourcesNote.objects.all()) +
    #     list(ResourcesBook.objects.all()) +
    #     list(ResourcesLecture.objects.all()),
    #     key=lambda x: x.upload_time,
    #     reverse=True
    # )[:50]  # Limit to the top 50 recent uploads
    
    recent_uploads = sorted(
    list(ResourcesQuestion.objects.only('upload_time', 'exam_name').all()) +
    list(ResourcesNote.objects.only('upload_time', 'note_title').all()) +
    list(ResourcesBook.objects.only('upload_time', 'book_title').all()) +
    list(ResourcesLecture.objects.only('upload_time', 'lecture_title').all()),
    key=lambda x: x.upload_time,
    reverse=True
)[:50]

    context = {
        'users_with_all_info': top_50_users,  # Pass only the top 50
        'user_rank': user_rank,
        'user_total_coins': user_total_coins,
        'recent_uploads': recent_uploads,
    }
    
    return render(request, 'contributions/leaderboard.html', context)



# TEST PURPOSES ==============================
