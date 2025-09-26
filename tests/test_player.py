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
