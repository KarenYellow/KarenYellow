#JUEGO DEL AHORCADO.PY/ Desarroladores, Alice  Ramirez, karen Amarrilla
#Umet/Diplomatura en Programacion/ Prof. Adriana Fachal

import time #importamos la siguiente para utilizar el método time.sleep 
import random #Importamos la siguiente para utilizar el método .random

#Asignaciones y Declaraciones de variables

nombre=str("");
respuesta=str ("");
palabras=[];
puntos=int(0);
ahorcado =[]
tupalabra=str("");
tuletra=str("");
fallas=int(0);
puntos = int(0);
#Cuerpo del programa

print("""Bienvenido a nuestro juego del ahorcado
      \nAlumnas: Alice Ramirez, Karen Amarilla
      \nTaller de programación 2021"""); #La presentancion o inicio del juego.
nombre=input("\n¿Cómo te llamas? "); # Nombre de quien lo juega o el usuario en este caso

#validación del nombre ingresado:
while not nombre.isalpha():
    print("Error, ingrese dato válido");
    nombre=input("¿Cómo te llamas? ");
    
print("\nhola",nombre,"es hora de jugar");
print(" ");
time.sleep(1)
print("¡Comienza a adivinar!"); 
time.sleep(0.5)
palabras = ["hormiga","mundo","murcielago","oso","carretera","crucigrama","cirujano",
"herramienta","almeja","cobra","pantera","coyote","cuervo","ciervo","perro","pato",
"aguila","zorro","geografia","tierra","ascensor","futbol","termometro","universidad",]; #Tupla que almacena las palabras a adivinar 
respuesta = "si";
ahorcado = ['''

   +---+
   |   |
       |
       |
       |
       |
=========''','''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']; #tupla con imagenes del ahorcado

while respuesta == "si": #Bucle General para repetir el Juego:
    palabra = list(random.choice(palabras)); #Asignacion aleatoria de una plabra de la tupla(palabras)
    tupalabra = " "
    vidas = 6
    print(ahorcado[0]);
    while vidas > 0:#Bucle de vidas para seguir jugando
        fallas=0;
        for letra in palabra:
            if letra in tupalabra:
                print(letra,end="");
            else:
                print("*",end="");
                fallas+=1
        if fallas==0: 
            print("");
            print("¡Felicidades!, Ganaste");
            puntos += 10;
            break;
        #Validacion de letras ingresadas
        tuletra=input(" Introduce una letra: ").lower();
        while not tuletra.isalpha(): #.isalpha()comprueba si el carácter es alfabético o no
            print("Error, ingrese dato válido");
            tuletra=input("Introduce una letra: ").lower();
        tupalabra+=tuletra #tuletra se almacena en tupalabra

        if tuletra not in palabra: #Verifica según las vidas que nos queda que dibujo corresponde
            if vidas == 6:
                print (ahorcado [1]);
            elif vidas == 5:
                print (ahorcado [2]);
            elif vidas == 4:
                print (ahorcado [3]);
            elif vidas == 3:
                print (ahorcado [4]);
            elif vidas == 2:
                print (ahorcado [5]);
            elif vidas == 1:
                print (ahorcado [6]);
            vidas-=1
            print("¡Te equivocaste!");
            print("Te quedan",vidas,"vidas.");
            print("");
        if vidas== 0:
            print("¡Perdiste!");
            print ("\nLa palabra correcta era: ");
            for n in palabra:#Nos imprime la palabra correcta..
                print (n,end="");
    
    print("");
    respuesta = input("\nDesea continuar el Juego? (si/no): ").lower(); #Verifica si quiere seguir jugando y valida el bucle General
    while respuesta != "si" and respuesta!= "no":
        print("Error, ingrese dato válido");
        respuesta =input("\nDesea continuar el Juego? (si/no): ").lower();
print("\n¡Gracias por Participar!");
print("Tu Puntaje:",puntos);
