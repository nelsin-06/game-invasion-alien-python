from distutils.command.config import config
import sys
from zoneinfo import available_timezones

import pygame

from bala import Bala

from alien import Alien


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


def updateScreen(aiSettings, screen, nave, grupoAliens, grupoBalas):
    # Estableciendo el color de fondo
    screen.fill(aiSettings.BG_color)

    # Vuelve a dibujar todas la balas detras de la nave y de los extraterrestres
    # Con sprites se obtiene toda la lista de las balas en el grupo que se paso en el archivo principal
    for balaDelGrupo in grupoBalas.sprites():
        balaDelGrupo.drawBala()
    nave.blitme()
    grupoAliens.draw(screen)

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

# Funcion auxiliar obtener el ancho de un alien
def getAliensInX(aiSettings, alienWidth):
    """Determina el numero de espacio disponibles para crear aliens en cada fila"""
    availableSpaceBeteewAliens = aiSettings.screen_width - 2 * alienWidth
    numbersAliensInX = int(availableSpaceBeteewAliens / (2 * alienWidth))
    return numbersAliensInX

def getNumberRows(aiSettings, naveHeidth, alienHeidth):
    """Determina el numero de filas de aliens que se ajustan en la pantala"""
    availableSpaceInY = (aiSettings.screen_height - (3 * alienHeidth) - naveHeidth)
    numberRows = int(availableSpaceInY / (2 * alienHeidth))
    return numberRows

# Funcion auxiliar para el metodo createdAliens (Toda una flota)
def createAlien(aiSettings, screen, grupoDeAliens, numberAlien, rowNumber):
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2 * alienWidth * numberAlien
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    grupoDeAliens.add(alien)


def createdAliens(aiSettings, screen, nave, grupoDeAliens):
    """Crear una flota completa de alienigenas"""
    # Crear un alien y encontrar la cantidad de aliens posibles
    # El espacio entre cada alien es igual al ancho de un alien
    alien = Alien(aiSettings, screen)
    numberAliensInX = getAliensInX(aiSettings, alien.rect.width)
    rowNumber = getNumberRows(aiSettings, nave.rect.height, alien.rect.height)

    # Creando la flota de aliens
    
    for rowNumber in range(rowNumber):
        for numberAlien in range(numberAliensInX):
            # Crea un alien y lo coloca en la fila
            createAlien(aiSettings, screen, grupoDeAliens, numberAlien, rowNumber)

def checkFleetEdges(aiSettings, grupoDeAliens):
    """Responder de forma apropiada si el alien llega a algun borde"""
    for alien in grupoDeAliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(aiSettings, grupoDeAliens)
            break

def changeFleetDirection(aiSettings, grupoDeAliens):
    """Cambia la direccion y deciende un espacio todas las naves"""
    for alien in grupoDeAliens:
        alien.rect.y += aiSettings.fleetDropSpeed
        aiSettings.fleetDirecion *= -1

def updateAliens(aiSettings ,grupoDeAliens):
    """Comprueba si alguna de las naves toca los bordes, actualiza su direccion y baja un espacion para estar cerca al piso"""
    checkFleetEdges(aiSettings, grupoDeAliens)
    grupoDeAliens.update()
