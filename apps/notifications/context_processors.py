from django.db.models import Count
from apps.notifications.models import Notification

def unread_notifications_count(request):
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(user=request.user, read=False).count()
    else:
        unread_count = 0
    return {
        'unread_notifications_count': unread_count,
    }
