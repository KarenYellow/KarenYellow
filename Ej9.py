#Ejercicio N° 9. Guía 6- Queremos guardar la temperatura mínima y máxima de 5
#días. Realiza un programa que de la siguiente información:
#La temperatura media de cada día
#Los días con menos temperatura
#Se lee una temperatura por teclado y se muestran los días cuya temperatura
#máxima coincide con ella. si no existe ningún día se muestra un mensaje de
#información.

#Variables-Listas:

lista_temperaturas= []
temperaturas_medias=int(0)
indice=int(0) #Para contar cantidad de días
temperatura_minima=int(0)
temperatura_maxima=int(0)
existe_temperatura=True
#Cuerpo del programa:
#Cargamos temperaturas

for indice in range (1,6):
    lista_temperatura=[]
    lista_temperatura.append(int(input("Día %d. Temperatura máxima: "% indice)))
    lista_temperatura.append(int(input("Día %d. Temperatura mínima: "% indice)))
    lista_temperaturas.append(lista_temperatura)

#Mostramos temperaturas medias:
print("********************")
print("Temperaturas medias: ")
print("********************")
indice = 1
for lista_temperatura in lista_temperaturas:
    temperaturas_medias=sum(lista_temperatura)/len(lista_temperatura)
    print("\nDía {0} Temperatura media: {1}".format(indice,temperaturas_medias))
    indice+=1


#En el enunciado dice los días con menos temperatura, en este caso sin un valor de
#referencia tomé como mostrar el día con menos temperatura
print("\n**************************")
print("Día con menos temperatura: ")
print("**************************")

temperatura_minima=min(lista_temperaturas)

indice = 1
for lista_temperatura in lista_temperaturas:
    if lista_temperatura == temperatura_minima:
        print("Día {0}".format(indice))
    indice+=1
                    
#Corroborar si tiene un máximo dentro de la lista:
    
temperatura_maxima=int(input("\nIngrese temperatura máxima que desea controlar si hubo y cuando fué: "))
indice=1
for lista_temperatura in lista_temperaturas:
    if lista_temperatura [0] == temperatura_maxima:
        print("Día {0}".format(indice))
        existe_temperatura= True
    indice+=1
if not existe_temperatura:
    print("No hay ningun día con dicha temperatura")
