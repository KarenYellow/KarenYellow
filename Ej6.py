# Ejercicio N° 6. Guía 6
# Crea un programa que pida un número al usuario un número de mes (por ejemplo,
# el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes
# usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.
# Alumno: Karen Amarilla.
#*******************************************************************************
#Variables:
asignar_mes=int(0)

#Listas:
lista_dias = [31,28,31,30,31,30,31,31,30,31,30,31]
lista_meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

def mostrar_dias(a,b,c):
    print("El mes de",a[b-1],"tiene",c[b-1],"días.")

#Cuerpo del programa:

#Ingreso en pantalla:
    
while True:
	asignar_mes = int(input("Introduce un mes (1-12): "))
        #Validaciones
	if asignar_mes < 1 or asignar_mes > 12:
		print("Error: mes incorrecto.")
	if asignar_mes>=1 and asignar_mes<=12: break

mostrar_dias(lista_meses,asignar_mes,lista_dias)
