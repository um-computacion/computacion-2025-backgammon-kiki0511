
import unittest
from core.checker import Checker


class TestChecker(unittest.TestCase):
  
   def setUp(self):
       #Configuracion inicial para cada test
       self.ficha_blanca = Checker('blanco')
       self.ficha_negra = Checker('negro')
  
   # ===== TESTS DE INICIALIZACION =====
  
   def test_crear_ficha_blanca(self):
       #Una ficha blanca debe crearse correctamente
       self.assertEqual(self.ficha_blanca.get_color(), 'blanco')
       self.assertIsNone(self.ficha_blanca.get_posicion())
  
   def test_crear_ficha_negra(self):
       #Una ficha negra debe crearse correctamente
       self.assertEqual(self.ficha_negra.get_color(), 'negro')
       self.assertIsNone(self.ficha_negra.get_posicion())
  
   def test_ficha_no_esta_en_barra_inicialmente(self):
       #Una ficha nueva no debe estar en la barra
       self.assertFalse(self.ficha_blanca.esta_en_barra())
       self.assertFalse(self.ficha_negra.esta_en_barra())
  
   def test_ficha_no_esta_sacada_inicialmente(self):
       #Una ficha nueva no debe estar sacada
       self.assertFalse(self.ficha_blanca.esta_sacada())
       self.assertFalse(self.ficha_negra.esta_sacada())

     # ===== TESTS DE POSICIÃ“N =====
  
   def test_establecer_posicion_normal(self):
       """Debe poder establecer una posiciÃ³n normal en el tablero"""
       self.ficha_blanca.set_posicion(13)
       self.assertEqual(self.ficha_blanca.get_posicion(), 13)
  
   def test_establecer_posicion_barra(self):
       """Debe poder establecer la posiciÃ³n en la barra (0)"""
       self.ficha_blanca.set_posicion(0)
       self.assertEqual(self.ficha_blanca.get_posicion(), 0)
       self.assertTrue(self.ficha_blanca.esta_en_barra())
       self.assertFalse(self.ficha_blanca.esta_sacada())
  
   def test_establecer_posicion_sacada(self):
       """Debe poder establecer la posiciÃ³n como sacada (25)"""
       self.ficha_blanca.set_posicion(25)
       self.assertEqual(self.ficha_blanca.get_posicion(), 25)
       self.assertFalse(self.ficha_blanca.esta_en_barra())
       self.assertTrue(self.ficha_blanca.esta_sacada())
  
   def test_cambiar_posicion_multiples_veces(self):
       """Debe poder cambiar la posiciÃ³n varias veces"""
       # Posicion inicial
       self.ficha_blanca.set_posicion(24)
       self.assertEqual(self.ficha_blanca.get_posicion(), 24)
      
       # Mover a otro punto
       self.ficha_blanca.set_posicion(18)
       self.assertEqual(self.ficha_blanca.get_posicion(), 18)
      
       # Mover a la barra
       self.ficha_blanca.set_posicion(0)
       self.assertTrue(self.ficha_blanca.esta_en_barra())
      
       # Sacar del tablero
       self.ficha_blanca.set_posicion(25)
       self.assertTrue(self.ficha_blanca.esta_sacada())