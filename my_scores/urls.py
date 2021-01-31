"""my_scores URL Configuration"""

# Django Imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Project Imports
from django.conf import settings
from users.views.users import UserView
from users.views.profile import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserView.as_view()),
    path('profile', ProfileView.as_view()),
    path('', include('books.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)