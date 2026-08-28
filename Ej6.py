#Ejercicio N°6-Guía 5
#Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA.
#El dato que recibe es un longint con una fecha en formato aaaammdd.
#Alumno:Karen Amarilla.
#***********************************************************************

asignar_numero=int(0)

def mostrar_fechas(a):
    print("\nFecha ingresada: ")
    print (str(a)[7:8]+("/")+str(a)[5:6]+("/")+str(a)[0:4])



#Cuerpo del programa:
asignar_numero=int(input("Ingrese fecha *formato para ingresar es AAAAMMDD*: "))

mostrar_fechas(asignar_numero)
