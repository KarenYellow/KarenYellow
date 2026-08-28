#Ejercicio N° 7-Guía 5
#Desarrollar una rutina tal que dados una base y un exponente, enteros
#positivos, calcule y retorne la potencia.
#Alumno: Karen Amarilla.
#**********************************************************************

#Variables:

asignar_n1=int(0)
asignar_n2=int(0)

def potencias(a,b):
    asignar_potencia=a**b
    return asignar_potencia

#Cuerpo del programa:

asignar_n1=int(input("Ingrese base: "))
while asignar_n1<0:
    print("Error, ingrese valor válido.")
    asignar_n1=int(input("Ingrese base: "))

asignar_n2=int(input("Ingrese exponente: "))

while asignar_n2<0:
    print("Error, ingrese valor válido.")
    asignar_n2=int(input("Ingrese exponente: "))
    
print("Potencia de los números ingresados: {0}".format (potencias(asignar_n1,asignar_n2)))
