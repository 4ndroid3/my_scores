""" Modelo de libros"""

# Project Imports
from users.models.users import User

# Django Imports
from django.db import models

class Book(models.Model):
    """ Modelo de libro leído

    El modelo contiene datos del libro que se leyo.
    Cargando aspectos importantes del mismo, para fines 
    estadisticos e informativos. Son:
    - Usuario que lo leyó.
    - Título del libro.
    - Autor.
    - Año de publicación del libro.
    - Cantidad de hojas del libro.
    - Fecha en la que se leyó el libro.
    """

    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        help_text = 'Autor que leyó el libro.',
        verbose_name = 'Usuario',
    )

    titulo = models.CharField(
        max_length = 80,
        help_text = 'Título del libro leido.',
        verbose_name = 'Título',
    )

    autor = models.CharField(
        max_length = 80,
        help_text = 'Autor del libro leido.',
        verbose_name = 'Autor',
    )

    año_publicacion = models.PositiveIntegerField(
        help_text = 'Año en que se publico el libro.',
        blank = True,
        null=True,
        verbose_name = 'Año de publicación',
    )

    cant_hojas = models.PositiveIntegerField(
        help_text = 'Cantidad de hojas que tiene el libro.',
        blank = True,
        null=True,
        verbose_name = 'Cantidad de Hojas',
    )

    fecha_leido = models.DateField(
        help_text = 'Fecha en la que se leyó el libro.',
        blank = True,
        null=True,
        verbose_name = 'Fecha Leido',
    )

    reseña = models.TextField(
        max_length = 500,
        help_text = 'Breve reseña del libro leido.',
        blank = True,
        null=True,
        verbose_name = 'Reseña',
    )

    def __str__(self):
        return '{} - {}'.format(self.titulo, self.autor)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
    
