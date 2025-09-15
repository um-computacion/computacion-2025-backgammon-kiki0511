# Board: representa el tablero.


from core.checker import Checker


class Board:
    def __init__(self):
       # Crear 26 listas vacías (0 a 25)
       self.__puntos__ = []
       for _ in range(26):
           self.__puntos__.append([])
       # Colocar fichas en posición inicial
       self.colocar_fichas_iniciales()
  
    def colocar_fichas_iniciales(self):
       #Coloca las fichas en la posición inicial del Backgammon (15 blancas y 15 negras)
       # Fichas blancas (jugador que mueve hacia derecha)
       # 2 fichas en punto 24
       for _ in range(2):
           ficha = Checker('blanco')
           ficha.set_posicion(24)
           self.__puntos__[24].append(ficha)
      
       # 5 fichas en punto 13
       for _ in range(5):
           ficha = Checker('blanco')
           ficha.set_posicion(13)
           self.__puntos__[13].append(ficha)
      
       # 3 fichas en punto 8
       for _ in range(3):
           ficha = Checker('blanco')
           ficha.set_posicion(8)
           self.__puntos__[8].append(ficha)

         # 5 fichas en punto 6
       for _ in range(5):
           ficha = Checker('blanco')
           ficha.set_posicion(6)
           self.__puntos__[6].append(ficha)
      
       # Fichas negras (jugador que mueve hacia izquierda)
       # 2 fichas en punto 1
       for _ in range(2):
           ficha = Checker('negro')
           ficha.set_posicion(1)
           self.__puntos__[1].append(ficha)
      
       # 5 fichas en punto 12
       for _ in range(5):
           ficha = Checker('negro')
           ficha.set_posicion(12)
           self.__puntos__[12].append(ficha)