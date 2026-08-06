from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('phone', 'is_phone_verified', 'avatar', 'location')}),
    )
    list_display = ['username', 'email', 'phone', 'is_phone_verified', 'is_staff']

admin.site.register(User, CustomUserAdmin)
