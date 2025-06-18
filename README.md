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
