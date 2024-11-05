from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import *
# from apps.education.models import *
from apps.account.models.profile_models import *
from apps.account.models.education_models import *
from apps.notifications.models import *
from ..forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.db import IntegrityError
from apps.admin_panel.models import *
# @login_required
# def my_profile_overview(request):
#     profile, created = Profile.objects.get_or_create(
#         user=request.user,
#         defaults={
#             'fullname': request.user.get_full_name(),
#             'email': request.user.email,
#             # 'slug': slugify(request.user.username)
#             # Add other default values if needed
#         }
#     )
    
#     return render(request, 'profile/my_profile/overview/my_profile_overview.html', {'d_profile': profile})



@login_required
def my_profile_overview(request):
    try:
        profile, created = Profile.objects.get_or_create(
            user=request.user,
            defaults={
                'fullname': request.user.get_full_name(),
                'email': request.user.email,
                # 'slug': slugify(request.user.username)
                # Add other default values if needed
            }
        )
    except IntegrityError:
        # If the profile creation fails due to IntegrityError, fetch the existing profile
        profile = Profile.objects.get(user=request.user)
    

    return render(request, 'profile/my_profile/overview/my_profile_overview.html', {'d_profile': profile})


def view_profile_overview(request, user_id):
    # user = get_object_or_404(User, id=user_id)
    # user = get_object_or_404(Profile, id=user_id)
    # profile = get_object_or_404(Profile, user=user)
    profile = get_object_or_404(Profile, id=user_id)
    # print(profile)
    # edu_university = get_object_or_404(EduUniversity, profile=profile)
    
    # Handle university and department info
    try:
        edu_university = EduUniversity.objects.get(profile=profile)
    except EduUniversity.DoesNotExist:
        edu_university = None

    # if edu_university is None:
        # Redirect the user if no EduUniversity exists
        # return redirect('home')
    
    return render(request, 'profile/view_profile/overview/view_profile_overview.html', {'d_profile': profile, 'd_user': profile, 'd_profile_edu_university': edu_university, 'edu_university': edu_university})



@login_required
def edit_personal_info_my_profile(request):
    user = request.user

    # Use get_or_create to handle retrieving or creating the profile in one step
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            if not profile.edu_university:
                return redirect('view_edu_university_my_profile')
            return redirect('personal_info_my_profile')
        else:
            # Log errors if form validation fails
            print(form.errors)
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'profile/my_profile/personal_info/edit_personal_info_my_profile.html', context)



from django.db import IntegrityError

@login_required
def personal_info_my_profile(request):
    # try:
    #     profile = request.user.profile
    # except Profile.DoesNotExist:
    #     # Create a new profile for the user if it does not exist
    #     profile = Profile(
    #         user=request.user,
    #         fullname=request.user.get_full_name(),
    #         email=request.user.email,
    #         # slug=slugify(request.user.username)
    #         # Add other default values if needed
    #         )
    #     profile.save()
    
    
    # profile, created = Profile.objects.get_or_create(
    #     user=request.user,
    #     defaults={
    #         'fullname': request.user.get_full_name(),
    #         'email': request.user.email,
    #         # 'slug': slugify(request.user.username)  # Uncomment if needed
    #         # Add other default values if needed
    #     }
    # )
    
    profile = request.user.profile
    

    # Provide user guidance based on their profile status
    # if profile.fullname is None:
    #     messages.success(request, mark_safe("অনুগ্রহ করে আপনার <strong>Fullname</strong>, <strong>Nickname</strong> এবং <strong>Email</strong> আপডেট করুন।"))
    # elif profile.user_type == 'Student' and not profile.edu_university:
    #     messages.success(request, mark_safe("অনুগ্রহ করে উপরে ডান পাশে <strong>Educational Qualifications</strong> আইকনে ক্লিক করে আপনার বিশ্ববিদ্যালয় সম্পর্কিত তথ্যাবলী আপডেট করুন।"))

    return render(request, 'profile/my_profile/personal_info/personal_info_my_profile.html', {'d_profile': profile})


def personal_info_view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    
    return render(request, 'profile/view_profile/personal_info/personal_info_view_profile.html', {'d_profile': profile, 'd_user': user})


