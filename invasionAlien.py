import pygame
from settings import Config
from nave import Nave
import functionsGame as functGame


def startGame():
    # Iniciar el juego y crear un objeto pantalla
    pygame.init()

    aiSettings = Config()

    screen = pygame.display.set_mode(
        (aiSettings.screen_width, aiSettings.screen_height))
    pygame.display.set_caption("INVASIÓN ALIEN")

    # Crear nueva nave
    nave = Nave(aiSettings, screen)

    # Iniciar el bloque principal de deteccion de eventos
    while True:

        # Detector de evento "QUIT" para salir del juego
        functGame.lookEvent(nave)

        # Actualizar posicion de la pantalla
        nave.update()

       # Establecer config de fondo, nave, y pantalla
        functGame.updateScreen(aiSettings, screen, nave)


startGame()
