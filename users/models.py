from django.db import models
from django.contrib.auth.models import AbstractUser

from books.models import Book


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


class Profile(models.Model):
    """ Perfil del usuario con informacion adicional
    Campos:
    - id_user: FK
    - biografia: text
    - nacimiento: date
    - profile_img
    - country: FK
    - libros_leidos: int
    - autores_leidos: int """

    users = models.OneToOneField(
        'users.User',
        on_delete = models.CASCADE,
        help_text = 'Nombre del Usuario',
        verbose_name = 'Usuario',
    )
    biography = models.TextField(
        max_length = 500,
        blank=True,
        help_text = 'Breve resumen del Perfil',
        verbose_name = 'Biografía',
    )
    fecha_nacimiento = models.DateField(
        blank = True,
        null=True,
        verbose_name = 'Fecha de Nacimiento',
        help_text = 'Fecha en la que nació',
    )
    user_img = models.ImageField(
        upload_to = 'profile_img', 
        blank = True,
        null=True,
        help_text = 'Imagen de perfil del usuario',
        verbose_name = 'Imagen de Perfil',
    )
    # pais = models.ForeignKey(
    #     'Paises', 
    #     on_delete = models.CASCADE, 
    #     verbose_name = 'País',
    #     blank = True,
    #     null=True,
    #     help_text = 'Pais donde vive el usuario',
    # )

    # Stats
    libros_leidos = models.PositiveIntegerField(
        default=0, 
        help_text = 'Libros leídos por el usuario',
        verbose_name = 'Libros leídos',
    )
    auth_leidos = models.PositiveIntegerField(
        default=0,
        help_text = 'Cantidad de autores leídos por el usuario',
        verbose_name = 'Autores leídos'
    )

    def __str__(self):
        return str(self.users)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


class User_Book(models.Model):
    """
    Libros leidos por un usuario en particular.

    Campos:
    - id_profile: FK
    - id_book: FK
    - fecha_leido: date
    - edicion: int
    - review: text
    """
    id_profile = models.ForeignKey(
        Profile, 
        on_delete = models.CASCADE,
        help_text = 'Autor que leyó el libro.',
        verbose_name = 'Usuario',
    )

    id_book = models.ForeignKey(
        Book, 
        on_delete = models.CASCADE,
        help_text = 'Libro leido',
        verbose_name = 'Libro Leido por el usuario',
    )

    fecha_leido = models.DateField(
        help_text = 'Fecha en la que se leyó el libro.',
        blank = True,
        null=True,
        verbose_name = 'Fecha Leido',
    )

    año_edicion = models.PositiveIntegerField(
        help_text = 'Año de la edicion leida',
        blank = True,
        null=True,
        verbose_name = 'Año de edición',
    )

    reseña = models.TextField(
        max_length = 500,
        help_text = 'Breve reseña del libro leido.',
        blank = True,
        null=True,
        verbose_name = 'Reseña',
    )

    class Meta:
        verbose_name = "Libro leido"
        verbose_name_plural = "Libros Leidos"

    def __str__(self):
        return '{} - {}'.format(self.id_book, self.fecha_leido)