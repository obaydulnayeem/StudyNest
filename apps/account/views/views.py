from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from ..forms import SignupForm, LoginForm, ProfileForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from ..models import *
from apps.notifications.models import *
from apps.university.models import *
from apps.mentorship.models import AskModel
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from ..forms import *

def user_login(request):  
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('my_department', university_id=1, department_id=1)
    else:
        form = LoginForm()
        # print('dkfjdk',form)
    return render(request, 'login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')

from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe

@login_required
def contribution_summary(request):
    # user = get_object_or_404(User, id=user_id)
    # Ensure that the user is authenticated
    # if not request.user.is_authenticated:
    #     return redirect('login')

    # Try to get the user's profile
    try:
    # Try to get the user's profile
        d_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
    # If the profile does not exist, create a new one
        d_profile = Profile.objects.create(user=request.user)
    
    # QUESTIONS ========================================
    qs_sem1 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='1st').count()
    # print('one',qs_sem1)
    
    qs_sem2 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='2nd').count()
    # print(qs_sem2)
    
    qs_sem3 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='3rd').count()
    
    qs_sem4 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='4th').count()
    
    qs_sem5 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='5th').count()
    
    qs_sem6 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='6th').count()
    
    qs_sem7 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='7th').count()
    
    qs_sem8 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='8th').count()
    
    qs_total = qs_sem1 + qs_sem2 + qs_sem3 + qs_sem4 + qs_sem5 + qs_sem6 + qs_sem7 + qs_sem8
    

# BOOKS ==============================================
    books_sem1 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='1st').count()
    
    books_sem2 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='2nd').count()
    
    books_sem3 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='3rd').count()
    
    books_sem4 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='4th').count()
    
    books_sem5 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='5th').count()
    
    books_sem6 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='6th').count()
    
    books_sem7 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='7th').count()
    
    books_sem8 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='8th').count()
    
    books_total = books_sem1 + books_sem2 + books_sem3 + books_sem4 + books_sem5 + books_sem6 + books_sem7 + books_sem8
    

# LECTURE SLIDES ============================================
    lectures_sem1 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='1st').count()
    
    lectures_sem2 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='2nd').count()
    
    lectures_sem3 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='3rd').count()
    
    lectures_sem4 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='4th').count()
    
    lectures_sem5 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='5th').count()
    
    lectures_sem6 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='6th').count()
    
    lectures_sem7 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='7th').count()
    
    lectures_sem8 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='8th').count()
    
    lectures_total = lectures_sem1 + lectures_sem2 + lectures_sem3 + lectures_sem4 + lectures_sem5 + lectures_sem6 + lectures_sem7 + lectures_sem8
    
    