from django.urls import reverse
@login_required
def view_edu_university_my_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if not authenticated

    profile = get_object_or_404(Profile, user=request.user)
    
    try:
        profile_edu_university = EduUniversity.objects.get(profile=profile)
        university = profile_edu_university.university
        department = profile_edu_university.department
        discipline = profile_edu_university.discipline
        institute = profile_edu_university.institute
        departmental_batch = profile_edu_university.departmental_batch
        discipline_batch = profile_edu_university.discipline_batch
        institute_batch = profile_edu_university.institute_batch
        
    except EduUniversity.DoesNotExist:
        profile_edu_university = None
        university = None
        department = None
        discipline = None
        institute = None
        departmental_batch = None
        discipline_batch = None 
        institute_batch = None
    
    batch_moderators = None
    departmental_moderators = None
    discipline_moderators = None
    institute_moderators = None
    university_moderators = None
    
    if department and departmental_batch:  # Only filter if both are not None
        batch_moderators = Profile.objects.filter(
            moderator_type='Batch Moderator',
            moderator_info__is_running = True,
            edu_university__department=department,
            edu_university__departmental_batch=departmental_batch,
        )
    # print('batch_moderators',batch_moderators)
        
    if discipline and discipline_batch: 
        batch_moderators = Profile.objects.filter(
            moderator_type='Batch Moderator',
            moderator_info__is_running = True,
            edu_university__discipline=discipline,
            edu_university__departmental_batch=departmental_batch,
        )
        
    if department:
        departmental_moderators = Profile.objects.filter(
            moderator_type='Departmental Moderator',
            moderator_info__is_running = True,
            edu_university__department=department,
        )
        
        # print('departmental_moderators',departmental_moderators)
        
    if discipline:
        discipline_moderators = Profile.objects.filter(
            moderator_type='Discipline Moderator',
            moderator_info__is_running = True,
            edu_university__discipline=discipline,
        )
        
    if institute:
        institute_moderators = Profile.objects.filter(
            moderator_type='Institute Moderator',
            moderator_info__is_running = True,
            edu_university__institute=institute,
        )
        
    if university:
        university_moderators = Profile.objects.filter(
            moderator_type='University Moderator',
            moderator_info__is_running = True,
            edu_university__university=university,
        )
        
        # print('university_moderators',university_moderators)
    
    if profile_edu_university is None:
        messages.success(request, mark_safe("অনুগ্রহ করে আপনার বিশ্ববিদ্যালয় সম্পর্কিত তথ্যাবলী Add করুন।"))
    elif profile_edu_university and not profile_edu_university.is_approved:
        moderator_links = [
            f'<div class="moderator-link">'
            f'<img src="{moderator.profile_image.url}" alt="{moderator.fullname}" style="width:40px; height:40px; border-radius:50%; margin-right:10px;">'
            f'<a href="{reverse("view_profile_overview", args=[moderator.pk])}">{moderator.fullname}</a> '
            f'{moderator.edu_university.departmental_batch if moderator.moderator_type == "Batch Moderator" else ""} '
            f'[{moderator.moderator_type}'
            f'{"(Departmental)" if moderator.moderator_type == "Batch Moderator" else ""}]'
            f'</div>'
            for moderator in list(batch_moderators or [])
                        + list(departmental_moderators or [])
                        + list(discipline_moderators or [])
                        + list(institute_moderators or [])
                        + list(university_moderators or [])
        ]

        # print(moderator_links)
        
        # Join the links with commas
        moderators_display = ', '.join(moderator_links)
        
        request_for_moderator = reverse('request_for_moderator')
        
        # Create the message with moderator links
        # if batch_moderators or departmental_moderators or discipline_moderators or institute_moderators or university_moderators:
        #     messages.success(
        #         request,
        #         mark_safe(
        #             f'প্রিয় {profile.fullname}, বিশ্ববিদ্যালয় সম্পর্কিত আপনার প্রদানকৃত তথ্যাবলী {university} এর মডারেটরদের কাছে পাঠিয়ে দেয়া হয়েছে। '
        #             f'খুব শীঘ্রই আপনার প্রোফাইল ও এডুকেশন ডিটেইলস যাচাই করে Verified করা হবে। অনুগ্রহ করে অপেক্ষা করুন। <br/><br/>'
        #             f'এই মুহুর্তে আপনি একেবারে নিচের দিকে বাটনগুলোতে ক্লিক করে আপনার University / Department / Discipline / Institute / Semester / Year এর রিসোর্সগুলো দেখে আসতে পারেন। <br/><br/>'
                    
        #             f'অ্যাপ্রুভ করতে বেশি বিলম্ব হলে আপনার বিশ্ববিদ্যালয়ের মডারেটরদের সাথে যোগাযোগ করতে পারেন। অথবা আমাদেরকে মেসেজ বা কল দিন। <br/><br/>'
                    
        #             f'<strong>আপনার বিশ্ববিদ্যালয়ের মডারেটরঃ</strong> {moderators_display}'
        #         )
        #     )
        # else:
        #     messages.success(
        #         request,
        #         mark_safe(
        #             f'প্রিয় {profile.fullname}, বিশ্ববিদ্যালয় সম্পর্কিত আপনার প্রদানকৃত তথ্যাবলী {university} এর মডারেটর দিয়ে ভেরিফাই করতে হবে। তবে আপনার বিশ্ববিদ্যালয়ের জন্য এখনও মডারেটর সিলেকশন প্রক্রীয়া চলমান। '
        #             f'চূড়ান্তভাবে মডারেটর সিলেক্টেড হয়ে গেলে সাথে সাথেই আপনার প্রোফাইল ও এডুকেশন ডিটেইলস যাচাই করে Verified করা হবে। অনুগ্রহ করে অপেক্ষা করুন। <br/><br/>'
                    
        #             # f'আপনিও একজন মডারেটর হতে চাইলে নিচের বাটনে ক্লিক করুনঃ<br/>'
                    
        #             # f'<a href="{request_for_moderator}" class="btn btn-secondary">Become a Moderator of Onebyzero Edu</a> <br/><br/>'
                    
        #             f'এই মুহুর্তে আপনি একেবারে নিচের দিকে বাটনগুলোতে ক্লিক করে আপনার University / Department / Discipline / Institute / Semester / Year এর রিসোর্সগুলো দেখে আসতে পারেন। <br/><br/>'
        #         )
        #     )
            
    
    context = {
        'profile': profile,
        'edu_university': profile_edu_university,
    }
    
    return render(request, 'profile/my_profile/education/university/view_edu_university_my_profile.html', context)



