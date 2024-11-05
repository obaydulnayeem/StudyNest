from django import forms
from .models import *

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'date_applied', 
            'job_title', 
            'company_name', 
            'work_environment',
            'job_type',
            'experience_level',
            'job_link',
            'job_description', 
            'job_location',
            'expected_salary', 
            'resume',
            'company_website',
            'company_linkedin_link',
            'company_location', 
            'hr_profile_link', 
            'notes',
            'is_in_task',
            'current_status',
            # 'interview_date',
        ]
        widgets = {
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job title',
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name',
            }),
            'company_website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company website (optional)',
            }),
            'company_linkedin_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company LinkedIn link (optional)',
            }),
            'company_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company location (optional)',
            }),
            'date_applied': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'job_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job description',
                'rows': 4,
            }),
            'job_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job location',
            }),
            'expected_salary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Expected Salary (optional)',
            }),
            'job_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job circular link',
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-control',
                'type': 'file',
                'accept': '.pdf, .doc, .docx',
            }),
            # 'interview_date': forms.DateInput(attrs={
            #     'class': 'form-control',
            #     'type': 'date',
            # }),
            'hr_profile_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'HR Profile Link (optional)',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional notes (optional)',
                'rows': 4,
            }),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'work_environment': forms.Select(attrs={'class': 'form-control'}),
            'experience_level': forms.Select(attrs={'class': 'form-control'}),

            # New Widgets for is_in_task and current_status
            'is_in_task': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'current_status': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Current Status',
                'rows': 2,
            }),
        }
        labels = {
            'job_title': 'Job Title',
            'company_name': 'Company Name',
            'company_website': 'Company Website (optional)',
            'company_location': 'Company Location (optional)',
            'date_applied': 'Date Applied',
            'job_description': 'Job Description',
            'expected_salary': 'Expected Salary (optional)',
            # 'interview_date': 'Interview Date (optional)',
            'resume': 'Resume (optional)',
            'hr_profile_link': 'HR Profile Link (optional)',
            'notes': 'Notes (optional)',
            'job_type': 'Job Type',
            'work_environment': 'Work Environment',
            'experience_level': 'Experience Level',
            'is_in_task': 'Is In Task',
            'current_status': 'Current Status',
        }




class SaveJobForm(forms.ModelForm):
    class Meta:
        model = SavedJobs
        fields = ['job_link', 'published', 'deadline']  # Only include the job_link field
        widgets = {
            'job_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job Link'}),
            'published': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        labels = {
            'job_link': 'Job Link',
            'published': 'Published',
            'deadline': 'Deadline',
        }
        
class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyList
        fields = ['company_name', 'company_location', 'website_link', 'linkedin', 'apply_link']
        
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name',
            }),
            'company_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company location',
            }),
            'website_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter website link (optional)',
            }),
            'linkedin': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter linkedin link (optional)',
            }),
            'apply_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter application link (optional)',
            }),
        }

        labels = {
            'company_name': 'Company Name',
            'company_location': 'Company Location',
            'apply_link': 'Apply Link (optional)',
            'website_link': 'Website Link (optional)',
            'linkedin': 'Linkedin Link (optional)',
        }
        

class FolloweeForm(forms.ModelForm):
    class Meta:
        model = Followee
        fields = ['name', 'designation', 'linkedin', 'github', 'facebook']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
        }
