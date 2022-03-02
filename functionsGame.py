import sys

import pygame

def lookEvent(nave):
    """Detecta pulsaciones de teclas y el raton"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    nave.rect.centerx += 1

def updateScreen(aiSettings, screen, nave):
    # Estableciendo el color de fondo
    screen.fill(aiSettings.BG_color)
    nave.blitme()

    #Hacer visible la pantalla mas reciente
    pygame.display.flip()
