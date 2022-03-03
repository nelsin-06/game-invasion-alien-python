# Clase destinada para establecer las configuraciones del juego (Dimenciones, color)
class Config():
    def __init__(self):

        # Config inicio de juego
        self.screen_width = 800
        self.screen_height = 600
        self.BG_color = (153, 152, 245)

        # Config nave
        self.velocidadNave = 1.5

        # Configuraciones de balas de nave
        self.velocidadBala = 1
        self.bala_width = 3
        self.bala_heigth = 3
        self.balaColor = 60, 60, 60
        self.balasAllowed = 3