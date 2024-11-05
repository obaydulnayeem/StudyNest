from django.db import models
from django.contrib.auth.models import User
from apps.account.models import Profile
from django.utils import timezone

WORK_ENVIRONMENT_TYPES = [
    ('On-site', 'On-site'),
    ('Remote', 'Remote'),
    ('Hybrid', 'Hybrid'),
]

JOB_TYPES = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Internship', 'Internship'),
    ('Contract', 'Contract'),
    ('Freelance', 'Freelance'),
]

EXPERIENCE_LEVELS = [
    ('Fresher', 'Fresher'),
    ('Mid-Senior', 'Mid-Senior'),
    ('Senior', 'Senior'),
    ('Associate', 'Associate'),
    ('Executive', 'Executive'),
]

class JobApplication(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='job_applications_tracker')
    job_title = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255, choices=JOB_TYPES, blank=True, null=True)
    work_environment = models.CharField(max_length=255, choices=WORK_ENVIRONMENT_TYPES, blank=True, null=True)
    experience_level = models.CharField(max_length=255, choices=EXPERIENCE_LEVELS, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True, null=True)
    company_linkedin_link = models.URLField(blank=True, null=True)
    company_location = models.CharField(max_length=255, blank=True, null=True)
    date_applied = models.DateField()
    job_description = models.TextField(blank=True, null=True)
    job_location = models.CharField(max_length=255, blank=True, null=True)
    expected_salary = models.CharField(max_length=255, blank=True, null=True)
    interview_date = models.DateField(blank=True, null=True)
    job_link = models.URLField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True)
    hr_profile_link = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    # added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    added_job_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    is_in_task = models.BooleanField(default=False)
    current_status = models.TextField(blank=True, null=True)
    cause_of_cancellation = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.job_title} at {self.company_name}'

class SavedJobs(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job_link = models.URLField()
    added_at = models.DateTimeField(auto_now_add=True)
    published = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    is_applied = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.job_link}'
    
class CompanyList(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_location = models.CharField(max_length=255, blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    apply_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.company_name}'
    
    
class Followee(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=255)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)