# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 17:49:26 2025

@author: repau
"""
print("BIENVENIDOS AL MEJOR JUEGO DE PIEDRA, PAPEL O TIJERA")   #Mensaje inicial
c = 1   #Variable para controlar la selección aleatoria de la computadora
modo = input("Selecciona contra quién deseas jugar (1)Humano o (2)Computadora: ")   #Seleccion de oponente

while True: #Iniciamos un bucle infinito hasta que exista un ganador
    a = int(input("Jugador 1, por favor selecciona (1) Piedra, (2) Papel o (3) Tijera): "))
    b = int(input("Jugador 2, por favor selecciona (1) Piedra, (2) Papel o (3) Tijera): ")) if modo == "1" else c
    c = 1 if c == 3 else c + 1
    print("Tu oponente eligió: ",b)
    if a == b:  #Logica del juego
        print("EMPATE, vuelve a intentarlo.\n")
        continue
    if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        print("¡GANASTE!")
    else:
        print("¡PERDISTE!")
    break    #Fin del bucle infinito
print("GRACIAS POR JUGAR")  #Mensaje final