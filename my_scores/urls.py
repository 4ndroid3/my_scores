"""my_scores URL Configuration"""

# Django Imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Project Imports
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)