# NOTES =============================================
    notes_sem1 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='1st').count()
    
    notes_sem2 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='2nd').count()
    
    notes_sem3 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='3rd').count()
    
    notes_sem4 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='4th').count()
    
    notes_sem5 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='5th').count()
    
    notes_sem6 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='6th').count()
    
    notes_sem7 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='7th').count()
    
    notes_sem8 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='8th').count()
    
    notes_total = notes_sem1 + notes_sem2 + notes_sem3 + notes_sem4 + notes_sem5 + notes_sem6 + notes_sem7 + notes_sem8
    
    # TOTAL UPLOADS ==================
    total_uploads = sum([qs_total, books_total, lectures_total, notes_total], 0)
    
    # TOTALS UPLOADS SEMESTER WISE
    all_sem1 = sum([qs_sem1, books_sem1, lectures_sem1, notes_sem1], 0)
    all_sem2 = sum([qs_sem2, books_sem2, lectures_sem2, notes_sem2], 0)
    all_sem3 = sum([qs_sem3, books_sem3, lectures_sem3, notes_sem3], 0)
    all_sem4 = sum([qs_sem4, books_sem4, lectures_sem4, notes_sem4], 0)
    all_sem5 = sum([qs_sem5, books_sem5, lectures_sem5, notes_sem5], 0)
    all_sem6 = sum([qs_sem6, books_sem6, lectures_sem6, notes_sem6], 0)
    all_sem7 = sum([qs_sem7, books_sem7, lectures_sem7, notes_sem7], 0)
    all_sem8 = sum([qs_sem8, books_sem8, lectures_sem8, notes_sem8], 0)
    
    # profile = get_object_or_404(Profile, user=request.user)
    # edu_university = EduUniversity.objects.filter(profile=d_profile)
    
   # Handle university and department info
    try:
        edu_university = EduUniversity.objects.get(profile=d_profile)
    except EduUniversity.DoesNotExist:
        edu_university = None  # Correct the variable name

    if edu_university is None:
        # Redirect the user if no EduUniversity exists
        return redirect('view_edu_university_my_profile')

    # university = d_profile.university
    # department = d_profile.department
    
    # You already have edu_university, no need to query again
    if edu_university.department:
        department_system = edu_university.department.system
        total_semester_or_year = edu_university.department.total_semester_or_year
    elif edu_university.discipline:
        department_system = edu_university.discipline.system
        total_semester_or_year = edu_university.discipline.total_semester_or_year
    elif edu_university.institute:
        department_system = edu_university.institute.system
        total_semester_or_year = edu_university.institute.total_semester_or_year
    else:
        department_system = 'Sem/Year'
        total_semester_or_year = 8
    
    context = {
        'department_system': department_system,
        'total_semester_or_year': total_semester_or_year,
        'd_profile': d_profile,
        'edu_university': edu_university,
        'qs_sem1': qs_sem1,
        'qs_sem2': qs_sem2,
        'qs_sem3': qs_sem3,
        'qs_sem4': qs_sem4,
        'qs_sem5': qs_sem5,
        'qs_sem6': qs_sem6,
        'qs_sem7': qs_sem7,
        'qs_sem8': qs_sem8,
        'qs_total': qs_total,
        
        'books_sem1': books_sem1,
        'books_sem2': books_sem2,
        'books_sem3': books_sem3,
        'books_sem4': books_sem4,
        'books_sem5': books_sem5,
        'books_sem6': books_sem6,
        'books_sem7': books_sem7,
        'books_sem8': books_sem8,
        'books_total': books_total,
        
        'lectures_sem1': lectures_sem1,
        'lectures_sem2': lectures_sem2,
        'lectures_sem3': lectures_sem3,
        'lectures_sem4': lectures_sem4,
        'lectures_sem5': lectures_sem5,
        'lectures_sem6': lectures_sem6,
        'lectures_sem7': lectures_sem7,
        'lectures_sem8': lectures_sem8,
        'lectures_total': lectures_total,
        
        'notes_sem1': notes_sem1,
        'notes_sem2': notes_sem2,
        'notes_sem3': notes_sem3,
        'notes_sem4': notes_sem4,
        'notes_sem5': notes_sem5,
        'notes_sem6': notes_sem6,
        'notes_sem7': notes_sem7,
        'notes_sem8': notes_sem8,
        'notes_total': notes_total,
        
        'total_uploads': total_uploads,
        
        'all_sem1': all_sem1,
        'all_sem2': all_sem2,
        'all_sem3': all_sem3,
        'all_sem4': all_sem4,
        'all_sem5': all_sem5,
        'all_sem6': all_sem6,
        'all_sem7': all_sem7,
        'all_sem8': all_sem8,
    }

    return render(request, 'profile/my_profile/contributions/contribution_summary.html', context)


def contribution_summary_view_profile(request, user_id):
    # print('uuu',user_id)
    # user = get_object_or_404(User, id=user_id)
    d_profile = get_object_or_404(Profile, id=user_id)
    
    # print(d_profile)
        # QUESTIONS ========================================
    qs_sem1 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='1st').count()
    # print('one',qs_sem1)
    
    qs_sem2 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='2nd').count()
    # print(qs_sem2)
    
    qs_sem3 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='3rd').count()
    
    qs_sem4 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='4th').count()
    
    qs_sem5 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='5th').count()
    
    qs_sem6 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='6th').count()
    
    qs_sem7 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='7th').count()
    
    qs_sem8 = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester='8th').count()
    
    qs_total = qs_sem1 + qs_sem2 + qs_sem3 + qs_sem4 + qs_sem5 + qs_sem6 + qs_sem7 + qs_sem8
    

# BOOKS ==============================================
    books_sem1 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='1st').count()
    
    books_sem2 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='2nd').count()
    
    books_sem3 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='3rd').count()
    
    books_sem4 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='4th').count()
    
    books_sem5 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='5th').count()
    
    books_sem6 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='6th').count()
    
    books_sem7 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='7th').count()
    
    books_sem8 = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester='8th').count()
    
    books_total = books_sem1 + books_sem2 + books_sem3 + books_sem4 + books_sem5 + books_sem6 + books_sem7 + books_sem8
    

