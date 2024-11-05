from django.shortcuts import render
from apps.account.models.profile_models import Profile
from apps.account.models.education_models import EduUniversity
from apps.university.models import *
from apps.feedback.models import Feedback
from django.contrib.auth.models import User
from django.db.models import Q

def home(request):
    # TOTALS
    total_questions = ResourcesQuestion.objects.count()
    total_books = ResourcesBook.objects.count()
    total_notes = ResourcesNote.objects.count()
    total_slides = ResourcesLecture.objects.count()
    total_resources = total_questions + total_books + total_notes + total_slides
    
    total_universities = University.objects.count()
    total_faculties = Faculty.objects.count()
    total_institutes = Institute.objects.count()
    total_schools = School.objects.count()
    total_centers = Center.objects.count()
    total_departments = Department.objects.count()
    total_disciplines = Discipline.objects.count()
    total_courses = Course.objects.count()
    total_students = User.objects.count()
    
    user = request.user
    university = None
    department = None
    # year = None
    semester = None
    
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            # Use filter().first() to avoid DoesNotExist exception
            profile_edu_university = EduUniversity.objects.filter(profile=profile).first()
            university = profile_edu_university.university if profile_edu_university else None
            department = profile_edu_university.department if profile_edu_university else None
            semester = profile_edu_university.semester if profile_edu_university else None
        except Profile.DoesNotExist:
            # Handle the case where the profile itself does not exist
            profile = None
            university = None
            department = None
            semester = None
    else:
        profile = None
        university = None
        department = None
        semester = None
    
    feedbacks = Feedback.objects.all().order_by('-created_at')
    
    # Search functionality
    query = request.GET.get('q', '')
    if query:
        universities = University.objects.filter(
            Q(acronym__icontains=query) |
            Q(name__icontains=query) |
            Q(location_district__icontains=query) |
            Q(location_division__icontains=query)
        )

        departments = Department.objects.filter(
            Q(name__icontains=query) |
            Q(university__name__icontains=query)
        )
        
        courses = Course.objects.filter(
            Q(title__icontains=query) |
            Q(code__icontains=query) |
            Q(department__name__icontains=query) |
            Q(department__university__name__icontains=query)
        )
        
        profiles = Profile.objects.filter(
        Q(user__username__icontains=query) |
        Q(fullname__icontains=query) |
        Q(nickname__icontains=query) |
        Q(email__icontains=query)
    )

        total_search_results_universities = universities.count()
        total_search_results_departments = departments.count()
        total_search_results_courses = courses.count()
        total_search_results_profiles = profiles.count()
    else:
        universities = University.objects.all()
        departments = Department.objects.all()
        courses = Course.objects.all()
        profiles = Profile.objects.all()
        
        total_search_results_universities = universities.count()
        total_search_results_departments = departments.count()
        total_search_results_courses = courses.count()
        total_search_results_profiles = profiles.count()


    context = {
        'profile': profile,
        'total_questions': total_questions,
        'total_books': total_books,
        'total_slides': total_slides,
        'total_notes': total_notes,
        'total_resources': total_resources,
        'total_courses': total_courses,
        'total_universities': total_universities,
        'total_faculties': total_faculties,
        'total_institutes': total_institutes,
        'total_schools': total_schools,
        'total_centers': total_centers,
        'total_departments': total_departments,
        'total_disciplines': total_disciplines,
        'total_students': total_students,
        'university': university,
        'department': department,
        # 'year': year,
        'semester': semester,
        'feedbacks': feedbacks,
        'universities': universities,
        'departments': departments,
        'courses': courses,
        'profiles': profiles,
        'total_search_results_universities': total_search_results_universities,
        'total_search_results_departments': total_search_results_departments,
        'total_search_results_courses': total_search_results_courses,
        'total_search_results_profiles': total_search_results_profiles,
        'query': query,
        'is_home': True,
    }

    return render(request, 'home/home_base.html', context)

