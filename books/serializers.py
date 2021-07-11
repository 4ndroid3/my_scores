# Project Imports.
from .models import Book

# Rest framework imports
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    """Serializer del model Book."""
    class Meta:
        model = Book
        fields = ( 
            'titulo', 
            'autor', 
            'año_publicacion', 
            'cant_hojas', 
            'img_cover',
        )