from django.db import models
from django.core.validators import FileExtensionValidator
from choices.varsity.varsity_choices import *
from choices.location import *
# from apps.account.models.profile_models import *

# Create your models here.
class UniversityType(models.Model):
    type = models.CharField(max_length=100, default='Public')
    
    def __str__(self):
        return f'{self.type}'
    

    
class University(models.Model):
    name = models.CharField(max_length=100)
    # type = models.CharField(max_length=100, choices=UNIVERSITY_TYPE_CHOICES, default='Public', blank = True, null = True)
    former_name = models.CharField(max_length=100, blank = True, null = True)
    acronym = models.CharField(max_length=20, blank = True, null = True)
    university_type = models.ForeignKey(UniversityType, on_delete=models.CASCADE, blank = True, null = True)
    # established = models.DateField(blank = True, null = True)
    established = models.IntegerField(blank=True, null=True)
    history = models.TextField(blank = True, null = True)
    location_division = models.CharField(max_length=100, blank = True, null = True, choices = DIVISIONS)
    location_district = models.CharField(max_length=100, blank = True, null = True, choices = DISTRICTS)
    location_permanent_campus = models.CharField(max_length=200, blank = True, null = True)
    # campus_area = models.DecimalField(max_digits=4, decimal_places=2, blank = True, null = True)
    campus_area = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    # motto = models.CharField(max_length=200, blank = True, null = True)
    motto = models.CharField(max_length=200, blank = True, null = True)
    # motto_english = models.CharField(max_length=200, blank = True, null = True)
    logo = models.ImageField(upload_to='university/university_logos/', blank = True, null = True)
    num_regular_students = models.PositiveIntegerField(blank = True, null = True)
    num_academic_staff = models.PositiveIntegerField(blank = True, null = True)
    num_residence_hall = models.PositiveIntegerField(blank = True, null = True)
    website = models.URLField(blank = True, null = True)
    colors = models.CharField(max_length=100, blank = True, null = True)
    moderators = models.ManyToManyField('admin_panel.ModeratorRequest', related_name='universities', blank=True)
    has_faculty = models.BooleanField(default = True)
    has_institute = models.BooleanField(default = True)
    has_school = models.BooleanField(default = True)
    has_center = models.BooleanField(default = True)
    has_department = models.BooleanField(default = True)
    has_discipline = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank = True, null = True)
    layer = models.PositiveIntegerField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Institute(models.Model):
    name = models.CharField(max_length=100)
    established = models.IntegerField(blank=True, null=True)
    history = models.TextField(blank = True, null = True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank = True, null = True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank = True, null = True)
    # school = models.ForeignKey(School, on_delete=models.CASCADE, blank = True, null = True)
    # layer = models.PositiveIntegerField(blank = True, null = True)
    system = models.CharField(max_length=100, choices=SYSTEM_CHOICES, default='Semester')
    total_semester_or_year = models.PositiveIntegerField(blank = True, null = True)
    course_has_code = models.BooleanField(default=True)
    course_has_credit = models.BooleanField(default=True)
    course_has_hour = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.name}'
    
class School(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank = True, null = True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank = True, null = True)
    layer = models.PositiveIntegerField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Center(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank = True, null = True)
    layer = models.PositiveIntegerField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'

