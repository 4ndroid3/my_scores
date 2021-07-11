""" URLS de books"""
# Django Imports
from django.urls import path

# App Imports
from .views import BookView

urlpatterns = [
    path('', BookView.as_view(), name = 'books'),
]