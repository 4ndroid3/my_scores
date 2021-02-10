""" URLS de users"""

# Project Imports
from django.urls import path

# Django Imports
from .views.profile import ProfileView
from .views.users import UserView, UserLoginAPIView

urlpatterns = [
    path('users/', UserView.as_view(), name = 'users'),
    path('users/login/', UserLoginAPIView.as_view(), name = 'login'),
    path('users/profile/', ProfileView.as_view(), name = 'profile'),
]