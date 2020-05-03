import pygame, sys
import numpy as np
import matplotlib.pyplot as plt
import time

pygame.init()  # inicializo pygame

tamanio = anchoW, altoH = 1000, 1000

ncellX = 75
ncellY = 75

dimcW = (anchoW - 1) / ncellX
dimcH = (altoH - 1) / ncellY

black = 30, 30, 30
white = 128, 128, 128

pantalla = pygame.display.set_mode(tamanio)  # creamos la pantalla

# stateGame = np.random.randint(0, 2, (ncellX, ncellY))  # puntos aleatorios
stateGame = np.zeros((ncellX, ncellY))

stateGame[20, 20] = 1
stateGame[20, 22] = 1
stateGame[21, 21] = 1
stateGame[21, 22] = 1
stateGame[22, 21] = 1

#stateGame[5, 5] = 1
#stateGame[5, 7] = 1
#stateGame[6, 6] = 1
#stateGame[6, 7] = 1
#stateGame[7, 6] = 1

#stateGame[45, 45] = 1
#stateGame[45, 47] = 1
#stateGame[45, 46] = 1

stateGame[6, 6] = 1
stateGame[9, 7] = 1
stateGame[6, 5] = 1
stateGame[6, 6] = 1
stateGame[7, 9] = 1

juego = True
pause = False

while juego:

    n_stateGame = np.copy(stateGame)
    pantalla.fill(black)  # color de fondo
    time.sleep(0.1)

    ev = pygame.event.get()  # eventos

    for event in ev:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
        mouseClick = pygame.mouse.get_pressed()
        print(mouseClick)

        if sum(mouseClick) > 0:
            posx, posy = pygame.mouse.get_pos()
            celx, cely = int(np.floor(posx/dimcW)), int(np.floor(posy/dimcH))
            n_stateGame[celx, cely] = 1

    for y in range(0, ncellY):
        for x in range(0, ncellX):

            if not pause:

                # seleccion de los vecinos
                n_vecinos = stateGame[(x - 1) % ncellX, (y - 1) % ncellY] + \
                            stateGame[x % ncellX, (y - 1) % ncellY] + \
                            stateGame[(x + 1) % ncellX, (y - 1) % ncellY] + \
                            stateGame[(x - 1) % ncellX, y % ncellY] + \
                            stateGame[(x + 1) % ncellX, y % ncellY] + \
                            stateGame[(x - 1) % ncellX, (y + 1) % ncellY] + \
                            stateGame[x % ncellX, (y + 1) % ncellY] + \
                            stateGame[(x + 1) % ncellX, (y + 1) % ncellY]

                # condiciones del juego de la vida
                # está viva en la posición actual y tiene 2 o 3 celdas vecinas vivas;
                # está vacía en la posición actual y tiene exactamente 3 celdas vecinas vivas.

                if stateGame[x, y] == 0 and n_vecinos == 3:
                    n_stateGame[x, y] = 1
                elif stateGame[x, y] == 1 and (n_vecinos > 3 or n_vecinos < 2):
                    n_stateGame[x, y] = 0

            # se definen los puntos para rellenar la matriz
            poly = [(x * dimcW, y * dimcH),
                    ((x + 1) * dimcW, y * dimcH),
                    ((x + 1) * dimcW, (y + 1) * dimcH),
                    (x * dimcW, (y + 1) * dimcH)]

            # pygame.draw.polygon(pantalla, white, poly, int(abs(1 - n_stateGame[x, y])))  # se dibuja el rect en pantalla, color, posicion, borde
            if n_stateGame[x, y] == 0:
                pygame.draw.polygon(pantalla, white, poly, 1)
            else:
                pygame.draw.polygon(pantalla, (255, 255, 255), poly, 0)

    #  stateGame = n_stateGame
    stateGame = np.copy(n_stateGame)

    # rect = pygame.rect.Rect(0, 0, 10, 10)  # se define la pisicion del rectangulo a definir

    pygame.display.flip()  # mostrar pantalla

    for event in pygame.event.get():  # se crea el evento de cierre
        if event.type == pygame.QUIT:
            juego = False