class Department(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank = True, null = True)
    layer = models.PositiveIntegerField(blank = True, null = True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank = True, null = True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank = True, null = True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank = True, null = True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, blank = True, null = True)
    established = models.IntegerField(blank=True, null=True)
    history = models.TextField(blank = True, null = True)
    system = models.CharField(max_length=100, choices=SYSTEM_CHOICES, default='Semester')
    total_semester_or_year = models.PositiveIntegerField(blank = True, null = True)
    course_has_code = models.BooleanField(default=True)
    course_has_credit = models.BooleanField(default=True)
    course_has_hour = models.BooleanField(default=True)
    users = models.ManyToManyField('account.Profile', related_name='departments', blank=True)
    moderators = models.ManyToManyField('admin_panel.ModeratorRequest', related_name='departments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    first_data_entry_by = models.ForeignKey('account.Profile', on_delete=models.CASCADE, related_name='first_data_entry_by', blank = True, null = True)
    syllabus_file = models.FileField(upload_to='university/syllabus/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])], blank=True, null=True)
    # established = models.DateField(blank = True, null = True)
    # num_of_seat = models.PositiveIntegerField(default=0)
    # ambassadors = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    def __str__(self):
        return f'{self.name}'
    
    
class Discipline(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank = True, null = True)
    layer = models.PositiveIntegerField(blank = True, null = True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank = True, null = True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank = True, null = True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank = True, null = True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, blank = True, null = True)
    established = models.IntegerField(blank=True, null=True)
    history = models.TextField(blank = True, null = True)
    system = models.CharField(max_length=100, choices=SYSTEM_CHOICES, default='Semester')
    total_semester_or_year = models.PositiveIntegerField(blank = True, null = True)
    course_has_code = models.BooleanField(default=True)
    course_has_credit = models.BooleanField(default=True)
    course_has_hour = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    # users = models.ManyToManyField('account.Profile', related_name='departments', blank=True)
    # moderators = models.ManyToManyField('admin_panel.ModeratorRequest', related_name='departments', blank=True)
    # num_of_seat = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.name}'

class CommonCourse(models.Model):
    title = models.CharField(max_length=100)
    course_type = models.CharField(max_length=100, choices=COURSE_TYPE_CHOICES, blank=True, null=True)
    
    prerequisite = models.TextField(blank=True, null=True)
    
    motivation = models.TextField(blank=True, null=True)
    
    objectives = models.TextField(blank=True, null=True)
    
    outcomes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    syllabus = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'





class Course(models.Model):
    # common_course = models.ForeignKey(CommonCourse, on_delete=models.CASCADE, blank = True, null = True)
    
     # Use ManyToManyField for linking multiple CommonCourse instances
    common_courses = models.ManyToManyField(CommonCourse, blank=True, related_name="courses")
    
    type = models.CharField(max_length=100, choices=COURSE_TYPE_CHOICES, blank=True, null=True) # not using
    
    course_type = models.CharField(max_length=100, choices=COURSE_TYPE_CHOICES, blank=True, null=True)
    
    status = models.CharField(max_length=100, choices=COURSE_STATUS_CHOICES, blank=True, null=True)
    
    prerequisite = models.TextField(blank=True, null=True)
    
    motivation = models.TextField(blank=True, null=True)
    
    objectives = models.TextField(blank=True, null=True)
    
    outcomes = models.TextField(blank=True, null=True)
    
    title = models.CharField(max_length=100)
    
    code = models.CharField(max_length=10)
    
    credit = models.DecimalField(max_digits=4, decimal_places=2)
    
    hour = models.DecimalField(max_digits=4, decimal_places=2, blank = True, null = True)
    # hour = models.PositiveIntegerField(blank = True, null = True)
    
    marks = models.PositiveIntegerField(blank = True, null = True)
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank = True, null = True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank = True, null = True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank = True, null = True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, blank = True, null = True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank = True, null = True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, blank = True, null = True)
    # year = models.CharField(max_length=50, choices=YEAR_CHOICES, blank=True, null=True)
    semester = models.CharField(max_length=50,choices=SEMESTER_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    syllabus = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    # last_update = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # tutors = models.ManyToManyField('account.Profile', blank=True)
    # total_resources = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ForeignKey('account.Profile', on_delete=models.CASCADE, blank = True, null = True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank = True, null = True)
    designation = models.CharField(max_length=100, choices=TEACHER_DESIGNATION_CHOICES, blank = True, null = True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank = True, null = True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank = True, null = True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, blank = True, null = True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank = True, null = True)
    added_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

class CommonResourceInfo(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, blank=True, null=True)
    # year = models.CharField(max_length=50, choices=YEAR_CHOICES, blank=True, null=True)
    semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    common_courses = models.ManyToManyField('CommonCourse', blank=True)
    session = models.CharField(max_length=50, choices=SESSION_CHOICES, blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('account.Profile', on_delete=models.CASCADE, blank=True, null=True)
    uploaded_by_team = models.CharField(max_length=100, choices=TEAM_MEMBERS_CHOICES, blank=True, null=True)
    uploaded_by_prev = models.CharField(choices= PREV_USERS_CHOICES, max_length=100, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

class ResourcesQuestion(CommonResourceInfo):
    exam_name = models.CharField(max_length=50, choices=EXAM_CHOICES)
    exam_date = models.DateField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    blank_teacher = models.CharField(max_length=100, blank=True, null=True)
    question_file = models.FileField(upload_to='university/resources/questions/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])])
    
    
    # def save(self, *args, **kwargs):
    #     # Automatically associate related common courses from the course
    #     if self.course and self.course.common_courses.exists():
    #         self.common_courses.set(self.course.common_courses.all())
    #     super().save(*args, **kwargs)  # Call the parent class's save method
    
    def save(self, *args, **kwargs):
        # Save the object first to get an ID
        super().save(*args, **kwargs)

        # After the object has been saved and has an ID, set the many-to-many field
        if self.course and self.course.common_courses.exists():
            self.common_courses.set(self.course.common_courses.all())


    def __str__(self):
        return self.exam_name

class ResourcesNote(CommonResourceInfo):
    note_title = models.CharField(max_length=200)
    note_author = models.CharField(max_length=100, blank = True, null = True)
    note_file = models.FileField(upload_to='university/resources/notes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])])

    def save(self, *args, **kwargs):
        # Save the object first to get an ID
        super().save(*args, **kwargs)

        # After the object has been saved and has an ID, set the many-to-many field
        if self.course and self.course.common_courses.exists():
            self.common_courses.set(self.course.common_courses.all())
            
    def __str__(self):
        return self.note_title

class ResourcesBook(CommonResourceInfo):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100, blank = True, null = True)
    book_edition = models.CharField(max_length=100, blank=True, null=True, choices=BOOK_EDITION_CHOICES)
    book_file = models.FileField(upload_to='university/resources/books/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    
    def save(self, *args, **kwargs):
        # Save the object first to get an ID
        super().save(*args, **kwargs)

        # After the object has been saved and has an ID, set the many-to-many field
        if self.course and self.course.common_courses.exists():
            self.common_courses.set(self.course.common_courses.all())

    def __str__(self):
        return self.book_title

class ResourcesLecture(CommonResourceInfo):
    lecture_title = models.CharField(max_length=200)
    lecture_author = models.CharField(max_length=100, blank = True, null = True)
    lecture_file = models.FileField(upload_to='university/resources/lectures/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'pptx', 'odp'])])

    def save(self, *args, **kwargs):
        # Save the object first to get an ID
        super().save(*args, **kwargs)

        # After the object has been saved and has an ID, set the many-to-many field
        if self.course and self.course.common_courses.exists():
            self.common_courses.set(self.course.common_courses.all())
    
    def __str__(self):
        return self.lecture_title


