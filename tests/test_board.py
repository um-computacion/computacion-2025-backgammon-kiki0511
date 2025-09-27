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

# ===== MOVER_FICHA =====


   def test_mover_ficha_a_punto_vacio(self):
       # Movimiento simple a vacio
       ok = self.board.mover_ficha(24, 23, "blanco")
       self.assertTrue(ok)
       self.assertEqual(self.board.contar_fichas_en_punto(24), 1)
       self.assertEqual(self.board.contar_fichas_en_punto(23), 1)
       self.assertEqual(self.board.get_color_en_punto(23), "blanco")


   def test_mover_ficha_a_punto_propio(self):
       # Movimiento a punto propio
       n = self.board.contar_fichas_en_punto(13)
       ok = self.board.mover_ficha(24, 13, "blanco")
       self.assertTrue(ok)
       self.assertEqual(self.board.contar_fichas_en_punto(13), n + 1)


   def test_mover_ficha_negativos(self):
       # No mover: origen vacio, color incorrecto, destino bloqueado 
       self.assertFalse(self.board.mover_ficha(2, 3, "blanco"))        # origen vacio
       self.assertFalse(self.board.mover_ficha(1, 2, "blanco"))        # color incorrecto (negra)
       self.assertFalse(self.board.mover_ficha(8, 12, "blanco"))       # bloqueado (5 negras)


   def test_capturar_ficha_enemiga_solitaria(self):
       # Captura al haber 1 enemiga 
       self.board.mover_ficha(1, 3, "negro")           # dejar 1 negra en 3
       ok = self.board.mover_ficha(8, 3, "blanco")     # captura
       self.assertTrue(ok)
       self.assertEqual(self.board.get_color_en_punto(3), "blanco")
       barra = self.board.get_fichas_en_punto(0)
       self.assertEqual(len(barra), 1)
       self.assertEqual(barra[0].get_color(), "negro")


   # ===== BARRA =====


   def test_detectar_fichas_en_barra(self):
       # Detecta fichas en barra por color
       self.assertFalse(self.board.jugador_tiene_fichas_en_barra("blanco"))
       self.assertFalse(self.board.jugador_tiene_fichas_en_barra("negro"))
       # simular captura de negra
       self.board.mover_ficha(1, 3, "negro")
       self.board.mover_ficha(8, 3, "blanco")
       self.assertTrue(self.board.jugador_tiene_fichas_en_barra("negro"))
       self.assertFalse(self.board.jugador_tiene_fichas_en_barra("blanco"))


   def test_sacar_ficha_de_barra_por_color(self):
       # Saca de barra o devuelve None si no hay
       self.assertIsNone(self.board.sacar_ficha_de_barra("blanco"))
       # poner 1 negra en barra
       self.board.mover_ficha(1, 3, "negro")
       self.board.mover_ficha(8, 3, "blanco")
       self.assertIsNone(self.board.sacar_ficha_de_barra("blanco"))  # no hay blancas
       f = self.board.sacar_ficha_de_barra("negro")
       self.assertIsNotNone(f)
       self.assertEqual(f.get_color(), "negro")


   # ===== REINGRESAR DESDE BARRA =====


   def test_reingresar_desde_barra_fallas(self):
       # Fallas: destino invalido, destino bloqueado o sin ficha en barra
       # destino fuera de rango
       self.assertFalse(self.board.reingresar_desde_barra("blanco", 0))
       self.assertFalse(self.board.reingresar_desde_barra("blanco", 25))
       # sin ficha en barra
       self.assertFalse(self.board.reingresar_desde_barra("blanco", 2))
       # bloquear destino con 2+ enemigas (punto 12 tiene 5 negras)
       # meter una blanca a barra para intentar reingresar a 12 y fallar
       self.board.mover_ficha(24, 23, "blanco")
       self.board.mover_ficha(1, 23, "negro")  # captura blanca -> barra
       self.assertFalse(self.board.reingresar_desde_barra("blanco", 12))


   def test_reingresar_desde_barra_ok_vacio_y_con_captura(self):
       # exitos: a vacío y capturando 1 enemiga
       # Dejar una blanca en barra
       self.board.mover_ficha(24, 23, "blanco")
       self.board.mover_ficha(1, 23, "negro")  # negra captura a blanca -> blanca a barra
       # A vacío (punto 2 está vacio al inicio)
       self.assertTrue(self.board.reingresar_desde_barra("blanco", 2))
       self.assertEqual(self.board.get_color_en_punto(2), "blanco")
       # Volver a dejar otra blanca en barra para probar captura al reingresar
       self.board.mover_ficha(24, 23, "blanco")
       self.board.mover_ficha(1, 23, "negro")  # de nuevo blanca a barra
       # Dejar 1 negra sola en 4 y reingresar capturando
       # si 4 no estuviera vacío, lo vaciamos
       self.board.get_fichas_en_punto(4).clear()
       g = Checker("negro")
       g.set_posicion(4)
       self.board.get_fichas_en_punto(4).append(g)
       self.assertTrue(self.board.reingresar_desde_barra("blanco", 4))
       self.assertEqual(self.board.get_color_en_punto(4), "blanco")
       # La negra capturada vuelve a barra
       self.assertTrue(self.board.jugador_tiene_fichas_en_barra("negro"))
