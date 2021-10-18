#Ejercicio N° 1. Guía 6
#Realizar un programa que inicialice una lista con 10 valores aleatorios
#(del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista
#junto con su cuadrado y su cubo.
#Alumno: Karen Amarilla
#*****************************************************************************

#Importamos random para poder utilizarla para asignar valores aleatorios

import random

#Función para mostrar la información en pantalla:
def mostrar_cuadrado_cubo (a):
    print("Lista: ")
    for numero in a:
        print(numero,"Al Cuadrado: ",numero ** 2,"Al cubo: ",numero ** 3)

#Cuerpo del programa:
lista_de_numeros = []
# Realizamos el primer recorrido para asignar los números random
for asignar in range(1,11):
	lista_de_numeros.append(random.randint(1,10))
mostrar_cuadrado_cubo(lista_de_numeros)
