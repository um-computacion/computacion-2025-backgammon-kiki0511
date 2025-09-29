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
      
       self.assertIn("fuera del rango valido", str(context.exception))
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

 # ===== TESTS DE ValorDadoInvalidoError =====
  
   def test_valor_dado_menor_a_1(self):
       # Valor de dado menor a 1 debe lanzar excepcion
       with self.assertRaises(ValorDadoInvalidoError) as context:
           self.juego.calcular_punto_destino(24, 0)
      
       self.assertIn("fuera del rango valido", str(context.exception))
       self.assertIn("0", str(context.exception))
  
   def test_valor_dado_mayor_a_6(self):
       # Valor de dado mayor a 6 debe lanzar excepcion
       with self.assertRaises(ValorDadoInvalidoError):
           self.juego.calcular_punto_destino(24, 7)
  
   def test_puede_hacer_movimiento_valor_invalido(self):
       # Verificar movimiento con valor invalido debe lanzar excepcion 
       with patch('core.dice.random.randint', side_effect=[3, 5]):
           self.juego.tirar_dados()
          
           with self.assertRaises(ValorDadoInvalidoError):
               self.juego.puede_hacer_movimiento(24, 0)
          
           with self.assertRaises(ValorDadoInvalidoError):
               self.juego.puede_hacer_movimiento(24, 8)
  
   def test_validar_entrada_usuario_valor_invalido(self):
       # Validar entrada con valor invalido debe lanzar excepcion
       with self.assertRaises(ValorDadoInvalidoError):
           self.juego.validar_entrada_usuario("24", "0")
      
       with self.assertRaises(ValorDadoInvalidoError):
           self.juego.validar_entrada_usuario("24", "7")
      
       with self.assertRaises(ValorDadoInvalidoError):
           self.juego.validar_entrada_usuario("24", "xyz")
  
   # ===== TESTS DE MovimientoInvalidoError =====
  
   @patch('core.dice.random.randint')
   def test_movimiento_desde_punto_vacio(self, mock_randint):
       # Mover desde punto vaci­o debe lanzar excepcion 
       mock_randint.side_effect = [3, 5]
       self.juego.tirar_dados()
      
       with self.assertRaises(MovimientoInvalidoError) as context:
           self.juego.hacer_movimiento(2, 3)  # Punto 2 esta vaci­o
      
       self.assertIn("no es valido", str(context.exception))
  
   @patch('core.dice.random.randint')
   def test_movimiento_ficha_enemiga(self, mock_randint):
       # Mover ficha enemiga debe lanzar excepcion
       mock_randint.side_effect = [3, 5]
       self.juego.tirar_dados()
      
       with self.assertRaises(MovimientoInvalidoError):
           self.juego.hacer_movimiento(1, 3)  # Punto 1 tiene fichas negras, turno de blancas
  
   @patch('core.dice.random.randint')
   def test_usar_valor_no_disponible(self, mock_randint):
       # Usar valor de dado no disponible debe lanzar excepcion
       mock_randint.side_effect = [3, 5]
       self.juego.tirar_dados()
      
       with self.assertRaises(ValorDadoInvalidoError):
           self.juego.hacer_movimiento(24, 2)  # Solo tiene 3 y 5 disponibles
  
   # ===== TESTS DE FichaEnBarraError =====
  
   @patch('core.dice.random.randint')
   def test_mover_con_fichas_en_barra(self, mock_randint):
       # Intentar mover del tablero teniendo fichas en barra debe fallar
       mock_randint.side_effect = [3, 5]
       self.juego.tirar_dados()
      
       # Simular ficha blanca en la barra
       from core.checker import Checker
       ficha_capturada = Checker('blanco')
       ficha_capturada.set_posicion(0)
       self.juego.get_tablero().get_fichas_en_punto(0).append(ficha_capturada)
      
       with self.assertRaises(FichaEnBarraError) as context:
           self.juego.hacer_movimiento(24, 3)  # Intentar mover del tablero
      
       self.assertIn("fichas de la barra", str(context.exception))
