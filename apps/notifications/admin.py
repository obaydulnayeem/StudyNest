from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'created_at')
    # Optionally, you can make 'type' and 'user' searchable
    search_fields = ('type', 'user__username')
    # You can also add filtering options if needed
    list_filter = ('type', 'read', 'created_at')

admin.site.register(Notification, NotificationAdmin)
