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
from rest_framework_extensions.routers import ExtendedSimpleRouter

router = ExtendedSimpleRouter()


# Nested Routers
(router.register(r'profiles', 
                ProfileView, 
                basename='profiles'
            )
        .register(r'books', 
                ReadedBooks, 
                basename='profile-readed',
                parents_query_lookups=['profiles_books']
            )
)
router.register(r'', 
                UserView, 
                basename='users'
            )

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
    path('signup/', UserSignUpAPIView.as_view(), name = 'signup'),
]