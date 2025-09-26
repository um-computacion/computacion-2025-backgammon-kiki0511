from core.board import Board
from core.player import Player
from core.dice import Dice


class BackgammonGame:
   def __init__(self, nombre_jugador1, nombre_jugador2):
       self.__tablero__ = Board()
       self.__jugador1__ = Player(nombre_jugador1, 1)   # dirección 1 -> blanco
       self.__jugador2__ = Player(nombre_jugador2, -1)  # dirección -1 -> negro
       self.__jugador_actual__ = self.__jugador1__
       self.__dados__ = Dice()
       self.__movimientos_disponibles__ = []
       self.__juego_terminado__ = False
       self.__ganador__ = None
       self.__turno_paso_automatico__ = False


   # ============== getters ==============

   def get_tablero(self): return self.__tablero__
   def get_jugador_actual(self): return self.__jugador_actual__
   def get_jugador1(self): return self.__jugador1__
   def get_jugador2(self): return self.__jugador2__
   def get_dados(self): return self.__dados__
   def get_movimientos_disponibles(self): return self.__movimientos_disponibles__
   def esta_terminado(self): return self.__juego_terminado__
   def get_ganador(self): return self.__ganador__
   def turno_paso_automaticamente(self): return self.__turno_paso_automatico__


   def get_color_jugador_actual(self):
       return 'blanco' if self.__jugador_actual__.get_direccion() == 1 else 'negro'


   # ============== dados ==============
   
   def tirar_dados(self):
       resultado = self.__dados__.tirar()
       self.__movimientos_disponibles__ = resultado.copy()
       return resultado
