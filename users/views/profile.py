# Project Imports
from users.models.profile import Profile
from users.serializers.profile import ProfileSerializer

# Django Imports
from django.shortcuts import render

# Rest Framework Imports
from rest_framework import generics

class ProfileView(generics.ListCreateAPIView):
    """ View general del Profile"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer