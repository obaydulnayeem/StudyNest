from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

def is_any_moderator(user):
    return (
        user.is_authenticated and
        user.profile.moderator_type and
        user.profile.moderator_info.is_running
    )

def is_batch_moderator(user):
    return (
        user.is_authenticated and
        user.profile.moderator_type == 'Batch Moderator' and
        user.profile.moderator_info.is_running
    )

def is_departmental_moderator(user):
    return (
        user.is_authenticated and
        user.profile.moderator_type == 'Departmental Moderator' and
        user.profile.moderator_info.is_running
    )
    
def is_discipline_moderator(user):
    return (
        user.is_authenticated and
        user.profile.moderator_type == 'Discipline Moderator' and
        user.profile.moderator_info.is_running
    )
    

def is_institute_moderator(user):
    return (
        user.is_authenticated and
        user.profile.moderator_type == 'Institute Moderator' and
        user.profile.moderator_info.is_running
    )

def is_university_moderator(user):
    return (
        user.is_authenticated and
        user.profile.moderator_type == 'University Moderator' and
        user.profile.moderator_info.is_running
    )
    
    
def is_central_moderator(user):
    return (
        user.is_authenticated and
        user.profile.moderator_type == 'Central Moderator' and
        user.profile.moderator_info.is_running
    )
    

def is_batch_or_central_moderator(user):
    return (
        user.is_authenticated and
        (user.profile.moderator_type == 'Batch Moderator' or user.profile.moderator_type == 'Central Moderator') and
        user.profile.moderator_info.is_running
    )
    

def is_batch_or_departmental_or_central_moderator(user):
    return (
        user.is_authenticated and
        (user.profile.moderator_type == 'Batch Moderator' or user.profile.moderator_type == 'Departmental Moderator' or user.profile.moderator_type == 'Central Moderator') and
        user.profile.moderator_info.is_running
    )

def is_department_or_university_moderator(user):
    return (
        user.is_authenticated and
        (user.profile.moderator_type == 'Departmental Moderator' or user.profile.moderator_type == 'University Moderator') and
        user.profile.moderator_info.is_running
    )
    
def is_departmental_or_university_or_central_moderator(user):
    return (
        user.is_authenticated and
        (user.profile.moderator_type == 'Departmental Moderator' or user.profile.moderator_type == 'University Moderator' or user.profile.moderator_type == 'Central Moderator') and
        user.profile.moderator_info.is_running
    )
    
    
def has_resources_upload_permission(user):
    return (
        user.is_authenticated and
        user.profile.edu_university
    )
    
def has_resources_edit_permission(user, resource):
    return (
        user.is_authenticated and (
            user.profile == resource.uploaded_by or  # Uploader
            user.profile.moderator_type == 'Batch Moderator' or  # Batch Moderator
            user.profile.moderator_type == 'Departmental Moderator' or  # Departmental Moderator
            user.profile.moderator_type == 'Central Moderator'  # Central Moderator
        )
    )

def has_resources_delete_permission(user, resource):
    return (
        user.is_authenticated and (
            user.profile == resource.uploaded_by or  # Uploader
            user.profile.moderator_type == 'Central Moderator'  # Central Moderator
        )
    )
    
    
# utils/permissions.py
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings
import os
from apps.university.models import *  # Adjust the import according to your app structure

# def serve_protected_question(request, resource_id):
#     resource = get_object_or_404(ResourcesQuestion, id=resource_id)
    
#     resource_department = resource.department
#     resource_university = resource.university
    
#     context = {
#         'resource': resource,
#         'resource_department': resource_department,
#         'resource_university': resource_university,
#     }
    
#     if not request.user.is_authenticated:
#         return render(request, 'error_pages/403_forbidden.html', context)
    
#     user_profile = request.user.profile
    
#     if user_profile.edu_university.department != resource.department:
#         return render(request, 'error_pages/403_forbidden.html', context)
    
#     file_full_path = os.path.join(settings.MEDIA_ROOT, resource.question_file.name)
    
#     # Determine the content type based on the file extension
#     file_extension = os.path.splitext(file_full_path)[1].lower()
    
#     if file_extension == '.pdf':
#         content_type = 'application/pdf'
#     elif file_extension in ['.png', '.jpeg', '.jpg']:
#         content_type = f'image/{file_extension[1:]}'  # Strip the dot and use the extension as the image type
#     else:
#         content_type = 'application/octet-stream'  # Fallback for unknown types
    
#     with open(file_full_path, 'rb') as f:
#         response = HttpResponse(f.read(), content_type=content_type)
#         response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_full_path)}"'
#         return response


