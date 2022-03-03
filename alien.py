import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Su funcion es representar un objeto Alien en la flota"""
    def __init__(self, aiSettings, screen):
        """Inicializa el alien y establece su posicion"""
        super(Alien, self).__init__()

        self.screen = screen
        self.aiSettings = aiSettings

        # Cargar la imagen y establece su posicion inicial y rect
        self.image = pygame.image.load("img/ovni.bmp") # Cargamos y referenciamos la imagen al atributo imagen.
        self.rect = self.image.get_rect() # Obtenemos y asignamos la forma rectacgular a la imagen y lo asignamos a la variable rect

        # Iniciamos el nuevo alien cerca a la parte superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenando la posicion del ovni en numero decimal
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibujar alien en su posicion actual"""
        self.screen.blit(self.image, self.rect)

    def checkEdges(self):
        """Devuelve verdadero si el alien llega al borde de la pantalla"""
        screenRect = self.screen.get_rect() # Se establece valores rect de la pantalla
        if self.rect.right >= screenRect.right: # Se declara. Si el valor de la nave ovni en su posicion derecha llega a ser igual o mayo a la posicion derecha de la pantalla return true
            return True
        elif self.rect.left <= 0: # Se declara. Si el valor de las naves ovni llega a tocar al posicion 0 retorna true
            return True

    def update(self):
        """Mueve el alien a la derecha"""
        self.x += (self.aiSettings.velocidadAlien * self.aiSettings.fleetDirecion)
        self.rect.x = self.x