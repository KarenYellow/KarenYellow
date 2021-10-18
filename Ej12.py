#Ejercicio N° 12. Guía 6-Diseñar el algoritmo correspondiente a un programa,que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las
# posiciones o elementos que delimitan la tabla, es decir, las más externas,
# mientras que el resto de los elementos contendrán el valor 0.
# Alummo: Karen Amarilla
#*****************************************************************************

lista_tabla= []

#Cuerpo del programa:
#Carga de información dentro de la tabla:
for indice_fila in range (0,5):
    lista_fila= []
    for indice_columna in range (0,15):
        #Tenemos que cargar uno en caso de diagonal y 0 en caso de no ser diagonal:
        if indice_fila==0 or indice_fila==4:
            lista_fila.append(1)
        elif indice_columna==0 or indice_columna==14:
            lista_fila.append(1)
        else:
            lista_fila.append(0)
    lista_tabla.append(lista_fila)

#Mostramos en pantalla:
for lista_fila in lista_tabla:
    for elemento in lista_fila:
        print(elemento," ",end="")
    print()
