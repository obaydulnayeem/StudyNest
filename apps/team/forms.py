from django import forms
from .models import Task
from apps.university.models import CommonCourse, Course

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'blank_task_name', 'description', 'duration', 'date']
        widgets = {
            'task_name': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task Description'}),
            'blank_task_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'If not available in the above option'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in minutes'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
   


class CommonCourseForm(forms.ModelForm):
    class Meta:
        model = CommonCourse
        fields = ['title', 'course_type', 'prerequisite', 'motivation', 'objectives', 'outcomes', 'syllabus', 'references']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course title'}),
            'course_type': forms.Select(attrs={'class': 'form-control'}),
            'prerequisite': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'motivation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'objectives': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'outcomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'syllabus': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'references': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

        
class CourseCommonCoursesForm(forms.ModelForm):
    common_courses = forms.ModelMultipleChoiceField(
        queryset=CommonCourse.objects.all().order_by('title'),
        widget=forms.CheckboxSelectMultiple,  # or use forms.SelectMultiple for a dropdown
        required=False
    )

    class Meta:
        model = Course
        fields = ['common_courses']
