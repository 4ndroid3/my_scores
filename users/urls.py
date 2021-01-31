""" URLS de users"""

# Project Imports
from django.urls import path

# Django Imports
from .views.profile import ProfileView
from .views.users import UserView

urlpatterns = [
    path('', UserView.as_view()),
    path('profile', ProfileView.as_view()),
]