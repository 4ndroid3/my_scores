# MyScores
Proyecto personal con Django, Django REST framework, donde se podrá cargar los libros leidos y luego hacer estadisticas y seguimientos a lo largo del tiempo.

El proyecto tiene su correspondiente docker-file.yml con el cual se ejecutan sus dependencias y se puede configurar el proyecto.

- Version de Python Instalada: 3.9
- Version de Django Instalada: 3.1.5
- Version de Django REST Framework: 3.12.2

Una vez iniciado el proyecto, hay que cargar el archivo CSV con la lista de los paises para la creacion del Perfil de usuario. 
Se debe ejecutar el archivo importar_paises.py que está en la carpeta principal del proyecto.

Cada usuario tiene un Perfil, con datos personales que complementan al Usuario.

## Diseño de Base de Datos
![drawSQL-export-2021-07-09_16_20](https://user-images.githubusercontent.com/35976464/125126673-d1f1bf00-e0d1-11eb-8ad8-72a13a538eb0.png)
