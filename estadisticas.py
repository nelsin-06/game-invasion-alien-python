class Estadisticas():
    """Seguimiento de las estadisticas del juego"""
    def __init__(self, aiSettings):
        """Inicializa las estadisticas"""

        self.aiSettings = aiSettings
        self.resetStats() # Se llama a la funcion resetStats para que cada vez que se instancie la clase se reinicien las estadisticas del juego

        # Estado del juego segun sus vidas disponibles
        self.statusGame = False

    def resetStats(self):
        """Inicializa las estadisticas del juego"""
        self.remainingShips = self.aiSettings.numberNaves # Se establece las vidas del juego de la nave.


