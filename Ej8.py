# Ejercicio N° 8. Guía 6
# Queremos guardar los nombres y las edades de los alumnos de un curso.
# Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre
# un asterisco (*) Al finalizar se mostrará los siguientes datos: Todos los
# alumnos mayores de edad y los alumnos mayores (los que tienen más edad)
# Alumno: Karen Amarilla.
#**************************************************************************
#Variables:
asignar_nombre=str("")
edad_maxima=int(0)
#Listas:
lista_nombres= []
lista_edades= []

#Inicializamos las listas hasta que se introduce el (*):

while True:
    asignar_nombre=input("Ingrese nombre del alumno: ")
    if asignar_nombre!=("*"):
        lista_nombres.append(asignar_nombre)
        lista_edades.append(int(input("Edad: ")))
    if asignar_nombre==("*"): break
        
#Calculamos la edad máxima ingresada en la lista:
edad_maxima= max(lista_edades)

#Mostramos en pantalla:
#Alumnos mayores de edad:
print("************************")
print("Alumnos mayores de edad: ")
print("************************")

for nombre,edad in zip (lista_nombres,lista_edades): #Utilizamos zip para mapear las dos listas al mismo tiempo
    if edad >= 18:
        print(nombre)

print("************************")
print("Alumno más viejo: ")
print("************************")

for nombre,edad in zip(lista_nombres,lista_edades):
    if edad == edad_maxima:
        print(nombre)
