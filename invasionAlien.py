from turtle import clear
import pygame
from pygame.sprite import Group
from settings import Config
from nave import Nave
import functionsGame as functGame
from estadisticas import Estadisticas
from button import Button

def startGame():
    # Iniciar el juego y crear un objeto pantalla
    pygame.init()

    aiSettings = Config()

    screen = pygame.display.set_mode(
        (aiSettings.screen_width, aiSettings.screen_height))
    pygame.display.set_caption("INVASIÓN ALIEN")

    # Se crea el button de la clase button
    buttonPlay = Button(aiSettings, screen, "PLAY")

    # Se crea una instancia donde se almacenan las estadisticas del juego
    estadisticas = Estadisticas(aiSettings)

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

        if estadisticas.statusGame:
            # Actualizar posicion de la pantalla
            nave.update()
            functGame.updateBalas(aiSettings, screen, nave, grupoDeBalas, grupoDeAliens)

            # Actualizar posicion de los alines
            functGame.updateAliens(aiSettings, estadisticas, screen, nave, grupoDeAliens, grupoDeBalas)

        # Establecer config de fondo, nave, y pantalla
        functGame.updateScreen(aiSettings, screen, estadisticas, nave, grupoDeAliens, grupoDeBalas, buttonPlay)


startGame()
