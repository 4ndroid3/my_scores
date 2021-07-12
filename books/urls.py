""" URLS de books"""
# Django Imports
from django.urls import path

# App Imports
from .views import BookListCreate, BookDetail

urlpatterns = [
    path('', BookListCreate.as_view(), name = 'books'),
    path('<pk>/', BookDetail.as_view(), name = 'books'),
]