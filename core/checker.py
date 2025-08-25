class Checker:
    """
    La clse representa Una ficha del juego.
    Cada ficha pertenece a un jugador (guarda el dueño).
    estas fichas 
    """
    
    def __init__(self, owner):
        # dueño de la ficha (un jugador)
        self.owner = owner
    
     # Devuelve el jugador dueño de la ficha
    def get_owner(self):
        return self.owner
    
      # Convierte la ficha a texto para mostrar en pantalla
    def __str__(self):
        return f"Ficha del jugador {self.owner.get_nombre()}"