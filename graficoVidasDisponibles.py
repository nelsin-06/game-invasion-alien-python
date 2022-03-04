import pygame
from pygame.sprite import Sprite

class Grafico (Sprite):
    def __init__(self, config, screen):
        super(Grafico, self).__init__()
        self.screen = screen
        self.config = config

        # Cargar imagen y obtener su rect
        self.image = pygame.image.load("img/corazon.bmp") # Cargamos y referenciamos la imagen a la variable imagen.
        self.rect = self.image.get_rect() # Obtenemos y asignamos la forma rectacgular a la imagen y lo asignamos a la variable rect
        self.screenRect = screen.get_rect() # Obtenemos y asignamos la forma rectangular 
