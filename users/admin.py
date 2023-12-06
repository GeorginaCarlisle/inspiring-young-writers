from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class AccountAdmin(UserAdmin):
    list_display = ('username', 'age', 'first_name', 'last_name', 'email', 'join_date', 'is_admin', 'is_staff')
    search_fields = ('username', 'email')

admin.site.register(User, AccountAdmin)
