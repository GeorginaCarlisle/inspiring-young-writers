from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    """
    Specifies which data fields from the Feedback model will be displayed
    on the admin page (list display), which the admin can edit (list editable)
    and which the admin can use to filter the displayed data with (list filter)
    """
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
