""" Admin de Libros"""

# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project Imports
from books.models import Book


class CustomBookAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'año_publicacion',)

admin.site.register(Book, CustomBookAdmin)