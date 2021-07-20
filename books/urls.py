""" URLS de books"""
# Django Imports
from django.urls import path, include

# App Imports
from .views import BookView

# Django REST Framework Imports
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookView, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]