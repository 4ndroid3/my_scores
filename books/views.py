# Project Imports
from .models import Book
from .serializers import BookSerializer

# Django Imports
from django.shortcuts import render

# Django Rest Framework Imports
from rest_framework import generics

class BookView(generics.ListCreateAPIView):
    """ View general de book"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
