""" Admin de Libros"""

# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Project Imports
from books.models import Book


class CustomBookAdmin(admin.ModelAdmin):
    list_display = ('user','titulo', 'autor', 'fecha_leido',)
    list_filter = ('user', 'titulo', 'autor', 'año_publicacion',)
    search_fields = ('user', 'titulo', 'autor',)

admin.site.register(Book, CustomBookAdmin)