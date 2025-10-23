import random


class Dice:
    """
    Clase que representa los dados del juego.
    
    Recibe: Nada
    Hace: Maneja las tiradas de dos dados de seis caras
    Devuelve: Nada
    """
    
    def __init__(self):
        """
        Inicializa los dados. 
        
        Recibe: Nada
        Hace: Crea el atributo para guardar la última tirada
        Devuelve: Nada
        """
        self.__ultima_tirada__ = None
    
    def tirar(self):
        """
        Realiza una tirada de dos dados.
        
        Recibe: Nada
        Hace: Tira dos dados y devuelve los valores (4 si son dobles)
        Devuelve: Lista con los valores de los dados
        """
        # tirar el primer dado
        dado1 = random.randint(1, 6)
        
        # tirar el segundo dado
        dado2 = random.randint(1, 6)
        
        # verificar si son dobles
        if dado1 == dado2:
            # si son dobles, devolver 4 veces el valor
            resultado = []
            resultado.append(dado1)
            resultado.append(dado1)
            resultado.append(dado1)
            resultado.append(dado1)
        else:
            # si no son dobles, devolver los dos valores
            resultado = []
            resultado.append(dado1)
            resultado.append(dado2)
        
        # guardar el resultado
        self.__ultima_tirada__ = resultado
        
        return resultado
    
    def get_ultima_tirada(self):
        """
        Obtiene la última tirada realizada.
        
        Recibe: Nada
        Hace: Devuelve el resultado de la última tirada
        Devuelve: Lista con los valores o None si no se ha tirado
        """
        return self.__ultima_tirada__
    
    def es_doble(self):
        """
        Verifica si la última tirada fue dobles.
        
        Recibe: Nada
        Hace: Comprueba si la última tirada tiene 4 valores
        Devuelve: Boolean True si fueron dobles, False si no
        """
        if self.__ultima_tirada__ == None:
            return False
        
        if len(self.__ultima_tirada__) == 4:
            return True
        else:
            return False