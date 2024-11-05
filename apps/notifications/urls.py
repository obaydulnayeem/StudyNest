# apps/notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications, name='notifications'),
    
    path('mark_as_read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    
    path('mark_all_as_read/', views.mark_all_as_read, name='mark_all_as_read'),
    
    path('notify-all-users/', views.notify_all_users, name='notify_all_users'),
]
