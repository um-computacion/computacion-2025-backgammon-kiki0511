import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        # Creo un jugador para usar en los tests
        self.jugador = Player("Naza", 1)
    
    #  TESTS BÁSICOS 
    
    def test_crear_jugador_nuevo(self):
        #Un jugador nuevo debe tener todo en cero
        self.assertEqual(self.jugador.get_nombre(), "Naza")
        self.assertEqual(self.jugador.get_direccion(), 1)
        self.assertEqual(self.jugador.get_fichas_en_barra(), 0)
        self.assertEqual(self.jugador.get_fichas_sacadas(), 0)
    
    def test_jugador_direccion_izquierda(self):
        #Pruebo crear un jugador que mueva hacia la izquierda
        jugador_izq = Player("Laura", -1)
        self.assertEqual(jugador_izq.get_direccion(), -1)
        self.assertEqual(jugador_izq.get_nombre(), "Laura")
    
   


if __name__ == "__main__":
    unittest.main()