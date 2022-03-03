import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Su funcion es representar un objeto Alien en la flota"""
    def __init__(self, iaSettings, screen):
        """Inicializa el alien y establece su posicion"""
        super(Alien, self).__init__()

        self.screen = screen
        self.iaSettings = iaSettings

        # Cargar la imagen y establece su posicion inicial y rect
        self.imagen = pygame.image.load("img/ovni.bmp") # Cargamos y referenciamos la imagen al atributo imagen.
        self.rect = self.imagen.get_rect() # Obtenemos y asignamos la forma rectacgular a la imagen y lo asignamos a la variable rect

        # Iniciamos el nuevo alien cerca a la parte superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenando la posicion del ovni en numero decimal
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibujar alien en su posicion actual"""
        self.screen.blit(self.imagen, self.rect)