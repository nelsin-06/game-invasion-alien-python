import pygame

class Nave ():
    def __init__(self, screen):
        self.screen = screen

        self.imagen = pygame.image.load("img/nave.bmp") # Cargamos y referenciamos la imagen a la variable imagen.
        self.rect = self.imagen.get_rect() # Obtenemos y asignamos la forma rectacgular a la imagen y lo asignamos a la variable rect
        self.screenRect = screen.get_rect() # Obtenemos y asignamos la forma rectangular 

        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

    def blitme(self):
        self.screen.blit(self.imagen, self.rect)