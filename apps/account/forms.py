from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from apps.university.models import *
# from apps.education.models import *
from apps.account.models.education_models import *
from apps.account.models.profile_models import *
# from .models import User, Profile
from django.forms import modelformset_factory
from choices.varsity.varsity_choices import *

class SignupForm(UserCreationForm):
    fullname = forms.CharField(max_length=100, required=True)
    nickname = forms.CharField(max_length=100, required=False)
    university = forms.ModelChoiceField(queryset=University.objects.all(), required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)
    session = forms.ChoiceField(choices=SESSION_CHOICES, required=True)
    departmental_batch = forms.ChoiceField(choices=DEPARTMENT_OR_VARCITY_BATCH_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Include other fields from the User model

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['university'].label = 'University'
    #     self.fields['department'].label = 'Department'

    #     if all(field in self.data for field in ['university', 'department']):
    #         try:
    #             university_id = int(self.data.get('university'))
    #             department_id = int(self.data.get('department'))
                
    #             # Filter the 'department' queryset based on the selected 'university'.
    #             self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')

    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['department'].queryset = self.instance.university.department_set.order_by('name')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        # Create a Profile instance and associate it with the user
        profile = Profile.objects.create(user=user,
        email = self.cleaned_data['email'], 
        fullname = self.cleaned_data['fullname'], 
        nickname = self.cleaned_data['nickname'],
        university=self.cleaned_data['university'], department=self.cleaned_data['department'],
        session=self.cleaned_data['session'],
        departmental_batch=self.cleaned_data['departmental_batch'])

        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'user_type', 'profile_image', 'email']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'gender',
            'fullname',
            'nickname',
            'profile_image',
            'email',
            'email_visibility',
            'blood_group',
            'blood_group_visibility',
            'mobile_number',
            'mobile_number_visibility',
            'facebook_id',
            'facebook_id_visibility',
            'instagram_id',
            'instagram_id_visibility',
            'linkedin_id',
            'linkedin_id_visibility',
            'youtube_channel',
            'youtube_channel_visibility',
            'twitter_id',
            'twitter_id_visibility',
            'github_id',
            'github_id_visibility',
            'google_scholar',
            'google_scholar_visibility',
            # 'user_type',
        ]
        widgets = {
            # 'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter your bio.'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Example: Software Developer'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your nickname'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'email_visibility': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'blood_group_visibility': forms.Select(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            'mobile_number_visibility': forms.Select(attrs={'class': 'form-control'}),
            'facebook_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Facebook ID link'}),
            'facebook_id_visibility': forms.Select(attrs={'class': 'form-control'}),
            'instagram_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Instagram ID link'}),
            'instagram_id_visibility': forms.Select(attrs={'class': 'form-control'}),
            'linkedin_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your LinkedIn ID link'}),
            'linkedin_id_visibility': forms.Select(attrs={'class': 'form-control'}),
            'youtube_channel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your YouTube Channel link'}),
            'youtube_channel_visibility': forms.Select(attrs={'class': 'form-control'}),
            'twitter_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Twitter ID link'}),
            'twitter_id_visibility': forms.Select(attrs={'class': 'form-control'}),
            'github_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your GitHub ID link'}),
            'github_id_visibility': forms.Select(attrs={'class': 'form-control'}),
            'google_scholar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Google Scholar profile link'}),
            'google_scholar_visibility': forms.Select(attrs={'class': 'form-control'}),
            # 'user_type': forms.Select(attrs={'class': 'form-control'}),
        }

class EduUniversityForm(forms.ModelForm):
    class Meta:
        model = EduUniversity
        fields = [
            'university_type', 'university', 'faculty', 
            'department', 'session', 'varsity_batch', 
            'departmental_batch', 'degree', 'semester', 
            'start_year', 'end_year', 'student_id', 'approval_query'
        ]
        widgets = {
            'university_type': forms.Select(attrs={'class': 'form-control'}),
            'university': forms.Select(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'varsity_batch': forms.Select(attrs={'class': 'form-control'}),
            'departmental_batch': forms.Select(attrs={'class': 'form-control'}),
            'degree': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'start_year': forms.Select(attrs={'class': 'form-control'}),
            'end_year': forms.Select(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID or Class Roll (Example: 24CSE001) or others'}),
            'approval_query': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'আপনার ব্যাচ সম্পর্কে এমন একটি তথ্য লিখুন যেটি দিয়ে আমরা আপনাকে সঠিকভাবে শনাক্ত করতে পারি। উদাহরণস্বরূপঃ আপনার ব্যাচের বর্তমান সিআর (Class Representative) এর নাম অথবা অন্যকিছু।'}),
        }

    def __init__(self, *args, **kwargs):
        super(EduUniversityForm, self).__init__(*args, **kwargs)
        self.fields['university'].queryset = University.objects.all().order_by('name')
        self.fields['faculty'].queryset = Faculty.objects.all().order_by('name')
        self.fields['department'].queryset = Department.objects.all().order_by('name')
        

