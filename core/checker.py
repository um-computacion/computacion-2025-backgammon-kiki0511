class Checker:
    """
    Clase que representa una ficha de Backgammon.
    
    Recibe: Nada
    Hace: Representa una ficha que puede ser blanca o negra
    Devuelve: Nada
    """
    
    def __init__(self, color):
        """
        Inicializa una ficha con su color.
        
        Recibe: String con el color ('blanco' o 'negro')
        Hace: Crea la ficha con el color especificado
        Devuelve: Nada
        """
        self.__color__ = color
        self.__posicion__ = None
    
    def get_color(self):
        """
        Obtiene el color de la ficha.
        
        Recibe: Nada
        Hace: Devuelve el color de la ficha
        Devuelve: String con el color ('blanco' o 'negro')
        """
        return self.__color__
    
    def get_posicion(self):
        """
        Obtiene la posición actual de la ficha.
        
        Recibe: Nada
        Hace: Devuelve la posición donde está la ficha
        Devuelve: Integer con el número del punto (0-25) o None
        """
        return self.__posicion__
    
    def set_posicion(self, nueva_posicion):
        """
        Establece una nueva posición para la ficha.
        
        Recibe: Integer con la nueva posición (0-25)
        Hace: Cambia la posición de la ficha
        Devuelve: Nada
        """
        self.__posicion__ = nueva_posicion
    
    def esta_en_barra(self):
        """
        Verifica si la ficha está en la barra.
        
        Recibe: Nada
        Hace: Comprueba si la posición es 0 (barra)
        Devuelve: Boolean True si está en barra, False si no
        """
        if self.__posicion__ == 0:
            return True
        else:
            return False
    
    def esta_sacada(self):
        """
        Verifica si la ficha fue sacada del tablero.
        
        Recibe: Nada
        Hace: Comprueba si la posición es 25 (sacada)
        Devuelve: Boolean True si está sacada, False si no
        """
        if self.__posicion__ == 25:
            return True
        else:
            return False
    
    def __str__(self):
        """
        Convierte la ficha a texto para mostrar.
        
        Recibe: Nada
        Hace: Crea una representación de texto de la ficha
        Devuelve: String con 'B' para blanco o 'N' para negro
        """
        if self.__color__ == 'blanco':
            simbolo = 'B'
        else:
            simbolo = 'N'
        
        return simbolo