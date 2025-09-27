import unittest
from core.board import Board
from core.checker import Checker




class TestBoard(unittest.TestCase):

   def setUp(self):
       #Crear tablero nuevo para cada test
       self.board = Board()


   # ===== INICIALIZACIÓN =====


   def test_board_se_inicializa_correctamente(self):
       # Posicion estándar inicial
       # Blancas
       self.assertEqual(self.board.contar_fichas_en_punto(24), 2)
       self.assertEqual(self.board.contar_fichas_en_punto(13), 5)
       self.assertEqual(self.board.contar_fichas_en_punto(8), 3)
       self.assertEqual(self.board.contar_fichas_en_punto(6), 5)
       # Negras
       self.assertEqual(self.board.contar_fichas_en_punto(1), 2)
       self.assertEqual(self.board.contar_fichas_en_punto(12), 5)
       self.assertEqual(self.board.contar_fichas_en_punto(17), 3)
       self.assertEqual(self.board.contar_fichas_en_punto(19), 5)
       # Colores
       self.assertEqual(self.board.get_color_en_punto(24), "blanco")
       self.assertEqual(self.board.get_color_en_punto(1), "negro")


   def test_puntos_vacios_inicialmente(self):
       #Puntos que estan vacios al inicio
       vacios = [2, 3, 4, 5, 7, 9, 10, 11, 14, 15, 16, 18, 20, 21, 22, 23]
       for p in vacios:
           self.assertTrue(self.board.punto_esta_vacio(p))
           self.assertIsNone(self.board.get_color_en_punto(p))


   def test_barra_y_sacado_vacios_inicialmente(self):
       #Barra y zona de sacado comienzan vacías
       self.assertTrue(self.board.punto_esta_vacio(0))
       self.assertTrue(self.board.punto_esta_vacio(25))


   # ===== UTILITARIAS BASICAS =====


   def test_get_fichas_en_punto_fuera_de_rango(self):
       # Fuera de rango devuelve lista vacio
       self.assertEqual(len(self.board.get_fichas_en_punto(-1)), 0)
       self.assertEqual(len(self.board.get_fichas_en_punto(26)), 0)


   def test_get_color_en_punto_vacio(self):
       # Color None cuando no hay fichas
       self.assertIsNone(self.board.get_color_en_punto(2))


   # ===== PUEDE_MOVER_A_PUNTO =====


   def test_puede_mover_a_punto_casos(self):
       #Todas las ramas de puede_mover_a_punto
       # fuera de rango
       self.assertFalse(self.board.puede_mover_a_punto(0, "blanco"))
       self.assertFalse(self.board.puede_mover_a_punto(25, "blanco"))
       # vacio
       self.assertTrue(self.board.puede_mover_a_punto(2, "blanco"))
       # propio
       self.assertTrue(self.board.puede_mover_a_punto(24, "blanco"))
       # enemigo 1 ficha -> preparar una blanca sola en 23 y capturar con negro
       self.board.mover_ficha(24, 23, "blanco")  # deja 1 blanca en 23
       self.assertTrue(self.board.puede_mover_a_punto(23, "negro"))
       # enemigo con 2+ -> punto 12 tiene 5 negras
       self.assertFalse(self.board.puede_mover_a_punto(12, "blanco"))