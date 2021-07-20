# Project Imports
from .models import Book
from .serializers import BookSerializer

# Django Imports
from django.shortcuts import render

# Django Rest Framework Imports
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, 
    RetrieveModelMixin, 
    UpdateModelMixin, 
    ListModelMixin)

# class BookListCreate(ListCreateAPIView):
#     """ View general de book"""
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDetail(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookView(CreateModelMixin, RetrieveModelMixin,
               UpdateModelMixin, ListModelMixin,
               GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer