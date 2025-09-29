import unittest
from unittest.mock import patch
from core.game import BackgammonGame
from core.exceptions import *


class TestExcepciones(unittest.TestCase):
  
   def setUp(self):
       #Configuracion inicial para cada test
       self.juego = BackgammonGame("Jugador1", "Jugador2")
  
   # ===== TESTS DE JuegoTerminadoError =====
  
   def test_tirar_dados_en_juego_terminado(self):
       #No debe poder tirar dados en un juego terminado
       # Simular juego terminado
       self.juego._BackgammonGame__juego_terminado__ = True
      
       with self.assertRaises(JuegoTerminadoError) as context:
           self.juego.tirar_dados()
      
       self.assertIn("juego terminado", str(context.exception))
  
   def test_hacer_movimiento_en_juego_terminado(self):
       # No debe poder hacer movimientos en un juego terminado
       # Simular juego terminado
       self.juego._BackgammonGame__juego_terminado__ = True
      
       with self.assertRaises(JuegoTerminadoError):
           self.juego.puede_hacer_movimiento(24, 3)
  
   def test_terminar_turno_en_juego_terminado(self):
       # No debe poder terminar turno en un juego terminado 
       # Simular juego terminado
       self.juego._BackgammonGame__juego_terminado__ = True
      
       with self.assertRaises(JuegoTerminadoError):
           self.juego.terminar_turno()
  
   def test_verificar_movimientos_en_juego_terminado(self):
       # No debe poder verificar movimientos en un juego terminado 
       # Simular juego terminado
       self.juego._BackgammonGame__juego_terminado__ = True
      
       with self.assertRaises(JuegoTerminadoError):
           self.juego.puede_hacer_algun_movimiento()
  
   # ===== TESTS DE TurnoIncorrectoError =====
  
   @patch('core.dice.random.randint')
   def test_tirar_dados_dos_veces_mismo_turno(self, mock_randint):
       # No debe poder tirar dados dos veces en el mismo turno
       mock_randint.side_effect = [3, 5]
      
       # Primera tirada exitosa
       self.juego.tirar_dados()
      
       # Segunda tirada debe fallar
       with self.assertRaises(TurnoIncorrectoError) as context:
           self.juego.tirar_dados()
      
       self.assertIn("Ya se tiraron los dados", str(context.exception))
  
   # ===== TESTS DE PuntoInvalidoError =====
  
   def test_punto_origen_negativo(self):
       # Punto origen negativo debe lanzar excepcion
       with self.assertRaises(PuntoInvalidoError) as context:
           self.juego.calcular_punto_destino(-1, 3)
      
       self.assertIn("fuera del rango vÃ¡lido", str(context.exception))
       self.assertIn("-1", str(context.exception))
  
   def test_punto_origen_mayor_a_25(self):
       # Punto origen mayor a 25 debe lanzar excepcion
       with self.assertRaises(PuntoInvalidoError):
           self.juego.calcular_punto_destino(26, 3)
  
   def test_puede_hacer_movimiento_punto_invalido(self):
       # Verificar movimiento con punto invalido debe lanzar excepcion
       with patch('core.dice.random.randint', side_effect=[3, 5]):
           self.juego.tirar_dados()
          
           with self.assertRaises(PuntoInvalidoError):
               self.juego.puede_hacer_movimiento(-5, 3)
          
           with self.assertRaises(PuntoInvalidoError):
               self.juego.puede_hacer_movimiento(30, 3)
  
   def test_validar_entrada_usuario_punto_invalido(self):
       # Validar entrada con punto invalido debe lanzar excepcion
       with self.assertRaises(PuntoInvalidoError):
           self.juego.validar_entrada_usuario("-1", "3")
      
       with self.assertRaises(PuntoInvalidoError):
           self.juego.validar_entrada_usuario("26", "3")
      
       with self.assertRaises(PuntoInvalidoError):
           self.juego.validar_entrada_usuario("abc", "3")
