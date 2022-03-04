from turtle import screensize
import pygame.font

class Marcador():
    """Destinada a toda la info de puntuacion/score"""
    def __init__(self, aiSettings, screen, estadisticas):
        """Iniciando atributos de puntaje"""

        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.aiSettings = aiSettings
        self.estadisticas = estadisticas

        # ajusts de fuente para mostrar la puntuacion
        self.textColor = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara la imagen del puntaje inicial
        self.prepMsg()

    def prepMsg(self):
        """Renderiza el marcador en una imagen visible para la pantalla"""
        stringScore = str(self.estadisticas.score)
        self.scoreImagen = self.font.render(stringScore, True, self.textColor, self.aiSettings.BG_color)

        # Mostrar el puntaje en la esquina superior derecha de la pantalla
        self.scoreRect = self.scoreImagen.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def drawScore(self):
        """Dibuja la puntuacion en la pantalla"""
        self.screen.blit(self.scoreImagen, self.scoreRect)