def view_edu_university_view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    
    try:
        profile_edu_university = EduUniversity.objects.get(profile=profile)
        university = profile_edu_university.university
        department = profile_edu_university.department
    except EduUniversity.DoesNotExist:
        profile_edu_university = None
        university = None
        department = None
    
    context = {
        'd_user': user,
        'profile': profile,
        'edu_university': profile_edu_university,
    }
    
    return render(request, 'profile/view_profile/education/university/view_edu_university_view_profile.html', context)


# @login_required
# def add_edu_university_my_profile(request):
#     profile = request.user.profile  # Fetch the logged-in user's profile
#     if request.method == "POST":
#         form = EduUniversityForm(request.POST)
#         if form.is_valid():
#             edu_university = form.save(commit=False)
#             requested_department = form.cleaned_data['department']
#             requested_batch = form.cleaned_data['departmental_batch']
#             edu_university.profile = profile  # Assign the profile to the new EduUniversity instance
#             edu_university.save()
            
#             # Notification to the user
#             Notification.objects.create(
#                 user=request.user,
#                 message=f'বিশ্ববিদ্যালয় সম্পর্কিত আপনার প্রদানকৃত তথ্যাবলী {requested_department} এর ব্যাচ মডারেটর ({requested_batch} Batch) এর কাছে পাঠিয়ে দেয়া হয়েছে। সর্বোচ্চ ২৪ ঘন্টার মধ্যে যাচাই করে আপনাকে উক্ত ডিপার্টমেন্টে যুক্ত করা হবে। অনুগ্রহ করে অপেক্ষা করুন।'
#             )
            
#             # Retrieve all batch moderators for the requested department and batch
#             batch_moderators = Profile.objects.filter(
#                 moderator_type='Batch Moderator',
#                 edu_university__department=requested_department,
#                 edu_university__departmental_batch=requested_batch
#             )
            
#             # print('batch_moderators: ', batch_moderators)

#             if batch_moderators.exists():
#                 for batch_moderator in batch_moderators:
#                     # Notification to each department's moderator
#                     Notification.objects.create(
#                         type='pending_for_verify_university',
#                         user=batch_moderator.user,
#                         message=f'প্রিয় ব্যাচ মডারেটর, আপনার ব্যাচে শিক্ষার্থী হিসেবে যুক্ত হওয়ার জন্য {profile.fullname} নামের একজন ইউজার অনুরোধ করেছেন। অনুগ্রহ করে মডারেটর প্যানেল থেকে যথাসম্ভব দ্রুত তার প্রোফাইল সঠিকভাবে যাচাই করে অ্যাপ্রুভ করুন।'
#                     )
            
#             # messages.success(request, mark_safe("আপনার প্রদানকৃত তথ্যাবলী উক্ত ডিপার্টমেন্টের মডারেটর এর কাছে পাঠিয়ে দেয়া হয়েছে। সর্বোচ্চ ২৪ ঘন্টার মধ্যে যাচাই করে আপনাকে উক্ত ডিপার্টমেন্টে যুক্ত করা হবে। অনুগ্রহ করে অপেক্ষা করুন।"))
            
#             return redirect('view_edu_university_my_profile')  # Redirect to a success page
#     else:
#         form = EduUniversityForm()
    
#     return render(request, 'profile/my_profile/education/university/add_edu_university_my_profile.html', {'form': form})



from django.contrib import messages

