# Project Imports
from users.models import User, Profile, User_Book

# Django Imports.
from django.contrib.auth import authenticate, password_validation

# Rest framework imports
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


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


class UserSignUpSerializer(serializers.Serializer):
    """ Serializer para el registro de usuarios """

    email = serializers.EmailField(
        validators = [UniqueValidator(queryset = User.objects.all())]
    )
    username = serializers.CharField(
        min_length = 4,
        max_length = 20,
        validators = [UniqueValidator(queryset = User.objects.all())]
    )

    # Password
    password = serializers.CharField(min_length = 8, max_length = 20)
    password_confirmation = serializers.CharField(min_length = 8, max_length = 20)

    # Nombres
    first_name = serializers.CharField(min_length = 2, max_length = 30)
    last_name = serializers.CharField(min_length = 2, max_length = 30)

    #fecha_nacimiento = serializers.DateField()

    def validate(self, data):
        """ controla si la contraseña ingresada es correcta """
        password = data['password']
        password_conf = data['password_confirmation']
        if password != password_conf:
            raise serializers.ValidationError('Las contraseñas no coinciden')
        password_validation.validate_password(password)
        return data
    def create(self, data):
        """ Crea usuarios y perfil """
        data.pop('password_confirmation') # Lo borro porque acá ya no me sirve
        user = User.objects.create_user(**data)
        profile = Profile.objects.create(users = user)
        return user


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


class UserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Book
        fields = (
            'id_profile',
            'id_book', 
            'fecha_leido', 
            'año_edicion', 
            'reseña',
        )
