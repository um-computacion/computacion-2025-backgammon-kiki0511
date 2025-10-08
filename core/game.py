from core.board import Board
from core.player import Player
from core.dice import Dice


class BackgammonGame:
    """
    Clase principal del juego de Backgammon.
    Maneja todo el flujo del juego y los turnos.
    """
    
    def __init__(self, nombre_jugador1, nombre_jugador2):
        """
        Inicializa un nuevo juego de Backgammon.
        
        Recibe:
            nombre_jugador1 (str): nombre del primer jugador
            nombre_jugador2 (str): nombre del segundo jugador
        Hace:
            crea el tablero, los jugadores y prepara el juego
        Devuelve:
            nada (es el constructor)
        """
        # creo el tablero del juego
        self.__tablero__ = Board()
        
        # creo el primer jugador (fichas blancas, direccion 1)
        self.__jugador1__ = Player(nombre_jugador1, 1)
        
        # creo el segundo jugador (fichas negras, direccion -1)  
        self.__jugador2__ = Player(nombre_jugador2, -1)
        
        # el jugador 1 empieza primero
        self.__jugador_actual__ = self.__jugador1__
        
        # creo los dados
        self.__dados__ = Dice()
        
        # lista vacia para guardar los movimientos disponibles
        self.__movimientos_disponibles__ = []
        
        # el juego no esta terminado al principio
        self.__juego_terminado__ = False
        
        # todavia no hay ganador
        self.__ganador__ = None
        
        # variable para saber si el turno paso automaticamente
        self.__turno_paso_automatico__ = False

    def get_tablero(self):
        """
        Obtiene el tablero del juego.
        
        Recibe:
            nada
        Hace:
            devuelve el tablero
        Devuelve:
            Board: el tablero actual del juego
        """
        return self.__tablero__
    
    def get_jugador_actual(self):
        """
        Obtiene el jugador que esta jugando ahora.
        
        Recibe:
            nada
        Hace:
            devuelve el jugador actual
        Devuelve:
            Player: el jugador actual
        """
        return self.__jugador_actual__
    
    def get_jugador1(self):
        """
        Obtiene el jugador 1.
        
        Recibe:
            nada
        Hace:
            devuelve el jugador 1
        Devuelve:
            Player: el primer jugador
        """
        return self.__jugador1__
    
    def get_jugador2(self):
        """
        Obtiene el jugador 2.
        
        Recibe:
            nada
        Hace:
            devuelve el jugador 2
        Devuelve:
            Player: el segundo jugador
        """
        return self.__jugador2__
    
    def get_dados(self):
        """
        Obtiene los dados del juego.
        
        Recibe:
            nada
        Hace:
            devuelve los dados
        Devuelve:
            Dice: los dados del juego
        """
        return self.__dados__
    
    def get_movimientos_disponibles(self):
        """
        Obtiene los movimientos disponibles.
        
        Recibe:
            nada
        Hace:
            devuelve la lista de movimientos
        Devuelve:
            list: lista con los valores de dados disponibles
        """
        return self.__movimientos_disponibles__
    
    def esta_terminado(self):
        """
        Verifica si el juego termino.
        
        Recibe:
            nada
        Hace:
            chequea si el juego esta terminado
        Devuelve:
            bool: True si termino, False si no
        """
        return self.__juego_terminado__
    
    def get_ganador(self):
        """
        Obtiene el ganador del juego.
        
        Recibe:
            nada
        Hace:
            devuelve el ganador si hay
        Devuelve:
            Player: el jugador ganador o None si no hay
        """
        return self.__ganador__
    
    def turno_paso_automaticamente(self):
        """
        Verifica si el turno paso automaticamente.
        
        Recibe:
            nada
        Hace:
            chequea si el turno paso solo
        Devuelve:
            bool: True si paso automaticamente
        """
        return self.__turno_paso_automatico__
    
    def get_color_jugador_actual(self):
        """
        Obtiene el color del jugador actual.
        
        Recibe:
            nada
        Hace:
            determina el color segun la direccion
        Devuelve:
            str: 'blanco' o 'negro'
        """
        # si la direccion es 1 es blanco, si no es negro
        if self.__jugador_actual__.get_direccion() == 1:
            color = 'blanco'
        else:
            color = 'negro'
        return color