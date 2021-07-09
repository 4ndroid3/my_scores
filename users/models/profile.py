# Django Imports
from django.db import models

# Project Imports
from books.models import Book

class Profile(models.Model):
    """Profile Model.

    Informacion informal del usuario, 
    contiene un perfil con imagen, estadisticas y datos adicionales.
    """

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
    pais = models.ForeignKey(
        'Paises', 
        on_delete = models.CASCADE, 
        verbose_name = 'País',
        blank = True,
        null=True,
        help_text = 'Pais donde vive el usuario',
    )
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


class Readed_Books(models.Model):
    """ Registro de los libros que va leyendo
    el usuario 
    Campos:
    - id_profile
    - id_book
    - readed_date
    - review"""

    id_profile = models.ForeignKey(
        Profile, 
        on_delete = models.CASCADE, 
        verbose_name = 'Usuario',
        help_text = 'Usuario que leyo el libro',
    )

    id_book = models.ForeignKey(
        'books.Book', 
        on_delete=models.CASCADE,
        verbose_name = 'Libro',
        help_text = 'Libro leido por el usuario',
    )

    readed_date = models.DateField(
        verbose_name = 'Fecha',
        help_text = 'Fecha en la que se leyo el libro',
    )

    review = models.TextField(
        verbose_name = 'Review',
        help_text = 'Reseña del libro leido',
    )
    

class Paises(models.Model):
    """Paises del mundo para agregar en el perfil de usuario
    Dicho modelo no tiene vista en el panel de administración
    """
    nombrePais = models.CharField(
        max_length = 80, 
        verbose_name = 'País',
    )

    def __str__(self):
        return self.nombrePais
