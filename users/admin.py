# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project Imports
from .models.users import User
from .models.profile import Profile

class CustomUserAdmin(UserAdmin):
    """Configuración del admin modificado"""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', )

class CustomProfileAdmin(admin.ModelAdmin):
    """ Configuracion de Muestra de Profiles en Admin"""
    list_display = ('users','pais', 'fecha_nacimiento', 'libros_leidos', 'auth_leidos',)
    search_fields = ('users__email','users__username', 'users__first_name','users__last_name')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, CustomProfileAdmin)