class BackgammonError(Exception):
    """
    Clase base para todas las excepciones del juego.
    
    Recibe: String con el mensaje de error (opcional)
    Hace: Crea una excepción general de Backgammon
    Devuelve: Nada
    """
    
    def __init__(self, mensaje="Error en el juego de Backgammon"):
        """
        Inicializa la excepción base.
        
        Recibe: String con el mensaje de error
        Hace: Guarda el mensaje de error
        Devuelve: Nada
        """
        self.__mensaje__ = mensaje
        super().__init__(self.__mensaje__)


class MovimientoInvalidoError(BackgammonError):
    """
    Error cuando se intenta hacer un movimiento inválido.
    
    Recibe: String con el mensaje de error (opcional)
    Hace: Crea una excepción para movimientos inválidos
    Devuelve: Nada
    """
    
    def __init__(self, mensaje="Movimiento no es valido"):
        """
        Inicializa la excepción de movimiento inválido.
        
        Recibe: String con el mensaje de error
        Hace: Guarda el mensaje sobre el movimiento inválido
        Devuelve: Nada
        """
        super().__init__(mensaje)


class PuntoInvalidoError(BackgammonError):
    """
    Error cuando se especifica un punto inválido.
    
    Recibe: String con el mensaje de error (opcional)
    Hace: Crea una excepción para puntos fuera de rango
    Devuelve: Nada
    """
    
    def __init__(self, mensaje="Punto fuera del rango valido"):
        """
        Inicializa la excepción de punto inválido.
        
        Recibe: String con el mensaje de error
        Hace: Guarda el mensaje sobre el punto inválido
        Devuelve: Nada
        """
        super().__init__(mensaje)


class ValorDadoInvalidoError(BackgammonError):
    """
    Error cuando se especifica un valor de dado inválido.
    
    Recibe: String con el mensaje de error (opcional)
    Hace: Crea una excepción para valores de dado incorrectos
    Devuelve: Nada
    """
    
    def __init__(self, mensaje="Valor de dado fuera del rango valido"):
        """
        Inicializa la excepción de valor de dado inválido.
        
        Recibe: String con el mensaje de error
        Hace: Guarda el mensaje sobre el valor inválido
        Devuelve: Nada
        """
        super().__init__(mensaje)


class JuegoTerminadoError(BackgammonError):
    """
    Error cuando se intenta jugar en un juego terminado.
    
    Recibe: String con el mensaje de error (opcional)
    Hace: Crea una excepción para acciones en juego terminado
    Devuelve: Nada
    """
    
    def __init__(self, mensaje="El juego ya esta terminado"):
        """
        Inicializa la excepción de juego terminado.
        
        Recibe: String con el mensaje de error
        Hace: Guarda el mensaje sobre el juego terminado
        Devuelve: Nada
        """
        super().__init__(mensaje)


class TurnoIncorrectoError(BackgammonError):
    """
    Error cuando se hace una acción fuera de turno.
    
    Recibe: String con el mensaje de error (opcional)
    Hace: Crea una excepción para acciones fuera de turno
    Devuelve: Nada
    """
    
    def __init__(self, mensaje="Accion fuera del turno correspondiente"):
        """
        Inicializa la excepción de turno incorrecto.
        
        Recibe: String con el mensaje de error
        Hace: Guarda el mensaje sobre el turno incorrecto
        Devuelve: Nada
        """
        super().__init__(mensaje)


class FichaEnBarraError(BackgammonError):
    """
    Error cuando hay fichas en la barra que deben moverse primero.
    
    Recibe: String con el mensaje de error (opcional)
    Hace: Crea una excepción para fichas en barra
    Devuelve: Nada
    """
    
    def __init__(self, mensaje="Debe mover fichas de la barra primero"):
        """
        Inicializa la excepción de ficha en barra.
        
        Recibe: String con el mensaje de error
        Hace: Guarda el mensaje sobre fichas en barra
        Devuelve: Nada
        """
        super().__init__(mensaje)


class BearOffInvalidoError(BackgammonError):
    """
    Error cuando se intenta sacar fichas incorrectamente.
    
    Recibe: String con el mensaje de error (opcional)
    Hace: Crea una excepción para bear off inválido
    Devuelve: Nada
    """
    
    def __init__(self, mensaje="No puede sacar fichas del cuadrante final"):
        """
        Inicializa la excepción de bear off inválido.
        
        Recibe: String con el mensaje de error
        Hace: Guarda el mensaje sobre bear off inválido
        Devuelve: Nada
        """
        super().__init__(mensaje)