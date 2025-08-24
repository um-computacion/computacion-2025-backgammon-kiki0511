class Checker:
    """
    Una ficha del juego de Backgammon.
    Cada ficha pertenece a un jugador.
    """
    
    def __init__(self, owner):
        self.owner = owner
    
    def get_owner(self):
        return self.owner
    
    def __str__(self):
        return f"Ficha del jugador {self.owner}"
