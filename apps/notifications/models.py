# apps/notifications/models.py
from django.db import models
from django.contrib.auth.models import User

NOTIFICATION_TYPE_CHOICES = (
    ('pending_for_verify_users', 'pending_for_verify_users'),
    ('approved_as_moderator', 'approved_as_moderator'),
    ('given_previous_website_coins', 'given_previous_website_coins'),
)

class Notification(models.Model):
    type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE_CHOICES, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    profile = models.ForeignKey('account.Profile', on_delete=models.CASCADE, related_name='notifications', blank=True, null=True)
    message = models.TextField()
    additional_id_one = models.PositiveIntegerField(blank=True, null=True)
    additional_id_two = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Notification for {self.user.username}"
