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
  
 # ===== TESTS DE TIRADA DE DADOS =====
  
   @patch('core.dice.random.randint')
   def test_tirar_dados_normal(self, mock_randint):
       #Debe poder tirar dados y obtener movimientos normales
       mock_randint.side_effect = [3, 5]
      
       resultado = self.juego.tirar_dados()
      
       self.assertEqual(resultado, [3, 5])
       self.assertEqual(self.juego.get_movimientos_disponibles(), [3, 5])
  
   @patch('core.dice.random.randint')
   def test_tirar_dados_dobles(self, mock_randint):
       #Debe poder tirar dobles y obtener 4 movimientos
       mock_randint.side_effect = [4, 4]
      
       resultado = self.juego.tirar_dados()
      
       self.assertEqual(resultado, [4, 4, 4, 4])
       self.assertEqual(self.juego.get_movimientos_disponibles(), [4, 4, 4, 4])
  
   def test_no_puede_tirar_dados_si_ya_tiro(self):
       #No debe poder tirar dados si ya tirÃ³ en este turno
       with patch('core.dice.random.randint', side_effect=[2, 6]):
           self.juego.tirar_dados()
          
           # Intentar tirar de nuevo debera fallar
           with self.assertRaises(TurnoIncorrectoError):
               self.juego.tirar_dados()
  
   # ===== TESTS DE COLORES DE JUGADORES =====
  
   def test_color_jugador_actual_inicial(self):
       #El primer jugador debe ser blanco
       self.assertEqual(self.juego.get_color_jugador_actual(), 'blanco')
  
   def test_color_jugador_cambia_con_turno(self):
       #El color debe cambiar cuando cambia el turno
       self.assertEqual(self.juego.get_color_jugador_actual(), 'blanco')
      
       self.juego.terminar_turno()
       self.assertEqual(self.juego.get_color_jugador_actual(), 'negro')
      
       self.juego.terminar_turno()
       self.assertEqual(self.juego.get_color_jugador_actual(), 'blanco')
  
