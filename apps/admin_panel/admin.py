from django.contrib import admin
from django.utils.timezone import now
from .models import ModeratorRequest, PendingUser

admin.site.register(PendingUser)

class ModeratorRequestAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = (
        'get_full_name',  # Display the full name at the first column
        'is_running',
        'profile',
        'requested_moderator_type',
        'is_temporary',
        'requested_at', 
        'is_approved_initial',
        'approved_initial_by',
        'approved_initial_at',
        'is_approved_final',
        'approved_final_at',
    )

    # Fields to filter the admin list view by
    list_filter = (
        'requested_moderator_type', 
        'is_approved_initial', 
        'is_approved_final', 
        'is_running', 
        'requested_at'
    )

    # Fields to search by in the admin list view
    search_fields = ('profile__user__username', 'profile__user__first_name', 'profile__user__last_name', 'requested_moderator_type')

    # Fields to display as readonly
    readonly_fields = ('requested_at', 'approved_initial_at', 'approved_final_at')

    # Organize fields into fieldsets in the admin detail view
    fieldsets = (
        (None, {
            'fields': ('profile', 'requested_moderator_type')
        }),
        ('Approval Information', {
            'fields': (
                'is_approved_initial', 
                'approved_initial_by', 
                'approved_initial_at', 
                'is_approved_final', 
                'approved_final_at', 
                'is_running',
                'is_temporary',
            ),
            'classes': ('collapse',),  # Collapsible section
        }),
        ('Timestamps', {
            'fields': ('requested_at',),
        }),
    )

    # Optionally, add the ability to approve requests directly from the admin interface
    actions = ['approve_initial', 'approve_final']

    def approve_initial(self, request, queryset):
        queryset.update(is_approved_initial=True, approved_initial_at=now())
        self.message_user(request, "Selected requests have been initially approved.")
    approve_initial.short_description = "Approve selected requests initially"

    def approve_final(self, request, queryset):
        queryset.update(is_approved_final=True, approved_final_at=now())
        self.message_user(request, "Selected requests have been finally approved.")
    approve_final.short_description = "Approve selected requests finally"

    def get_full_name(self, obj):
        return f"{obj.profile.user.first_name} {obj.profile.user.last_name}"
    get_full_name.short_description = 'Full Name'
    get_full_name.admin_order_field = 'profile__user__first_name'  # Enables ordering by full name

# Register the customized admin view
admin.site.register(ModeratorRequest, ModeratorRequestAdmin)
