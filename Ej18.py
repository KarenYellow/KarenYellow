# Ejercicio N° 18. Guía 6*
# Alumno: Karen Amarilla *
# ************************

#Variables-listas:
asignar_cadena=str("")
buscar_modificar_cadena=str("")
buscar_modificar_cadena2=str("")
indice=int(0)
opcion=int(0)
lista=[]

asignar_cadena=input("Ingrese cadena (* para finalizar): ")
while asignar_cadena!="*":
    lista.append(asignar_cadena)
    asignar_cadena=input("Ingrese cadena (* para finalizar): ")

while True:
    print("\n***Menú***")
    print("1-Contar")
    print("2-Modificar")
    print("3-Eliminar")
    print("4-Mostrar")
    print("5-Salir")
    opcion=int(input("\nIngrese opción elegida: "))
    if opcion == 1:
        buscar_modificar_cadena=input("\nIntroduce cadena a buscar: ")
        print("\nLa cadena aparece {0} veces".format(lista.count(buscar_modificar_cadena)))
    elif opcion == 2:
        buscar_modificar_cadena=input("\nIntroduce cadena a buscar: ")
        buscar_modificar_cadena2=input("Introduce cadena a modificar: ")
        indice=0
        for elemento in lista:
            if elemento == buscar_modificar_cadena:
                lista[indice]=buscar_modificar_cadena2
            indice+=1
    elif opcion == 3:
        buscar_modificar_cadena=input("\nIntroduce cadena a eliminar: ")
        if buscar_modificar_cadena in lista:
            lista.remove(buscar_modificar_cadena)
        else:
            print("No existe cadena ingresada en la lista.")
    elif opcion== 4:
        for elemento in lista:
            print(elemento," ",end="")
    elif opcion== 5:
        break
    else:
        print("\nOpción ingresada incorrecta.")
        
        
               
    
    
    
    
