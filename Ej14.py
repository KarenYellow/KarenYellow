# Ejercicio 14, Guía 6-
# Crear un programa que lea los precios de 5 artículos y las cantidades
# vendidas por una empresa en sus 4 sucursales. Informar:
# Las cantidades totales de cada artículo.
# La cantidad de artículos en la sucursal 2.
# La cantidad del artículo 3 en la sucursal 1.
# La recaudación total de cada sucursal.
# La recaudación total de la empresa.
# La sucursal de mayor recaudación.
# Alumno: Karen Amarilla.
#***********************************************************************

precios = []
cantidades = []
num_articulos = 5
num_sucursales = 4

# Solicitamos precios:
for indice_art in range(0, num_articulos):
   precios.append(float(input("Ingrese Precio Articulo {0}: ".format((indice_art+1)))))

# Solicitamos cantidades:

for indice_sucursal in range(0, num_sucursales):
    cant_art = []
    for indice_articulos in range(0, num_articulos):
        cant_art.append(int(input("Ingrese Cant. de Articulo {0}, en sucursal {1}: ".format(indice_articulos+1,indice_sucursal+1))))
    cantidades.append(cant_art)
   
#Se realiza la suma x artículos:

print('\nCantidades por artículos:')
for indice_articulos in range(0, num_articulos):
    suma = 0
    for cant_sucursal in cantidades:
        suma = suma + cant_sucursal[indice_art]
    print("Total articulo {0}: {1}".format (indice_art + 1,suma))

# Informar Total de artículos Sucursal 2
print("\nTotal Sucursal 2: {0}".format(sum(cantidades[1])))

# Informar Sucursal 1, Articulo 3:
print("\nSucursal 1, Articulo 3: {0}".format(cantidades[0][2]))

# Guardo en una lista las recaudaciones de cada sucursal
total_por_sucursal = []
for cant_sucursal in cantidades:
    total=0
    for precio,cantidad in zip(precios,cant_sucursal):
        total=total+precio*cantidad
    total_por_sucursal.append(total)
# Calculo el máximo que se ha vendido
mayor_recaudacion = max(total_por_sucursal)   
indice_sucursal = 1
for indice_sucursal in range(0, num_sucursales):
    print("\nRecaudaciones Sucursal {0}: {1}".format(indice_sucursal+1,total_por_sucursal[indice_sucursal]))
    indice_sucursal += 1

# Calculo la sucursal con mayor recaudación
indice_sucursal = 1
for cant_sucursal in total_por_sucursal:
    if cant_sucursal == mayor_recaudacion: break
    indice_sucursal += 1

print("\nRecaudación total de la empresa: {0}".format(sum(total_por_sucursal)))
print("\nSucursal de Mayor Recaudación: {0}".format (indice_sucursal))


