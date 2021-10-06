#Ejercicio 3, Guía 4.
#Dado un conjunto de Nombres y Fechas de nacimientos (AAAAMMDD), que finaliza
#con un Nombre = ‘FIN’,informar el nombre de la persona con mayor edad y el de la más joven
#Alumno= Karen Amarilla
#Inspiración para realizar el ejercicio:
#https://youtu.be/sV-w2HgTOEg
#Variables:
fecha_anio=int(0)
fecha_mes=int(0)
fecha_dia=int(0)
fecha_nacimiento=int(0)#Volcamos la información ingresada
fecha_hoy=int(0)#Se va a cargar los datos del dia de hoy
asignar_resultado=int(0) #Para hacer la comparación entre fecha ingresada y el dia de hoy
asignar_nombre=str("") #Nombre de los usuarios
contador_mayor=int(0)
contador_menor=int(0)
asignar_fmayor=str("") #Persona con mayor edad
asignar_fmenor=str("") #Persona con menor de edad
contador=0

#Cuerpo de programa:

from datetime import date #Para poder realizar la comparacion de años

fecha_hoy = date.today()

while asignar_nombre!= "FIN":
    print("Cálculo de edad\nSí desea finalizar el programa ingrese FIN.")
    asignar_nombre=input("\nPor favor, Ingrese nombre: ")
    while not (asignar_nombre.isalpha()):
        print("Error, Ingrese dato válido.")
        asignar_nombre=input("\nPor favor, Ingrese nombre: ")
    if asignar_nombre!="FIN":
        
        fecha_anio=input("Ingrese su fecha de nacimiento:\nAño: ")
        while not(fecha_anio.isdigit()):
            print("Error, Ingrese dato válido.")
            fecha_anio=input("Ingrese su fecha de nacimiento:\nAño: ")

        fecha_mes=input("Mes: ")
        while not(fecha_mes.isdigit()):
            print("Error, Ingrese dato válido.")
            fecha_mes=input("Mes: ")

        fecha_dia=input("Día: ")
        while not(fecha_dia.isdigit()):
            print("Error, Ingrese dato válido.")
            fecha_dia=input("Día: ")

        fecha_nacimiento=date(int (fecha_anio),int (fecha_mes),int (fecha_dia))

        asignar_resultado= fecha_hoy.year - fecha_nacimiento.year
        contador+=1
        
        if contador==1:
            contador_mayor=asignar_resultado
            contador_menor=asignar_resultado

        #Comparaciones:
        if asignar_resultado>=contador_mayor:
            asignar_fmayor=asignar_nombre

        if asignar_resultado<=contador_menor:
            asignar_fmenor=asignar_nombre
    
print("Persona con mayor edad: {0}".format(asignar_fmayor))
print("Persona con menor edad: {0}".format(asignar_fmenor))
