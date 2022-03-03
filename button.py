import pygame.font

class Button():
    """Clase para botones"""
    def __init__(self, aiSettings, screen, msg):
        """Iniciar atributos de boton"""

        self.screen = screen
        self.screenRect = self.screen.get_rect()

        # Establecer propiedades y dimenciones del boton
        self.width, self.height = 200, 50
        self.buttonColor = (0, 255, 0)
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Contruye el objeto rect y lo centra
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center

        # Se crea el mensaje del boton el cual se prepara una sola vez
        self.prepMsg(msg)

    def prepMsg(self, msg):
        """Conviertiendo el texto en una imagen y la centra"""

        self.msgImage = self.font.render(msg, True, self.textColor, self.buttonColor)
        self.msgImagenRect = self.msgImage.get_rect()
        self.msgImagenRect.center = self.rect.center

    def drawButton(self):
        # Dibuja el boton en blaco y luego dibuja el mensa
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage, self.msgImagenRect)