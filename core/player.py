## Módulo Player: estado de un jugador.
    
"""Representa a un jugador en el juego de Backgammon.
    
    Cada jugador tiene:
    - Un nombre
    - Una dirección de movimiento (hacia donde mueve sus fichas)
    - Fichas en la "barra" (fichas capturadas que debe volver a poner)
    - Fichas "sacadas" del tablero (fichas que ya terminaron el recorrido)
    """  
class Player:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.fichas_en_barra = 0
        self.fichas_sacadas = 0
    
     #Devuelve el nombre del jugador.
    def get_nombre(self): 
        return self.nombre
   
   ##Devuelve la dirección de movimiento del jugador.
   ##     1 = hacia la derecha, -1 = hacia la izquierda
    def get_direccion(self): 
        return self.direccion
    
    ##Devuelve cuántas fichas tiene el jugador en la barra.
    ##   (fichas capturadas que debe volver a meter al tablero)
    def get_fichas_en_barra(self): 
        return self.fichas_en_barra
    
    ##Devuelve cuántas fichas ha sacado del tablero.
    ##    (fichas que completaron todo el recorrido)
    def get_fichas_sacadas(self): 
        return self.fichas_sacadas
    
    ##Agrega una ficha a la barra (cuando le capturan una ficha)
    def agregar_ficha_a_barra(self): 
        self.fichas_en_barra += 1
    
    ##Quita una ficha de la barra
    def quitar_ficha_de_barra(self): 
        if self.fichas_en_barra > 0: 
            self.fichas_en_barra -= 1
    
    ##Saca una ficha del tablero (cuando completa el recorrido)
    def sacar_ficha_del_tablero(self): 
        self.fichas_sacadas += 1
    
    ##Verifica si el jugador tiene fichas en la barra.
     ##   Devuelve True si tiene fichas en la barra, False si no.
    def tiene_fichas_en_barra(self): 
        return self.fichas_en_barra > 0
    
    ##Verifica si el jugador ha ganado.
    ##    Un jugador gana cuando saca todas sus 15 fichas del tablero.
    def ha_ganado(self): 
        return self.fichas_sacadas == 15
    
    ## Convierte el jugador a texto para mostrarlo en pantalla.
        
    def __str__(self): 
        direccion_texto = "derecha" if self.direccion == 1 else "izquierda"
        return f"Jugador: {self.nombre} (mueve hacia {direccion_texto})"
