#Ejercicio 5-Guía 5. Diseñar una rutina que imprima el cartel:
#	    		PRESIONE ENTER 
#    			PARA CONTINUAR
#Alumno: Karen Amarilla.
#*************************************************************

asignar_ingreso=str("a")
ciclo=bool(True)

def cartel_pantalla():
        print("""
            PRESIONE ENTER 
   	    PARA CONTINUAR""")

#Cuerpo del programa:

while ciclo!=False:
    asignar_ingreso=input("")
    if asignar_ingreso:
        ciclo=False
    else:
        cartel_pantalla()
    
