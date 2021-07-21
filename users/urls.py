""" URLS de users"""

# Project Imports
from django.urls import path, include

# Django Imports
from .views import (
    UserView, 
    UserLoginAPIView, 
    UserSignUpAPIView,
    ProfileView,
    ReadedBooks,
    )

# Django REST Framework Imports
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileView, basename='profiles')
router.register(r'books', ReadedBooks, basename='readed')
router.register(r'', UserView, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
    path('signup/', UserSignUpAPIView.as_view(), name = 'signup'),
]