from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    """
    Specifies which data fields from the User model will be displayed
    on the admin page (list display)
    and which the admin can use to filter the displayed data with (list filter)
    """
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'join_date',
        'is_superuser',
    )
    list_filter = (
        'is_superuser',
    )


admin.site.register(User, UserAdmin)
