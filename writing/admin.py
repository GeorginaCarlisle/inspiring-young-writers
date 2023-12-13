from django.contrib import admin
from .models import Writing

class WritingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'author', 
        'updated_on', 
        'pending_approval', 
        'date_submitted', 
        'approved', 
        'date_approved',
        'featured',
        'failed_approval',
        'date_failed',
        'reason_failed'
        )
    list_editable = (
        'pending_approval',  
        'approved', 
        'date_approved',
        'failed_approval',
        'date_failed',
        'reason_failed',
        'featured'
        )
    list_filter = (
        'pending_approval',
        'approved',
        'failed_approval',
        'featured'
        )


admin.site.register(Writing, WritingAdmin)

