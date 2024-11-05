from django.urls import path
from .views import *

urlpatterns = [
    path('team_base/', team_base, name='team_base'),
    
    path('add_task/', add_task, name='add_task'),
    
    path('view_tasks', view_tasks, name='view_tasks'),
    
    path('show_all_universities_team/', show_all_universities_team, name='show_all_universities_team'),
    
    path('show_university_team/<int:university_id>/', show_university_team, name='show_university_team'),
    
    path('show_department_team/<int:department_id>/', show_department_team, name='show_department_team'),
    
    path('show_course_team/<int:course_id>/', show_course_team, name='show_course_team'),
    
    path('show_common_courses_team/', show_common_courses_team, name='show_common_courses_team'),
    
    path('add_common_course/', add_common_course, name='add_common_course'),
    
    path('edit_common_course/<int:course_id>/', edit_common_course, name='edit_common_course'),
    
    path('delete_common_course/<int:course_id>/', delete_common_course, name='delete_common_course'),
    
    path('edit_common_courses/<int:course_id>/', edit_common_courses, name='edit_common_courses'),
    
    path('resource_uploads/', resource_uploads, name='resource_uploads'),
    
    path('previous_uploaders_total_contribution/', previous_uploaders_total_contribution, name='previous_uploaders_total_contribution'),
    
    path('requested_for_previous_coin/', requested_for_previous_coin, name='requested_for_previous_coin'),
]
