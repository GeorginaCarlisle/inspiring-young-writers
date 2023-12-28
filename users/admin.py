from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
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
