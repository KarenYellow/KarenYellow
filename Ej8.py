#8. Desarrollar una rutina tal que dada una fecha (AAAAMMDD) y un número natural que representa una cantidad de días,
#calcule y retorne la nueva fecha en tres parámetros año (AAAA), mes (MM) y día (DD) que resulte de incrementar al
#parámetro fecha con el parámetro cantidad de días. 
#Alumno: Karen Amarilla
#*****************************************************************************

#Variables:
asignar_dias=int(0)
suma=int(0)
asignar_hoy=int(0)
suma_dias=int(0)

#Funciones:

def suma_dias (hoy,dias):
    suma_dias=datetime.timedelta(days=dias)
    suma=hoy+suma_dias
    return suma

#Cuerpo del programa
import datetime
asignar_hoy=datetime.date.today()
asignar_dias=int(input("Ingrese días: "))

while asignar_dias<=0 or asignar_dias>31:
    
    print ("Error, Ingrese dato válido.")
    asignar_dias=int(input("Ingrese días: "))

print("Nueva fecha según la cantidad de días ingresados: {0}".format(suma_dias(asignar_hoy,asignar_dias)))
