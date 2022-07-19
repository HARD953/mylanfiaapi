from django.contrib import admin
from .models import*
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdminConfig(UserAdmin):
    ordering=('-start_date',)
    list_display=('user_name','first_name','email','is_staff','is_active')

admin.site.register(NewUser,UserAdminConfig)