@login_required
def add_edu_university_step1(request):
    profile = request.user.profile  # Fetch the logged-in user's profile
    
    # Try to fetch all EduUniversity entries associated with this profile
    edu_universities = EduUniversity.objects.filter(profile=profile)
    
    if request.method == "POST":
        form = EduUniversityForm1(request.POST)
        if form.is_valid():
            university = form.cleaned_data['university']
            blank_university = form.cleaned_data['blank_university']
            
            if university is None and blank_university is None:
                # If both fields are empty, add a message and stay on the same page
                messages.success(request, "অনুগ্রহ করে ইউনিভার্সিটি যুক্ত করুন")
            else:
                # Filter by the specific university and blank_university fields
                edu_university = edu_universities.filter(
                    university=university,
                    blank_university=blank_university
                ).first()  # Get the first matching object or None

                if edu_university:
                    # If it exists, update the existing instance
                    form = EduUniversityForm1(request.POST, instance=edu_university)
                    form.save()
                else:
                    # Create a new instance if one doesn't already exist
                    edu_university = form.save(commit=False)
                    edu_university.profile = profile
                    edu_university.save()

                # Determine the university_id to pass to step 2, but only if university is not None
                if university:
                    university_id = university.id
                    return redirect('add_edu_university_step2', university_id=university_id)
                else:
                    # If no university is selected, provide feedback
                    messages.error(request, "Please select a university.")
        else:
            messages.error(request, "Form is invalid. Please correct the errors.")
    
    else:
        # If GET request, use the first EduUniversity instance to prepopulate the form
        edu_university = edu_universities.first()
        form = EduUniversityForm1(instance=edu_university)

    # Display information about blank universities associated with the profile
    blank_edu_university = edu_universities.filter(blank_university__isnull=False)
    
    return render(
        request, 
        'profile/my_profile/education/university/add_edu_university_step1.html', 
        {'form': form, 'blank_edu_university': blank_edu_university}
    )


import logging
from django.http import Http404
from django.core.exceptions import MultipleObjectsReturned
@login_required
def add_edu_university_step2(request, university_id):
    profile = request.user.profile
    university = get_object_or_404(University, id=university_id)
    # print(university)
    # print(f"Profile ID: {profile.id}, University ID: {university.id}")
    # print(f"University Name: {university.name}")

    edu_university = None
    
    try:
        # Try to get EduUniversity by university ForeignKey
        edu_university = EduUniversity.objects.get(profile=profile)
        # print("Found EduUniversity by university ForeignKey")
    except EduUniversity.DoesNotExist:
        # print("EduUniversity not found by university ForeignKey, trying by blank_university")
        try:
            # Try to get EduUniversity by blank_university field
            edu_university = EduUniversity.objects.get(profile=profile, blank_university__isnull=False)
            # print("Found EduUniversity by blank_university")
        except EduUniversity.DoesNotExist:
            # print("EduUniversity not found by blank_university")
            raise Http404("EduUniversity not found")

    if request.method == "POST":
        form = EduUniversityForm2(request.POST, instance=edu_university, university=university)
        if form.is_valid():
            edu_university = form.save()
            faculty_id = edu_university.faculty.id if edu_university.faculty else None
            return redirect('add_edu_university_step3')
            # if faculty_id:
            #     return redirect('add_edu_university_step3', faculty_id=faculty_id)
            # else:
            #     return redirect('view_edu_university_my_profile')
    else:
        form = EduUniversityForm2(instance=edu_university, university=university)

    faculty_exists = Faculty.objects.filter(university=university).exists()
    institute_exists = Institute.objects.filter(university=university).exists()
    school_exists = School.objects.filter(university=university).exists()
    center_exists = Center.objects.filter(university=university).exists()
    department_exists = Department.objects.filter(university=university).exists()
    discipline_exists = Discipline.objects.filter(university=university).exists()
    

    context = {
        'form': form,
        'university': university,
        'faculty_exists': faculty_exists,
        'institute_exists': institute_exists,
        'school_exists': school_exists,
        'center_exists': center_exists,
        'department_exists': department_exists,
        'discipline_exists': discipline_exists
    }    
    
    return render(request, 'profile/my_profile/education/university/add_edu_university_step2.html', context)

@login_required
def add_edu_university_step3(request):
    profile = request.user.profile
    # Fetch the existing EduUniversity instance for the current profile and university
    edu_university = get_object_or_404(EduUniversity, profile=profile)
    
    if request.method == "POST":
        form = EduUniversityForm3(request.POST, instance=edu_university)
        if form.is_valid():
            form.save()  # Update the existing EduUniversity instance
            
            edu_university.is_approved = True
            edu_university.save()
            
            profile.edu_university = edu_university
            profile.save()
            
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
                    
                #     Notification.objects.create(
                #     user=profile.user,
                #     # type='approved_edu_university',
                #     message=(
                #         f'অভিনন্দন! আপনার প্রদানকৃত সকল তথ্য যাচাই করে প্রোফাইলটি অ্যাপ্রুভ করা হয়েছে। এখন থেকে আপনি {edu_university.department}, {edu_university.university} -এর সকল রিসোর্স ব্যবহার করতে পারবেন।'
                #     ),
                #     # additional_id_one = profile.edu_university.university,
                #     # additional_id_two = profile.edu_university.department
                # )
                    
                    Notification.objects.create(
                    user=profile.user,
                    type='coin_for_referral',
                    message=(
                        f'অভিনন্দন! {referrer_profile.fullname} আপনাকে রেফার করার জন্য 50টি Onebyzero Coin পেয়েছেন! আপনিও {profile.edu_university.university} বা বাংলাদেশের অন্য কোনো বিশ্ববিদ্যালয়ের যেকোনো বন্ধুকে রেফার করে 100 করে Onebyzero Coin অর্জন করতে পারেন। রেফার করতে লিংকে ক্লিক করুন।'
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
                # Notification.objects.create(
                #     user=profile.user,
                #     type='creating_new_account',
                #     message=(
                #         f'অভিনন্দন! আপনার প্রদানকৃত সকল তথ্য যাচাই করে প্রোফাইলটি অ্যাপ্রুভ করা হয়েছে। এখন থেকে আপনি '
                #         f'{edu_university.department.name + ", " if edu_university.department else ""}'
                #         f'{edu_university.discipline.name + ", " if edu_university.discipline else ""}'
                #         f'{edu_university.institute.name + ", " if edu_university.institute else ""}'
                #         f'{edu_university.university.name} -এর সকল রিসোর্স ব্যবহার করতে পারবেন।'
                #     )
                # )
     
                Notification.objects.create(
                    user=profile.user,
                    type='coin_for_referral',
                    message=(
                        f'অভিনন্দন! Onebyzero Edu -তে যুক্ত হওয়ার জন্য আপনি 25টি Onebyzero Coin পেয়েছেন! {profile.edu_university.university} বা বাংলাদেশের অন্য কোনো বিশ্ববিদ্যালয়ে অধ্যয়ণরত আপনার যেকোনো বন্ধুকে রেফার করে 100 করে Onebyzero Coin অর্জন করতে পারেন। রেফার করতে লিংকে ক্লিক করুন।'
                    )
                )
                
                
                
            Notification.objects.create(
                    user=profile.user,
                    type='req_for_upload',
                    message=(
                        f'এখন থেকে আপনি আপনার ডিপার্টমেন্টের যেকোনো কোর্সের জন্য Question / Book / Lecture Slide / Note আপলোড দিতে পারবেন। কয়েক মিনিট সময় ব্যয়ে আপনার যেকোনো আপলোডকৃত রিসোর্স থেকে বাংলাদেশের অসংখ্য বিশ্ববিদ্যালয় শিক্ষার্থী বছরের পর উপকৃত হতে থাকবে। আপলোড দিতে নেভিগেশন বার থেকে Upload আইকনে ক্লিক করুন।'
                    )
                )
            
            return redirect('edit_basic_personal_info')  # Redirect to the view page
    else:
        form = EduUniversityForm3(instance=edu_university)

    context = {
        'form': form,
    }
    
    return render(request, 'profile/my_profile/education/university/add_edu_university_step3.html', context)


@login_required
def edit_basic_personal_info(request):
    user = request.user

    # Use get_or_create to handle retrieving or creating the profile in one step
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = EditBasicProfileInfoForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_edu_university_my_profile')
        else:
            # Log errors if form validation fails
            print(form.errors)
    else:
        form = EditBasicProfileInfoForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'profile/my_profile/personal_info/edit_basic_personal_info.html', context)

@login_required
def edit_edu_university_my_profile(request, pk):
    profile = request.user.profile  # Fetch the logged-in user's profile
    edu_university = get_object_or_404(EduUniversity, profile=profile)
    
    ctxp_profile_edu_university = EduUniversity.objects.get(profile=profile)
    # print('yyy',ctxp_profile_edu_university.department)

    if request.method == 'POST':
        form = EduUniversityForm(request.POST, instance=edu_university)
        if form.is_valid():
            # Save the form data temporarily but do not commit yet
            updated_edu_university = form.save(commit=False)

            # Ensure updated instance reflects form data
            updated_edu_university.university = form.cleaned_data['university']
            updated_edu_university.faculty = form.cleaned_data['faculty']
            updated_edu_university.department = form.cleaned_data['department']
            updated_edu_university.departmental_batch = form.cleaned_data['departmental_batch']
            
            # Check if any fields have changed by comparing IDs and values
            if (updated_edu_university.university != ctxp_profile_edu_university.university or updated_edu_university.faculty != ctxp_profile_edu_university.faculty or updated_edu_university.department != ctxp_profile_edu_university.department or updated_edu_university.departmental_batch != ctxp_profile_edu_university.departmental_batch):
                
                # If changed, update the profile approval status
                if profile.edu_university:
                    profile.edu_university.is_approved = False

                # Send notification to the user
                Notification.objects.create(
                    user=request.user,
                    message=f'বিশ্ববিদ্যালয় সম্পর্কিত আপনার প্রদানকৃত তথ্যাবলী {updated_edu_university.department} এর ব্যাচ মডারেটর ({updated_edu_university.departmental_batch} Batch) এর কাছে পাঠিয়ে দেয়া হয়েছে। সর্বোচ্চ ২৪ ঘন্টার মধ্যে যাচাই করে আপনাকে উক্ত ডিপার্টমেন্টে যুক্ত করা হবে। অনুগ্রহ করে অপেক্ষা করুন।'
                )

                # Retrieve all batch moderators for the requested department and batch
                batch_moderators = Profile.objects.filter(
                    moderator_type='Batch Moderator',
                    edu_university__department=updated_edu_university.department,
                    edu_university__departmental_batch=updated_edu_university.departmental_batch
                )
                
                print('batch_moderators: ', batch_moderators)

                if batch_moderators.exists():
                    for batch_moderator in batch_moderators:
                        # Notification to each department's moderator
                        Notification.objects.create(
                            type='pending_for_verify_university',
                            user=batch_moderator.user,
                            message=f'প্রিয় ব্যাচ মডারেটর, আপনার ব্যাচে শিক্ষার্থী হিসেবে যুক্ত হওয়ার জন্য {profile.fullname} নামের একজন ইউজার অনুরোধ করেছেন। অনুগ্রহ করে মডারেটর প্যানেল থেকে যথাসম্ভব দ্রুত তার প্রোফাইল সঠিকভাবে যাচাই করে অ্যাপ্রুভ করুন।'
                        )

                # Save the updated instance to the database
                updated_edu_university.is_approved = False
                updated_edu_university.save()

                return redirect('view_edu_university_my_profile')
            
            else:
                updated_edu_university.save()
                return redirect('view_edu_university_my_profile')
    else:
        form = EduUniversityForm(instance=edu_university)

    return render(request, 'profile/my_profile/education/university/edit_edu_university_my_profile.html', {'form': form})



# def contributions(request):
#     user = request.user.id
#     profile = Profile.objects.get(user=user)

#     # QUESTIONS ========================================
#     qs_sem1 = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester='1st').count()
#     qs_sem2 = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester='2nd').count()
#     qs_sem3 = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester='3rd').count()
#     qs_sem4 = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester='4th').count()
#     qs_sem5 = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester='5th').count()
#     qs_sem6 = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester='6th').count()
#     qs_sem7 = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester='7th').count()
#     qs_sem8 = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester='8th').count()
#     qs_total = qs_sem1 + qs_sem2 + qs_sem3 + qs_sem4 + qs_sem5 + qs_sem6 + qs_sem7 + qs_sem8

#     # BOOKS ==============================================
#     books_sem1 = ResourcesBook.objects.filter(uploaded_by=profile, course__semester='1st').count()
#     books_sem2 = ResourcesBook.objects.filter(uploaded_by=profile, course__semester='2nd').count()
#     books_sem3 = ResourcesBook.objects.filter(uploaded_by=profile, course__semester='3rd').count()
#     books_sem4 = ResourcesBook.objects.filter(uploaded_by=profile, course__semester='4th').count()
#     books_sem5 = ResourcesBook.objects.filter(uploaded_by=profile, course__semester='5th').count()
#     books_sem6 = ResourcesBook.objects.filter(uploaded_by=profile, course__semester='6th').count()
#     books_sem7 = ResourcesBook.objects.filter(uploaded_by=profile, course__semester='7th').count()
#     books_sem8 = ResourcesBook.objects.filter(uploaded_by=profile, course__semester='8th').count()
#     books_total = books_sem1 + books_sem2 + books_sem3 + books_sem4 + books_sem5 + books_sem6 + books_sem7 + books_sem8

#     # LECTURE SLIDES ============================================
#     lectures_sem1 = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester='1st').count()
#     lectures_sem2 = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester='2nd').count()
#     lectures_sem3 = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester='3rd').count()
#     lectures_sem4 = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester='4th').count()
#     lectures_sem5 = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester='5th').count()
#     lectures_sem6 = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester='6th').count()
#     lectures_sem7 = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester='7th').count()
#     lectures_sem8 = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester='8th').count()
#     lectures_total = lectures_sem1 + lectures_sem2 + lectures_sem3 + lectures_sem4 + lectures_sem5 + lectures_sem6 + lectures_sem7 + lectures_sem8

#     # NOTES =============================================
#     notes_sem1 = ResourcesNote.objects.filter(uploaded_by=profile, course__semester='1st').count()
#     notes_sem2 = ResourcesNote.objects.filter(uploaded_by=profile, course__semester='2nd').count()
#     notes_sem3 = ResourcesNote.objects.filter(uploaded_by=profile, course__semester='3rd').count()
#     notes_sem4 = ResourcesNote.objects.filter(uploaded_by=profile, course__semester='4th').count()
#     notes_sem5 = ResourcesNote.objects.filter(uploaded_by=profile, course__semester='5th').count()
#     notes_sem6 = ResourcesNote.objects.filter(uploaded_by=profile, course__semester='6th').count()
#     notes_sem7 = ResourcesNote.objects.filter(uploaded_by=profile, course__semester='7th').count()
#     notes_sem8 = ResourcesNote.objects.filter(uploaded_by=profile, course__semester='8th').count()
#     notes_total = notes_sem1 + notes_sem2 + notes_sem3 + notes_sem4 + notes_sem5 + notes_sem6 + notes_sem7 + notes_sem8

#     # TOTAL UPLOADS ==================
#     total_uploads = sum([qs_total, books_total, lectures_total, notes_total], 0)
    
#     # TOTALS UPLOADS SEMESTER WISE
#     all_sem1 = sum([qs_sem1, books_sem1, lectures_sem1, notes_sem1], 0)
#     all_sem2 = sum([qs_sem2, books_sem2, lectures_sem2, notes_sem2], 0)
#     all_sem3 = sum([qs_sem3, books_sem3, lectures_sem3, notes_sem3], 0)
#     all_sem4 = sum([qs_sem4, books_sem4, lectures_sem4, notes_sem4], 0)
#     all_sem5 = sum([qs_sem5, books_sem5, lectures_sem5, notes_sem5], 0)
#     all_sem6 = sum([qs_sem6, books_sem6, lectures_sem6, notes_sem6], 0)
#     all_sem7 = sum([qs_sem7, books_sem7, lectures_sem7, notes_sem7], 0)
#     all_sem8 = sum([qs_sem8, books_sem8, lectures_sem8, notes_sem8], 0)
    
    
#     # Helper function to get resources by course for a specific semester
#     def get_resources_by_course(semester):
#         courses = Course.objects.filter(semester=semester)
#         questions = ResourcesQuestion.objects.filter(uploaded_by=profile, course__semester=semester)
#         books = ResourcesBook.objects.filter(uploaded_by=profile, course__semester=semester)
#         notes = ResourcesNote.objects.filter(uploaded_by=profile, course__semester=semester)
#         lectures = ResourcesLecture.objects.filter(uploaded_by=profile, course__semester=semester)

#         resources_by_course = {}
#         for course in courses:
#             resources_by_course[course.title] = {
#                 'questions': questions.filter(course=course),
#                 'books': books.filter(course=course),
#                 'notes': notes.filter(course=course),
#                 'lectures': lectures.filter(course=course),
#             }

#         return resources_by_course

#     # Get resources for each semester
#     resources_by_semester = {
#         '1st': get_resources_by_course('1st'),
#         '2nd': get_resources_by_course('2nd'),
#         '3rd': get_resources_by_course('3rd'),
#         '4th': get_resources_by_course('4th'),
#         '5th': get_resources_by_course('5th'),
#         '6th': get_resources_by_course('6th'),
#         '7th': get_resources_by_course('7th'),
#         '8th': get_resources_by_course('8th'),
#     }

#     context = {
#         # Questions
#         'resources_by_semester': resources_by_semester,
#         'qs_sem1': qs_sem1,
#         'qs_sem2': qs_sem2,
#         'qs_sem3': qs_sem3,
#         'qs_sem4': qs_sem4,
#         'qs_sem5': qs_sem5,
#         'qs_sem6': qs_sem6,
#         'qs_sem7': qs_sem7,
#         'qs_sem8': qs_sem8,
#         'qs_total': qs_total,

#         # Books
#         'books_sem1': books_sem1,
#         'books_sem2': books_sem2,
#         'books_sem3': books_sem3,
#         'books_sem4': books_sem4,
#         'books_sem5': books_sem5,
#         'books_sem6': books_sem6,
#         'books_sem7': books_sem7,
#         'books_sem8': books_sem8,
#         'books_total': books_total,

#         # Notes
#         'notes_sem1': notes_sem1,
#         'notes_sem2': notes_sem2,
#         'notes_sem3': notes_sem3,
#         'notes_sem4': notes_sem4,
#         'notes_sem5': notes_sem5,
#         'notes_sem6': notes_sem6,
#         'notes_sem7': notes_sem7,
#         'notes_sem8': notes_sem8,
#         'notes_total': notes_total,

#         # Lectures
#         'lectures_sem1': lectures_sem1,
#         'lectures_sem2': lectures_sem2,
#         'lectures_sem3': lectures_sem3,
#         'lectures_sem4': lectures_sem4,
#         'lectures_sem5': lectures_sem5,
#         'lectures_sem6': lectures_sem6,
#         'lectures_sem7': lectures_sem7,
#         'lectures_sem8': lectures_sem8,
#         'lectures_total': lectures_total,
     
#         # Total
#         'total_uploads': total_uploads,
#         'all_sem1': all_sem1,
#         'all_sem2': all_sem2,
#         'all_sem3': all_sem3,
#         'all_sem4': all_sem4,
#         'all_sem5': all_sem5,
#         'all_sem6': all_sem6,
#         'all_sem7': all_sem7,
#         'all_sem8': all_sem8,
#     }

#     return render(request, 'profile/my_profile/contributions.html', context)


@login_required
def generate_referral_link(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        # Ensure the profile is saved and referral code is generated
        if not profile.referral_code:
            profile.generate_referral_code()
        referral_link = request.build_absolute_uri(f'/?ref={profile.referral_code}')
        return render(request, 'profile/referral_link.html', {'referral_link': referral_link})


from django.shortcuts import get_object_or_404

def handle_referral(request):
    # Assuming `ref` is passed as a GET parameter in the URL
    referral_code = request.GET.get('ref')
    # print('referral_code', referral_code)
    if referral_code:
        # Try to find the profile that corresponds to the referral code
        referrer_profile = get_object_or_404(Profile, referral_code=referral_code)
        print('referrer_profile', referrer_profile)

        # Check if the user is authenticated and has a profile
        if request.user.is_authenticated:
            try:
                profile = request.user.profile

                # Check if profile.edu_university is approved
                # if profile.edu_university and profile.edu_university.is_approved:
                    # Award coins to the referrer
                referrer_profile.total_coins += 100
                referrer_profile.save()

                # Optionally, add a CoinTransaction entry
                CoinTransaction.objects.create(
                    profile=referrer_profile,
                    activity='refer_new_user',
                    coins=100
                )

                # Provide feedback to the user
                messages.success(request, 'Referral successful! 100 coins have been awarded to the referrer.')

                # else:
                #     # Handle case where edu_university is not approved
                #     messages.warning(request, 'Your university must be approved to complete the referral process.')

            except Profile.DoesNotExist:
                # Handle case where the user does not have a profile
                messages.error(request, 'You need to create a profile before you can complete the referral process.')

    return redirect('home')  # Replace with the view you want to redirect to


def check_referral(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            # Create a new profile if it doesn't exist
            user = request.user
            profile = Profile(
                user=user,
                fullname=user.get_full_name(),
                email=user.email
            )
            profile.save()

        # Redirect if referral is done
        if profile.is_referral_done:
            return redirect('personal_info_my_profile')
        
        # profile.is_visited_check_referral = True
        # profile.save()

        # Debugging prints
        # print(f"Request Method: {request.method}")
        
        if request.method == 'POST':
            # print('POST request received.')
            form = ReferralForm(request.POST)
            if form.is_valid():
                # print('Form is valid.')
                referral_url = form.cleaned_data['referral_url']
                referral_code = referral_url.split('ref=')[-1]
                
                # print(f"Referral URL: {referral_url}")
                # print(f"Referral Code: {referral_code}")
                
                referral_profile = Profile.objects.filter(referral_code=referral_code).first()
                profile.referred_by = referral_profile
                profile.is_visited_check_referral = True
                profile.save()

                if not profile.referred_by_code and referral_profile:
                    profile.referred_by_code = referral_code
                    profile.save()
                    messages.success(request, f'ধন্যবাদ! আপনাকে {referral_profile.fullname} রেফার করেছেন। আপনার প্রোফাইলে বিশ্ববিদ্যালয় সম্পর্কিত প্রয়োজনীয় তথ্যাবলী যুক্ত করার সাথে সাথেই 50টি Onebyzero Coin পেয়ে যাবেন। এবারে নিচের বাটনে ক্লিক করে তথ্যগুলো আপডেট করুন।')
                else:
                    messages.warning(request, 'দুঃখিত! আপনি ভুল রেফারাল লিংক দিয়েছেন। অনুগ্রহ করে সঠিক রেফারাল লিংক বসান।')
                return redirect('check_referral')
            else:
                print('Form is invalid.')
        else:
            form = ReferralForm()
                    
        return render(request, 'profile/check_referral.html', {'form': form})
    else:
        return redirect('login')
