from django import forms
from . models import *
from apps.account.models.profile_models import Profile
from apps.account.models.education_models import EduUniversity
from apps.university.models import *
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
    class Meta:
        model = ResourcesQuestion
        fields = ['semester', 'course', 'exam_name', 'session', 'exam_date', 'teacher', 'blank_teacher', 'question_file', 'uploaded_by_team', 'uploaded_by_prev']
        
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'exam_name': forms.Select(attrs={'class': 'form-control'}),
            'exam_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'blank_teacher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher name (if not available in the above options)'}),
            'question_file': forms.FileInput(attrs={'class': 'form-control'}),
            'uploaded_by_team': forms.Select(attrs={'class': 'form-control'}),
            'uploaded_by_prev': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        # Pop 'user' from kwargs if it's there, default to None if not
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            # Filter the teacher queryset based on the logged-in user's university and department
            edu_university = EduUniversity.objects.get(profile=user.profile)
            self.fields['teacher'].queryset = Teacher.objects.filter(
                university=edu_university.university,
                department=edu_university.department
            )
        else:
            self.fields['teacher'].queryset = Teacher.objects.none()


class NoteForm(forms.ModelForm):
    class Meta:
        model = ResourcesNote
        fields = ['semester', 'course', 'session', 'note_title', 'note_author', 'note_file', 'uploaded_by_team',  'uploaded_by_prev']
        
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-control'}),
            
            'course': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'note_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note title: (title/topic of the note)'}),
            
            'note_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter note author: (who wrote/prepared this note)'}),
            
            'note_file': forms.FileInput(attrs={'class': 'form-control'}),
            
            'uploaded_by_team': forms.Select(attrs={'class': 'form-control'}),
            
            'uploaded_by_prev': forms.Select(attrs={'class': 'form-control'}),
        }

        
class BookForm(forms.ModelForm):
    class Meta:
        model = ResourcesBook
        fields = ['semester', 'course', 'book_title', 'book_author', 'book_edition', 'book_file',  'uploaded_by_team', 'uploaded_by_prev']
        
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-control'}),
            
            'course': forms.Select(attrs={'class': 'form-control'}),
            
            'book_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title: (the name of the book)'}),
            
            'book_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book author: (who wrote this book)'}),
            
            'book_file': forms.FileInput(attrs={'class': 'form-control'}),
            
            'book_edition': forms.Select(attrs={'class': 'form-control'}),
            
            'uploaded_by_team': forms.Select(attrs={'class': 'form-control'}),
            
            'uploaded_by_prev': forms.Select(attrs={'class': 'form-control'}), 
        }
        
        
class LectureForm(forms.ModelForm):
    class Meta:
        model = ResourcesLecture
        fields = ['semester', 'course', 'session',  'lecture_title', 'lecture_author', 'lecture_file', 'uploaded_by_team', 'uploaded_by_prev']
        
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-control'}),
            
            'course': forms.Select(attrs={'class': 'form-control'}),
            
            'session': forms.Select(attrs={'class': 'form-control'}),
            
            'lecture_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lecture title: (the title/topic of the lecture slide)'}),
            
            'lecture_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lecture author: (who prepared/taught this lecture)'}),
            
            'lecture_file': forms.FileInput(attrs={'class': 'form-control'}),
            
            'uploaded_by_team': forms.Select(attrs={'class': 'form-control'}),
            
            'uploaded_by_prev': forms.Select(attrs={'class': 'form-control'}),
        }

class MyDepartmentForm(forms.Form):
    university = forms.ModelChoiceField(
        queryset=University.objects.all(),
        empty_label="Select a university",
        widget=forms.Select(attrs={'id': 'id_university'})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select a department",
        widget=forms.Select(attrs={'id': 'id_department'})
    )

class SwitchDepartmentForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['university', 'department']
    
class MyResourcesSelectionForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.none())
    semester = forms.IntegerField()
    # year = forms.IntegerField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['department'].queryset = Department.objects.none()

    #     if 'university' in self.data:
    #         try:
    #             university_id = int(self.data.get('university'))
    #             self.fields['department'].queryset = Department.objects.filter(university_id=university_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # Invalid input from the client; ignore and fallback to an empty queryset
            
class MakeAmbassadorForm(forms.Form):
    selected_users = forms.ModelMultipleChoiceField(
        queryset=Profile.objects.all(),  # Replace with your user profile queryset
        widget=forms.CheckboxSelectMultiple,
    )
    
    # def __init__(self, *args, **kwargs):
    #     department_id = kwargs.pop('department_id', None)
    #     super(MakeAmbassadorForm, self).__init__(*args, **kwargs)

    #     # Define 'department_id' as a hidden field
    #     self.fields['department_id'] = forms.IntegerField(widget=forms.HiddenInput(), initial=department_id)