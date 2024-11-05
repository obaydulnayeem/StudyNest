from django import forms
from apps.university.models import *
from .models import ModeratorRequest, MODERATOR_TYPE_CHOICES

class EditDepartmentInfoModerator(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['system', 'total_semester_or_year', 'course_has_code', 'course_has_credit', 'course_has_hour']
        labels = {
            'system': 'Education System',
            'total_semester_or_year': 'Total Semesters/Years',
            'course_has_code': 'Courses Have Code',
            'course_has_credit': 'Courses Have Credit',
            'course_has_hour': 'Courses Have Hour',
        }
        widgets = {
            'system': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select System'}),
            'total_semester_or_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 4 or 8'}),
            'course_has_code': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'course_has_credit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'course_has_hour': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        help_texts = {
            'system': 'Select the education system for the department.',
            'total_semester_or_year': 'Enter the total number of semesters or years for the program.',
        }


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = [
            'name', 'former_name', 'acronym', 'university_type', 'established', 
            'history', 'location_division', 'location_district', 'location_permanent_campus',
            'campus_area', 'motto', 'logo', 'num_regular_students', 'num_academic_staff', 
            'num_residence_hall', 'website', 'colors', 'has_faculty', 'has_institute', 
            'has_school', 'has_center', 'has_department', 'has_discipline'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter university name'}),
            'former_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter former name'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter acronym'}),
            'university_type': forms.Select(attrs={'class': 'form-control'}),
            'established': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter established year'}),
            'history': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter university history'}),
            'location_division': forms.Select(attrs={'class': 'form-control'}),
            'location_district': forms.Select(attrs={'class': 'form-control'}),
            'location_permanent_campus': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter permanent campus location'}),
            'campus_area': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter campus area in acres'}),
            'motto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter motto'}),
            'num_regular_students': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of regular students'}),
            'num_academic_staff': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of academic staff'}),
            'num_residence_hall': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of residence halls'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter website URL'}),
            'colors': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter university colors'}),
            'has_faculty': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_institute': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_school': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_center': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_department': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_discipline': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FacultyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        super(FacultyForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Faculty
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter faculty name'}),
        }
        
class InstituteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Pop the university from kwargs, if provided
        university = kwargs.pop('university', None)
        super(InstituteForm, self).__init__(*args, **kwargs)
        
        # Filter faculties based on the provided university
        if university:
            self.fields['faculty'].queryset = Faculty.objects.filter(university=university)
        else:
            # Optionally, you can handle the case where no university is passed
            self.fields['faculty'].queryset = Faculty.objects.none()

    class Meta:
        model = Institute
        fields = ['name', 'faculty']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter institute name'}),
            'faculty': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select faculty'}),
        }
        
        
class SchoolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Pop the university from kwargs, if provided
        university = kwargs.pop('university', None)
        super(SchoolForm, self).__init__(*args, **kwargs)
        
        # Filter faculties based on the provided university
        if university:
            self.fields['faculty'].queryset = Faculty.objects.filter(university=university)
        else:
            # Optionally, you can handle the case where no university is passed
            self.fields['faculty'].queryset = Faculty.objects.none()

    class Meta:
        model = School
        fields = ['name', 'faculty']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter school name'}),
            'faculty': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select faculty'}),
        }
        

class CenterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Pop the university from kwargs, if provided
        university = kwargs.pop('university', None)
        super(CenterForm, self).__init__(*args, **kwargs)
        
        # Filter faculties based on the provided university
        # if university:
            # self.fields['faculty'].queryset = Faculty.objects.filter(university=university)
        # else:
            # Optionally, you can handle the case where no university is passed
            # self.fields['faculty'].queryset = Faculty.objects.none()

    class Meta:
        model = Center
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter center name'}),
        }



class DepartmentByFacultyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        faculty = kwargs.pop('faculty', None)
        super(DepartmentByFacultyForm, self).__init__(*args, **kwargs)
        # No need to filter by faculty since this form is to create a new department
        # Just ensure the faculty is passed correctly in the view
    
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department name'}),
        }
        
        
class InstituteByFacultyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        faculty = kwargs.pop('faculty', None)
        super(InstituteByFacultyForm, self).__init__(*args, **kwargs)
        # No need to filter by faculty since this form is to create a new department
        # Just ensure the faculty is passed correctly in the view
    
    class Meta:
        model = Institute
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter institute name'}),
        }



class DepartmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        super(DepartmentForm, self).__init__(*args, **kwargs)
        if university:
            self.fields['faculty'].queryset = Faculty.objects.filter(university=university)
            self.fields['institute'].queryset = Institute.objects.filter(university=university)
            self.fields['school'].queryset = School.objects.filter(university=university)
            self.fields['center'].queryset = Center.objects.filter(university=university)

    class Meta:
        model = Department
        fields = ['faculty', 'institute', 'school', 'center', 'name']
        widgets = {
            'faculty': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Faculty'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department name'}),
            'institute': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select institute'}),
            'school': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select school'}),
            'center': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select center'}),
            # 'syllabus_file': forms.FileInput(attrs={'accept': '.pdf,.jpg,.png,.jpeg'})
        }


class DisciplineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        super(DisciplineForm, self).__init__(*args, **kwargs)
        if university:
            self.fields['faculty'].queryset = Faculty.objects.filter(university=university)
            self.fields['institute'].queryset = Institute.objects.filter(university=university)
            self.fields['school'].queryset = School.objects.filter(university=university)
            self.fields['center'].queryset = Center.objects.filter(university=university)

    class Meta:
        model = Discipline
        fields = ['faculty', 'institute', 'school', 'center', 'name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter discipline name'}),
            'faculty': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Faculty'}),
            'institute': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select institute'}),
            'school': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select school'}),
            'center': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select center'}),
        }


# class CourseSettingsForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['type', 'course_type', 'status', 'prerequisite', 'motivation', 'objectives', 'outcomes', 'hour', 'references']

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['type', 'course_type', 'status', 'prerequisite', 'motivation', 'objectives', 'outcomes', 'title', 'code', 'credit', 'hour', 'marks', 'semester', 'syllabus', 'references']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            
            'course_type': forms.Select(attrs={'class': 'form-control'}),
            
            'status': forms.Select(attrs={'class': 'form-control'}),
            
            'prerequisite': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter prerequisite'}),
            
            'motivation': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter motivation'}),
            
            'objectives': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter objectives'}),
            
            'outcomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter outcomes'}),
            
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course title'}),
            
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course code'}),
            
            'credit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter course credit'}),
            
            'hour': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter course hour'}),
            
            'marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter total course marks'}),
            
            'semester': forms.Select(attrs={'class': 'form-control'}),
            
            'syllabus': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter syllabus'}),
            
            'references': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter references'}),
        }
         
class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['semester', 'course_type', 'status', 'prerequisite', 'motivation', 'objectives', 'outcomes', 'title', 'code', 'credit', 'hour', 'marks', 'syllabus', 'references']
        
        # Define labels for each field
        labels = {
            'semester': 'Semester',
            'course_type': 'Course Type',
            'status': 'Course Status',
            'prerequisite': 'Prerequisite',
            'motivation': 'Motivation',
            'objectives': 'Objectives',
            'outcomes': 'Course Outcomes',
            'title': 'Course Title',
            'code': 'Course Code',
            'credit': 'Credit Hours',
            'hour': 'Weekly Hours',
            'marks': 'Marks',
            'syllabus': 'Syllabus',
            'references': 'References',
        }
    
        # Define widgets and include placeholders in the widget attributes
        widgets = {
            # 'type': forms.Select(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Select course type...'
            # }),
            
            'course_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select course type...'}),
            
            
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select course status...'
            }),
            
            'prerequisite': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,  # This increases the height of the textarea
                'placeholder': 'Enter course prerequisite...'
            }),
            
            'motivation': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,  # This increases the height of the textarea
                'placeholder': 'Enter course motivation...'
            }),
            
            'objectives': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,  # This increases the height of the textarea
                'placeholder': 'Enter course objectives...'
            }),
            
            'outcomes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,  # This increases the height of the textarea
                'placeholder': 'Enter course outcomes...'
            }),
            
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter course title...'
            }),
            'code': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter course code...'
            }),
            'credit': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter credit hours...'
            }),
            'hour': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter weekly hours...'
            }),
            
            'marks': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter total course marks...'
            }),
            
            'syllabus': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5,  # This increases the height of the textarea
                'placeholder': 'Enter course syllabus...'
            }),
            
            'references': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,  # This increases the height of the textarea
                'placeholder': 'Enter course references...'
            }),
        }
        
        # error_messages = {
        #     'title': {'required': 'Please enter the course title.'},
        #     'code': {'required': 'Please enter the course code.'},
        #     'credit': {'required': 'Please enter the credit hours.'},
        #     'hour': {'required': 'Please enter the weekly hours.'},
        #     'syllabus': {'required': 'Please enter the course syllabus.'},
        # }
        
  
class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['syllabus_file']
        
        widgets = {
            'syllabus_file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        
class RetiredFromModeratorForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label="I confirm that I want to retire from my moderator role.",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
        

class ModeratorRequestForm(forms.ModelForm):
    requested_moderator_type = forms.ChoiceField(
        choices=MODERATOR_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Moderator Type'})
    )
    has_laptop = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    has_wifi = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_dropped_student = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    write_something = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write something...',
            'rows': 4,
        })
    )
    read_terms_and_conditions = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = ModeratorRequest
        fields = [
            'requested_moderator_type', 
            'has_laptop', 
            'has_wifi', 
            'is_dropped_student', 
            'write_something',
            'read_terms_and_conditions',
        ]

        