def serve_protected_question(request, resource_id):
    resource = get_object_or_404(ResourcesQuestion, id=resource_id)
    
    resource_department = resource.department
    resource_university = resource.university
    
    context = {
        'resource': resource,
        'resource_department': resource_department,
        'resource_university': resource_university,
    }
    
    if not request.user.is_authenticated:
        return render(request, 'error_pages/403_forbidden.html', context)
    
    user_profile = request.user.profile
    
    # Check if user_profile.edu_university is None or if department is None
    if user_profile.edu_university is None or user_profile.edu_university.department != resource.department:
        return render(request, 'error_pages/403_forbidden.html', context)
    
    file_full_path = os.path.join(settings.MEDIA_ROOT, resource.question_file.name)
    
    # Determine the content type based on the file extension
    file_extension = os.path.splitext(file_full_path)[1].lower()
    
    if file_extension == '.pdf':
        content_type = 'application/pdf'
    elif file_extension in ['.png', '.jpeg', '.jpg']:
        content_type = f'image/{file_extension[1:]}'  # Strip the dot and use the extension as the image type
    else:
        content_type = 'application/octet-stream'  # Fallback for unknown types
    
    with open(file_full_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=content_type)
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_full_path)}"'
        return response


def serve_protected_book(request, resource_id):
    resource = get_object_or_404(ResourcesBook, id=resource_id)
    
    resource_department = resource.department
    resource_university = resource.university
    
    context = {
        'resource': resource,
        'resource_department': resource_department,
        'resource_university': resource_university,
    }
    
    if not request.user.is_authenticated:
        return render(request, 'error_pages/403_forbidden.html', context)
    
    user_profile = request.user.profile
    
    # Check if user_profile.edu_university is None or if department is None
    if user_profile.edu_university is None or user_profile.edu_university.department != resource.department:
        return render(request, 'error_pages/403_forbidden.html', context)
    
    file_full_path = os.path.join(settings.MEDIA_ROOT, resource.book_file.name)
    
    # Determine the content type based on the file extension
    file_extension = os.path.splitext(file_full_path)[1].lower()
    
    if file_extension == '.pdf':
        content_type = 'application/pdf'
    # elif file_extension in ['.png', '.jpeg', '.jpg']:
    #     content_type = f'image/{file_extension[1:]}'  # Strip the dot and use the extension as the image type
    else:
        content_type = 'application/octet-stream'  # Fallback for unknown types
    
    with open(file_full_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=content_type)
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_full_path)}"'
        return response


def serve_protected_note(request, resource_id):
    resource = get_object_or_404(ResourcesNote, id=resource_id)
    
    resource_department = resource.department
    resource_university = resource.university
    
    context = {
        'resource': resource,
        'resource_department': resource_department,
        'resource_university': resource_university,
    }
    
    if not request.user.is_authenticated:
        return render(request, 'error_pages/403_forbidden.html', context)
    
    user_profile = request.user.profile
    
    # Check if user_profile.edu_university is None or if department is None
    if user_profile.edu_university is None or user_profile.edu_university.department != resource.department:
        return render(request, 'error_pages/403_forbidden.html', context)
    
    file_full_path = os.path.join(settings.MEDIA_ROOT, resource.note_file.name)
    
    # Determine the content type based on the file extension
    file_extension = os.path.splitext(file_full_path)[1].lower()
    
    if file_extension == '.pdf':
        content_type = 'application/pdf'
    elif file_extension in ['.png', '.jpeg', '.jpg']:
        content_type = f'image/{file_extension[1:]}'  # Strip the dot and use the extension as the image type
    else:
        content_type = 'application/octet-stream'  # Fallback for unknown types
    
    with open(file_full_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=content_type)
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_full_path)}"'
        return response
    
    
def serve_protected_lecture(request, resource_id):
    resource = get_object_or_404(ResourcesLecture, id=resource_id)
    
    resource_department = resource.department
    resource_university = resource.university
    
    context = {
        'resource': resource,
        'resource_department': resource_department,
        'resource_university': resource_university,
    }
    
    if not request.user.is_authenticated:
        return render(request, 'error_pages/403_forbidden.html', context)
    
    user_profile = request.user.profile
    
    # Check if user_profile.edu_university is None or if department is None
    if user_profile.edu_university is None or user_profile.edu_university.department != resource.department:
        return render(request, 'error_pages/403_forbidden.html', context)
    
    file_full_path = os.path.join(settings.MEDIA_ROOT, resource.lecture_file.name)
    
    # Determine the content type based on the file extension
    file_extension = os.path.splitext(file_full_path)[1].lower()
    
    if file_extension == '.pdf':
        content_type = 'application/pdf'
    elif file_extension == '.ppt':
        content_type = 'application/vnd.ms-powerpoint'
    elif file_extension == '.pptx':
        content_type = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    elif file_extension == '.odp':
        content_type = 'application/vnd.oasis.opendocument.presentation'
    else:
        content_type = 'application/octet-stream'  # Fallback for unknown types
    
    with open(file_full_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=content_type)
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_full_path)}"'
        return response


def is_team_member(user):
    return (
        user.profile.is_team_member or
        user.is_superuser
    )