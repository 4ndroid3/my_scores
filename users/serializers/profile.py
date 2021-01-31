# Project Imports
from users.models.profile import Profile

# Rest Framework Imports
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'users',
            'biography', 
            'fecha_nacimiento', 
            'user_img', 
            'pais', 
            'libros_leidos', 
            'auth_leidos',
        )
