# Project Imports
from users.models.users import User

# Django Imports.
from django.contrib.auth import authenticate

# Rest framework imports
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'is_staff', 
            'is_active', 
            'date_joined',
        )

class UserLoginSerializer(serializers.Serializer):
    """Serializer para realizar Login de Usuario """
    
    email = serializers.EmailField()
    password = serializers.CharField(min_length = 8, max_length = 64)

    def validate(self, data):
        """ Verifica las credenciales ingresadas en el serializer
        la funcion authenticate importada de django va a comparar los datos de la db
        vs los datos ingresados. Si estos no son correctos se va a levantar el 
        ValidationError.
        """
        user = authenticate(username = data['email'], password = data['password'])
        if not user:
            raise serializers.ValidationError('Credenciales Invalidas')
        self.context['user'] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user = self.context['user'])
        return self.context['user'], token.key