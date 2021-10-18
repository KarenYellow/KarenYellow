# Ejercio N° 7. Guía 6
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco
# enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule
# lista3=lista1+lista2.
# Alumno: Karen Amarilla.
#************************************************************************

#Variables:

#Listas:
lista_1 = []
lista_2 = []
lista_3 = []

def mostrar_suma_lista3(b):
    print("\nLa suma de los vectores es: ")
    for numero in b:
        print(numero," ",end=(""))

#Cuerpo del programa:
#Recorremos la lista y agregamos números:
for indice in range(1,6):
    lista_1.append(int(input("Introduce número entero %d de la lista : " % indice)))
print()
for indice in range(1,6):
    lista_2.append(int(input("Introduce número entero %d de la lista 2: " % indice)))

#Realizamos las suma en la lista 3:
for indice in range(0,5):
    lista_3.append(lista_1[indice] + lista_2[indice])

#Salida en pantalla:
mostrar_suma_lista3(lista_3)


