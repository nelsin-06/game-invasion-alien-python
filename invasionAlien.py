from turtle import clear
import pygame
from pygame.sprite import Group
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

    # Se crea un grupo para almacenar las balas 
    grupoDeBalas = Group()

    # Se crea un nuevo grupo de aliens, una flota de aliens
    grupoDeAliens = Group()

    # Crear flota de aliens
    functGame.createdAliens(aiSettings, screen, nave,grupoDeAliens)

    # Iniciar el bloque principal de deteccion de eventos
    while True:

        # Detector de evento "QUIT" para salir del juego
        functGame.lookEvent(aiSettings, screen, nave, grupoDeBalas)

        # Actualizar posicion de la pantalla
        nave.update()
        functGame.updateBalas(grupoDeBalas)

        # Actualizar posicion de los alines
        functGame.updateAliens(aiSettings, grupoDeAliens)

        # Establecer config de fondo, nave, y pantalla
        functGame.updateScreen(aiSettings, screen, nave, grupoDeAliens, grupoDeBalas)


startGame()
