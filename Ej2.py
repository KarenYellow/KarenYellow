#2. Desarrollar una función tal que dado un  número entero positivo calcule
#y retorne su factorial.

#Alumno: Karen Amarilla

#variables:
asignar_numero=int(0)

#Definición de la función:
def factorial(n):
    if n!= 0:
        asignar_r=n*factorial(n-1)
    else: #El caso que el número ingresado es 0 el resultado es "1":
        asignar_r=1
    return asignar_r

#Cuerpo del programa:

asignar_numero=int(input("Ingrese número: "))
#Validaciones:
while asignar_numero<0:
    print("Error, ingrese valor correcto")
    asignar_numero=int(input("Ingrese número: "))

#Salida en pantalla:
print("Factorial del número ingresado: {0}".format(factorial(asignar_numero)))
