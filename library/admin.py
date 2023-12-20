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
        'date_approved'
        )
    list_editable = (
        'approved',
        'date_approved'
        )
    list_filter = (
        'approved',
        )

admin.site.register(Feedback, FeedbackAdmin)
