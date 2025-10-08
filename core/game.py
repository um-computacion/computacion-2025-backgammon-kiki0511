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
def tirar_dados(self):
        """
        Tira los dados para el turno actual.
        
        Recibe:
            nada
        Hace:
            tira los dados y guarda los valores
        Devuelve:
            list: lista con los valores de los dados
        """
        # tiro los dados
        resultado = self.__dados__.tirar()
        
        # copio el resultado a movimientos disponibles
        # uso copy para no modificar el original
        self.__movimientos_disponibles__ = resultado.copy()
        
        return resultado
    
def puede_hacer_movimiento(self, punto_origen, valor_dado):
        """
        Verifica si un movimiento es valido.
        
        Recibe:
            punto_origen (int): punto desde donde mover
            valor_dado (int): valor del dado a usar
        Hace:
            chequea todas las reglas para ver si el movimiento es posible
        Devuelve:
            bool: True si puede hacer el movimiento, False si no
        """
        # primero verifico si el dado esta disponible
        if valor_dado not in self.__movimientos_disponibles__:
            return False
        
        # obtengo el color del jugador actual
        color = self.get_color_jugador_actual()
        
        # obtengo el tablero
        tablero = self.__tablero__
        
        # verifico si hay fichas en la barra
        if tablero.jugador_tiene_fichas_en_barra(color) == True:
            # si hay fichas en barra solo puedo mover desde ahi
            if punto_origen != 0:
                return False
            
            # calculo el destino desde la barra
            if color == 'blanco':
                destino = 25 - valor_dado
            else:
                destino = valor_dado
            
            # verifico si el destino es valido
            if destino < 1 or destino > 24:
                return False
            
            # verifico si puedo mover a ese punto
            if tablero.puede_mover_a_punto(destino, color) == True:
                return True
            else:
                return False
        
        # si no hay fichas en barra, verifico movimiento normal
        
        # verifico que haya fichas en el origen
        if tablero.contar_fichas_en_punto(punto_origen) == 0:
            return False
        
        # verifico que las fichas sean del color correcto
        if tablero.get_color_en_punto(punto_origen) != color:
            return False
        
        # calculo el destino
        if color == 'blanco':
            destino = punto_origen - valor_dado
        else:
            destino = punto_origen + valor_dado
        
        # verifico que el destino este dentro del tablero
        # por ahora no implemento bear off
        if destino < 1 or destino > 24:
            return False
        
        # verifico si puedo mover al destino
        if tablero.puede_mover_a_punto(destino, color) == True:
            return True
        else:
            return False
    
def puede_hacer_algun_movimiento(self):
        """
        Verifica si el jugador actual puede hacer algun movimiento.
        
        Recibe:
            nada
        Hace:
            chequea si hay movimientos disponibles
        Devuelve:
            bool: True si hay movimientos, False si no
        """
        if len(self.__movimientos_disponibles__) > 0:
            return True
        else:
            return False