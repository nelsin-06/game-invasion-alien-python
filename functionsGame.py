import sys

import pygame

from bala import Bala


def eventKeyDown(event, aiSettings, screen, nave, grupoBalas):
    if event.key == pygame.K_RIGHT:
        nave.movingRigth = True
    elif event.key == pygame.K_LEFT:
        nave.movingLeft = True
    elif event.key == pygame.K_SPACE:
        # Crea una nueva bala y la agrega al grupo del balas
        nuevaBala = Bala(aiSettings, screen, nave)
        grupoBalas.add(nuevaBala)


def eventKeyUp(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.movingRigth = False
    elif event.key == pygame.K_LEFT:
        nave.movingLeft = False


def lookEvent(aiSettings, screen, nave, grupoBalas):
    """Detecta pulsaciones de teclas y el raton"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            eventKeyDown(event, aiSettings, screen, nave, grupoBalas)

        elif event.type == pygame.KEYUP:
            eventKeyUp(event, nave)


def updateScreen(aiSettings, screen, nave, grupoBalas):
    # Estableciendo el color de fondo
    screen.fill(aiSettings.BG_color)
    
    # Vuelve a dibujar todas la balas detras de la nave y de los extraterrestres
    for balaDelGrupo in grupoBalas.sprites(): # Con sprites se obtiene toda la lista de las balas en el grupo que se paso en el archivo principal
        balaDelGrupo.drawBala()
    nave.blitme()

    # Hacer visible la pantalla mas reciente
    pygame.display.flip()