# LECTURE SLIDES ============================================
    lectures_sem1 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='1st').count()
    
    lectures_sem2 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='2nd').count()
    
    lectures_sem3 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='3rd').count()
    
    lectures_sem4 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='4th').count()
    
    lectures_sem5 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='5th').count()
    
    lectures_sem6 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='6th').count()
    
    lectures_sem7 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='7th').count()
    
    lectures_sem8 = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester='8th').count()
    
    lectures_total = lectures_sem1 + lectures_sem2 + lectures_sem3 + lectures_sem4 + lectures_sem5 + lectures_sem6 + lectures_sem7 + lectures_sem8
    
    
# NOTES =============================================
    notes_sem1 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='1st').count()
    
    notes_sem2 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='2nd').count()
    
    notes_sem3 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='3rd').count()
    
    notes_sem4 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='4th').count()
    
    notes_sem5 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='5th').count()
    
    notes_sem6 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='6th').count()
    
    notes_sem7 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='7th').count()
    
    notes_sem8 = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester='8th').count()
    
    notes_total = notes_sem1 + notes_sem2 + notes_sem3 + notes_sem4 + notes_sem5 + notes_sem6 + notes_sem7 + notes_sem8
    
    # TOTAL UPLOADS ==================
    total_uploads = sum([qs_total, books_total, lectures_total, notes_total], 0)
    
    # TOTALS UPLOADS SEMESTER WISE
    all_sem1 = sum([qs_sem1, books_sem1, lectures_sem1, notes_sem1], 0)
    all_sem2 = sum([qs_sem2, books_sem2, lectures_sem2, notes_sem2], 0)
    all_sem3 = sum([qs_sem3, books_sem3, lectures_sem3, notes_sem3], 0)
    all_sem4 = sum([qs_sem4, books_sem4, lectures_sem4, notes_sem4], 0)
    all_sem5 = sum([qs_sem5, books_sem5, lectures_sem5, notes_sem5], 0)
    all_sem6 = sum([qs_sem6, books_sem6, lectures_sem6, notes_sem6], 0)
    all_sem7 = sum([qs_sem7, books_sem7, lectures_sem7, notes_sem7], 0)
    all_sem8 = sum([qs_sem8, books_sem8, lectures_sem8, notes_sem8], 0)
    
    # profile = get_object_or_404(Profile, user=request.user)
    edu_university = EduUniversity.objects.filter(profile=d_profile)
    
    # Handle university and department info
    # try:
    #     edu_university = EduUniversity.objects.get(profile=d_profile)
    # except EduUniversity.DoesNotExist:
    #     edu_university = None

    # if edu_university is None:
    #     # Redirect the user if no EduUniversity exists
    #     return redirect('view_profile_overview', user_id)

    
  
    # try:
    #     profile_edu_university = EduUniversity.objects.get(profile=d_profile)
    # except EduUniversity.DoesNotExist:
    #     profile_edu_university = None

    # if profile_edu_university.department:
    #     department_system = profile_edu_university.department.system
    #     total_semester_or_year = profile_edu_university.department.total_semester_or_year
    # elif profile_edu_university.discipline:
    #     department_system = profile_edu_university.discipline.system
    #     total_semester_or_year = profile_edu_university.discipline.total_semester_or_year
    # elif profile_edu_university.institute:
    #     department_system = profile_edu_university.institute.system
    #     total_semester_or_year = profile_edu_university.institute.total_semester_or_year
    # else:
    #     department_system = 'Sem/Year'
    #     total_semester_or_year = 8
    
    try:
        profile_edu_university = EduUniversity.objects.get(profile=d_profile)
    except EduUniversity.DoesNotExist:
        profile_edu_university = None

# Check if profile_edu_university is None before proceeding
    if profile_edu_university:
        # Check if department exists
        if profile_edu_university.department:
            department_system = profile_edu_university.department.system
            total_semester_or_year = profile_edu_university.department.total_semester_or_year
        # Check if discipline exists
        elif profile_edu_university.discipline:
            department_system = profile_edu_university.discipline.system
            total_semester_or_year = profile_edu_university.discipline.total_semester_or_year
        # Check if institute exists
        elif profile_edu_university.institute:
            department_system = profile_edu_university.institute.system
            total_semester_or_year = profile_edu_university.institute.total_semester_or_year
        # Default case when none of the above exists
        else:
            department_system = 'Sem/Year'
            total_semester_or_year = 8
    else:
        # Handle the case where profile_edu_university is None
        department_system = 'Sem/Year'
        total_semester_or_year = 8


    
    context = {
        'd_user': d_profile,
        'department_system': department_system,
        'total_semester_or_year': total_semester_or_year,
        'd_profile': d_profile,
        'edu_university': edu_university,
        'qs_sem1': qs_sem1,
        'qs_sem2': qs_sem2,
        'qs_sem3': qs_sem3,
        'qs_sem4': qs_sem4,
        'qs_sem5': qs_sem5,
        'qs_sem6': qs_sem6,
        'qs_sem7': qs_sem7,
        'qs_sem8': qs_sem8,
        'qs_total': qs_total,
        
        'books_sem1': books_sem1,
        'books_sem2': books_sem2,
        'books_sem3': books_sem3,
        'books_sem4': books_sem4,
        'books_sem5': books_sem5,
        'books_sem6': books_sem6,
        'books_sem7': books_sem7,
        'books_sem8': books_sem8,
        'books_total': books_total,
        
        'lectures_sem1': lectures_sem1,
        'lectures_sem2': lectures_sem2,
        'lectures_sem3': lectures_sem3,
        'lectures_sem4': lectures_sem4,
        'lectures_sem5': lectures_sem5,
        'lectures_sem6': lectures_sem6,
        'lectures_sem7': lectures_sem7,
        'lectures_sem8': lectures_sem8,
        'lectures_total': lectures_total,
        
        'notes_sem1': notes_sem1,
        'notes_sem2': notes_sem2,
        'notes_sem3': notes_sem3,
        'notes_sem4': notes_sem4,
        'notes_sem5': notes_sem5,
        'notes_sem6': notes_sem6,
        'notes_sem7': notes_sem7,
        'notes_sem8': notes_sem8,
        'notes_total': notes_total,
        
        'total_uploads': total_uploads,
        
        'all_sem1': all_sem1,
        'all_sem2': all_sem2,
        'all_sem3': all_sem3,
        'all_sem4': all_sem4,
        'all_sem5': all_sem5,
        'all_sem6': all_sem6,
        'all_sem7': all_sem7,
        'all_sem8': all_sem8,
    }
    
    return render(request, 'profile/view_profile/contributions/contribution_summary_view_profile.html', context)


@login_required
def detailed_contribution(request):
    # user = get_object_or_404(User, id=user_id)
    # Ensure that the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')

    # Try to get the user's profile
    try:
    # Try to get the user's profile
        d_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
    # If the profile does not exist, create a new one
        d_profile = Profile.objects.create(user=request.user)
    
    # edu_university = EduUniversity.objects.get(profile=d_profile)
    
    # Handle university and department info
    try:
        edu_university = EduUniversity.objects.get(profile=d_profile)
    except EduUniversity.DoesNotExist:
        edu_university = None

    if edu_university is None:
        # Redirect the user if no EduUniversity exists
        return redirect('view_edu_university_my_profile')
    
    department = edu_university.department
    
        # Helper function to get resources by course for a specific semester
    def get_resources_by_course(semester):
        courses = Course.objects.filter(semester=semester, department=department)
        questions = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester=semester, course__department=department)
        books = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester=semester, course__department=department)
        notes = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester=semester, course__department=department)
        lectures = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester=semester, course__department=department)

        resources_by_course = {}
        for course in courses:
            resources_by_course[course.title] = {
                'questions': questions.filter(course=course),
                'books': books.filter(course=course),
                'notes': notes.filter(course=course),
                'lectures': lectures.filter(course=course),
            }

        return resources_by_course

    # Get resources for each semester
    resources_by_semester = {
        '1st': get_resources_by_course('1st'),
        '2nd': get_resources_by_course('2nd'),
        '3rd': get_resources_by_course('3rd'),
        '4th': get_resources_by_course('4th'),
        '5th': get_resources_by_course('5th'),
        '6th': get_resources_by_course('6th'),
        '7th': get_resources_by_course('7th'),
        '8th': get_resources_by_course('8th'),
    }
    
    # profile = get_object_or_404(Profile, user=request.user)
    # edu_university = EduUniversity.objects.filter(profile=d_profile)

    try:
        profile_edu_university = EduUniversity.objects.get(profile=d_profile)
    except EduUniversity.DoesNotExist:
        profile_edu_university = None
        
    # university = profile_edu_university.university
    if profile_edu_university.department:
        department_system = profile_edu_university.department.system
        total_semester_or_year = profile_edu_university.department.total_semester_or_year
    elif profile_edu_university.discipline:
        department_system = profile_edu_university.discipline.system
        total_semester_or_year = profile_edu_university.discipline.total_semester_or_year
    elif profile_edu_university.institute:
        department_system = profile_edu_university.institute.system
        total_semester_or_year = profile_edu_university.institute.total_semester_or_year
    else:
        department_system = 'Sem/Year'
        total_semester_or_year = 8

    # if d_profile.fullname is None and d_profile.nickname is None:
    #     messages.success(request, mark_safe("অনুগ্রহ করে আপনার নামের সম্পর্কিত তথ্যাবলী আপডেট করুন।"))

    # if university is None and department is None:
    #     messages.success(request, mark_safe("Please update your <strong>University</strong>, <strong>Faculty</strong> and <strong>Department</strong> to show any resources!"))

    
    context = {
        'resources_by_semester': resources_by_semester,
        'd_profile': d_profile,
        'department_system': department_system,
        'total_semester_or_year': total_semester_or_year,
        # 'edu_university': edu_university,
    }

    return render(request, 'profile/my_profile/contributions/detailed_contribution.html', context)


