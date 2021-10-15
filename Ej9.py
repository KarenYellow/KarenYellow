#Ejercicio N° 9- Guía 5.
#Desarrollar un procedimiento tal que dada una hora (HHMMSS) y un tiempo
#también en formato HHMMSS devuelva la nueva hora que surge de sumar el tiempo
#a la hora inicial, considere también si cambió el día.
#Alumno: Karen Amarilla
#******************************************************************************
#Variables:
asignar_horas=int(0)
asignar_hoy=int(0)
asignar_suma_horas=int(0)

#Funciones:

def suma_horas(hoy,hora):
    suma_horas=datetime.timedelta(hours=hora)
    suma=hoy+suma_horas
    if suma.strftime('%d')>hoy.strftime('%d'):
        return suma.strftime('%H:%M:%S ''Fecha: %d-%m-%Y'),"Se cambió el día"
    else:
        return suma.strftime ('%H:%M:%S ''Fecha: %d-%m-%Y'),"No se cambió el día"

#Cuerpo del programa
import datetime

asignar_hoy=datetime.datetime.now()

asignar_horas=int(input("Ingrese horas: "))

while asignar_horas<=0:
    print ("Error, Ingrese dato válido.")
    asignar_horas=int(input("Ingrese días: "))

asignar_suma_horas=suma_horas(asignar_hoy,asignar_horas)

print("Nueva hora según la cantidad de horas ingresados: {0}".format(asignar_suma_horas))
