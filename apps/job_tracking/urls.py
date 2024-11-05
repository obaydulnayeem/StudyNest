from django.urls import path
from . import views

urlpatterns = [
    path('add_job_application/', views.add_job_application, name='add_job_application'),
    path('edit_job_application/<int:job_id>/', views.edit_job_application, name='edit_job_application'),
    path('delete_job_application/<int:pk>/', views.delete_job_application, name='delete_job_application'),
    path('view_job_details/<int:job_id>/', views.view_job_details, name='view_job_details'),
    path('job_application_list/', views.job_application_list, name='job_application_list'),
    path('job_list_in_task/', views.job_list_in_task, name='job_list_in_task'),
    
    path('company_list/', views.company_list, name='company_list'),
    path('add_company/', views.add_company, name='add_company'),
    path('edit_company/<int:pk>/', views.edit_company, name='edit_company'), 
    path('delete_company/<int:pk>/', views.delete_company, name='delete_company'),
    
    path('followees/', views.followees, name='followees'),
    path('add_followee/', views.add_followee, name='add_followee'),
    path('edit_followee/<int:followee_id>/', views.edit_followee, name='edit_followee'),
    path('delete_followee/<int:pk>/', views.delete_followee, name='delete_followee'),
    
    path('save_job/', views.save_job, name='save_job'),
    path('saved_jobs_list/', views.saved_jobs_list, name='saved_jobs_list'),
    path('edit_saved_job/<int:job_id>/', views.edit_saved_job, name='edit_saved_job'),
    path('mark_as_applied/<int:job_id>/', views.mark_as_applied, name='mark_as_applied'),
]
