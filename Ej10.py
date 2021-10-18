#Ejercicio N° 10. Guía 6
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna
# visualizando los resultados en pantalla.
# Alumno: Karen Amarilla.
#****************************************************************************

#Variables y listas

asignar_suma=int(0)
lista_tabla=[]

def suma_filas(a,b):
    asignar_indice = 1
    for a in b:
        print("La suma de los elementos de la fila {0} es: {1}".format(asignar_indice,sum(a)))
    asignar_indice+=1
    
def suma_columnas (a,b):
    for indice_columna in range (1,6):
        suma=0
        for a in b:
            suma=suma+a[indice_columna - 1]
        print("La suma de los elemento de la columna {0} es {1}".format(indice_columna,suma))
        
#Cuerpo del programa:
import random
for indice_fila in range (1,6):
    lista_fila=[]
    for indice_columna in range(1,6):
        lista_fila.append(random.randint(1,100))
    lista_tabla.append(lista_fila)

#Suma de las filas y columnas:
suma_filas(lista_fila,lista_tabla)
print()
suma_columnas(lista_fila,lista_tabla)

print()
print("Tabla 5x5: ")
#Mostrar en pantalla:
for lista_fila in lista_tabla:
    for elemento in lista_fila:
        print(elemento," ",end="")
    print()
