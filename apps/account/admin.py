from django.contrib import admin
from .models.profile_models import *
from .models.education_models import *

# admin.site.register(Profile)
# admin.site.register(EduUniversity)
admin.site.register(CoinTransaction)


from django.utils.html import format_html
from django.urls import reverse

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'fullname_with_link', 
        'created_at', 
        'get_department', 
        'get_university', 
        'get_username', 
        'last_updated',
    )

    def fullname_with_link(self, obj):
        if obj.fullname:
            return obj.fullname
        else:
            url = reverse('admin:account_profile_change', args=[obj.pk])  # Ensure 'account' is the correct app label
            return format_html('<a href="{}">View / Edit Profile</a>', url)
    fullname_with_link.short_description = 'Fullname'

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

    def get_department(self, obj):
        return obj.edu_university.department if obj.edu_university else None
    get_department.short_description = 'Department'

    def get_university(self, obj):
        return obj.edu_university.university if obj.edu_university else None
    get_university.short_description = 'University'


admin.site.register(Profile, ProfileAdmin)


class EduUniversityAdmin(admin.ModelAdmin):
    list_display = (
        'profile', 
        'university', 
        'faculty', 
        'department', 
        'degree', 
        'session', 
        'varsity_batch', 
        'departmental_batch', 
        'semester', 
        'start_year', 
        'end_year'
    )  # Display these fields in the list view
    
    list_filter = (
        'university', 
        'faculty', 
        'department', 
        'degree', 
        'session', 
        'semester', 
        'start_year', 
        'end_year'
    )  # Enable filtering by these fields
    
    search_fields = (
        'profile__user__username', 
        'university__name', 
        'faculty__name', 
        'department__name', 
        'degree', 
        'session'
    )  # Enable searching by related user, university, faculty, etc.
    
    list_select_related = ('profile', 'university', 'faculty', 'department')  # Optimize queries with related data

admin.site.register(EduUniversity, EduUniversityAdmin)