class EduUniversityForm1(forms.ModelForm):
    class Meta:
        model = EduUniversity
        fields = [
            'university_type', 'university', 'blank_university',
        ]
        widgets = {
            'university_type': forms.Select(attrs={'class': 'form-control'}),
            'university': forms.Select(attrs={'class': 'form-control'}),
            'blank_university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter university name if not avilable in the above options; otherwise leave blank'}),
            # 'form-control', 'placeholder': 'Enter '
        }

    # def __init__(self, *args, **kwargs):
    #     super(EduUniversityForm, self).__init__(*args, **kwargs)
    #     self.fields['university'].queryset = University.objects.all().order_by('name')
    #     self.fields['faculty'].queryset = Faculty.objects.all().order_by('name')
    #     self.fields['department'].queryset = Department.objects.all().order_by('name') 
    
    
class EduUniversityForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        super(EduUniversityForm2, self).__init__(*args, **kwargs)
        if university:
            self.fields['faculty'].queryset = Faculty.objects.filter(university=university)
            self.fields['institute'].queryset = Institute.objects.filter(university=university)
            self.fields['school'].queryset = School.objects.filter(university=university)
            self.fields['center'].queryset = Center.objects.filter(university=university)
            self.fields['department'].queryset = Department.objects.filter(university=university)
            self.fields['discipline'].queryset = Discipline.objects.filter(university=university)
            # self.fields['department'].queryset = Department.objects.filter(university=university)
            # self.fields['discipline'].queryset = Discipline.objects.filter(university=university)
    
    class Meta:
        model = EduUniversity
        fields = [
            'faculty', 'blank_faculty', 'institute', 'blank_institute', 'school', 'blank_school', 'center', 'blank_center', 'department', 'blank_department', 'discipline', 'blank_discipline',
        ]
        widgets = {
            'faculty': forms.Select(attrs={'class': 'form-control'}),
            'blank_faculty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter faculty name if not avilable in the above options; otherwise leave blank'}),
            'institute': forms.Select(attrs={'class': 'form-control'}),
            'blank_institute': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter institute name if not avilable in the above options; otherwise leave blank'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
            'blank_school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school name if not avilable in the above options; otherwise leave blank'}),
            'center': forms.Select(attrs={'class': 'form-control'}),
            'blank_center': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter center name if not avilable in the above options; otherwise leave blank'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'blank_department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department name if not avilable in the above options; otherwise leave blank'}),
            'discipline': forms.Select(attrs={'class': 'form-control'}),
            'blank_discipline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter discipline name if not avilable in the above options; otherwise leave blank'}),
        }
        
        
class EduUniversityForm3(forms.ModelForm):
    class Meta:
        model = EduUniversity
        fields = [
            'session', 'varsity_batch', 'departmental_batch', 'discipline_batch', 'institute_batch', 'degree', 'blank_degree', 'semester',
            'start_year', 'end_year', 'student_id', 'approval_query'
        ]
        widgets = {
            'discipline': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'varsity_batch': forms.Select(attrs={'class': 'form-control'}),
            'departmental_batch': forms.Select(attrs={'class': 'form-control'}),
            'degree': forms.Select(attrs={'class': 'form-control'}),
            'institute_batch': forms.Select(attrs={'class': 'form-control'}),
            'discipline_batch': forms.Select(attrs={'class': 'form-control'}),
            'blank_degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter degree name if not avilable in the above options; otherwise leave blank'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'start_year': forms.Select(attrs={'class': 'form-control'}),
            'end_year': forms.Select(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID or Class Roll (Example: 24CSE001) or others'}),
            'approval_query': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'আপনার ব্যাচ সম্পর্কে এমন একটি তথ্য লিখুন যেটি দিয়ে আমরা আপনাকে সঠিকভাবে শনাক্ত করতে পারি। উদাহরণস্বরূপঃ আপনার ব্যাচের বর্তমান সিআর (Class Representative) এর নাম অথবা অন্যকিছু।'}),
        }



class EditBasicProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'mobile_number', 'mobile_number_visibility']
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your WhatsApp or mobile number'}),
            'mobile_number_visibility': forms.Select(attrs={'class': 'form-control'}),
        }
        

class ReferralForm(forms.Form):
    referral_url = forms.URLField(
        label='Referral URL',
        required=True,
        widget=forms.URLInput(attrs={
            'placeholder': '(Example: http://onebyzeroedu.com/?ref=F7060C****)',
            'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ced4da;',
            'aria-label': 'Referral URL'
        })
    )

# class EditEduSchoolForm(forms.ModelForm):
#     class Meta:
#         model = EduSchool
#         fields = ['school', 'ssc_division', 'start_year', 'end_year']
        

# class SkillsUniversityCoursesForm(forms.ModelForm):
#     courses = forms.ModelMultipleChoiceField(
#         queryset=Course.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )

#     class Meta:
#         model = SkillsUniversityCourses
#         fields = ['profile', 'university', 'faculty', 'department', 'courses']

# class SkillsUniversityCoursesForm(forms.ModelForm):
#     class Meta:
#         model = SkillsUniversityCourses
#         fields = ['courses']
#         widgets = {
#             'courses': forms.CheckboxSelectMultiple
#         }

    # def __init__(self, *args, **kwargs):
    #     profile = kwargs.pop('profile', None)
    #     super().__init__(*args, **kwargs)
    #     if profile:
    #         department = profile.department
    #         university = profile.university
        
    #         if department and university:
    #             self.fields['courses'].queryset = Course.objects.filter(
    #                 department=department,
    #                 university=university
    #             )
    #         else:
    #             self.fields['courses'].queryset = Course.objects.none()  # No courses if department or university is missing