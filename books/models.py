""" Modelo de libros"""

# Project Imports

# Django Imports
from django.db import models

class Book(models.Model):
    """ Modelo de libro, 
    contiene todos los datos de un libro, el cual luego

    - Usuario que lo leyó.
    - Título del libro.
    - Autor.
    - Año de publicación del libro.
    - Cantidad de hojas del libro.
    - Fecha en la que se leyó el libro.
    """

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

    img_cover = models.ImageField(
        upload_to = 'cover_img', 
        blank = True,
        null=True,
        help_text = 'Imagen de perfil del usuario',
        verbose_name = 'Imagen de Perfil',
    )

    def __str__(self):
        return '{} - {}'.format(self.titulo, self.autor)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
