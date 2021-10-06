#1. Desarrollar una función que calcule el máximo común divisor de dos
#números enteros A, B con el siguiente algoritmo:
#1) Dividir A por B, y calcular el resto (0 < R < B)
#2) Si R = 0, el MCD es B, si no seguir en 3)
#3) Reemplazar A por B, B por R, y volver al paso 1)

asignar_a=int(0)
asignar_b=int(0)

#Definición de la función:
def max_comun_divisor(a,b):
    asignar_div=1
    while asignar_div > 0:
        asignar_div=a%b
        if asignar_div == 0:
            asignar_mcd=b
        else:
            a=b
            b=asignar_div
    
    return asignar_mcd
    

#Cuerpo del programa:

asignar_a=int(input("Ingrese numero: "))

while asignar_a<0:
    print("Error, ingrese valor válido")
    asignar_a=int(input("Ingrese numero: "))

asignar_b=int(input("Ingrese segundo numero: "))

while asignar_b<0:
    print("Error, ingrese valor válido")
    asignar_b=int(input("Ingrese segundo numero: "))

print("MCD de los números ingresados:{0} y {1} es :{2}".format(asignar_a,asignar_b,max_comun_divisor(asignar_a,asignar_b)))
