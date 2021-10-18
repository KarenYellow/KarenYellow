#Ejercicio N° 11. Guía 6
#Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
#Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
#Muestra el contenido de la tabla en pantalla.
#Alumno: Karen Amarilla.
#******************************************************************************

lista_tabla= []

#Cuerpo del programa:
#Carga de información dentro de la tabla:
for indice_fila in range (0,5):
    lista_fila= []
    for indice_columna in range (0,5):
        #Tenemos que cargar uno en caso de diagonal y 0 en caso de no ser diagonal:
        if indice_fila==indice_columna or indice_fila== 4 - indice_columna:
            lista_fila.append(1)
        else:
            lista_fila.append(0)
    lista_tabla.append(lista_fila)

#Mostramos en pantalla:
for lista_fila in lista_tabla:
    for elemento in lista_fila:
        print(elemento," ",end="")
    print()
