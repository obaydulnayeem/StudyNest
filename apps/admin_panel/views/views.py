from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import *
from apps.account.models import *
from apps.university.models import *
from apps.notifications.models import *
from django.contrib.auth.models import User
from ..forms import *
from django.contrib import messages
from datetime import datetime
from apps.university.templatetags.semester_year_filters import semester_converter
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from utils.permissions import *

@user_passes_test(is_team_member, login_url='home')
def moderator_base(request):
    return render(request, 'moderators/moderator_base.html')


@user_passes_test(is_team_member, login_url='home')
def department_info_moderator(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    
    if request.method == 'POST':
        form = EditDepartmentInfoModerator(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_info_moderator', department_id=department.id)
    else:
        form = EditDepartmentInfoModerator(instance=department)

    context = {
        'department': department,
        'form': form,
    }
    return render(request, 'moderators/department/department_info_moderator.html', context)


@user_passes_test(is_team_member, login_url='home')
def edit_department_info_moderator(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    
    if request.method == 'POST':
        form = EditDepartmentInfoModerator(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_info_moderator', department_id=department.id)
    else:
        form = EditDepartmentInfoModerator(instance=department)

    context = {
        'form': form,
        'department': department,
    }
    return render(request, 'moderators/department/edit_department_info_moderator.html', context)


@user_passes_test(is_team_member, login_url='home')
def edit_syllabus(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    
    # Print university for debugging
    print(f"University for the department: {department.university}")
    
    if request.method == 'POST':
        print("POST data:", request.POST)  # Debugging POST data
        print("FILES data:", request.FILES)  # Debugging FILES data
        
        form = SyllabusForm(request.POST, request.FILES, instance=department)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Syllabus file uploaded successfully!")
            return redirect('department_info_moderator', department_id=department.id)
        else:
            print("Form errors:", form.errors)  # Print form errors for debugging
    else:
        form = SyllabusForm(instance=department)
    
    return render(request, 'moderators/department/edit_syllabus.html', {'form': form, 'department': department})


@user_passes_test(is_team_member, login_url='home')
def course_details(request):
    profile = Profile.objects.get(user=request.user)
    
    # Get the EduUniversity instance for the profile
    edu_university = EduUniversity.objects.get(profile=profile)
    university = edu_university.university
    department = edu_university.department

    total_semester_or_year = department.total_semester_or_year

    context = {
        'university': university,
        'department': department,
        'total_semester_or_year': total_semester_or_year,
    }
    
    return render(request, 'moderators/department/course_details.html', context)


@user_passes_test(is_team_member, login_url='home')
def view_courses_s(request, university_id, department_id, semester_id):
    
    courses = Course.objects.filter(university_id=university_id, department_id=department_id, semester=semester_converter(semester_id)).order_by('created_at')
    
    semester_name = semester_converter(semester_id)
    department_name = Department.objects.get(id=department_id).name
    university_name = University.objects.get(id=university_id).name
    
    # print(university_id, department_id, year_id, sem_id)
    
    context = {
        'courses': courses,
        'university_name': university_name,
        'department_name': department_name,
        'semester_name': semester_name
    }
    
    return render(request, 'moderators/department/view_courses_s.html', context)


@user_passes_test(is_team_member, login_url='home')
def add_course(request):
    profile = Profile.objects.get(user=request.user)
    
    # Get the EduUniversity instance for the profile
    edu_university = EduUniversity.objects.get(profile=profile)
    
    # Extract IDs
    university_id = edu_university.university.id
    department_id = edu_university.department.id
    faculty_id = edu_university.faculty.id
    department_system = edu_university.department.system
    
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        semester = request.POST.get('semester')
        semester = semester_converter(semester)
        
        if form.is_valid():
            course = form.save(commit=False)
            course.university = edu_university.university
            course.faculty = edu_university.faculty
            course.department = edu_university.department
            course.save()
            
            messages.success(request, "Course added successfully!")
            print(form.errors)
            
            return redirect('show_department_team', department_id=department_id)
    else:
        form = AddCourseForm()
        print(form.errors)
        
    context = {
        'form': form,
        'department_system': department_system,
    }
    
    return render(request, 'moderators/department/add_course.html', context)

@user_passes_test(is_team_member, login_url='home')
def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    
    university_id = course.university.id
    department_id = course.department.id
    # year_id = course.year
    # semester = course.semester
    semester = semester_converter(course.semester)
    profile = Profile.objects.get(user=request.user)
    edu_university = EduUniversity.objects.get(profile=profile)
    department_system = edu_university.department.system

    # print(semester)
    
    
    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=course)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('show_course_team', course_id=course_id)
    else:
        form = EditCourseForm(instance=course)
    return render(request, 'moderators/department/edit_course.html', {'form': form, 'course': course, 'department_system': department_system})

@user_passes_test(is_team_member, login_url='home')
def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    messages.success(request, "Course deleted successfully!")
    return redirect('view_courses_s', university_id=course.university.id, department_id=course.department.id, semester_id=semester_converter(course.semester))


@user_passes_test(is_team_member, login_url='home')
def pending_user_list(request):
    # Get the profile of the logged-in moderator
    moderator_profile = get_object_or_404(Profile, user=request.user)

    # Initialize variables
    moderator_edu_university = None
    moderator_department = None

    # Get the associated EduUniversity and Department
    try:
        moderator_edu_university = EduUniversity.objects.get(profile=moderator_profile)
        moderator_department = moderator_edu_university.department
        moderator_batch = moderator_edu_university.departmental_batch
    except EduUniversity.DoesNotExist:
        pass

    # Retrieve all profiles where the department matches the moderator's department
    # users_list = Profile.objects.filter(eduuniversity__department=moderator_department) if moderator_department else Profile.objects.none()

    # List all pending profiles for approval
    pending_profiles = EduUniversity.objects.filter(department=moderator_department, departmental_batch=moderator_batch, is_approved=False).order_by('-created_at')
    
    approved_profiles = EduUniversity.objects.filter(department=moderator_department, departmental_batch=moderator_batch, is_approved=True).order_by('-created_at')
    
    pending_profiles_departmental_mod = EduUniversity.objects.filter(department=moderator_department, is_approved=False).order_by('-created_at')
    
    approved_profiles_departmental_mod = EduUniversity.objects.filter(department=moderator_department, is_approved=True).order_by('-created_at')
    
    all_pending_profiles = EduUniversity.objects.filter(is_approved=False).order_by('-created_at')
    
    approved_profiles_central_mod = EduUniversity.objects.filter(is_approved=True).order_by('-created_at')

    return render(request, 'moderators/batch/pending_user_list.html', {
        # 'users_list': users_list,
        'pending_profiles': pending_profiles,
        'approved_profiles': approved_profiles,
        
        'pending_profiles_departmental_mod': pending_profiles_departmental_mod,
        'approved_profiles_departmental_mod': approved_profiles_departmental_mod,
        
        'moderator_department': moderator_department,
        'moderator_university': moderator_edu_university.university if moderator_edu_university else None,
        # 'mod_edu_university': moderator_edu_university if moderator_edu_university else None,

        'all_pending_profiles': all_pending_profiles,
        'approved_profiles_central_mod': approved_profiles_central_mod,
    })


@user_passes_test(is_team_member, login_url='home')
def approved_moderator_list(request):
    batch_moderators = Profile.objects.filter(moderator_type='Batch Moderator')
    
    # all_moderators = ModeratorRequest.objects.filter(is_approved_final=True)
    # all_moderators = Profile.objects.filter(moderator_info__is_approved_final=True)
    all_moderators = Profile.objects.filter(moderator_info__is_approved_final=True, moderator_info__is_running=True)
    
    context = {
        'batch_moderators': batch_moderators,
        'all_moderators': all_moderators,
    }
    
    return render(request, 'moderators/department/approved_moderator_list.html', context)
        


@user_passes_test(is_team_member, login_url='home')
def approve_profile(request, profile_id):
    # Get the EduUniversity record of the user to approve
    edu_university = get_object_or_404(EduUniversity, id=profile_id)
    
    # Approve the profile and add the user to the department
    if not edu_university.is_approved:
        edu_university.is_approved = True
        edu_university.approved_by = request.user.profile
        edu_university.save()
        
        # Update the edu_university field in the associated Profile model
        profile = edu_university.profile
        profile.edu_university = edu_university
        
        profile.save()
        
        # Add the user to the department's users list
        # edu_university.department.users.add(profile)

        # Check if the profile has a referral code and award coins
        if profile.referred_by_code and not profile.is_referral_done:
            try:
                referrer_profile = Profile.objects.get(referral_code=profile.referred_by_code)
                referrer_profile.total_coins += 100
                referrer_profile.save()

                # Optionally, add a CoinTransaction entry if you track coin transactions
                CoinTransaction.objects.create(
                    profile=referrer_profile,
                    activity='refer_new_user',
                    coins=100
                )
                
                Notification.objects.create(
                user=referrer_profile.user,
                type='refer_new_user',
                message=(
                    f'অভিনন্দন! {profile.fullname}-কে রেফার করার জন্য আপনি 100টি Onebyzero Coin পেয়েছেন! আবারও কাউকে রেফার করতে লিংকে ক্লিক করুন।'
                )
            )
                
                profile.total_coins += 50
                profile.referred_by_code = None
                profile.is_referral_done = True
                profile.save()
                
                CoinTransaction.objects.create(
                    profile=profile,
                    activity='referred_by_existing_user',
                    coins=50
                )
                
                Notification.objects.create(
                user=profile.user,
                # type='approved_edu_university',
                message=(
                    f'অভিনন্দন! আপনার প্রদানকৃত সকল তথ্য যাচাই করে প্রোফাইলটি অ্যাপ্রুভ করা হয়েছে। এখন থেকে আপনি {edu_university.department}, {edu_university.university} -এর সকল রিসোর্স ব্যবহার করতে পারবেন।'
                ),
                # additional_id_one = profile.edu_university.university,
                # additional_id_two = profile.edu_university.department
            )
                
                Notification.objects.create(
                user=profile.user,
                type='coin_for_referral',
                message=(
                    f'অভিনন্দন!{referrer_profile.fullname} আপনাকে রেফার করার জন্য আপনি 50টি Onebyzero Coin পেয়েছেন! আপনিও {profile.edu_university.university} বা বাংলাদেশের অন্য কোনো বিশ্ববিদ্যালয়ের যেকোনো বন্ধুকে রেফার করে 100 করে Onebyzero Coin অর্জন করতে পারেন।'
                )
            )

            except Profile.DoesNotExist:
                pass  # Handle case where referral code does not match any profile
        else:
            profile.total_coins += 25
            profile.save()
            
            CoinTransaction.objects.create(
                    profile=profile,
                    activity='Creating Account',
                    coins=25
                )
        
            # Send notification to the user
            Notification.objects.create(
                user=profile.user,
                type='creating_new_account',
                message=(
                    f'অভিনন্দন! আপনার প্রদানকৃত সকল তথ্য যাচাই করে প্রোফাইলটি অ্যাপ্রুভ করা হয়েছে। এখন থেকে আপনি '
                    f'{edu_university.department.name + ", " if edu_university.department else ""}'
                    f'{edu_university.discipline.name + ", " if edu_university.discipline else ""}'
                    f'{edu_university.institute.name + ", " if edu_university.institute else ""}'
                    f'{edu_university.university.name} -এর সকল রিসোর্স ব্যবহার করতে পারবেন।'
                )
            )


            
            Notification.objects.create(
                user=profile.user,
                type='coin_for_referral',
                message=(
                    f'অভিনন্দন! Onebyzero Edu -তে প্রোফাইল তৈরি করার জন্য আপনি 25টি Onebyzero Coin পেয়েছেন! {profile.edu_university.university} বা বাংলাদেশের অন্য কোনো বিশ্ববিদ্যালয়ের যেকোনো বন্ধুকে আপনি রেফার করে 100 করে Onebyzero Coin অর্জন করতে পারেন। রেফার করতে লিংকে ক্লিক করুন।'
                )
            )
    
    return redirect('pending_user_list')



@user_passes_test(is_team_member, login_url='home')
def reject_profile(request, profile_id):
    # Get the EduUniversity record of the user to approve
    edu_university = get_object_or_404(EduUniversity, id=profile_id)

    # Approve the profile and add the user to the department
    if edu_university.is_approved:
        edu_university.is_approved = False
        edu_university.save()
        
        edu_university.department.users.remove(edu_university.profile)

         # Remove the edu_university from the associated Profile model
        # profile = edu_university.profile
        # profile.edu_university = None
        # profile.save()
        
    return redirect('pending_user_list')


# MODERATOR REQUEST

@login_required
def request_for_moderator(request):
    profile = request.user.profile
    
    if not profile.edu_university:
        messages.warning(request, "মডারেটর রিকয়েস্ট পাঠানোর পূর্বে অনুগ্রহ করে আপনার বিশ্ববিদ্যালয় সম্পর্কিত তথ্যাবলী আপডেট ও ভেরিফাইড করে নিন এবং পরবর্তীতে প্রোফাইলে গিয়ে মডারেটর রিকয়েস্ট পাঠান।")
        return redirect('view_edu_university_my_profile')
    
    elif not profile.mobile_number or not profile.facebook_id:
        messages.warning(request, "মডারেটর রিকয়েস্ট পাঠানোর পূর্বে অনুগ্রহ করে আপনার Mobile Number এবং Facebook ID আপডেট করে নিন এবং পরবর্তীতে পুনরায় প্রোফাইলে গিয়ে মডারেটর রিকয়েস্ট পাঠান। নিচের Edit বাটনে ক্লিক করুন।")
        return redirect('personal_info_my_profile')  # Redirect to personal info page
    
    if request.method == 'POST':
        
        form = ModeratorRequestForm(request.POST)
        if form.is_valid():
            # Check if the user agreed to the terms and conditions
            # if not form.cleaned_data.get('read_terms_and_conditions'):
            #     messages.success(request, 'মডারেটর হওয়ার জন্য Terms & Conditions গুলো অনুগ্রহ করে ভালোভাবে পড়ুন এবং সম্পূর্ণ একমত থাকলে চেকবক্সে টিক মার্ক করুন')
            #     return redirect('request_for_moderator')  # Replace with the appropriate view name or URL
            
            
            moderator_request = form.save(commit=False)
            moderator_request.profile = request.user.profile
            moderator_request.save()
            return redirect('moderator_request_sent')
    else:
        form = ModeratorRequestForm()
    
    university = request.user.profile.edu_university.university
    department = request.user.profile.edu_university.department
    departmental_batch = request.user.profile.edu_university.departmental_batch
    
    is_available_university_moderator = ModeratorRequest.objects.filter(profile__edu_university__university=university, requested_moderator_type='University Moderator', is_approved_final=True, is_running=True).exists()
    # available_university_moderator_info = ModeratorRequest.objects.filter(profile__edu_university__university=university, requested_moderator_type='University Moderator', is_approved_final=True, is_running=True)
    
    is_available_department_moderator = ModeratorRequest.objects.filter(profile__edu_university__university=university, profile__edu_university__department=department, requested_moderator_type='Departmental Moderator', is_approved_final=True, is_running=True).exists()
    # available_department_moderator_info = ModeratorRequest.objects.filter(profile__edu_university__university=university, requested_moderator_type='Departmental Moderator', is_approved_final=True, is_running=True)
    
    is_available_batch_moderator = ModeratorRequest.objects.filter(profile__edu_university__university=university, profile__edu_university__department=department, profile__edu_university__departmental_batch=departmental_batch, requested_moderator_type='Batch Moderator', is_approved_final=True, is_running=True).exists()
    # available_batch_moderator_info = ModeratorRequest.objects.filter(profile__edu_university__university=university, requested_moderator_type='Batch Moderator', is_approved_final=True, is_running=True)
    
    # has_sent_moderator_request = ModeratorRequest.objects.filter(profile=profile).exists()
    # sent_moderator_request_object = ModeratorRequest.objects.filter(profile=profile)
    # sent_moderator_request_type = sent_moderator_request_object.first().requested_moderator_type
  
    # Check if the user has sent a moderator request
    has_sent_moderator_request = ModeratorRequest.objects.filter(profile=profile).exists()

    # Initialize variables
    sent_moderator_request_type = None

    if has_sent_moderator_request:
        sent_moderator_request_object = ModeratorRequest.objects.filter(profile=profile).first()
        if sent_moderator_request_object:
            sent_moderator_request_type = sent_moderator_request_object.requested_moderator_type

    # Now you can use `sent_moderator_request_type` safely, knowing it won't cause an AttributeError

    
    context = {
        'form': form,
        'university': university,
        'department': department,
        'is_available_university_moderator': is_available_university_moderator,
        # 'available_university_moderator_info': available_university_moderator_info,
        'is_available_department_moderator': is_available_department_moderator,
        # 'available_department_moderator_info': available_department_moderator_info,
        'is_available_batch_moderator': is_available_batch_moderator,
        # 'available_batch_moderator_info': available_batch_moderator_info
        'has_sent_moderator_request': has_sent_moderator_request,
        'sent_moderator_request_type': sent_moderator_request_type,
    }
    
    return render(request, 'moderators/request/request_for_moderator.html', context)


@user_passes_test(is_any_moderator, login_url='home')
def retire_from_moderator(request):
    profile = request.user.profile
    
    # Fetch the moderator request associated with the profile
    moderator_request = profile.moderator_info
    
    if request.method == 'POST':
        form = RetiredFromModeratorForm(request.POST)
        
        if form.is_valid() and form.cleaned_data['confirm']:
            # Check if the moderator request exists and is_running is True
            if moderator_request and moderator_request.is_running:
                # Clear the moderator_info reference before deleting the object
                profile.moderator_info = None
                profile.moderator_type = None
                profile.save()
                
                # Delete the moderator request
                moderator_request.delete()
                
                return redirect('my_profile_overview')
    else:
        form = RetiredFromModeratorForm()
    
    return render(request, 'moderators/request/retired_from_moderator.html', {'form': form})


@login_required
def delete_prev_moderator_req(request):
    moderator_request = ModeratorRequest.objects.filter(profile=request.user.profile).first()
    moderator_request.delete()

    messages.success(request, "Moderator request deleted successfully! Now you can send a new request to be a moderator.")
    
    return redirect('request_for_moderator')

@login_required
def moderator_request_sent(request):
    moderator_request = get_object_or_404(ModeratorRequest, profile=request.user.profile)
    if moderator_request:
        return render(request, 'moderators/request/moderator_request_sent.html')
    else:
        return redirect('home')


@user_passes_test(is_team_member, login_url='home')
def moderator_request_list_initial(request):
    # Fetch all the requests where the user is a superior moderator
    requests = ModeratorRequest.objects.filter(is_approved_initial=False, is_approved_final=False).order_by('-requested_at')
    requests_approved_initial = ModeratorRequest.objects.filter(is_approved_initial=True).order_by('-approved_initial_at')
    return render(request, 'moderators/request/moderator_request_list_initial.html', {'requests': requests, 'requests_approved_initial': requests_approved_initial})


@user_passes_test(is_team_member, login_url='home')
def moderator_request_list_final(request):
    # Fetch all the requests where the user is a superior moderator    
    requests = ModeratorRequest.objects.filter(is_approved_initial=True).order_by('-approved_initial_at')
    
    all_requests = ModeratorRequest.objects.all().order_by('-requested_at')
    
    context = {
        'requests': requests,
        'all_requests': all_requests,
    }
    
    return render(request, 'moderators/request/moderator_request_list_final.html', context)


@user_passes_test(is_team_member, login_url='home')
def approve_moderator_initial(request, request_id):
    moderator_request = get_object_or_404(ModeratorRequest, id=request_id)
    
    # if request.method == 'POST':
        # Approve the request based on the user's moderator level
        # if request.user.profile.is_superior_to(moderator_request.profile):
    moderator_request.is_approved_initial = True
    moderator_request.approved_initial_by = request.user.profile
    moderator_request.approved_initial_at = timezone.now()
    moderator_request.save()
    # Redirect after approval
    return redirect('moderator_request_list_initial')

    # return render(request, 'moderators/request/moderator_request_list_initial.html', {'moderator_request': moderator_request})


@user_passes_test(is_team_member, login_url='home')
def reject_moderator_initial(request, request_id):
    moderator_request = get_object_or_404(ModeratorRequest, id=request_id)
    # print(moderator_request)
    moderator_request.is_approved_initial = False
    # moderator_request.is_approved_initial_at = timezone.now()

    moderator_request.is_approved_final = False
    moderator_request.is_running = False
    moderator_request.profile.moderator_type = None
    moderator_request.profile.moderator_info = None
    moderator_request.save()
    moderator_request.profile.save()
    
    # print(moderator_request)
    
    if request.user.profile.moderator_type == 'Central Moderator':
        return redirect('approved_moderator_list')
    else:
        return redirect('moderator_request_list_initial')


@user_passes_test(is_team_member, login_url='home')
def approve_moderator_final(request, request_id):
    moderator_request = get_object_or_404(ModeratorRequest, id=request_id)
    requested_moderator_profile = moderator_request.profile
    moderator_university = requested_moderator_profile.edu_university.university
    moderator_department = requested_moderator_profile.edu_university.department
    moderator_request.is_approved_final = True
    requested_moderator_profile.moderator_type = moderator_request.requested_moderator_type
    requested_moderator_profile.moderator_info = moderator_request
    moderator_request.approved_final_at = timezone.now()
    # moderator_university.moderators = F('moderators').union(requested_moderator_profile)
    # moderator_university.moderators = 
    
    moderator_request.is_running = True

    # if requested_moderator_profile.moderator_type == 'Departmental Moderator':
    #     moderator_department.moderators.add(requested_moderator_profile)
        
    #     moderator_department.save()
    
    moderator_request.save()
    requested_moderator_profile.save()
    
    Notification.objects.create(
        user = requested_moderator_profile.user,
        type = 'approved_as_moderator',
        message = f"অভিনন্দন, {requested_moderator_profile.fullname}! আপনাকে {moderator_request.requested_moderator_type} হিসেবে চূড়ান্তভাবে সিলেক্ট করা হয়েছে। এখানে অথবা উপরে প্রোফাইল আইকনে Moderator [{moderator_request.requested_moderator_type}] -এ ক্লিক করে পরবর্তী ধাপগুলো জেনে নিন।"
    )
    
    return redirect('moderator_request_list_final')

# UNIVERSITY MODERATOR VIEWS --------------------------


@user_passes_test(is_team_member, login_url='home')
def add_base_university_mod(request):
    university = get_object_or_404(University, id=request.user.profile.edu_university.university.id)
    
    total_faculties = Faculty.objects.filter(university=university).count()
    total_institutes = Institute.objects.filter(university=university).count()
    total_schools = School.objects.filter(university=university).count()
    total_centers = Center.objects.filter(university=university).count()
    total_departments = Department.objects.filter(university=university).count()
    total_disciplines = Discipline.objects.filter(university=university).count()
    
    context = {
        'university': university,
        'total_faculties': total_faculties,
        'total_institutes': total_institutes,
        'total_schools': total_schools,
        'total_centers': total_centers,
        'total_departments': total_departments,
        'total_disciplines': total_disciplines,
    }
    
    return render(request, 'moderators/university/add_base_university_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_base_university_mod(request):
    university = get_object_or_404(University, id=request.user.profile.edu_university.university.id)
    
    context = {
        'university': university,
    }
    
    return render(request, 'moderators/university/show_base_university_mod.html', context)


from django.db.models import Count

@user_passes_test(is_team_member, login_url='home')
def show_faculties_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    # Annotate faculties with the number of departments
    faculties = Faculty.objects.filter(university=university).annotate(total_departments=Count('department'))

    total_faculties = len(faculties)
    # total_departments = Department.objects.filter(university=university).count()
    # Count the total departments where faculty is not NULL
    total_departments = Department.objects.filter(university=university).exclude(faculty__isnull=True).count()
    
    total_institutes = Institute.objects.filter(university=university).exclude(faculty__isnull=True).count()
    
    context = {
        'university': university,
        'faculties': faculties,
        'total_faculties': total_faculties,
        'total_departments': total_departments,
        'total_institutes': total_institutes,
    }
    return render(request, 'moderators/university/show_faculties_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_schools_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    # Annotate faculties with the number of departments
    # faculties = Faculty.objects.filter(university=university).annotate(total_departments=Count('department'))
    
    schools = School.objects.filter(university=university)

    total_schools = len(schools)
    # total_departments = Department.objects.filter(university=university).count()
    # Count the total departments where faculty is not NULL
    total_departments = Department.objects.filter(university=university).exclude(school__isnull=True).count()
    
    # total_institutes = Institute.objects.filter(university=university).exclude(school__isnull=True).count()
    
    context = {
        'university': university,
        'schools': schools,
        'total_schools': total_schools,
        'total_departments': total_departments,
        # 'total_institutes': total_institutes,
    }
    return render(request, 'moderators/university/show_schools_mod.html', context)

@user_passes_test(is_team_member, login_url='home')
def show_centers_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    # Annotate faculties with the number of departments
    # faculties = Faculty.objects.filter(university=university).annotate(total_departments=Count('department'))
    
    centers = Center.objects.filter(university=university)

    total_centers = len(centers)
    # total_departments = Department.objects.filter(university=university).count()
    # Count the total departments where faculty is not NULL
    # total_departments = Department.objects.filter(university=university).exclude(school__isnull=True).count()
    
    # total_institutes = Institute.objects.filter(university=university).exclude(school__isnull=True).count()
    
    context = {
        'university': university,
        'centers': centers,
        'total_centers': total_centers,
        # 'total_departments': total_departments,
        # 'total_institutes': total_institutes,
    }
    return render(request, 'moderators/university/show_centers_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_departments_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    # Annotate faculties with the number of departments
    # faculties = Faculty.objects.filter(university=university).annotate(total_departments=Count('department'))
    
    departments = Department.objects.filter(university=university)

    total_departments = len(departments)
    # total_departments = Department.objects.filter(university=university).count()
    # Count the total departments where faculty is not NULL
    # total_departments = Department.objects.filter(university=university).exclude(school__isnull=True).count()
    
    # total_institutes = Institute.objects.filter(university=university).exclude(school__isnull=True).count()
    
    context = {
        'university': university,
        'departments': departments,
        'total_departments': total_departments,
        # 'total_departments': total_departments,
        # 'total_institutes': total_institutes,
    }
    return render(request, 'moderators/university/show_departments_mod.html', context)

@user_passes_test(is_team_member, login_url='home')
def show_disciplines_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    # Annotate faculties with the number of departments
    # faculties = Faculty.objects.filter(university=university).annotate(total_departments=Count('department'))
    
    disciplines = Discipline.objects.filter(university=university)

    total_disciplines = len(disciplines)
    # total_departments = Department.objects.filter(university=university).count()
    # Count the total departments where faculty is not NULL
    # total_departments = Department.objects.filter(university=university).exclude(school__isnull=True).count()
    
    # total_institutes = Institute.objects.filter(university=university).exclude(school__isnull=True).count()
    
    context = {
        'university': university,
        'disciplines': disciplines,
        'total_disciplines': total_disciplines,
        # 'total_departments': total_departments,
        # 'total_institutes': total_institutes,
    }
    return render(request, 'moderators/university/show_disciplines_mod.html', context)


# 017
@user_passes_test(is_team_member, login_url='home')
def edit_faculty_mod(request, university_id, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    university = faculty.university
    university_id = university.id
    
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty, university=university)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty updated successfully!")
            return redirect('show_faculties_mod', university_id=university_id)
    else:
        form = FacultyForm(instance=faculty, university=university)
        
    context = {
        'form': form,
        'university': university,
        'university_id': university_id,
        'faculty': faculty,
        'faculty_id': faculty_id,
    }
    
    return render(request, 'moderators/university/edit_faculty_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def edit_institute_mod(request, university_id, institute_id):
    institute = Institute.objects.get(id=institute_id)
    university = institute.university
    university_id = university.id
    
    if request.method == 'POST':
        form = InstituteForm(request.POST, instance=institute, university=university)
        if form.is_valid():
            form.save()
            messages.success(request, "Institute updated successfully!")
            return redirect('show_institutes_mod', university_id=university_id)
    else:
        form = FacultyForm(instance=institute, university=university)
        
    context = {
        'form': form,
        'university': university,
        'university_id': university_id,
        'institute': institute,
        'institute_id': institute_id,
    }
    
    return render(request, 'moderators/university/edit_institute_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def edit_school_mod(request, school_id):
    school = School.objects.get(id=school_id)
    university = school.university
    university_id = university.id
    
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school, university=university)
        if form.is_valid():
            form.save()
            messages.success(request, "School updated successfully!")
            return redirect('show_schools_mod', university_id=university_id)
    else:
        form = FacultyForm(instance=school, university=university)
        
    context = {
        'form': form,
        'university': university,
        'university_id': university_id,
        'school': school,
        'school_id': school_id,
    }
    
    return render(request, 'moderators/university/edit_school_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def edit_center_mod(request, center_id):
    center = Center.objects.get(id=center_id)
    university = center.university
    university_id = university.id
    
    if request.method == 'POST':
        form = CenterForm(request.POST, instance=center, university=university)
        if form.is_valid():
            form.save()
            messages.success(request, "Center updated successfully!")
            return redirect('show_centers_mod', university_id=university_id)
    else:
        form = CenterForm(instance=center, university=university)
        
    context = {
        'form': form,
        'university': university,
        'university_id': university_id,
        'center': center,
        'center_id': center_id,
    }
    
    return render(request, 'moderators/university/edit_center_mod.html', context)



@user_passes_test(is_team_member, login_url='home')
def edit_department_mod(request, department_id):
    department = Department.objects.get(id=department_id)
    university = department.university
    university_id = university.id
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department, university=university)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully!")
            return redirect('show_departments_mod', university_id=university_id)
    else:
        form = DepartmentForm(instance=department, university=university)
        
    context = {
        'form': form,
        'university': university,
        'university_id': university_id,
        'department': department,
        'department_id': department_id,
    }
    
    return render(request, 'moderators/university/edit_department_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def edit_discipline_mod(request, discipline_id):
    discipline = Discipline.objects.get(id=discipline_id)
    university = discipline.university
    university_id = university.id
    
    if request.method == 'POST':
        form = DisciplineForm(request.POST, instance=discipline, university=university)
        if form.is_valid():
            form.save()
            messages.success(request, "Discipline updated successfully!")
            return redirect('show_disciplines_mod', university_id=university_id)
    else:
        form = DepartmentForm(instance=discipline, university=university)
        
    context = {
        'form': form,
        'university': university,
        'university_id': university_id,
        'discipline': discipline,
        'discipline_id': discipline_id,
    }
    
    return render(request, 'moderators/university/edit_discipline_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_institutes_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    # Annotate faculties with the number of departments
    institutes = Institute.objects.filter(university=university).annotate(total_departments=Count('department'))
    
    total_institutes = len(institutes)
    # Count the total departments where institute is not NULL
    total_departments = Department.objects.filter(university=university).exclude(institute__isnull=True).count()
    
    context = {
        'university': university,
        'institutes': institutes,
        'total_institutes': total_institutes,
        'total_departments': total_departments,
    }
    return render(request, 'moderators/university/show_institutes_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def add_institute_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    if request.method == 'POST':
        form = InstituteForm(request.POST, university=university)
        if form.is_valid():
            institute = form.save(commit=False)
            institute.university = university
            institute.save()
            messages.success(request, 'New institute added successfully!')
            return redirect('show_institutes_mod', university_id=university_id)
    else:
        form = InstituteForm(university=university)
    
    context = {
        'form': form,
        'university': university
    }
    return render(request, 'moderators/university/add_institute_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def add_school_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    if request.method == 'POST':
        form = SchoolForm(request.POST, university=university)
        if form.is_valid():
            school = form.save(commit=False)
            school.university = university
            school.save()
            messages.success(request, 'New school added successfully!')
            return redirect('show_schools_mod', university_id=university_id)
    else:
        form = SchoolForm(university=university)
    
    context = {
        'form': form,
        'university': university
    }
    return render(request, 'moderators/university/add_school_mod.html', context)



@user_passes_test(is_team_member, login_url='home')
def add_center_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    if request.method == 'POST':
        form = CenterForm(request.POST, university=university)
        if form.is_valid():
            center = form.save(commit=False)
            center.university = university
            center.save()
            messages.success(request, 'New center added successfully!')
            return redirect('show_centers_mod', university_id=university_id)
    else:
        form = CenterForm(university=university)
    
    context = {
        'form': form,
        'university': university
    }
    return render(request, 'moderators/university/add_center_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def add_faculty_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    if request.method == 'POST':
        form = FacultyForm(request.POST, university=university)
        if form.is_valid():
            faculty = form.save(commit=False)
            faculty.university = university
            faculty.save()
            messages.success(request, 'New faculty added successfully!')
            return redirect('show_faculties_mod', university_id=university.id)
    else:
        form = FacultyForm(university=university)
    
    context = {
        'form': form,
        'university': university
    }
    return render(request, 'moderators/university/add_faculty_mod.html', context)

@user_passes_test(is_team_member, login_url='home')
def show_departments_by_faculty_mod(request, faculty_id):
    university = get_object_or_404(University, id=faculty_id)
    faculty = get_object_or_404(Faculty, id=faculty_id)
    departments = Department.objects.filter(faculty=faculty)
    total_departments = len(departments)
    
    context = {
        'university': university,
        'faculty': faculty,
        'departments': departments,
        'total_departments': total_departments,
    }
    return render(request, 'moderators/university/show_departments_by_faculty_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_institutes_by_faculty_mod(request, faculty_id):
    university = get_object_or_404(University, id=faculty_id)
    faculty = get_object_or_404(Faculty, id=faculty_id)
    institutes = Institute.objects.filter(faculty=faculty)
    total_institutes = len(institutes)
    
    context = {
        'university': university,
        'faculty': faculty,
        'institutes': institutes,
        'total_institutes': total_institutes,
    }
    return render(request, 'moderators/university/show_institutes_by_faculty_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def show_departments_by_institute_mod(request, institute_id):
    university = get_object_or_404(University, id=institute_id)
    institute = get_object_or_404(Institute, id=institute_id)
    departments = Department.objects.filter(institute=institute)
    total_departments = len(departments)
    
    context = {
        'university': university,
        'institute': institute,
        'departments': departments,
        'total_departments': total_departments,
    }
    return render(request, 'moderators/university/show_departments_by_institute_mod.html', context)

@user_passes_test(is_team_member, login_url='home')
def add_department_by_faculty_mod(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    university = faculty.university
    
    if request.method == 'POST':
        form = DepartmentByFacultyForm(request.POST, faculty=faculty)
        if form.is_valid():
            department = form.save(commit=False)
            department.faculty = faculty
            department.university = university
            department.save()
            messages.success(request, 'New department added successfully!')
            return redirect('show_departments_by_faculty_mod', faculty_id=faculty.id)
    else:
        form = DepartmentByFacultyForm(faculty=faculty)
    
    context = {
        'form': form,
        'university': university,
        'faculty': faculty,
    }
    return render(request, 'moderators/university/add_department_by_faculty_mod.html', context)

@user_passes_test(is_team_member, login_url='home')
def add_institute_by_faculty_mod(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    university = faculty.university
    
    if request.method == 'POST':
        form = InstituteByFacultyForm(request.POST, faculty=faculty)
        if form.is_valid():
            institute = form.save(commit=False)
            institute.faculty = faculty
            institute.university = university
            institute.save()
            messages.success(request, 'New institute added successfully!')
            return redirect('show_institutes_by_faculty_mod', faculty_id=faculty.id)
    else:
        form = InstituteByFacultyForm(faculty=faculty)
    
    context = {
        'form': form,
        'university': university,
        'faculty': faculty,
    }
    return render(request, 'moderators/university/add_institute_by_faculty_mod.html', context)



@user_passes_test(is_team_member, login_url='home')
def edit_department_by_faculty_mod(request, faculty_id, department_id):
    department = Department.objects.get(id=department_id)
    university = department.university
    faculty = department.faculty  # Retrieve the faculty object
    university_id = department.university.id
    
    if request.method == 'POST':
        form = DepartmentByFacultyForm(request.POST, instance=department, faculty=faculty)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully!")
            return redirect('show_departments_by_faculty_mod', faculty_id=faculty_id)
    else:
        form = DepartmentByFacultyForm(instance=department, faculty=faculty)
        
    context = {
        'form': form,
        'university': university,
        'faculty': faculty,
        'faculty_id': faculty_id,
        'department': department,
    }
    
    return render(request, 'moderators/university/edit_department_by_faculty_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def edit_institute_by_faculty_mod(request, faculty_id, institute_id):
    institute = Institute.objects.get(id=institute_id)
    university = institute.university
    faculty = institute.faculty  # Retrieve the faculty object
    university_id = institute.university.id
    
    if request.method == 'POST':
        form = InstituteByFacultyForm(request.POST, instance=institute, faculty=faculty)
        if form.is_valid():
            form.save()
            messages.success(request, "Institute updated successfully!")
            return redirect('show_institutes_by_faculty_mod', faculty_id=faculty_id)
    else:
        form = InstituteByFacultyForm(instance=institute, faculty=faculty)
        
    context = {
        'form': form,
        'university': university,
        'faculty': faculty,
        'faculty_id': faculty_id,
        'institute': institute,
    }
    
    return render(request, 'moderators/university/edit_institute_by_faculty_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    # university_id = department.university.id
    faculty_id = department.faculty.id
    department.delete()
    messages.success(request, "Department deleted successfully!")
    return redirect('show_departments_by_faculty_mod', faculty_id=faculty_id)

@user_passes_test(is_team_member, login_url='home')
def delete_institute(request, institute_id):
    institute = get_object_or_404(Institute, id=institute_id)
    # university_id = department.university.id
    # faculty_id = institute.faculty.id
    university_id = institute.university.id
    institute.delete()
    messages.success(request, "Institute deleted successfully!")
    return redirect('show_institutes_mod', university_id=university_id)


@user_passes_test(is_team_member, login_url='home')
def delete_school_mod(request, school_id):
    school = get_object_or_404(School, id=school_id)
    # university_id = department.university.id
    # faculty_id = institute.faculty.id
    university_id = school.university.id
    school.delete()
    messages.success(request, "School deleted successfully!")
    return redirect('show_schools_mod', university_id=university_id)


@user_passes_test(is_team_member, login_url='home')
def delete_center_mod(request, center_id):
    this_center = get_object_or_404(Center, id=center_id)
    # university_id = department.university.id
    # faculty_id = institute.faculty.id
    university_id = this_center.university.id
    this_center.delete()
    messages.success(request, "Center deleted successfully!")
    return redirect('show_centers_mod', university_id=university_id)

@user_passes_test(is_team_member, login_url='home')
def delete_department_mod(request, department_id):
    this_department = get_object_or_404(Department, id=department_id)
    # university_id = department.university.id
    # faculty_id = institute.faculty.id
    university_id = this_department.university.id
    this_department.delete()
    messages.success(request, "Department deleted successfully!")
    return redirect('show_departments_mod', university_id=university_id)

@user_passes_test(is_team_member, login_url='home')
def delete_discipline_mod(request, discipline_id):
    this_discipline = get_object_or_404(Discipline, id=discipline_id)
    # university_id = department.university.id
    # faculty_id = institute.faculty.id
    university_id = this_discipline.university.id
    this_discipline.delete()
    messages.success(request, "Discipline deleted successfully!")
    return redirect('show_disciplines_mod', university_id=university_id)

@user_passes_test(is_team_member, login_url='home')
def delete_faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    university_id = faculty.university.id
    faculty_id = faculty.id
    faculty.delete()
    messages.success(request, "Faculty deleted successfully!")
    return redirect('show_faculties_mod', university_id=university_id)

@user_passes_test(is_team_member, login_url='home')
def settings_university_mod(request, university_id):
    # Fetch the university object by its ID
    university = get_object_or_404(University, id=university_id)
    
    # Render the template and pass the university object to the context
    return render(request, 'moderators/university/settings_university_mod.html', {'university': university})

@user_passes_test(is_team_member, login_url='home')
def edit_university_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    if request.method == 'POST':
        form = UniversityForm(request.POST, request.FILES, instance=university)
        if form.is_valid():
            form.save()
            messages.success(request, 'University information has been updated successfully.')
            return redirect('settings_university_mod', university_id=university.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UniversityForm(instance=university)
    
    context = {
        'form': form,
        'university': university,
    }
    return render(request, 'moderators/university/edit_university_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def others_central_mod(request):
    return render(request, 'moderators/central/others_central_mod.html')

@user_passes_test(is_team_member, login_url='home')
def requested_for_prev_coins(request):
    
    requested_profiles = Profile.objects.filter(has_req_for_prev_coin=True)
    
    context = {
        'requested_profiles': requested_profiles
    }
    
    return render(request, 'moderators/central/requested_for_prev_coins.html', context)

from django.urls import reverse
@user_passes_test(is_team_member, login_url='home')
def given_prev_coin(request, profile_id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, id=profile_id)
        profile.given_prev_coin = True
        profile.save()
    
    return redirect(reverse('requested_for_prev_coins'))

@user_passes_test(is_team_member, login_url='home')
def notification_base_mod(request):
    return render(request, 'moderators/notification_base_mod.html')

@user_passes_test(is_team_member, login_url='home')
def quick_buttons_mod(request):
    return render(request, 'moderators/quick_buttons_mod.html')

@user_passes_test(is_team_member, login_url='home')
def department_list(request, university_id):
    university = get_object_or_404(University, id=university_id)
    departments = Department.objects.filter(university=university)
    context = {
        'university': university,
        'departments': departments
    }
    return render(request, 'moderators/university/department_list.html', context)


@user_passes_test(is_team_member, login_url='home')
def add_department_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, university=university)
        if form.is_valid():
            department = form.save(commit=False)
            department.university = university
            department.save()
            messages.success(request, 'New department added successfully!')
            return redirect('show_departments_mod', university_id=university_id)
    else:
        form = DepartmentForm(university=university)
    
    context = {
        'form': form,
        'university': university
    }
    return render(request, 'moderators/university/add_department_mod.html', context)


@user_passes_test(is_team_member, login_url='home')
def add_discipline_mod(request, university_id):
    university = get_object_or_404(University, id=university_id)
    
    if request.method == 'POST':
        form = DisciplineForm(request.POST, university=university)
        if form.is_valid():
            discipline = form.save(commit=False)
            discipline.university = university
            discipline.save()
            messages.success(request, 'New discipline added successfully!')
            return redirect('show_disciplines_mod', university_id=university_id)
    else:
        form = DisciplineForm(university=university)
    
    context = {
        'form': form,
        'university': university
    }
    return render(request, 'moderators/university/add_discipline_mod.html', context)



@user_passes_test(is_team_member, login_url='home')
def edit_department(request, department_id):
    department = Department.objects.get(id=department_id)
    
    university_id = department.university.id
    # department_id = course.department.id
    # # year_id = course.year
    # # semester = course.semester
    # semester = semester_converter(course.semester)
    
    # print(semester)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        # print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully!")
            return redirect('department_list', university_id=university_id)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'moderators/university/edit_department.html', {'form': form, 'department': department})

