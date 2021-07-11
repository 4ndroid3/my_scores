# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project Imports
from .models import User, Profile, User_Book


class CustomUserAdmin(UserAdmin):
    """Configuración del admin modificado"""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', )


class CustomProfileAdmin(admin.ModelAdmin):
    """ Configuracion de Muestra de Profiles en Admin"""
    list_display = ('users','fecha_nacimiento', 'libros_leidos', 'auth_leidos',)


class CustomUserBookAdmin(admin.ModelAdmin):
    """ Configuracion de Muestra de Profiles en Admin"""
    list_display = ('id_profile','id_book', 'fecha_leido',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, CustomProfileAdmin)
admin.site.register(User_Book, CustomUserBookAdmin)