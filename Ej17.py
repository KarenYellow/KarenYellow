# Ejercicio N° 17. Guía 6*
# Alumno: Karen Amarilla *
# ************************

#Variables/listas:
asignar_num=int(0)
lista=[]
lista_sin_duplicados=[]

#Cuerpo del programa:
asignar_num=int(input("Ingrese número, ingrese negativo para terminar: "))
while asignar_num>=0:
    lista.append(asignar_num)
    asignar_num=int(input("Ingrese número, ingrese negativo para terminar: "))

#Ingresamos los números en la lista sin duplicados:
for num in lista:
    if num not in lista_sin_duplicados:
        lista_sin_duplicados.append(num)

#Mostramos en pantalla la lista:

for num in lista_sin_duplicados:
    print(num," ",end="")

