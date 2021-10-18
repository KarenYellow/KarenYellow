# Ejercicio N° 15. Guía 6
# Alumno: Karen Amarilla
# ************************

cantidad_equipos = 15
equipos = []
resultados = []

#Recorremos las listas para ingresar los datos:

for indice in range (0,cantidad_equipos):
    partido=[]
    partido.append(input("Introduce el nombre del equipo 1 del partido {0}: ".format(indice+1)))
    partido.append(input("Introduce el nombre del equipo 2 del partido {0}: ".format(indice+1)))
    equipos.append(partido)
    goles=[]
    goles.append(int(input("Ingrese goles realizados por el equipo {0}: ".format(partido[0]))))
    goles.append(int(input("Ingrese goles realizados por el equipo {0}: ".format(partido[1]))))
    resultados.append(goles)

print("QUINIELA")
print("========")
print("Resultados: 1 Ganó equipo 1, 2 Ganó equipo 2, X Empate")

for partido,goles in zip(equipos,resultados):
    print(partido[0],"-",partido[1],":",end="")
    if goles[0] > goles [1]:
        print("-> 1")
    else:
        if goles[0] < goles [1]:
            print("-> 2")
        else:
            print("-> X")
