import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Clase dedicada a manejar las balas por la nave"""
    def __init__(self, config, screen, nave):
        super(Bala, self).__init__() # El super es para heredar los atributos y metodos de la clase Sprite
        self.screen = screen

        # Crear y establecer las posiciones correctas de una nave.
        self.rect = pygame.Rect(0,0, config.bala_width, config.bala_heigth) # Como la bala no tiene imagen se contruye un rect desde 0
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        # Almacenar la posciion de la bala como un valor decimal
        self.y = float(self.rect.y)

        # Configuracion de la bala
        self.color = config.balaColor
        self.velocidadBala = config.velocidadBala

    def update(self):
        """Moviendo la bala hacia arriba en la pantalla"""
        # Actualizar la posicion de la bala segun su trayectoriaa
        self.y -= self.velocidadBala

        # Actualizando la posicion del rect (bala)
        self.rect.y = self.y

    def drawBala(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)