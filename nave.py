import pygame
from pygame.sprite import Sprite

class Nave (Sprite):
    def __init__(self, config, screen):
        super(Nave, self).__init__()
        self.screen = screen
        self.config = config

        # Cargar imagen y obtener su rect
        self.image = pygame.image.load("img/nave-espacial.bmp") # Cargamos y referenciamos la imagen a la variable imagen.
        self.rect = self.image.get_rect() # Obtenemos y asignamos la forma rectacgular a la imagen y lo asignamos a la variable rect
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
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Actualizando la posicion de la nave segun la bandera de movimiento"""
        if self.movingRigth == True and self.rect.right < self.screenRect.right:
            self.centerDecimal += self.config.velocidadNave

        if self.movingLeft == True and self.rect.left > self.screenRect.left:
            self.centerDecimal -= self.config.velocidadNave

        self.rect.centerx = self.centerDecimal

    def centerNave(self):
        """Centrar la nave en la pantalla"""
        self.center = self.screenRect.centerx
        self.rect.centerx = self.center
