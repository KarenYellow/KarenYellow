# Juego base:
# Idea de juego en base a la consigna de la docente
# Juego a realizar: Preguntados de tipo programación/informática.

#Variables
nombre_jugador=str("")
seleccion_nivel=int(0)
seleccion=bool (True) 

#Función donde se encuentra cargado las preguntas del nivel principiante:
def nivel_principiante(nombre):
    respuesta=int(0)
    respuesta_correcta=int(0)
    respuesta_incorrecta=int(0)
    print("**Principante**")
    print("\nPregunta 1: ¿Qué es la informática?  ")

    print("""\n1- Ciencia que estudia el comportamiento computacional
    \n2- Ciencia que se encarga del estudio y aplicación del tratamiento automático de la información.
    \n3- Ciencia que se encarga de desarrollar programas.""")
    respuesta=int(input(""))
    if respuesta == 2:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 2: ¿Qué es una computadora? ")
    print("""\n1- Es un sistema electrónico que permite la entrada de datos, el procesamiento y almacenamiento de los mismos.
    \n2- Es un artefacto que me permite utilizar Facebook.
    \n3- Es un sistema que me permite realizar experimentos científicos.""")
    respuesta=int(input(""))
    if respuesta == 1:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    
    print("\nPregunta 3: ¿Qué es un lenguaje de programación? ")
    print("""\n1- Es la unidad lógica de una computadora.
    \n2- Es un componente de la computadora.
    \n3- Es un lenguaje formal diseñado para realizar procesos que pueden ser llevados a cabo por máquinas como las computadoras.""")
    respuesta=int(input(""))
    if respuesta == 3:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 4: Tipos de lenguajes de programación: ")
    print("""\n1- Teclado, mouse, parlantes, webcam.
    \n2- C#, C++, JavaScript, Python.
    \n3- Monitor, CPU, impresora.""")
    respuesta=int(input(""))
    if respuesta == 2:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 5: ¿Qué es el hardware? ")
    print("""\n1-  Son los componentes físicos y tangibles.
    \n2- Son los circuitos electrónicos.
    \n3- Es la unidad lógica.""")
    respuesta=int(input(""))
    if respuesta == 1:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\n ¡Gracias por participar {0}!".format(nombre))
    print("\n Cantidad de respuestas correctas: {0} , incorrectas: {1}".format(respuesta_correcta, respuesta_incorrecta)) 
#Función donde se encuentra cargado las preguntas del nivel intermedio
def nivel_intermedio(nombre):
    respuesta=int(0)
    respuesta_correcta=int(0)
    respuesta_incorrecta=int(0)
    print("**Intermedio**")
    print("\nPregunta 1: ¿Qué es un compilador?")
    print("""\n1- Es un componente electrónico.
    \n2- Es un programa informático que traduce un programa escrito en un lenguaje de programación a otro lenguaje diferente.
    \n3- Es un programa que crea archivos pdf.""")
    respuesta=int(input(""))
    if respuesta == 2:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 2: ¿Qué es el sistema binario? ")
    print("""\n1- Sistema de numeración cuya base es 8 el cual utiliza los dígitos: 0, 1, 2, 3, 4, 5, 6, 7.
    \n2- Sistema de numeración el cual utiliza como base aritmética el número diez (10).
    \n3- Sistema de numeración en el cual los números son representados utilizando dos cifras (0 y 1).""")
    respuesta=int(input(""))
    if respuesta == 3:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 3: ¿Qué es el Sistema operativo (SO)?")
    print("""\n1- Es el conjunto de programas llamados "de oficina" tales como Word, Excel, PowerPoint, etc.
    \n2- Es el conjunto de órdenes y programas que controlan los procesos básicos de una computadora y permiten el funcionamiento de otros programas.
    \n3- Es el conjunto de navegadores de internet.""")
    respuesta=int(input(""))
    if respuesta == 2:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 4: ¿Qué es un archivo ejecutable?")
    print("""\n1- Es un archivo diseñado para dañar las computadoras.
    \n2- Es un archivo diseñado para poder iniciar un programa
    \n3- Es un archivo diseñado para crear planillas de cálculos.""")
    respuesta=int(input(""))
    if respuesta == 2:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 5: ¿Qué es una memoria RAM?")
    print("""\n1- Es la memoria flash de un dispositivo.
    \n2- Es la memoria secundaria de un dispositivo, se almacenan de forma permanente.
    \n3- Es la memoria principal de un dispositivo, se almacenan de forma temporal los programas que se utilizan.""")
    respuesta=int(input(""))
    if respuesta == 3:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\n¡Gracias por participar {0}!".format(nombre))
    print("\nCantidad de respuestas correctas: {0} , incorrectas: {1}".format(respuesta_correcta, respuesta_incorrecta)) 
