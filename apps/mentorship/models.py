from django.db import models
from choices.varsity.varsity_choices import *
from apps.university.models import *
from apps.account.models.profile_models import Profile

class AskModel(models.Model):
    asked_by = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    
    # year = models.CharField(max_length=50, choices=YEAR_CHOICES, blank=True, null=True)
    
    semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES, blank=True, null=True)
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    
    problem_details = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.course} - {self.semester}" if self.course and self.semester else "AskModel"

session_type_choices = [
    ('short_term', 'Short Term'),
    ('long_term', 'Long Term'),
]

session_duration_choices = [
    ('15', '15 minutes'),
    ('30', '30 minutes'),
    ('45', '45 minutes'),
    ('60', '60 minutes'),
]

class SessionDetails(models.Model):
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    session_type = models.CharField(max_length=50, choices=session_type_choices)
    session_duration = models.CharField(max_length=50, choices=session_duration_choices)
    available_dates = models.DateField()
    available_time_slots = models.CharField(max_length=5)


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('bkash', 'bKash'),
        ('nagad', 'Nagad'),
        ('rocket', 'Rocket'),
    ]

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.method} - {self.transaction_id}"
