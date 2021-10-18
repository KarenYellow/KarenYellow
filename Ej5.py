#Ejercicio N° 5. Guía N° 6.
# Hacer un programa que inicialice una lista de números con valores aleatorios
# (10 valores), y posterior ordene los elementos de menor a mayor.
# Alumno: Karen Amarilla
#*****************************************************************************

#Variables-listas
lista_numeros = []

def ordenar(a):
    a.sort()

#cuerpo del programa:
import random
for indice in range (1,11):
    lista_numeros.append( random.randint(1,100))

ordenar(lista_numeros) #función para ordenar los números de la lista.
#Impresión en pantalla
print("\nLista de números: ")
for numero in lista_numeros:
    print(numero," ",end="")
