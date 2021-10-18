#Ejercicio N° 3- Guía 6.
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por
# un alumno (comprendidas entre 0 y 10).A continuación debe mostrar todas las
# notas, la nota media, la nota más alta que ha sacado y la menor.
# Alumno: Karen Amarilla.
#*******************************************************************************

#Variables-listas:
lista_notas = []

def mostrar_notas(a, b):
    print("\nNotas Ingresadas: ",end="")
    for a in b:
        print(a," ",end="")
    print()
    print("\nLa nota media: ",sum(b)/len(b))
    print("La nota más alta: ",max(b))
    print("La nota menor: ",min(b))

#Cuerpo del programa:
for indice in range(1,6):   #Carga de notas en la lista:
    while True:
	    nota = int(input("Introduce la nota %d: " % indice))
            #Validacion de la nota ingresada:
	    if nota>=0 and nota<=10:break
    lista_notas.append(nota) #Cargamos la nota en la lista.
# Muestro resultados
mostrar_notas(nota,lista_notas)


