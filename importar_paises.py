""" Script para importar datos desde el .csv que contiene 
todos los nombres de los paises."""
import csv
from users.models.profile import Paises
with open('paises.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(str(row['nombre']))
		pais = Paises()
		pais.nombrePais = str(row['nombre'])
		pais.save()