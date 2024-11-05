from django.db import models

from apps.account.models.profile_models import Profile

class Task(models.Model):
    TASK_CHOICES = [
        ('Added Syllabus/Courses in a Department', 'Added Syllabus/Courses in a Department'),
        ('Added Info for a University', 'Added Info for a University'),
        ('Added Previous Resources', 'Added Previous Resources'),
        ('Video Editing', 'Video Editing'),
        ('Graphic Design', 'Graphic Design'),
        ('Script Writing', 'Script Writing'),
        ('Interview Program', 'Interview Program'),
        ('Video Timestamp', 'Video Timestamp'),
        ('Facebook Post', 'Facebook Post'),
    ]
    
    team_member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200, choices=TASK_CHOICES, blank=True, null=True)
    blank_task_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')  # Store duration in minutes
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.task_name} by {self.team_member}'
