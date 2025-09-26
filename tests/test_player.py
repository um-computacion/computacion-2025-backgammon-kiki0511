import unittest
from core.player import Player


class TestPlayer(unittest.TestCase):
  
   def setUp(self):
       # Configuracion inicial para cada test
       self.jugador_blanco = Player("Ana", 1)
       self.jugador_negro = Player("Luis", -1)
  
   # ===== TESTS DE INICIALIZACION =====
  
   def test_crear_jugador_blanco_correctamente(self):
       #Un jugador blanco nuevo debe tener todo en estado inicial
       self.assertEqual(self.jugador_blanco.get_nombre(), "Ana")
       self.assertEqual(self.jugador_blanco.get_direccion(), 1)
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 0)
       self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 0)
       self.assertFalse(self.jugador_blanco.tiene_fichas_en_barra())
       self.assertFalse(self.jugador_blanco.ha_ganado())
  
   def test_crear_jugador_negro_correctamente(self):
       #Un jugador negro nuevo debe tener todo en estado inicial
       self.assertEqual(self.jugador_negro.get_nombre(), "Luis")
       self.assertEqual(self.jugador_negro.get_direccion(), -1)
       self.assertEqual(self.jugador_negro.get_fichas_en_barra(), 0)
       self.assertEqual(self.jugador_negro.get_fichas_sacadas(), 0)
       self.assertFalse(self.jugador_negro.tiene_fichas_en_barra())
       self.assertFalse(self.jugador_negro.ha_ganado())
  
   def test_direcciones_opuestas(self):
       #Los jugadores deben tener direcciones opuestas
       self.assertNotEqual(self.jugador_blanco.get_direccion(),
                          self.jugador_negro.get_direccion())
       self.assertEqual(self.jugador_blanco.get_direccion(), 1)
       self.assertEqual(self.jugador_negro.get_direccion(), -1)
  
   def test_nombres_diferentes(self):
       #Los jugadores deben tener nombres diferentes 
       self.assertNotEqual(self.jugador_blanco.get_nombre(),
                          self.jugador_negro.get_nombre())

# ===== TESTS DE FICHAS EN LA BARRA =====
  
   def test_agregar_una_ficha_a_la_barra(self):
       #Debe poder agregar una ficha a la barra
       self.jugador_blanco.agregar_ficha_a_barra()
      
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 1)
       self.assertTrue(self.jugador_blanco.tiene_fichas_en_barra())
  
   def test_agregar_multiples_fichas_a_la_barra(self):
       #Debe poder agregar multiples fichas a la barra
       for i in range(5):
           self.jugador_blanco.agregar_ficha_a_barra()
      
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 5)
       self.assertTrue(self.jugador_blanco.tiene_fichas_en_barra())
  
   def test_quitar_ficha_de_la_barra(self):
       #Debe poder quitar fichas de la barra
       # Agregar algunas fichas primero
       self.jugador_blanco.agregar_ficha_a_barra()
       self.jugador_blanco.agregar_ficha_a_barra()
       self.jugador_blanco.agregar_ficha_a_barra()
      
       # Quitar una ficha
       self.jugador_blanco.quitar_ficha_de_barra()
      
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 2)
       self.assertTrue(self.jugador_blanco.tiene_fichas_en_barra())
  
   def test_quitar_todas_las_fichas_de_la_barra(self):
       # Debe poder quitar todas las fichas de la barra
       # Agregar fichas
       self.jugador_blanco.agregar_ficha_a_barra()
       self.jugador_blanco.agregar_ficha_a_barra()
      
       # Quitar todas
       self.jugador_blanco.quitar_ficha_de_barra()
       self.jugador_blanco.quitar_ficha_de_barra()
      
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 0)
       self.assertFalse(self.jugador_blanco.tiene_fichas_en_barra())
  
   def test_no_puede_quitar_fichas_inexistentes_de_barra(self):
       # No debe poder tener fichas negativas en la barra
       # Intentar quitar cuando no hay fichas
       self.jugador_blanco.quitar_ficha_de_barra()
       self.jugador_blanco.quitar_ficha_de_barra()
       self.jugador_blanco.quitar_ficha_de_barra()
      
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 0)
       self.assertFalse(self.jugador_blanco.tiene_fichas_en_barra())
  
   def test_quitar_mas_fichas_de_las_disponibles(self):
       # Quitar mas fichas de las disponibles debe dejar el contador en 0
       # Agregar solo 2 fichas
       self.jugador_blanco.agregar_ficha_a_barra()
       self.jugador_blanco.agregar_ficha_a_barra()
      
       # Intentar quitar 5 fichas
       for i in range(5):
           self.jugador_blanco.quitar_ficha_de_barra()
      
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 0)
       self.assertFalse(self.jugador_blanco.tiene_fichas_en_barra())
  
   # ===== TESTS DE FICHAS SACADAS =====
  
   def test_sacar_una_ficha_del_tablero(self):
       # Debe poder sacar una ficha del tablero
       self.jugador_blanco.sacar_ficha_del_tablero()
      
       self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 1)
       self.assertFalse(self.jugador_blanco.ha_ganado())  # Necesita 15
  
   def test_sacar_multiples_fichas_del_tablero(self):
       #Debe poder sacar multiples fichas del tablero
       for i in range(10):
           self.jugador_blanco.sacar_ficha_del_tablero()
      
       self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 10)
       self.assertFalse(self.jugador_blanco.ha_ganado())  # Necesita 15
  
   def test_sacar_exactamente_15_fichas_gana(self):
       #Sacar exactamente 15 fichas debe hacer ganar al jugador
       for i in range(15):
           self.jugador_blanco.sacar_ficha_del_tablero()
      
       self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 15)
       self.assertTrue(self.jugador_blanco.ha_ganado())
  
   def test_sacar_mas_de_15_fichas_sigue_ganando(self):
       #Sacar mas de 15 fichas debe seguir marcando como ganador
       for i in range(20):  # Mas de 15
           self.jugador_blanco.sacar_ficha_del_tablero()
      
       self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 20)
       self.assertTrue(self.jugador_blanco.ha_ganado())
  
   def test_progresion_hacia_victoria(self):
       #Debe mostrar progresion correcta hacia la victoria
       pasos_victoria = [5, 10, 14, 15]
      
       for paso in pasos_victoria:
           # Sacar fichas hasta el paso actual
           while self.jugador_negro.get_fichas_sacadas() < paso:
               self.jugador_negro.sacar_ficha_del_tablero()
          
           if paso < 15:
               self.assertFalse(self.jugador_negro.ha_ganado())
           else:
               self.assertTrue(self.jugador_negro.ha_ganado())
