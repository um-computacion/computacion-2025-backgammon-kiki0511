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
    
   # ===== TESTS DE FICHAS EN LA BARRA =====
    
    def test_agregar_fichas_a_la_barra(self):
        """Cuando me capturan fichas, deben ir a la barra"""
        self.jugador.agregar_ficha_a_barra()
        self.assertEqual(self.jugador.get_fichas_en_barra(), 1)
        
        # Agrego otra más
        self.jugador.agregar_ficha_a_barra()
        self.assertEqual(self.jugador.get_fichas_en_barra(), 2)
    
    def test_sacar_ficha_de_la_barra(self):
        """Puedo sacar fichas de la barra para volver a jugarlas"""
        # Primero pongo algunas fichas en la barra
        self.jugador.agregar_ficha_a_barra()
        self.jugador.agregar_ficha_a_barra()
        
        # Ahora saco una
        self.jugador.quitar_ficha_de_barra()
        self.assertEqual(self.jugador.get_fichas_en_barra(), 1)
    
    def test_no_puedo_sacar_mas_fichas_de_las_que_tengo(self):
        """Si no tengo fichas en la barra, no debería poder sacar"""
        # Intento quitar una ficha cuando no tengo ninguna
        self.jugador.quitar_ficha_de_barra()
        self.assertEqual(self.jugador.get_fichas_en_barra(), 0)
    
    def test_verificar_si_tengo_fichas_en_barra(self):
        """Debo poder saber si tengo fichas en la barra o no"""
        # Al principio no tengo fichas
        self.assertFalse(self.jugador.tiene_fichas_en_barra())
        
        # Agrego una ficha
        self.jugador.agregar_ficha_a_barra()
        self.assertTrue(self.jugador.tiene_fichas_en_barra())
        
        # La saco
        self.jugador.quitar_ficha_de_barra()
        self.assertFalse(self.jugador.tiene_fichas_en_barra())
    
    


if __name__ == "__main__":
    unittest.main()