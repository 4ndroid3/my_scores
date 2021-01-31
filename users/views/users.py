# Project imports
from users.models.users import User
from users.serializers.users import UserSerializer

# Django Imports
from django.shortcuts import render

# Rest framework Imports
from rest_framework import generics

class UserView(generics.ListCreateAPIView):
    """ View general del User"""
    queryset = User.objects.filter(is_staff = False)
    serializer_class = UserSerializer

