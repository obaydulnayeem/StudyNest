from django.shortcuts import render, redirect
from apps.account.models.profile_models import *
from apps.university.models import *
from django.db.models import Max
from utils.permissions import *
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import *
from .forms import *
from django.db.models import Sum

@user_passes_test(is_team_member, login_url='home')
def team_base(request):
    return render(request, 'team_base.html')

@user_passes_test(is_team_member, login_url='home')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.team_member = request.user.profile  # Set the team member to the logged-in user
            task.save()
            return redirect('view_tasks')  # Redirect to a view that shows tasks
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@user_passes_test(is_team_member, login_url='home')
def view_tasks(request):
    # tasks = Task.objects.filter(team_member=request.user.profile)  # Display only tasks of the logged-in user
    tasks = Task.objects.all().order_by('-date')
    
    
    # Add formatted duration to each task
    for task in tasks:
        total_minutes = task.duration
        hours, minutes = divmod(total_minutes, 60)
        task.duration_formatted = f"{hours}h {minutes}m"
    
    # Calculate total duration for each team member
    total_durations = (
        Task.objects.values('team_member__fullname', 'team_member__id')
        .annotate(total_duration=Sum('duration'))
        .order_by('-total_duration')
    )
    
    # Convert durations to hours and minutes
    for duration in total_durations:
        total_minutes = duration['total_duration']
        hours, minutes = divmod(total_minutes, 60)
        duration['total_duration_formatted'] = f"{hours}h {minutes}m"

    context = {
        'tasks': tasks,
        'total_durations': total_durations
    }
    
    return render(request, 'view_tasks.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_all_universities_team(request):
    universities = University.objects.all()
    
    context = {
        'universities': universities
    }
    
    return render(request, 'show_all_universities_team.html', context)

@user_passes_test(is_team_member, login_url='home')
def show_university_team(request, university_id):
    university = get_object_or_404(University, id=university_id)
    faculties = Faculty.objects.filter(university=university)
    institutes = Institute.objects.filter(university=university)
    schools = School.objects.filter(university=university)
    centers = Center.objects.filter(university=university)
    departments = Department.objects.filter(university=university)
    disciplines = Discipline.objects.filter(university=university)

    # Count the number of courses for each department
    departments_with_course_counts = departments.annotate(num_courses=Count('course'))

    context = {
        'university': university,
        'faculties': faculties,
        'institutes': institutes,
        'schools': schools,
        'centers': centers,
        'departments': departments_with_course_counts,
        'disciplines': disciplines,
    }

    return render(request, 'show_university_team.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_department_team(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    university = department.university
    # departments = Department.objects.filter(university=university)
    
    # courses = Course.objects.filter(department=department).order_by('')
    # Annotate courses with the total number of common courses and order by this count
    courses = Course.objects.filter(department=department).annotate(
        num_common_courses=Count('common_courses')
    ).order_by('num_common_courses')  # Ordering from lowest to highest

    
    context = {
        'university': university,
        'department': department,
        'courses': courses,
    }
    return render(request, 'show_department_team.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_course_team(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    department = course.department
    # Assuming 'team_members' is a ManyToMany or ForeignKey field related to the course
    # team_members = course.team_members.all()

    context = {
        'course': course,
        'common_courses': course.common_courses.all(),
        'department': department,
        # 'team_members': team_members,
    }
    return render(request, 'show_course_team.html', context)


@user_passes_test(is_batch_or_central_moderator, login_url='home')
def resource_uploads(request):
    maria_qs = ResourcesQuestion.objects.filter(uploaded_by_team = 'Maria Islam').count()
    maria_bk = ResourcesBook.objects.filter(uploaded_by_team = 'Maria Islam').count()
    maria_nt = ResourcesNote.objects.filter(uploaded_by_team = 'Maria Islam').count()
    maria_lc = ResourcesLecture.objects.filter(uploaded_by_team = 'Maria Islam').count()
    
    baishakhi_qs = ResourcesQuestion.objects.filter(uploaded_by_team = 'Baishakhi Bir').count()
    baishakhi_bk = ResourcesBook.objects.filter(uploaded_by_team = 'Baishakhi Bir').count()
    baishakhi_nt = ResourcesNote.objects.filter(uploaded_by_team = 'Baishakhi Bir').count()
    baishakhi_lc = ResourcesLecture.objects.filter(uploaded_by_team = 'Baishakhi Bir').count()
    
    samia_qs = ResourcesQuestion.objects.filter(uploaded_by_team = 'Ritu Akter Samia').count()
    samia_bk = ResourcesBook.objects.filter(uploaded_by_team = 'Ritu Akter Samia').count()
    samia_nt = ResourcesNote.objects.filter(uploaded_by_team = 'Ritu Akter Samia').count()
    samia_lc = ResourcesLecture.objects.filter(uploaded_by_team = 'Ritu Akter Samia').count()
    
    tanvir_qs = ResourcesQuestion.objects.filter(uploaded_by_team = 'Md. Tanvir Ahmed').count()
    tanvir_lc = ResourcesLecture.objects.filter(uploaded_by_team = 'Md. Tanvir Ahmed').count()
    tanvir_bk = ResourcesBook.objects.filter(uploaded_by_team = 'Md. Tanvir Ahmed').count()
    tanvir_nt = ResourcesNote.objects.filter(uploaded_by_team = 'Md. Tanvir Ahmed').count()
    
    
    rayhan_qs = ResourcesQuestion.objects.filter(uploaded_by_team = 'Md Rayhanul Islam Rony').count()
    rayhan_lc = ResourcesLecture.objects.filter(uploaded_by_team = 'Md Rayhanul Islam Rony').count()
    rayhan_bk = ResourcesBook.objects.filter(uploaded_by_team = 'Md Rayhanul Islam Rony').count()
    rayhan_nt = ResourcesNote.objects.filter(uploaded_by_team = 'Md Rayhanul Islam Rony').count()
    
    
    # Get the latest upload time from each model
    latest_resource_question = ResourcesQuestion.objects.aggregate(latest=Max('upload_time'))['latest']
    latest_resource_book = ResourcesBook.objects.aggregate(latest=Max('upload_time'))['latest']
    latest_resource_note = ResourcesNote.objects.aggregate(latest=Max('upload_time'))['latest']
    latest_resource_lecture = ResourcesLecture.objects.aggregate(latest=Max('upload_time'))['latest']

    # Filter out None values and find the latest time
    latest_upload_times = [
        latest_resource_question,
        latest_resource_book,
        latest_resource_note,
        latest_resource_lecture
    ]

    # Get the latest time
    latest_upload = max(filter(None, latest_upload_times))

    
    total_qs = ResourcesQuestion.objects.all().count()
    total_bk = ResourcesBook.objects.all().count()
    total_nt = ResourcesNote.objects.all().count()
    total_lc = ResourcesLecture.objects.all().count()
    total_tl = total_qs + total_bk + total_nt + total_lc
    
    
    context = {
        'maria_qs': maria_qs,
        'maria_bk': maria_bk,
        'maria_nt': maria_nt,
        'maria_lc': maria_lc,
        'maria_tl': maria_qs + maria_bk + maria_nt + maria_lc,
        
        'baishakhi_qs': baishakhi_qs,
        'baishakhi_bk': baishakhi_bk,
        'baishakhi_nt': baishakhi_nt,
        'baishakhi_lc': baishakhi_lc,
        'baishakhi_tl': baishakhi_qs + baishakhi_bk + baishakhi_nt + baishakhi_lc,
        
        'samia_qs': samia_qs,
        'samia_bk': samia_bk,
        'samia_nt': samia_nt,
        'samia_lc': samia_lc,
        'samia_tl': samia_qs + samia_bk + samia_nt + samia_lc,
        
        'tanvir_qs': tanvir_qs,
        'tanvir_lc': tanvir_lc,
        'tanvir_bk': tanvir_bk,
        'tanvir_nt': tanvir_nt,
        'tanvir_tl': tanvir_qs + tanvir_bk + tanvir_nt + tanvir_lc,
        
        'rayhan_qs': rayhan_qs,
        'rayhan_lc': rayhan_lc,
        'rayhan_bk': rayhan_bk,
        'rayhan_nt': rayhan_nt,
        'rayhan_tl': rayhan_qs + rayhan_bk + rayhan_nt + rayhan_lc,
        
        'latest_upload': latest_upload,
        
        'total_qs': total_qs,
        'total_bk': total_bk,
        'total_nt': total_nt,
        'total_lc': total_lc,
        'total_tl': total_tl
    }
    

    return render(request, 'resource_uploads.html', context)



from django.db.models import Count
from django.shortcuts import render

def previous_uploaders_total_contribution(request):
    
    request.user.profile.has_clicked_previous_coin_announce = True
    
    # if request.user.profile.edu_university.department != 'Computer Science and Engineering' and request.user.profile.edu_university.university != 'University of Barishal':
    #     return redirect('home')
    
    # Create a list to hold the data for each user
    contributions = []

    # Define the coin values
    coin_values = {
        'question': 30,
        'book': 20,
        'note': 50,
        'lecture': 10,
    }

    # Iterate over all users in PREV_USERS_CHOICES
    for user, _ in PREV_USERS_CHOICES:
        # Calculate individual contributions
        questions_count = ResourcesQuestion.objects.filter(uploaded_by_prev=user).count()
        notes_count = ResourcesNote.objects.filter(uploaded_by_prev=user).count()
        books_count = ResourcesBook.objects.filter(uploaded_by_prev=user).count()
        lectures_count = ResourcesLecture.objects.filter(uploaded_by_prev=user).count()

        # Calculate individual coins
        questions_coins = questions_count * coin_values['question']
        notes_coins = notes_count * coin_values['note']
        books_coins = books_count * coin_values['book']
        lectures_coins = lectures_count * coin_values['lecture']

        # Calculate total contributions and total coins
        total_contributions = questions_count + notes_count + books_count + lectures_count
        total_coins = questions_coins + notes_coins + books_coins + lectures_coins

        # Append the data to the contributions list
        contributions.append({
            'user': user,
            'questions': questions_count,
            'notes': notes_count,
            'books': books_count,
            'lectures': lectures_count,
            'total_contributions': total_contributions,
            'questions_coins': questions_coins,
            'notes_coins': notes_coins,
            'books_coins': books_coins,
            'lectures_coins': lectures_coins,
            'total_coins': total_coins,
        })

    # Sort the contributions list by total coins in descending order
    contributions.sort(key=lambda x: x['total_coins'], reverse=True)

    # Render the template with the sorted contributions data
    return render(request, 'previous_uploaders_total_contribution.html', {'contributions': contributions})


def requested_for_previous_coin(request):
    
    profile = request.user.profile
    
    if not profile.has_req_for_prev_coin:
        profile.has_req_for_prev_coin = True
        profile.save()
        messages.success(request, 'ধন্যবাদ! আমরা আপনার Request টি পেয়েছি। শীঘ্রই আমরা আপনার প্রোফাইল যাচাই করে পূর্বের ওয়েবসাইটে আপলোডের জন্য পাওনা কয়েনগুলো বর্তমান কয়েনের সাথে যুক্ত করে দিবো।')
    
    return render(request, 'previous_uploaders_total_contribution.html')

@user_passes_test(is_team_member, login_url='home')
def show_common_courses_team(request):
    common_courses = CommonCourse.objects.all().order_by('title')
    return render(request, 'show_common_courses_team.html', {'common_courses': common_courses})

@user_passes_test(is_team_member, login_url='home')
def add_common_course(request):
    if request.method == 'POST':
        form = CommonCourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Common Course added successfully!')
            return redirect('show_common_courses_team')  # Redirect to the same page or another view
    else:
        form = CommonCourseForm()

    return render(request, 'add_common_course.html', {'form': form})

@user_passes_test(is_team_member, login_url='home')
def edit_common_course(request, course_id):
    course = get_object_or_404(CommonCourse, id=course_id)
    
    if request.method == 'POST':
        form = CommonCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('show_common_courses_team')  # Redirect to the same page or another view
    else:
        form = CommonCourseForm(instance=course)

    return render(request, 'edit_common_course.html', {'form': form, 'course': course})

@user_passes_test(is_team_member, login_url='home')
def delete_common_course(request, course_id):
    course = get_object_or_404(CommonCourse, id=course_id)

    course.delete()
    messages.success(request, "The common course deleted successfully!")
    return redirect('show_common_courses_team')


@user_passes_test(is_team_member, login_url='home')
def edit_common_courses(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CourseCommonCoursesForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('show_department_team', department_id=course.department.id)  # Redirect to course detail or another page
    else:
        form = CourseCommonCoursesForm(instance=course)

    return render(request, 'edit_common_courses.html', {'form': form, 'course': course})
