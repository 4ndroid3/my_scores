# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """User Model Modificado

    Se extiende de la clase AbstractUser para agregar nuevas funcionalidades
    al usuario base.
    - Se edita el email, haciendo que sea unico, se agregan mensajes de error.
    - Se agrega el email como campo para loguearse.
    - Se agrega el usuario, nombre y apellido como usuarios requeridos.
    """

    email = models.EmailField(
        unique=True,
        error_messages = {
            'Unico' : 'Ya existe un usuario con esa dirección de Email'
        },
    )

    # USERNAME_FIELD me idica que el campo email ahora me lo va a pedir para iniciar sesion.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return str(self.username)
