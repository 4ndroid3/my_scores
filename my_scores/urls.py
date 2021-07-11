"""URLS Cofiguration"""

# Django Imports
from django.contrib import admin
from django.urls import path, include

# Django REST Framework Imports
from rest_framework.routers import DefaultRouter

# JWT Imports
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/users/', include('users.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]