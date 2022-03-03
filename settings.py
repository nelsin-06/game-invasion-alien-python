# Clase destinada para establecer las configuraciones del juego (Dimenciones, color)
class Config():
    def __init__(self):

        # Config inicio de juego
        self.screen_width = 800
        self.screen_height = 600
        self.BG_color = (153, 152, 245)

        # Config nave
        self.velocidadNave = 1.5
        self.numberNaves = 3

        # Configuraciones de balas de nave
        self.velocidadBala = 1
        self.bala_width = 3
        self.bala_heigth = 15
        self.balaColor = 60, 60, 60
        self.balasAllowed = 3

        # Config aliens
        self.velocidadAlien = 1
        self.fleetDropSpeed = 10

        # fleet direcction si es 1 se mueve a la derecha; si es -1 se mueve hacia la izquierda
        self.fleetDirecion = 1