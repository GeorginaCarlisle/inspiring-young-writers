from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'giver',
        'writing',
        'star_one',
        'star_two',
        'wish',
        'date_created',
        'date_last_edit',
        'approved',
        'date_approved',
        'failed_approval',
        'date_failed',
        'reason_failed'
        )
    list_editable = (
        'approved',
        'date_approved',
        'failed_approval',
        'date_failed',
        'reason_failed'
        )
    list_filter = (
        'approved',
        'failed_approval',
        )


admin.site.register(Feedback, FeedbackAdmin)
