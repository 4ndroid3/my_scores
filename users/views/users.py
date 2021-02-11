# Project imports
from users.models.users import User

# Serializers
from users.serializers.users import (
    UserSerializer, 
    UserLoginSerializer, 
    UserSignUpSerializer
)


# Django Imports

# Django REST framework Imports
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class UserView(generics.ListCreateAPIView):
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