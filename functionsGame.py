from distutils.command.config import config
import sys

import pygame

from bala import Bala


def eventKeyDown(event, aiSettings, screen, nave, grupoBalas):
    if event.key == pygame.K_RIGHT:
        nave.movingRigth = True
    elif event.key == pygame.K_LEFT:
        nave.movingLeft = True
    elif event.key == pygame.K_SPACE:
        shotingBullet(aiSettings, screen, nave, grupoBalas)
    elif event.key == pygame.K_q:
        sys.exit()

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
    # Con sprites se obtiene toda la lista de las balas en el grupo que se paso en el archivo principal
    for balaDelGrupo in grupoBalas.sprites():
        balaDelGrupo.drawBala()
    nave.blitme()

    # Hacer visible la pantalla mas reciente
    pygame.display.flip()


def updateBalas(grupoBalas):
    """Actualiza la posicion de las nuevas balas y elimina las antiguas"""

    # Actualizar posicion de las balas
    grupoBalas.update()

    # Deshacer las balas que han desaparecido
    for bala in grupoBalas.copy():
        if bala.rect.bottom <= 0:
            grupoBalas.remove(bala)

def shotingBullet(aiSettings, screen, nave, grupoBalas):
    # Crea una nueva bala y la agrega al grupo del balas ///////////////////
    # Si la longitud del grupo de balas es menor a las balas establecidas se puede dispara
    if len(grupoBalas) < aiSettings.balasAllowed:
        nuevaBala = Bala(aiSettings, screen, nave)
        grupoBalas.add(nuevaBala)