from django.contrib import admin
from django.urls import path, include
from apps.core.views.home_views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('admin_panel/', include('apps.admin_panel.urls')),
    
    path('', home, name='home'),
            
    path('university/', include('apps.university.urls')),
    
    path('account/', include('apps.account.urls')),
    
    path('core/', include('apps.core.urls')),
    
    path('mentorship/', include('apps.mentorship.urls')),
    
    path('notifications/', include('apps.notifications.urls')),
    
    path('feedback/', include('apps.feedback.urls')),
    
    path('team/', include('apps.team.urls')),
    
    # path('job_tracker/', include('apps.job_tracker.urls')),
    
    path('job_tracking/', include('apps.job_tracking.urls')),

    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)