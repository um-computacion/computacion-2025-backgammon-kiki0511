
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