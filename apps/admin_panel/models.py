from django.db import models
from apps.account.models.profile_models import Profile
from django.contrib.auth.models import User
from choices.choices import *
from django.db.models import Min
from django.db.models import Subquery, OuterRef
from django.db.models import F

class ModeratorRequest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    requested_moderator_type = models.CharField(max_length=50, choices=MODERATOR_TYPE_CHOICES)
    
    requested_at = models.DateTimeField(auto_now_add=True)
    
    is_approved_initial = models.BooleanField(default=False)
    
    approved_initial_by = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='approved_initial_by')
    
    approved_initial_at = models.DateTimeField(blank=True, null=True)
    
    is_approved_final = models.BooleanField(default=False)
    
    approved_final_at = models.DateTimeField(blank=True, null=True)
    
    is_running = models.BooleanField(default=False)
    
    is_temporary = models.BooleanField(default=False)
    
    has_laptop = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    is_dropped_student = models.BooleanField(default=False)
    write_something = models.TextField(blank=True, null=True)
    read_terms_and_conditions = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.profile.user} - {self.requested_moderator_type}"
    
class PendingUser(models.Model):
    # profile_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # requested_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.requested_user.username} - {self.requested_at}"




# class SomethingModel(models.Model):
#     name = models.CharField(max_length=255)

# class AdminModel(models.Model):
#     name = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     # Add other fields as needed