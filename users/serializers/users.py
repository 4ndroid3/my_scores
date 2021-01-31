# Project Imports
from users.models.users import User

# Rest framework imports
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'is_staff', 
            'is_active', 
            'date_joined',
        )
