
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

     # ===== TESTS DE POSICION=====
  
   def test_establecer_posicion_normal(self):
       #Debe poder establecer una posicion normal en el tablero
       self.ficha_blanca.set_posicion(13)
       self.assertEqual(self.ficha_blanca.get_posicion(), 13)
  
   def test_establecer_posicion_barra(self):
       #Debe poder establecer la posicion en la barra (0)
       self.ficha_blanca.set_posicion(0)
       self.assertEqual(self.ficha_blanca.get_posicion(), 0)
       self.assertTrue(self.ficha_blanca.esta_en_barra())
       self.assertFalse(self.ficha_blanca.esta_sacada())
  
   def test_establecer_posicion_sacada(self):
       #Debe poder establecer la posicion como sacada (25)
       self.ficha_blanca.set_posicion(25)
       self.assertEqual(self.ficha_blanca.get_posicion(), 25)
       self.assertFalse(self.ficha_blanca.esta_en_barra())
       self.assertTrue(self.ficha_blanca.esta_sacada())
  
   def test_cambiar_posicion_multiples_veces(self):
       #Debe poder cambiar la posicion varias veces
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

     # ===== TESTS DE ESTADOS ESPECIALES =====
  
   def test_esta_en_barra_solo_posicion_0(self):
       #Solo la posicion 0 debe considerarse en la barra
       posiciones_no_barra = [1, 5, 12, 18, 24, 25, None]
      
       for pos in posiciones_no_barra:
           self.ficha_blanca.set_posicion(pos)
           self.assertFalse(self.ficha_blanca.esta_en_barra(),
                          f"Posicion {pos} no deberia estar en barra")
  
   def test_esta_sacada_solo_posicion_25(self):
       #Solo la posicion 25 debe considerarse sacada
       posiciones_no_sacadas = [0, 1, 5, 12, 18, 24, None]
      
       for pos in posiciones_no_sacadas:
           self.ficha_blanca.set_posicion(pos)
           self.assertFalse(self.ficha_blanca.esta_sacada(),
                          f"Posicion {pos} no deberia estar sacada")
  
   def test_estados_mutuamente_excluyentes(self):
       #Una ficha no puede estar en barra y sacada al mismo tiempo
       # En barra
       self.ficha_blanca.set_posicion(0)
       self.assertTrue(self.ficha_blanca.esta_en_barra())
       self.assertFalse(self.ficha_blanca.esta_sacada())
      
       # Sacada
       self.ficha_blanca.set_posicion(25)
       self.assertFalse(self.ficha_blanca.esta_en_barra())
       self.assertTrue(self.ficha_blanca.esta_sacada())
      
       # En tablero normal
       self.ficha_blanca.set_posicion(12)
       self.assertFalse(self.ficha_blanca.esta_en_barra())
       self.assertFalse(self.ficha_blanca.esta_sacada())
  
  # ===== TESTS DE REPRESENTACION =====
  
   def test_str_ficha_blanca(self):
       #La representacion en string de ficha blanca debe ser B
       resultado = str(self.ficha_blanca)
       self.assertEqual(resultado, 'B')
  
   def test_str_ficha_negra(self):
       #La representacion en string de ficha negra debe ser N
       resultado = str(self.ficha_negra)
       self.assertEqual(resultado, 'N')
  
   def test_str_no_cambia_con_posicion(self):
       #La representacion en string no debe cambiar segun la posicion
       # Ficha blanca en diferentes posiciones
       posiciones = [None, 0, 12, 25]
       for pos in posiciones:
           self.ficha_blanca.set_posicion(pos)
           self.assertEqual(str(self.ficha_blanca), 'B')
      
       # Ficha negra en diferentes posiciones
       for pos in posiciones:
           self.ficha_negra.set_posicion(pos)
           self.assertEqual(str(self.ficha_negra), 'N')
