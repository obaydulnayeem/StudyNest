from django.db import models
from .profile_models import Profile
from apps.university.models import *
from ..choices.choices import *
from datetime import datetime
from choices.varsity.varsity_choices import *


def year_choices():
    return [(r, r) for r in range(1950, datetime.now().year+7)]

def current_year():
    return datetime.now().year

UNIVERSITY_DEGREE_CHOICES = [  
    ('Bachelor of Science (B.Sc)', 'Bachelor of Science (B.Sc)'),
    ('Bachelor of Arts (B.A)', 'Bachelor of Arts (B.A)'),
    ('Bachelor of Business Administration (BBA)', 'Bachelor of Business Administration (BBA)'),
    ('Bachelor of Business Studies (BBS)', 'Bachelor of Business Studies (BBS)'),
    ('Bachelor of Commerce (B.Com)', 'Bachelor of Commerce (B.Com)'),
    ('Bachelor of Law (B.L)', 'Bachelor of Law (B.L)'),
    ('Bachelor of Engineering (B.E)', 'Bachelor of Engineering (B.E)'),
    ('Bachelor of Technology (B.Tech)', 'Bachelor of Technology (B.Tech)'),
    ('Bachelor of Pharmacy (B.Pharm)', 'Bachelor of Pharmacy (B.Pharm)'),
    ('Bachelor of Architecture (B.Arch)', 'Bachelor of Architecture (B.Arch)'),
    ('Bachelor of Fine Arts (BFA)', 'Bachelor of Fine Arts (BFA)'),
    ('Bachelor of Social Science (BSS)', 'Bachelor of Social Science (BSS)'),
    ('Bachelor of Environmental Science (BES)', 'Bachelor of Environmental Science (BES)'),
    ('Bachelor of Veterinary Science (BVSc)', 'Bachelor of Vet Science (BVSc)'),
    ('Bachelor of Hotel Management (BHM)', 'Bachelor of Hotel Management (BHM)'),
    ('Bachelor of Music (BM)', 'Bachelor of Music (BM)'),
    ('Others', 'Others')
]


class EduUniversity(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    # type = models.CharField(max_length=100, choices=UNIVERSITY_TYPE_CHOICES, blank = True, null = True)
    
    university_type = models.ForeignKey(UniversityType, on_delete=models.CASCADE, null = True, blank = True)
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, null = True, blank = True)
    
    blank_university = models.CharField(max_length=255, blank = True, null = True)
    
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank = True, null = True)
    
    blank_faculty = models.CharField(max_length=255, blank = True, null = True)
    
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank = True, null = True)
    
    blank_institute = models.CharField(max_length=255, blank = True, null = True)
    
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank = True, null = True)
    
    blank_school = models.CharField(max_length=255, blank = True, null = True)
    
    center = models.ForeignKey(Center, on_delete=models.CASCADE, blank = True, null = True)
    
    blank_center = models.CharField(max_length=255, blank = True, null = True)
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank = True, null = True)
    
    blank_department = models.CharField(max_length=255, blank = True, null = True)
    
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, blank = True, null = True)
    
    blank_discipline = models.CharField(max_length=255, blank = True, null = True)
    
    degree = models.CharField(max_length=100, choices=UNIVERSITY_DEGREE_CHOICES, blank = True, null = True)
    
    blank_degree = models.CharField(max_length=100, blank = True, null = True)
    
    session = models.CharField(max_length=50, choices=SESSION_CHOICES, blank = True, null = True)
    
    varsity_batch = models.CharField(max_length=50, choices=DEPARTMENT_OR_VARCITY_BATCH_CHOICES, blank = True, null = True)
    
    departmental_batch = models.CharField(max_length=50, choices=DEPARTMENT_OR_VARCITY_BATCH_CHOICES, blank = True, null = True)
    
    discipline_batch = models.CharField(max_length=50, choices=DEPARTMENT_OR_VARCITY_BATCH_CHOICES, blank = True, null = True)
    
    institute_batch = models.CharField(max_length=50, choices=DEPARTMENT_OR_VARCITY_BATCH_CHOICES, blank = True, null = True)
    
    semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES, blank = True, null = True)
        
    student_id = models.CharField(max_length=50, blank = True, null = True)
    
    start_year = models.PositiveIntegerField(choices=year_choices(), default=current_year, null=True, blank=True)
    
    end_year = models.PositiveIntegerField(choices=year_choices(), default=current_year, null=True, blank=True)
        
    approval_query = models.TextField(blank = True, null = True)
    
    is_approved = models.BooleanField(default=False)
    
    approved_by = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='approved_by')
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.profile} - {self.university} - {self.faculty} - {self.department} - {self.degree} - {self.session} - {self.departmental_batch} - {self.start_year} - {self.end_year}'

# class EduCollege(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
#     college = models.ForeignKey(College, on_delete=models.CASCADE, default=1, null = True, blank = True)
    
#     division = models.CharField(max_length=100, choices=SSC_and_HSC_DIVISIONS, default="Science", blank = True, null = True)
    
#     start_year = models.PositiveIntegerField(null=True, blank=True)
   
#     end_year = models.PositiveIntegerField(null=True, blank=True)
    
#     def __str__(self):
#         return f'{self.profile} - {self.college} - {self.division} - {self.start_year} - {self.end_year}'
    
    
    
# class EduSchool(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
#     school = models.ForeignKey(School, on_delete=models.CASCADE, default=1, null = True, blank = True)
    
#     ssc_division = models.CharField(max_length=100, choices=SSC_and_HSC_DIVISIONS, default="Science", blank = True, null = True)
    
#     start_year = models.PositiveIntegerField(null=True, blank=True)
   
#     end_year = models.PositiveIntegerField(null=True, blank=True)
    
#     def __str__(self):
#         return f'{self.profile} - {self.school} - {self.start_year} - {self.end_year}'
    
# class SomethingModel(models.Model):
#     name = models.CharField(max_length=255)