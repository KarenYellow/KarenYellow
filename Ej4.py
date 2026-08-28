# Ejercicio N° 4- Guía 6.
# Programa que declare una lista y la vaya llenando de números hasta que
# introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo
# los elementos introducidos).
# Alumno: Karen Amarilla.
#****************************************************************************

#Variables-Listas:
asignar_numero=int(0)
lista_numeros= []

def mostrar_numeros(a,b):
    print("Números ingresados: ")
    for a in b:
        print(a," ",end="")
    
#Cuerpo del programa:

asignar_numero=int(input("Ingrese números: "))

# Ingresamos en el while para cargar positivos hasta que se ingrese el negativo      
while asignar_numero>=0:    
    lista_numeros.append(asignar_numero)
    asignar_numero=int(input("Ingrese números: "))

#Imprimimos la lista:
mostrar_numeros(asignar_numero,lista_numeros)
    
