# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project Imports
from .models.users import User
from .models.profile import Profile


admin.site.register(User, UserAdmin)
admin.site.register(Profile)