#Ejercicio 3-Guía 5, Dada una serie de números enteros, informar:
#a) su factorial
#b) cuantos múltiplos de 3
#c) cuantos múltiplos de 5
#d) cuantos múltiplos de 3 y de 5
#Utilice las funciones de ejercicios anteriores.
#Alumno: Karen Amarilla
#*************************************************
#Variables:
asignar_numero=int(0)
acumulador_factoriales=str("")
acumulador_multiplos=str("")
asignar_acumulador3=int(0)
asignar_acumulador5=int(0)
asignar_acumulador3_5=int(0)
#Definición de la función:
def factorial(n):
    if n!= 0:
        asignar_r=n*factorial(n-1)     
    else: #El caso que el número ingresado es 0 el resultado es "1":
        asignar_r=1
    return asignar_r

def multiplos_3(n):
    acumulador3=int(0)
    if int(n)%3==0:
        acumulador3=acumulador3+1
    else:
        acumulador3=0
    return acumulador3
def multiplos_5(n):
    acumulador5=int(0)
    if int(n)%5==0:
        acumulador5=acumulador5+1
    else:
        acumulador5=0
    return acumulador5
def multiplos_3_5(n):
    acumulador3_5=int(0)
    if int(n)%3==0 and int(n)%5==0:
        acumulador3_5=acumulador3_5+1
    else:
        acumulador3_5=0
    return acumulador3_5
def cantidades(a,b,c,d):
    print("Factorial de cada número: {0}".format(a))
    print("múltiplos de 3: {0}".format(b))
    print("múltiplos de 5: {0}".format(c))
    print("múltiplos de 3 y 5: {0}".format(d))

#cuerpo del programa: 
from random import randint
for i in range (1,11):
    asignar_numero=randint(1,100)
    print("números:", asignar_numero)
    factorial(asignar_numero)
    multiplos_3(asignar_numero)
    multiplos_5(asignar_numero)
    multiplos_3_5(asignar_numero)
    acumulador_factoriales=acumulador_factoriales+("\n")+str(factorial(asignar_numero))
    asignar_acumulador3=asignar_acumulador3+multiplos_3(asignar_numero)
    asignar_acummulador5=asignar_acumulador5+multiplos_5(asignar_numero)
    asignar_acumulador3_5=asignar_acumulador3_5+multiplos_3_5(asignar_numero)
    
cantidades(acumulador_factoriales,asignar_acumulador3,asignar_acummulador5,asignar_acumulador3_5)
    
    



