import sys
from time import sleep

import pygame

from bala import Bala

from alien import Alien
from estadisticas import Estadisticas


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


def updateScreen(aiSettings, screen, estadisticas, nave, grupoAliens, grupoBalas, buttonPlay):
    # Estableciendo el color de fondo
    screen.fill(aiSettings.BG_color)

    # Vuelve a dibujar todas la balas detras de la nave y de los extraterrestres
    # Con sprites se obtiene toda la lista de las balas en el grupo que se paso en el archivo principal
    for balaDelGrupo in grupoBalas.sprites():
        balaDelGrupo.drawBala()
    nave.blitme()
    grupoAliens.draw(screen)

    # Dibuja el juego mientras este inactivo
    if not estadisticas.statusGame:
        buttonPlay.drawButton()

    # Hacer visible la pantalla mas reciente
    pygame.display.flip()


def updateBalas(aiSettings, screen, nave, grupoBalas, grupoDeAliens):
    """Actualiza la posicion de las nuevas balas y elimina las antiguas"""

    # Actualizar posicion de las balas
    grupoBalas.update()

    # Deshacer las balas que han desaparecido
    for bala in grupoBalas.copy():
        if bala.rect.bottom <= 0:
            grupoBalas.remove(bala)
    checkBalasAliensCollision(aiSettings, screen, nave,
                              grupoBalas, grupoDeAliens)


def checkBalasAliensCollision(aiSettings, screen, nave, grupoBalas, grupoDeAliens):
    # Comprobar si existen balas que hayan alcanzado a los aliens, si es asi se desaparecen ambos objetos
    collisions = pygame.sprite.groupcollide(
        grupoBalas, grupoDeAliens, True, True)
    if len(grupoDeAliens) == 0:
        # Destruye las balas existentes y crear una nueva flota
        grupoBalas.empty()
        createdAliens(aiSettings, screen, nave, grupoDeAliens)


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
    availableSpaceInY = (aiSettings.screen_height -
                         (3 * alienHeidth) - naveHeidth)
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
            createAlien(aiSettings, screen, grupoDeAliens,
                        numberAlien, rowNumber)


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


def naveHit(aiSettings, estadisticas, screen, nave, grupoDeAliens, grupoDeBalas):
    """Reacciona la nave siendo golpeada por un ovni/alien"""
    
    if estadisticas.remainingShips > 0:
        # Disminuye la cantidad de vidas de la nave
        estadisticas.remainingShips -= 1

        # Limpia grupos de balas y naves para efecto reinicio
        grupoDeBalas.empty()
        grupoDeAliens.empty()


        # Crear una nueva flota de aliens y centrar la nave
        createdAliens(aiSettings, screen, nave, grupoDeAliens)
        nave.centerNave()

        # pausa para efecto
        sleep(0.5)
    else:
        estadisticas.statusGame = False

def checkAlienBottom(aiSettings, estadisticas, screen, nave, grupoDeAliens, grupoDeBalas):
    """COomprobar si los alines llegaron al limite de abajo de la pantalla"""
    screenRect = screen.get_rect()

    for alien in grupoDeAliens.sprites():
        if alien.rect.bottom == screenRect.bottom:
            # Se maneja de la misma forma que si los aliens tocan la nave
            naveHit(aiSettings, estadisticas, screen, nave, grupoDeAliens, grupoDeBalas)
            break

def updateAliens(aiSettings, estadisticas, screen, nave, grupoDeAliens, grupoDeBalas):
    """Comprueba si alguna de las naves toca los bordes, actualiza su direccion y baja un espacion para estar cerca al piso"""
    checkFleetEdges(aiSettings, grupoDeAliens)
    grupoDeAliens.update()

    # Buscar colisiones entre los aliens y la nave
    if pygame.sprite.spritecollideany(nave, grupoDeAliens):
        naveHit(aiSettings, estadisticas, screen, nave, grupoDeAliens, grupoDeBalas)
    
    # Detectando si algun alien toco el fondo de la pantalla
    checkAlienBottom(aiSettings, estadisticas, screen, nave, grupoDeAliens, grupoDeBalas)
