import sys

import pygame

def eventKeyDown(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.movingRigth = True
    elif event.key == pygame.K_LEFT:
        nave.movingLeft = True


def eventKeyUp(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.movingRigth = False
    elif event.key == pygame.K_LEFT:
        nave.movingLeft = False


def lookEvent(nave):
    """Detecta pulsaciones de teclas y el raton"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            eventKeyDown(event, nave)

        elif event.type == pygame.KEYUP:
            eventKeyUp(event, nave)


def updateScreen(aiSettings, screen, nave):
    # Estableciendo el color de fondo
    screen.fill(aiSettings.BG_color)
    nave.blitme()

    # Hacer visible la pantalla mas reciente
    pygame.display.flip()
