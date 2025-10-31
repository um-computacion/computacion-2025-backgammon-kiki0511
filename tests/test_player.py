import unittest
from core.player import Player


class TestPlayer(unittest.TestCase):
    """
    Clase de pruebas para Player con 100% de cobertura.
    
    Recibe: Nada
    Hace: Prueba todos los metodos de Player
    Devuelve: Nada
    """
    
    def setUp(self):
        """
        Configuracion inicial para cada test.
        
        Recibe: Nada
        Hace: Crea dos jugadores para cada test
        Devuelve: Nada
        """
        self.__jugador_blanco__ = Player("Ana", 1)
        self.__jugador_negro__ = Player("Luis", -1)
    
    # ===== TESTS DE INICIALIZACION Y GETTERS =====
    
    def test_get_nombre(self):
        """
        Prueba get_nombre.
        
        Recibe: Nada
        Hace: Verifica que devuelve el nombre correcto
        Devuelve: Nada
        """
        self.assertEqual(self.__jugador_blanco__.get_nombre(), "Ana")
        self.assertEqual(self.__jugador_negro__.get_nombre(), "Luis")
    
    def test_get_direccion(self):
        """
        Prueba get_direccion.
        
        Recibe: Nada
        Hace: Verifica que devuelve la direccion correcta
        Devuelve: Nada
        """
        self.assertEqual(self.__jugador_blanco__.get_direccion(), 1)
        self.assertEqual(self.__jugador_negro__.get_direccion(), -1)
    
    def test_get_fichas_en_barra_inicial(self):
        """
        Prueba get_fichas_en_barra al inicio.
        
        Recibe: Nada
        Hace: Verifica que empieza en 0
        Devuelve: Nada
        """
        self.assertEqual(self.__jugador_blanco__.get_fichas_en_barra(), 0)
        self.assertEqual(self.__jugador_negro__.get_fichas_en_barra(), 0)
    
    def test_get_fichas_sacadas_inicial(self):
        """
        Prueba get_fichas_sacadas al inicio.
        
        Recibe: Nada
        Hace: Verifica que empieza en 0
        Devuelve: Nada
        """
        self.assertEqual(self.__jugador_blanco__.get_fichas_sacadas(), 0)
        self.assertEqual(self.__jugador_negro__.get_fichas_sacadas(), 0)
    
    # ===== TESTS DE FICHAS EN BARRA =====
    
    def test_agregar_ficha_a_barra(self):
        """
        Prueba agregar_ficha_a_barra.
        
        Recibe: Nada
        Hace: Verifica que incrementa el contador (linea 31)
        Devuelve: Nada
        """
        self.__jugador_blanco__.agregar_ficha_a_barra()
        self.assertEqual(self.__jugador_blanco__.get_fichas_en_barra(), 1)
        
        self.__jugador_blanco__.agregar_ficha_a_barra()
        self.assertEqual(self.__jugador_blanco__.get_fichas_en_barra(), 2)
    
    def test_quitar_ficha_de_barra_cuando_hay(self):
        """
        Prueba quitar_ficha_de_barra cuando hay fichas.
        
        Recibe: Nada
        Hace: Verifica que decrementa (linea 37, rama if > 0)
        Devuelve: Nada
        """
        # agregar fichas primero
        self.__jugador_blanco__.agregar_ficha_a_barra()
        self.__jugador_blanco__.agregar_ficha_a_barra()
        
        # quitar una
        self.__jugador_blanco__.quitar_ficha_de_barra()
        self.assertEqual(self.__jugador_blanco__.get_fichas_en_barra(), 1)
        
        # quitar otra
        self.__jugador_blanco__.quitar_ficha_de_barra()
        self.assertEqual(self.__jugador_blanco__.get_fichas_en_barra(), 0)
    
    def test_quitar_ficha_de_barra_cuando_no_hay(self):
        """
        Prueba quitar_ficha_de_barra cuando no hay fichas.
        
        Recibe: Nada
        Hace: Verifica que no pasa nada (linea 34, no entra al if)
        Devuelve: Nada
        """
        # sin agregar fichas, intentar quitar
        self.__jugador_blanco__.quitar_ficha_de_barra()
        self.assertEqual(self.__jugador_blanco__.get_fichas_en_barra(), 0)
    
    def test_tiene_fichas_en_barra_true(self):
        """
        Prueba tiene_fichas_en_barra cuando hay fichas.
        
        Recibe: Nada
        Hace: Verifica rama if > 0 devuelve True (linea 43)
        Devuelve: Nada
        """
        self.__jugador_blanco__.agregar_ficha_a_barra()
        self.assertTrue(self.__jugador_blanco__.tiene_fichas_en_barra())
    
    def test_tiene_fichas_en_barra_false(self):
        """
        Prueba tiene_fichas_en_barra cuando no hay fichas.
        
        Recibe: Nada
        Hace: Verifica rama else devuelve False (linea 44)
        Devuelve: Nada
        """
        self.assertFalse(self.__jugador_blanco__.tiene_fichas_en_barra())
    
    # ===== TESTS DE FICHAS SACADAS =====
    
    def test_agregar_ficha_sacada(self):
        """
        Prueba agregar_ficha_sacada.
        
        Recibe: Nada
        Hace: Verifica que incrementa el contador (linea 22)
        Devuelve: Nada
        """
        self.__jugador_blanco__.agregar_ficha_sacada()
        self.assertEqual(self.__jugador_blanco__.get_fichas_sacadas(), 1)
        
        self.__jugador_blanco__.agregar_ficha_sacada()
        self.assertEqual(self.__jugador_blanco__.get_fichas_sacadas(), 2)
    
    def test_ha_ganado_false(self):
        """
        Prueba ha_ganado cuando no ha sacado todas las fichas.
        
        Recibe: Nada
        Hace: Verifica rama else devuelve False (linea 26)
        Devuelve: Nada
        """
        # sin sacar fichas
        self.assertFalse(self.__jugador_blanco__.ha_ganado())
        
        # con algunas fichas sacadas
        contador = 0
        while contador < 10:
            self.__jugador_blanco__.agregar_ficha_sacada()
            contador = contador + 1
        
        self.assertFalse(self.__jugador_blanco__.ha_ganado())
    
    def test_ha_ganado_true(self):
        """
        Prueba ha_ganado cuando ha sacado todas las fichas.
        
        Recibe: Nada
        Hace: Verifica rama if == 15 devuelve True (linea 25)
        Devuelve: Nada
        """
        # agregar 15 fichas sacadas
        contador = 0
        while contador < 15:
            self.__jugador_blanco__.agregar_ficha_sacada()
            contador = contador + 1
        
        self.assertTrue(self.__jugador_blanco__.ha_ganado())
    
    # ===== TESTS DE CASOS LIMITE =====
    
    def test_multiples_operaciones(self):
        """
        Prueba multiples operaciones en secuencia.
        
        Recibe: Nada
        Hace: Verifica que todo funciona correctamente
        Devuelve: Nada
        """
        # agregar a barra
        self.__jugador_blanco__.agregar_ficha_a_barra()
        self.__jugador_blanco__.agregar_ficha_a_barra()
        self.assertEqual(self.__jugador_blanco__.get_fichas_en_barra(), 2)
        
        # agregar sacadas
        self.__jugador_blanco__.agregar_ficha_sacada()
        self.assertEqual(self.__jugador_blanco__.get_fichas_sacadas(), 1)
        
        # quitar de barra
        self.__jugador_blanco__.quitar_ficha_de_barra()
        self.assertEqual(self.__jugador_blanco__.get_fichas_en_barra(), 1)
        
        # agregar mas sacadas
        contador = 0
        while contador < 14:
            self.__jugador_blanco__.agregar_ficha_sacada()
            contador = contador + 1
        
        # verificar ganador
        self.assertTrue(self.__jugador_blanco__.ha_ganado())
    
    def test_jugadores_independientes(self):
        """
        Prueba que los jugadores son independientes.
        
        Recibe: Nada
        Hace: Verifica que modificar uno no afecta al otro
        Devuelve: Nada
        """
        # modificar jugador blanco
        self.__jugador_blanco__.agregar_ficha_a_barra()
        self.__jugador_blanco__.agregar_ficha_sacada()
        
        # verificar que el negro no cambio
        self.assertEqual(self.__jugador_negro__.get_fichas_en_barra(), 0)
        self.assertEqual(self.__jugador_negro__.get_fichas_sacadas(), 0)
        self.assertFalse(self.__jugador_negro__.tiene_fichas_en_barra())
        self.assertFalse(self.__jugador_negro__.ha_ganado())

    def test_str_representacion(self):
        """
        Prueba la representacion en texto del jugador.
        """
        descripcion_blanco = str(self.__jugador_blanco__)
        self.assertIn("Ana", descripcion_blanco)
        self.assertIn("derecha", descripcion_blanco)

        descripcion_negro = str(self.__jugador_negro__)
        self.assertIn("Luis", descripcion_negro)
        self.assertIn("izquierda", descripcion_negro)


if __name__ == "__main__":
    unittest.main()
