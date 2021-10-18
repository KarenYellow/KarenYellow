#2.Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado.
#Copia los elementos de la lista en otra lista pero en orden inverso, y muestra
#sus elementos por la pantalla.
#Alumno: Karen Amarilla.
#*******************************************************************************
lista_normal = []
lista_al_inverso = []
# Recorro la lista normal y leo cada elemento por teclado.
for inicializacion in range(1,6):
	lista_normal.append(input("Ingrese cadena %d:" % inicializacion))
	
#Copiamos en la segunda lista de manera inversa:
lista_al_inverso = lista_normal[::-1]

#Se recorre la lista para mostrar los elementos:
for cadena in lista_al_inverso:
	print(cadena)

