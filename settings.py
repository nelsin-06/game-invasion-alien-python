# Clase destinada para establecer las configuraciones del juego (Dimenciones, color)
class Config():
    def __init__(self):

        # Config inicio de juego
        self.screen_width = 990
        self.screen_height = 690
        self.BG_color = (153, 152, 245)

        # Config nave
        
        self.numberNaves = 3

        # Configuraciones de balas de nave
        
        self.bala_width = 3
        self.bala_heigth = 15
        self.balaColor = 60, 60, 60
        self.balasAllowed = 3

        # Config aliens
        
        self.fleetDropSpeed = 10

        # Escala aceleracion de los aliens
        self.escalaAceleracion = 1.1

        # escala del valor de los aliens dependiendo de que tan lejos hayan llegado al juego
        self.escalaPuntaje = 1.5

        # Se restablecen/inicializan las configuraciones dinamicas del juego
        self.setDefaultConfigDinamic()

    def setDefaultConfigDinamic(self):
        self.velocidadNave = 1.5
        self.velocidadBala = 1
        self.velocidadAlien = 1
        # fleet direcction si es 1 se mueve a la derecha; si es -1 se mueve hacia la izquierda
        self.fleetDirecion = 1
        # Score
        self.valueAlien = 5

    def increaseSpeedGame(self):
        """Aumenta las velocidades del juego"""
        self.velocidadNave *= self.escalaAceleracion
        self.velocidadBala *= self.escalaAceleracion
        self.velocidadAlien *= self.escalaAceleracion
        
        self.valueAlien = int(self.valueAlien * self.escalaPuntaje)