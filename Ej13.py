# Ejercicio N° 13 Guía 6-De una empresa de transporte se quiere guardar el
# nombre de los conductores que tiene, y los kilómetros que conducen cada día
# de la semana. Para guardar esta información se van a utilizar dos arreglos:
# Nombre: Lista para guardar los nombres de los conductores.
# kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que
# realiza cada conductor. Al finalizar se muestra la lista con los nombres de
# conductores y los kilómetros que ha realizado.
# Alumno: Karen Amarilla.
#******************************************************************************
#Variables:
cantidad_conductores=int(0)
#Lista constante:
dias=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
#Lista para cargar datos solicitados en pantalla:
nombre=[]
kms=[]

while True:
    cantidad_conductores=int(input("Ingrese cantidad de conductores trabajando: "))
    if cantidad_conductores>0:break

for indice_conductores in range (0,cantidad_conductores):
    nombre.append(input("\nIngrese nombre del conductor {0}: ".format(indice_conductores+1)))
    km_dia=[]
    for indice_dias in range (0,7):
        km_dia.append(int(input("Ingrese cantidad de kms realizado el {0}: ".format(dias[indice_dias]))))
    kms.append(km_dia)

#Lista para volcar los totales:
                                                                                  
total_kms=[]
for km in kms:
    total_kms.append(sum(km))

print()
#Utilizamos el zip para mostrar ambas listas:
for nombre,km in zip(nombre,total_kms):
    print("{0} ha realizado {1} Kilómetros.".format(nombre,km))                   
