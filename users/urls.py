""" URLS de users"""

# Project Imports
from django.urls import path

# Django Imports
from .views import (
    UserView, 
    UserLoginAPIView, 
    UserSignUpAPIView,
    ProfileView,
    ReadedBooks,
    ReadedBookDetail,
    ProfileDetailView
    )

urlpatterns = [
    path('', UserView.as_view(), name = 'users'),
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
    path('signup/', UserSignUpAPIView.as_view(), name = 'signup'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('profile/<pk>/', ProfileDetailView.as_view(), name = 'profile'),
    path('books/', ReadedBooks.as_view(), name = 'readed'),
    path('books/<pk>/', ReadedBookDetail.as_view(), name='readed_detail')
]