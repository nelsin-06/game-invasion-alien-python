from distutils.command.config import config
from pickle import TRUE
import pygame

class Nave ():
    def __init__(self, config, screen):
        
        self.screen = screen
        self.config = config

        # Cargar imagen y obtener su rect
        self.imagen = pygame.image.load("img/nave.bmp") # Cargamos y referenciamos la imagen a la variable imagen.
        self.rect = self.imagen.get_rect() # Obtenemos y asignamos la forma rectacgular a la imagen y lo asignamos a la variable rect
        self.screenRect = screen.get_rect() # Obtenemos y asignamos la forma rectangular 

        # Posicionar la nave en la parte central de la pantalla
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        # Almacenar el valor central como decimal para su facil y controlada modificacion
        self.centerDecimal = float(self.rect.centerx)

        # Bandera de movimiento
        self.movingRigth = False
        self.movingLeft = False

    def blitme(self):
        self.screen.blit(self.imagen, self.rect)

    def update(self):
        """Actualizando la posicion de la nave segun la bandera de movimiento"""
        if self.movingRigth == True:
            self.centerDecimal += self.config.velocidadNave

        if self.movingLeft == True:
            self.centerDecimal -= self.config.velocidadNave

        self.rect.centerx = self.centerDecimal