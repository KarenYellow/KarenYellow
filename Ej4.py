#Ejercicio N°4-Guía 5. Dada la fracción P/Q, para P y Q naturales informar la mayor cantidad
#de simplificaciones. Desarrolle y utilice una función que reciba dos números
#naturales y retorne el menor factor común. Ej: 360/60 = 180/30 = 90/15 = 30/5
#= 6/1
#Alumnno: Karen Amarilla
#*********************************************************************************************************
#Variables
asignar_n1=int(0)
asignar_n2=int(0)
mcm=int(0)
asignar_simplificaciones=int(0)

def maximo_comun_divisor(a, b):
    num_temporal = 0
    while b != 0:
        num_temporal = b
        b = a % b
        a = num_temporal
    return a

def simplificaciones(r, a, b):
    division_1=int(0)
    division_2=int(0)
    asignar_contador=int(0)
    while b!=1:
        division_1=a//r
        division_2=b//r
        a=division_1
        b=division_2
        asignar_contador+=1
    return asignar_contador

def menor_factor_comun(mcm,a,b):
    resultado=a*b/mcm
    return resultado

#Cuerpo del programa:

asignar_n1 =int(input("Ingrese numerador: "))
#validaciones:
while asignar_n1<0:
    print("Error, ingrese valor correcto.")
    asignar_n1 =int(input("Ingrese numerador: "))
    
asignar_n2 =int(input("Ingrese denominador: "))
#validaciones
while asignar_n2<0:
    print("Error, ingrese valor correcto.")
    asignar_n2 =int(input("Ingrese denominador: "))
    
mcm = maximo_comun_divisor(asignar_n1,asignar_n2)
asignar_simplificaciones= simplificaciones(mcm, asignar_n1, asignar_n2)
mfc= menor_factor_comun (mcm, asignar_n1, asignar_n2)

print ("Cantidad de simplificaciones realizadas: {0}.".format(asignar_simplificaciones))
print ("Menor factor común {0}.".format(mfc))



