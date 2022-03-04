import pygame.font
from pygame.sprite import Group

from graficoVidasDisponibles import Grafico

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
        self.fontLevel = pygame.font.SysFont(None, 20)
        self.fontRecord = pygame.font.SysFont(None, 30)

        # Prepara la imagen del puntaje inicial y la maxima
        self.prepMsg()
        self.prepScoreMax()
        self.prepLevel()
        self.prepNave()

    def prepLevel(self):
        """Renderiza el nivel del juego"""
        self.levelImage = self.fontLevel.render("Level " + str(self.estadisticas.level), True, self.textColor, self.aiSettings.BG_color)

        # Mostrar el puntaje en la esquina superior derecha de la pantalla
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.screenRect.right - 20
        self.levelRect.top = self.levelRect.bottom + 50

    def prepScoreMax(self):
        """Renderiza la maxima puntuacion"""
        scoreMax = int(round(self.estadisticas.score, -1))
        stringScoreMax = "{:,}".format(scoreMax)
        self.scoreImagenMax = self.fontRecord.render("Record " + stringScoreMax, True, self.textColor, self.aiSettings.BG_color)

        # Mostrar el puntaje en la esquina superior derecha de la pantalla
        self.scoreRectMax = self.scoreImagenMax.get_rect()
        self.scoreRectMax.centerx = self.screenRect.centerx
        self.scoreRectMax.top = self.scoreRect.top

    def prepMsg(self):
        """Renderiza el marcador en una imagen visible para la pantalla"""
        scoreRound = int(round(self.estadisticas.score, -1))
        stringScore = "{:,}".format(scoreRound)
        self.scoreImagen = self.font.render(stringScore, True, self.textColor, self.aiSettings.BG_color)

        # Mostrar el puntaje en la esquina superior derecha de la pantalla
        self.scoreRect = self.scoreImagen.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def prepNave(self):
        self.grupoDeVidas = Group()
        for numeroNaves in range(self.estadisticas.remainingShips):
            graficoVidas = Grafico(self.aiSettings, self.screen)
            graficoVidas.rect.x = 10 + numeroNaves * graficoVidas.rect.width
            graficoVidas.rect.y = 10
            self.grupoDeVidas.add(graficoVidas)

    def drawScore(self):
        """Dibuja la puntuacion en la pantalla"""
        self.screen.blit(self.scoreImagen, self.scoreRect)
        self.screen.blit(self.scoreImagenMax, self.scoreRectMax)
        self.screen.blit(self.levelImage, self.levelRect)
        self.grupoDeVidas.draw(self.screen)