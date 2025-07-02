MODIFICACIONES AL TRABAJO AUTONOMO NUMERO 2
Tomando en cuenta las observaciones del trabajo presentado anteriormente, se procede a actulizar el trabajo de programacion del Juego de piedra, papel o tijera.

Para el desarrollo del mismo se ha utilizado el lenguaje de programacion Python version 3.13, con la consola de spyder version 6.0.

De igual manera se procedio a actualizar el diagrama de bloques, para que este acorde a la estructura del programa.

De acuerdo a las observaciones del trabajo anterior, se procedio a utilizar la libreria de random y funciones de entrada y salida, al igual que listas, estructuras de control y diccionarios.

A continuacion se explica como jugar nuestro juego de piedra, papel o tijera.

Como punto de partida tenemos un mensaje inicial.

Se despliega un menu principal, el mismo que consta de tres opciones que son 1. Jugar, 2. Reglas del Juego y 3. Salir

Si se elige la opcion numero 2, se desplegaran las reglas generales del juego. Una vez leida la información, con la tecla enter volvemos al menu principal.

Si se elige la opcion numero 3, se desplegara un mensaje final y abandonaremos el juego.

Ahora bien, si se elige la opcion numero 1, se desplegara un submenu que nos solicitara elegir a nuestro oponente, en este cas 1. contra la computadora y 2. contra un jugador humano.

Si dentro de este submenu se elige la opcion de oponente de la computadora, el programa nos solicitara que ingresemos nuestro nombre.

A continuación nos pedira ingresar la cantidad de rondas que jugaremos en la partida.

Inmediatamente nos solicitara ingresar nuestra selección entre piedra, papel o tijera.

La computadora elegira aleatoriamente entre piedra, papel o tijera.

Despues de cada ronda, el programa nos preguntara si deseamos seguir jugando, en caso de ingresar "si" pasaremos a la siguiente ronda hasta completar la partida total.

En caso de empate, la computadora nos preguntara si deseamos seguir juagnado la misma ronda hasta que alguno de los participantes gane, ya que en nuestra proyeccion de resultados solo registramos las rondas ganadas o perdidas. En caso de no volver a jugar la ronda de empate, pasaremos a la siguiente ronda y al finalizar nuestro numero de partidas solo se mostraran los resultados de las rondas ganadas y perdidas mas no las de empate.

Una vez finalizada la partida total, nos mostrara los resultados de todas las rondas y volveremos al menu principal, donde podemos salir ya del juego.

Ahora bien, si en nuestro submenu de elección de oponente, seleccionamos jugar contra un jugador humano, el programa nos solicitara ingresar el nombre del jugador numero 1, despues el nombre del jugador numero 2 y el numero de rondas a jugar.

Una vez que ya ingresamos nuestros nombres, se le pedira seleccionar entre piedra, papel o tijera primero al jugador numero 1 y despues al jugador numero 2.

Igual que en el proceso de jugar cotra la computadora, n caso de empate, se nos preguntara si deseamos seguir juagnado la misma ronda hasta que alguno de los participantes gane, ya que en nuestra proyeccion de resultados solo registramos las rondas ganadas o perdidas. En caso de no volver a jugar la ronda de empate, pasaremos a la siguiente ronda y al finalizar nuestro numero de partidas solo se mostraran los resultados de las rondas ganadas y perdidas mas no las de empate.

Al finalizar la partida, se desplegara los resultados de todas las rondas exceptuando los empates y volveremos al menu principal, donde podemos salir del programa.



# Autonomo2
Repositorio que contiene el desarrollo del trabajo autónomo 2 de la materia de lógica de programación, que consiste en desarrollar el juego de piedra, papel o tijera mediante python.

Mostramos un mensaje inicial mediante la funcion print

print("BIENVENIDOS AL MEJOR JUEGO DE PIEDRA, PAPEL O TIJERA")

Creamos la variable c para poder controlar la eleccion automatica de la computadora, donde 1 representa piedra y a medida que se requiere en forma ordenada a papel y por ultimo a tijera para simular un orden aleatorio de la selección

c = 1

Creamos la variable modo, la misma que me permite seleccionar contra quien se desea jugar

modo = input("Selecciona contra quién deseas jugar (1)Humano o (2)Computadora: ")

Iniciamos un bucle infinito con el comando while True que se repetira hasta que se declare un ganador

while True: #Iniciamos un bucle infinito hasta que exista un ganador

Se solicita al jugador numero 1 que ingrese su selección utilizando el comando int para usar un numero entero

    a = int(input("Jugador 1, por favor selecciona (1) Piedra, (2) Papel o (3) Tijera): "))
 
A contiuacion se utiliza el codigo if como operador para determinar la selección del jugador numero 2    
    
    b = int(input("Jugador 2, por favor selecciona (1) Piedra, (2) Papel o (3) Tijera): ")) if modo == "1" else c

Esta linea actualiza la jugada de la computadora dentro de la misma ronda
    
    c = 1 if c == 3 else c + 1

A continuacion se utiliza un print para mostrar la seleccion de la computadora si es el caso 

print("la computadora eligió: ",b)

Con la funcion if determinamos si la selección del jugador 1 es igual a la del jugador 2 o a la seleccion de la computadora, entonces declaramos un empate, y con el codigo continue reiniciamos el ciclo hasta que se declare un ganador
    
    if a == b:
        print("EMPATE, vuelve a intentarlo.\n")
        continue
    
Para determinar si ganamos, utilizamos el codigo if, con el cual vamos a comparar las jugadas logicas posibles
    
    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("¡GANASTE!")
    else:
        print("¡PERDISTE!")

Para detener el bucle iniciado anteriormente, utilizamos el siguiente codigo:
    
    break

Y mostramos un mensaje final:

print("GRACIAS POR JUGAR")
