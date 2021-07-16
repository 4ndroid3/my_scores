# Project imports
from users.models import User, Profile, User_Book

# Serializers
from users.serializers import (
    UserSerializer, 
    UserLoginSerializer, 
    UserSignUpSerializer,
    ProfileSerializer,
    UserBookSerializer
)

# Django Imports

# Django REST framework Imports
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class UserView(ListCreateAPIView):
    """ View general del User"""
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer


class UserLoginAPIView(APIView):
    """ Login de usuario con APIview"""
    
    def post(self, request, *args, **kwargs):
        """Maneja los request HTTP POST"""
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user, token= serializer.save()
        data = {
            'user': UserSerializer(user).data,
            'access_token': token,
        }

        return Response(data, status = status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    """ Signup de usuario con APIview"""
    
    def post(self, request, *args, **kwargs):
        """Maneja los request HTTP POST"""
        serializer = UserSignUpSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        data = UserSerializer(user).data

        return Response(data, status = status.HTTP_201_CREATED)


class ProfileView(ListCreateAPIView):
    """ View general del Profile"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(RetrieveAPIView):
    """ View general del Profile"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ReadedBooks(ListCreateAPIView):
    """ View general del Profile"""
    queryset = User_Book.objects.all()
    serializer_class = UserBookSerializer

class ReadedBookDetail(RetrieveAPIView):
    queryset = User_Book.objects.all()
    serializer_class = UserBookSerializer