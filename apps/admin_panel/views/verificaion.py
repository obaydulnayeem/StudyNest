from django.shortcuts import render, redirect, get_object_or_404
from ..models import *
from apps.account.models.education_models import *
from apps.notifications.models import *
from apps.university.models import *
from django.contrib.auth.models import User


def sent_verification_req(request):
    user = request.user
    already_sent = PendingUser.objects.filter(requested_user=user).exists()

    # Get the profile and associated EduUniversity
    profile = Profile.objects.get(user=user)
    edu_university = EduUniversity.objects.get(profile=profile)

    department = edu_university.department
    semester = edu_university.semester

    # Filter moderators based on department and semester using EduUniversity
    departmental_moderators = Profile.objects.filter(
        eduuniversity__department=department, 
        moderator_type='Departmental Moderator'
    )

    batch_moderators = Profile.objects.filter(
        eduuniversity__department=department, 
        eduuniversity__semester=semester, 
        moderator_type='Batch Moderator'
    )

    if request.method == 'POST':
        if not already_sent:
            PendingUser.objects.create(
                requested_user=user
            )

        Notification.objects.create(
            user=user,
            message='Your verification request has been sent to the moderator.'
        )

        for moderator in batch_moderators:
            Notification.objects.create(
                type='pending_for_verify_users',
                user=moderator.user,
                message=f'A user has requested to be a student in your department ({department}). Please verify it.'
            )

        return render(request, 'verification/sent_verification_req.html')

    return render(request, 'verification/sent_verification_req.html')

    
    # return render(request, 'access_denied.html')
    
    
def need_verification(request):    
    return render(request, 'verification/need_verification.html', status=403)

def pending_for_verify_users(request):
    pending_users = PendingUser.objects.all()
    return render(request, 'moderators/batch/pending_for_verify_users.html', {'pending_users': pending_users})

def batch_wise_users(request):
    # Get the profile of the current user
    profile = Profile.objects.get(user=request.user)
    
    # Get the EduUniversity associated with the profile
    edu_university = EduUniversity.objects.get(profile=profile)
    
    # Get the department and departmental_batch from the EduUniversity
    department = edu_university.department
    departmental_batch = edu_university.departmental_batch
    
    # Filter EduUniversity instances that match the department and departmental_batch
    edu_universities = EduUniversity.objects.filter(department=department, departmental_batch=departmental_batch)
    
    # Retrieve the associated profiles for the filtered EduUniversity instances
    batch_wise_users = Profile.objects.filter(eduuniversity__in=edu_universities)
    
    return render(request, 'moderators/batch/batch_wise_users.html', {'batch_wise_users': batch_wise_users})


def make_verified_user(request, user_id):
    # print('make_verified_user', user_id)
    if request.method == 'POST':

        requested_user = Profile.objects.get(id=user_id)
        # print('tttttttttt', requested_user.email)
        requested_user.is_verified = True
        requested_user.save()
        # print(requested_user.is_verified)
        
        Notification.objects.create(
            user = requested_user.user,
            # notification_type = 1
            message = f"Congratulations! Your Batch Moderator {request.user.profile.fullname} has verified your account."
        )

        return redirect('pending_for_verify_users')
    return render(request, 'moderator_base.html')

def make_not_verified_user(request, user_id):
    # print('make_not_verified_user', user_id)
    if request.method == 'POST':
        user = get_object_or_404(Profile, id=user_id)
        user.is_verified = False
        user.save()
        return redirect('batch_wise_users')
    return render(request, 'moderator_base.html')