#Función donde se encuentran cargadas las preguntas del nivel dificil
def nivel_dificil(nombre):
    respuesta=int(0)
    respuesta_correcta=int(0)
    respuesta_incorrecta=int(0)
    print("**Dificil**")
    print("\nPregunta 1: ¿Qué es una variable?")
    print("""\n1- Son espacios reservados en la memoria que pueden cambiar de contenido a lo largo de la ejecución de un programa.
    \n2- Es un archivo ejecutable.
    \n3- Son espacios reservados en la memoria que no pueden cambiar de contenido a lo largo de la ejecución de un programa.""")
    respuesta=int(input(""))
    if respuesta == 1:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 2: ¿Qué es una constante?")
    print("""\n1- Es un valor que se puede modificar a lo largo de la ejecución de un programa.
    \n2- Es una función dentro de un programa.
    \n3- Es un valor que no se puede alterar durante la ejecución de un programa, solo se puede leer.""")
    respuesta=int(input(""))
    if respuesta == 3:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 3: ¿Cuál es la sentencia para la toma de decisiones?")
    print("""\n1- IF
    \n2- WHILE
    \n3- FOR""")
    respuesta=int(input(""))
    if respuesta == 1:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 4: ¿Cuáles son las sentencias que se usan para realizar acciones repetitivas?")
    print("""\n1- FOR y WHILE.
    \n2- IF y WHILE.
    \n3- IF y ELSE.""")
    respuesta=int(input(""))
    if respuesta == 1:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\nPregunta 5: ¿Qué son las funciones en programación?")
    print("""\n1- Es un diccionario. 
    \n2- Es una variable donde se guarda todo tipo de datos.
    \n3- Es una sección de un programa que calcula un valor de manera independiente al resto del programa.""")
    respuesta=int(input(""))
    if respuesta == 3:
        respuesta_correcta+=1
    else:
        respuesta_incorrecta+=1
    print("\n¡Gracias por participar {0}!".format(nombre))
    print("\nCantidad de respuestas correctas: {0} , incorrectas: {1}".format(respuesta_correcta, respuesta_incorrecta)) 
#Función para mostrar el inicio del programa
def mostrar_inicio():
    print("""✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩
            \n¡Bienvenidos a mi juego de preguntados!
            \n✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩""")
    print("\nIngrese cualquier tecla para comenzar a jugar")
    input()

#Cuerpo del programa
mostrar_inicio()
#Solicitamos en pantalla el nombre del jugador:
nombre_jugador=input("Ingrese nombre: ")
#Validaciones:
while not nombre_jugador.isalpha():
    print ("Error, ingrese dato válido")
    nombre_jugador=input("Ingrese nombre: ")
#El ciclo repetitivo para seguir jugando hasta que alguien presione la opción 4(salida)
while seleccion!=False:
    print("\nIngrese dificultad elegida: ")
    print("1-Principiante")
    print("2-Intermedio")
    print("3-Dificil")
    print("4-Salir")
    print(" ")
    seleccion_nivel=int(input(""))
    while seleccion_nivel<1 or seleccion_nivel>4:
        print ("Error, Ingrese valor correcto")
        seleccion_nivel=int(input(""))
    if seleccion_nivel== 1:
        nivel_principiante(nombre_jugador)
    elif seleccion_nivel== 2:
        nivel_intermedio(nombre_jugador)
    elif seleccion_nivel==3:
        nivel_dificil(nombre_jugador)
    elif seleccion_nivel==4:
        seleccion=False

        
    
