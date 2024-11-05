from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UniversityType)
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Discipline)
admin.site.register(Institute)
admin.site.register(School)
admin.site.register(Center)
# admin.site.register(Course)
# admin.site.register(ResourcesQuestion)
admin.site.register(ResourcesBook)
admin.site.register(ResourcesNote)
admin.site.register(ResourcesLecture)
admin.site.register(CommonCourse)
admin.site.register(Teacher)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'course', 'department', 'university')
admin.site.register(ResourcesQuestion, QuestionAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'university')

admin.site.register(Course, CourseAdmin)