def detailed_contribution_view_profile(request, user_id):
    # user = get_object_or_404(User, id=user_id)
    d_profile = get_object_or_404(Profile, id=user_id)
    # print(d_profile)
    
    # edu_university = EduUniversity.objects.get(profile=d_profile)
    try:
        edu_university = EduUniversity.objects.get(profile=d_profile)
        department = edu_university.department
    except EduUniversity.DoesNotExist:
        edu_university = None
        department = None  # Set department to None or handle as needed

        # Helper function to get resources by course for a specific semester
    def get_resources_by_course(semester):
        courses = Course.objects.filter(semester=semester, department=department)
        questions = ResourcesQuestion.objects.filter(uploaded_by=d_profile, course__semester=semester, course__department=department)
        books = ResourcesBook.objects.filter(uploaded_by=d_profile, course__semester=semester, course__department=department)
        notes = ResourcesNote.objects.filter(uploaded_by=d_profile, course__semester=semester, course__department=department)
        lectures = ResourcesLecture.objects.filter(uploaded_by=d_profile, course__semester=semester, course__department=department)

        resources_by_course = {}
        for course in courses:
            resources_by_course[course.title] = {
                'questions': questions.filter(course=course),
                'books': books.filter(course=course),
                'notes': notes.filter(course=course),
                'lectures': lectures.filter(course=course),
            }

        return resources_by_course

    # Get resources for each semester
    resources_by_semester = {
        '1st': get_resources_by_course('1st'),
        '2nd': get_resources_by_course('2nd'),
        '3rd': get_resources_by_course('3rd'),
        '4th': get_resources_by_course('4th'),
        '5th': get_resources_by_course('5th'),
        '6th': get_resources_by_course('6th'),
        '7th': get_resources_by_course('7th'),
        '8th': get_resources_by_course('8th'),
    }
    
    # profile = get_object_or_404(Profile, user=request.user)
    # edu_university = EduUniversity.objects.filter(profile=d_profile)

    try:
        profile_edu_university = EduUniversity.objects.get(profile=d_profile)
    except EduUniversity.DoesNotExist:
        profile_edu_university = None

    # Ensure profile_edu_university is not None before proceeding
    if profile_edu_university:
        if profile_edu_university.department:
            department_system = profile_edu_university.department.system
            total_semester_or_year = profile_edu_university.department.total_semester_or_year
        elif profile_edu_university.discipline:
            department_system = profile_edu_university.discipline.system
            total_semester_or_year = profile_edu_university.discipline.total_semester_or_year
        elif profile_edu_university.institute:
            department_system = profile_edu_university.institute.system
            total_semester_or_year = profile_edu_university.institute.total_semester_or_year
        else:
            department_system = 'Sem/Year'
            total_semester_or_year = 8
    else:
        # If profile_edu_university is None, use default values
        department_system = 'Sem/Year'
        total_semester_or_year = 8




    
    context = {
        'd_user': d_profile,
        'resources_by_semester': resources_by_semester,
        'd_profile': d_profile,
        'department_system': department_system,
        'total_semester_or_year': total_semester_or_year,
        # 'edu_university': edu_university,
    }

    return render(request, 'profile/view_profile/contributions/detailed_contribution_view_profile.html', context)



def coin_details(request):
    return render(request, 'coin_details.html')