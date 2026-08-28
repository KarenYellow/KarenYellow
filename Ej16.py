# Ejercicio N° 16. Guía 6
# Alumno: Karen Amarilla
# ************************
#Variables:
opcion=int(0)
ingreso_num=int(0)
posicion_lista=int(0)
lista = []
while True:
    print("\nMenú")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

    opcion=int(input("\nIngrese opción elegida: "))

    if opcion==1:
        ingreso_num=int(input("Ingrese número: "))
        lista.append(ingreso_num)
    elif opcion ==2:
        ingreso_num=int(input("Ingrese número: "))
        posicion_lista=int(input("Ingrese posición (Empezando por 1): "))
        if posicion_lista>len(lista):
            print("Error, posición incorrecta")
        else:
            lista.insert(posicion_lista-1,ingreso_num)
    elif opcion == 3:
        print("Longitud de la lista: {0}".format(len(lista)))
    elif opcion == 4:
        if len(lista)>0:
            print("Último elemento es {0}, se borrará.".format(lista.pop()))
        else:
            print("La lista está vacia.")
    elif opcion ==5:
        posicion_lista=int(input("Ingrese posición (Empezando por 1): "))
        if posicion_lista>len(lista):
            print("Error, posición incorrecta.")
        else:
            print("Él elemento es {0}, se borrará.".format(lista.pop()))
    elif opcion == 6:
        ingreso_num=int(input("Ingrese número: "))
        print("El número {0} aparece {1} de veces en la lista.".format(ingreso_num,lista.count(lista)))
    elif opcion == 7:
        ingreso_num=int(input("Ingrese número: "))
        indice_buscar=0
        print("Posiciones: ",end="")
        for indice in range(0,lista.count(ingreso_num)):
            indice_buscar=lista.index(ingreso_num,indice_buscar)
            indice_buscar+=1
            print(indice_buscar," ",end="")
        print()
    elif opcion == 8:
        for num in lista:
            print(num," ",end="")
        print()
    elif opcion == 9:
        break
    else:
        print("Opción incorrecta.")
        
