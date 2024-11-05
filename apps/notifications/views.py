# apps/notifications/views.py
from django.shortcuts import render, redirect
from .models import Notification
from apps.account.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Notification
from utils.permissions import *

def notifications(request):
    if request.user.is_authenticated:
        user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    else:
        user_notifications = []  # Empty list or another method of indicating no notifications

    return render(request, 'notifications/notifications.html', {'notifications': user_notifications})

def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.read = True
    notification.save()
    return redirect('notifications')


def mark_all_as_read(request):
    if request.user.is_authenticated:
        Notification.objects.filter(user=request.user, read=False).update(read=True)
    return redirect('notifications')  # Redirect back to the notifications page


@user_passes_test(is_team_member, login_url='home')
def send_notification_to_all(type, message, additional_id_one=None, additional_id_two=None):
    # Get all profiles that have users
    profiles = Profile.objects.select_related('user').all()
    notifications = [
        Notification(
            type=type,
            user=profile.user,
            profile=profile,
            message=message,
            additional_id_one=additional_id_one,
            additional_id_two=additional_id_two
        )
        for profile in profiles
    ]
    # Bulk create notifications for performance
    Notification.objects.bulk_create(notifications)


@user_passes_test(is_team_member, login_url='home')
def notify_all_users(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        message = request.POST.get('message')
        
        # Call the function to send notifications to all users with profiles
        send_notification_to_all(type=type, message=message)
        return JsonResponse({'message': 'Notifications sent to all users.'})
    
    return render(request, 'notifications/notify_all.html')  # Renders a template to input type and message
