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

 # ===== TESTS DE INDEPENDENCIA ENTRE JUGADORES =====
  
   def test_jugadores_son_independientes_barra(self):
       #Las fichas en barra de un jugador no afectan al otro
       self.jugador_blanco.agregar_ficha_a_barra()
       self.jugador_blanco.agregar_ficha_a_barra()
      
       # El jugador negro no debe verse afectado
       self.assertEqual(self.jugador_negro.get_fichas_en_barra(), 0)
       self.assertFalse(self.jugador_negro.tiene_fichas_en_barra())
  
   def test_jugadores_son_independientes_sacadas(self):
       #Las fichas sacadas de un jugador no afectan al otro
       for i in range(10):
           self.jugador_blanco.sacar_ficha_del_tablero()
      
       # El jugador negro no debe verse afectado
       self.assertEqual(self.jugador_negro.get_fichas_sacadas(), 0)
       self.assertFalse(self.jugador_negro.ha_ganado())
  
   def test_victoria_independiente(self):
       # La victoria de un jugador no afecta al otro
       # Jugador blanco gana
       for i in range(15):
           self.jugador_blanco.sacar_ficha_del_tablero()
      
       self.assertTrue(self.jugador_blanco.ha_ganado())
       self.assertFalse(self.jugador_negro.ha_ganado())
  
   # ===== TESTS DE REPRESENTACION STRING =====
  
   def test_str_jugador_blanco(self):
       #La representacion string del jugador blanco debe ser correcta
       resultado = str(self.jugador_blanco)
      
       self.assertIn("Ana", resultado)
       self.assertIn("derecha", resultado)
       self.assertIn("Jugador:", resultado)
  
   def test_str_jugador_negro(self):
       #La representacion string del jugador negro debe ser correcta
       resultado = str(self.jugador_negro)
      
       self.assertIn("Luis", resultado)
       self.assertIn("izquierda", resultado)
       self.assertIn("Jugador:", resultado)
  
   def test_str_direcciones_correctas(self):
       #Las direcciones en string deben ser correctas para cada jugador
       str_blanco = str(self.jugador_blanco)
       str_negro = str(self.jugador_negro)
      
       self.assertIn("derecha", str_blanco)
       self.assertNotIn("izquierda", str_blanco)
      
       self.assertIn("izquierda", str_negro)
       self.assertNotIn("derecha", str_negro)
  
   # ===== TESTS DE CASOS LIMITE =====
  
   def test_nombre_vacio(self):
       #Debe manejar nombres vaci­os correctamente
       jugador_sin_nombre = Player("", 1)
      
       self.assertEqual(jugador_sin_nombre.get_nombre(), "")
       resultado = str(jugador_sin_nombre)
       self.assertIn("Jugador:", resultado)
  
   def test_nombre_muy_largo(self):
       #Debe manejar nombres muy largos
       nombre_largo = "A" * 100
       jugador_nombre_largo = Player(nombre_largo, 1)
      
       self.assertEqual(jugador_nombre_largo.get_nombre(), nombre_largo)
       resultado = str(jugador_nombre_largo)
       self.assertIn(nombre_largo, resultado)
  
   def test_direccion_invalida_procesada_correctamente(self):
       #Debe procesar direcciones no estandar
       jugador_dir_rara = Player("Test", 0)
      
       self.assertEqual(jugador_dir_rara.get_direccion(), 0)
       resultado = str(jugador_dir_rara)
       self.assertIn("izquierda", resultado)  # Cualquier cosa != 1 es izquierda
  
   def test_multiples_operaciones_secuenciales(self):
       # Debe manejar multiples operaciones en secuencia
       # Secuencia compleja de operaciones
       self.jugador_blanco.agregar_ficha_a_barra()
       self.jugador_blanco.agregar_ficha_a_barra()
       self.jugador_blanco.sacar_ficha_del_tablero()
       self.jugador_blanco.quitar_ficha_de_barra()
       self.jugador_blanco.sacar_ficha_del_tablero()
       self.jugador_blanco.sacar_ficha_del_tablero()
      
       # Verificar estado final
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 1)
       self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 3)
       self.assertTrue(self.jugador_blanco.tiene_fichas_en_barra())
       self.assertFalse(self.jugador_blanco.ha_ganado())

  # ===== TESTS DE VALORES LIMITE =====
  
   def test_exactamente_14_fichas_sacadas(self):
       # Con 14 fichas sacadas no debe haber victoria
       for i in range(14):
           self.jugador_blanco.sacar_ficha_del_tablero()
      
       self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 14)
       self.assertFalse(self.jugador_blanco.ha_ganado())
  
   def test_exactamente_16_fichas_sacadas(self):
       # Con 16 fichas sacadas debe haber victoria
       for i in range(16):
           self.jugador_blanco.sacar_ficha_del_tablero()
      
       self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 16)
       self.assertTrue(self.jugador_blanco.ha_ganado())
  
   def test_muchas_fichas_en_barra(self):
       # Debe manejar muchas fichas en la barra 
       for i in range(50):  # Mas fichas de las que tiene un jugador
           self.jugador_blanco.agregar_ficha_a_barra()
      
       self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 50)
       self.assertTrue(self.jugador_blanco.tiene_fichas_en_barra())


if __name__ == "__main__":
   unittest.main()