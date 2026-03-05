from django.contrib import admin
from .models import Program, BrochureSubmission

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    # Fixed: 'title' is now first so it can act as the link to the edit page
    list_display = ('title', 'position', 'program_type') 
    
    # You can still edit the position numbers directly from the list
    list_editable = ('position',) 
    
    search_fields = ('title',)

@admin.register(BrochureSubmission)
class BrochureSubmissionAdmin(admin.ModelAdmin):
    # This defines the columns shown in the admin list view
    list_display = ('full_name', 'email', 'program_name', 'submitted_at')
    
    # Adds a sidebar filter for programs and dates
    list_filter = ('program_name', 'submitted_at')
    
    # Adds a search bar at the top to find students by name or email
    search_fields = ('full_name', 'email', 'mobile_number')
    
    # Makes the list read-only by default if you want to prevent accidental admin edits
    readonly_fields = ('submitted_at',)
    
    # Shows the newest leads first in the admin panel
    ordering = ('-submitted_at',)