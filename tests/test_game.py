import unittest
from unittest.mock import patch, MagicMock
from core.game import BackgammonGame
from core.exceptions import *


class TestBackgammonGame(unittest.TestCase):
  
   def setUp(self):
       #configuracion inicial para cada test
       self.juego = BackgammonGame("Jugador1", "Jugador2")
  
   # ===== TESTS DE INICIALIZACION =====
  
   def test_crear_juego_correctamente(self):
       #Un juego nuevo debe crearse con todos los componentes
       self.assertEqual(self.juego.get_jugador1().get_nombre(), "Jugador1")
       self.assertEqual(self.juego.get_jugador2().get_nombre(), "Jugador2")
       self.assertEqual(self.juego.get_jugador_actual(), self.juego.get_jugador1())
       self.assertFalse(self.juego.esta_terminado())
       self.assertIsNone(self.juego.get_ganador())
  
   def test_jugadores_tienen_direcciones_correctas(self):
       #Los jugadores deben tener direcciones opuestas
       self.assertEqual(self.juego.get_jugador1().get_direccion(), 1)  # Derecha
       self.assertEqual(self.juego.get_jugador2().get_direccion(), -1)  # Izquierda
  
   def test_tablero_inicializado_correctamente(self):
       # El tablero debe estar en posicion inicial
       tablero = self.juego.get_tablero()
       # Verificar algunas posiciones iniciales
       self.assertEqual(tablero.contar_fichas_en_punto(24), 2)  # Fichas blancas
       self.assertEqual(tablero.contar_fichas_en_punto(1), 2)   # Fichas negras
  
   def test_sin_movimientos_disponibles_inicialmente(self):
       #No debe haber movimientos disponibles antes de tirar dados
       self.assertEqual(len(self.juego.get_movimientos_disponibles()), 0)
  
