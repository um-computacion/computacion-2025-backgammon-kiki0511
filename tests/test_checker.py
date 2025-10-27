import unittest
from core.checker import Checker


class TestChecker(unittest.TestCase):
    """
    Clase de pruebas para Checker con 100% de cobertura.
    
    Recibe: Nada
    Hace: Prueba todos los metodos de Checker
    Devuelve: Nada
    """
    
    def setUp(self):
        """
        Configuracion inicial para cada test.
        
        Recibe: Nada
        Hace: Crea fichas blanca y negra para cada test
        Devuelve: Nada
        """
        self.__ficha_blanca__ = Checker('blanco')
        self.__ficha_negra__ = Checker('negro')
    
    # ===== TESTS DE INICIALIZACION =====
    
    def test_crear_ficha_blanca(self):
        """
        Una ficha blanca debe crearse correctamente.
        
        Recibe: Nada
        Hace: Verifica inicializacion de ficha blanca
        Devuelve: Nada
        """
        self.assertEqual(self.__ficha_blanca__.get_color(), 'blanco')
        self.assertIsNone(self.__ficha_blanca__.get_posicion())
    
    def test_crear_ficha_negra(self):
        """
        Una ficha negra debe crearse correctamente.
        
        Recibe: Nada
        Hace: Verifica inicializacion de ficha negra
        Devuelve: Nada
        """
        self.assertEqual(self.__ficha_negra__.get_color(), 'negro')
        self.assertIsNone(self.__ficha_negra__.get_posicion())
    
    def test_ficha_no_esta_en_barra_inicialmente(self):
        """
        Una ficha nueva no debe estar en la barra.
        
        Recibe: Nada
        Hace: Verifica que esta_en_barra devuelve False
        Devuelve: Nada
        """
        self.assertFalse(self.__ficha_blanca__.esta_en_barra())
        self.assertFalse(self.__ficha_negra__.esta_en_barra())
    
    def test_ficha_no_esta_sacada_inicialmente(self):
        """
        Una ficha nueva no debe estar sacada.
        
        Recibe: Nada
        Hace: Verifica que esta_sacada devuelve False
        Devuelve: Nada
        """
        self.assertFalse(self.__ficha_blanca__.esta_sacada())
        self.assertFalse(self.__ficha_negra__.esta_sacada())
    
    # ===== TESTS DE POSICION =====
    
    def test_establecer_posicion_normal(self):
        """
        Debe poder establecer una posicion normal en el tablero.
        
        Recibe: Nada
        Hace: Verifica set_posicion con valor normal
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(13)
        self.assertEqual(self.__ficha_blanca__.get_posicion(), 13)
    
    def test_establecer_posicion_barra(self):
        """
        Debe poder establecer la posicion en la barra (0).
        
        Recibe: Nada
        Hace: Verifica posicion 0 y esta_en_barra
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(0)
        self.assertEqual(self.__ficha_blanca__.get_posicion(), 0)
        self.assertTrue(self.__ficha_blanca__.esta_en_barra())
        self.assertFalse(self.__ficha_blanca__.esta_sacada())
    
    def test_establecer_posicion_sacada(self):
        """
        Debe poder establecer la posicion como sacada (25).
        
        Recibe: Nada
        Hace: Verifica posicion 25 y esta_sacada
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(25)
        self.assertEqual(self.__ficha_blanca__.get_posicion(), 25)
        self.assertFalse(self.__ficha_blanca__.esta_en_barra())
        self.assertTrue(self.__ficha_blanca__.esta_sacada())
    
    def test_cambiar_posicion_multiples_veces(self):
        """
        Debe poder cambiar la posicion varias veces.
        
        Recibe: Nada
        Hace: Verifica multiples cambios de posicion
        Devuelve: Nada
        """
        # posicion inicial
        self.__ficha_blanca__.set_posicion(24)
        self.assertEqual(self.__ficha_blanca__.get_posicion(), 24)
        
        # mover a otro punto
        self.__ficha_blanca__.set_posicion(18)
        self.assertEqual(self.__ficha_blanca__.get_posicion(), 18)
        
        # mover a la barra
        self.__ficha_blanca__.set_posicion(0)
        self.assertTrue(self.__ficha_blanca__.esta_en_barra())
        
        # sacar del tablero
        self.__ficha_blanca__.set_posicion(25)
        self.assertTrue(self.__ficha_blanca__.esta_sacada())
    
    # ===== TESTS DE ESTA_EN_BARRA (CUBRIR LINEA 39) =====
    
    def test_esta_en_barra_true_cuando_posicion_0(self):
        """
        Debe devolver True cuando la posicion es 0.
        
        Recibe: Nada
        Hace: Cubre la rama if posicion == 0 (linea 39)
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(0)
        resultado = self.__ficha_blanca__.esta_en_barra()
        self.assertTrue(resultado)
    
    def test_esta_en_barra_false_cuando_posicion_no_0(self):
        """
        Debe devolver False cuando la posicion no es 0.
        
        Recibe: Nada
        Hace: Cubre la rama else (retorna False)
        Devuelve: Nada
        """
        # probar con varias posiciones
        self.__ficha_blanca__.set_posicion(1)
        self.assertFalse(self.__ficha_blanca__.esta_en_barra())
        
        self.__ficha_blanca__.set_posicion(12)
        self.assertFalse(self.__ficha_blanca__.esta_en_barra())
        
        self.__ficha_blanca__.set_posicion(25)
        self.assertFalse(self.__ficha_blanca__.esta_en_barra())
    
    def test_esta_en_barra_false_cuando_posicion_none(self):
        """
        Debe devolver False cuando la posicion es None.
        
        Recibe: Nada
        Hace: Cubre el caso None
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(None)
        self.assertFalse(self.__ficha_blanca__.esta_en_barra())
    
    # ===== TESTS DE ESTA_SACADA (CUBRIR LINEAS 59-62) =====
    
    def test_esta_sacada_false_cuando_posicion_none(self):
        """
        Debe devolver False cuando la posicion es None.
        
        Recibe: Nada
        Hace: Cubre la rama if posicion == None (linea 59)
        Devuelve: Nada
        """
        # la ficha nueva tiene posicion None
        resultado = self.__ficha_blanca__.esta_sacada()
        self.assertFalse(resultado)
    
    def test_esta_sacada_true_cuando_posicion_25(self):
        """
        Debe devolver True cuando la posicion es 25.
        
        Recibe: Nada
        Hace: Cubre la rama if posicion == 25 (linea 61)
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(25)
        resultado = self.__ficha_blanca__.esta_sacada()
        self.assertTrue(resultado)
    
    def test_esta_sacada_false_cuando_posicion_no_25(self):
        """
        Debe devolver False cuando la posicion no es 25.
        
        Recibe: Nada
        Hace: Cubre la rama else (linea 62)
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(0)
        self.assertFalse(self.__ficha_blanca__.esta_sacada())
        
        self.__ficha_blanca__.set_posicion(12)
        self.assertFalse(self.__ficha_blanca__.esta_sacada())
        
        self.__ficha_blanca__.set_posicion(24)
        self.assertFalse(self.__ficha_blanca__.esta_sacada())
    
    # ===== TESTS DE __STR__ (CUBRIR LINEAS 72-75) =====
    
    def test_str_ficha_blanca(self):
        """
        La representacion en string de ficha blanca debe ser B.
        
        Recibe: Nada
        Hace: Cubre la rama if color == blanco (linea 72)
        Devuelve: Nada
        """
        resultado = str(self.__ficha_blanca__)
        self.assertEqual(resultado, 'B')
    
    def test_str_ficha_negra(self):
        """
        La representacion en string de ficha negra debe ser N.
        
        Recibe: Nada
        Hace: Cubre la rama else (linea 75)
        Devuelve: Nada
        """
        resultado = str(self.__ficha_negra__)
        self.assertEqual(resultado, 'N')
    
    def test_str_no_cambia_con_posicion(self):
        """
        La representacion en string no debe cambiar segun la posicion.
        
        Recibe: Nada
        Hace: Verifica que str es consistente
        Devuelve: Nada
        """
        # ficha blanca en diferentes posiciones
        posiciones = [None, 0, 12, 25]
        for pos in posiciones:
            self.__ficha_blanca__.set_posicion(pos)
            self.assertEqual(str(self.__ficha_blanca__), 'B')
        
        # ficha negra en diferentes posiciones
        for pos in posiciones:
            self.__ficha_negra__.set_posicion(pos)
            self.assertEqual(str(self.__ficha_negra__), 'N')
    
    # ===== TESTS DE CASOS LIMITE =====
    
    def test_posicion_none_no_es_barra_ni_sacada(self):
        """
        Una posicion None no debe considerarse barra ni sacada.
        
        Recibe: Nada
        Hace: Verifica ambos metodos con None
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(None)
        self.assertFalse(self.__ficha_blanca__.esta_en_barra())
        self.assertFalse(self.__ficha_blanca__.esta_sacada())
        self.assertIsNone(self.__ficha_blanca__.get_posicion())
    
    def test_colores_diferentes_son_diferentes(self):
        """
        Fichas de colores diferentes deben tener colores diferentes.
        
        Recibe: Nada
        Hace: Verifica que los colores no son iguales
        Devuelve: Nada
        """
        self.assertNotEqual(self.__ficha_blanca__.get_color(),
                           self.__ficha_negra__.get_color())
    
    def test_fichas_independientes(self):
        """
        Las fichas deben ser independientes entre si.
        
        Recibe: Nada
        Hace: Verifica que cambiar una no afecta la otra
        Devuelve: Nada
        """
        self.__ficha_blanca__.set_posicion(10)
        self.__ficha_negra__.set_posicion(20)
        
        # cambiar una no debe afectar la otra
        self.assertEqual(self.__ficha_blanca__.get_posicion(), 10)
        self.assertEqual(self.__ficha_negra__.get_posicion(), 20)
        
        self.__ficha_blanca__.set_posicion(0)
        self.assertEqual(self.__ficha_negra__.get_posicion(), 20)
    
    def test_todas_las_posiciones_validas(self):
        """
        Debe poder establecer cualquier posicion valida del tablero.
        
        Recibe: Nada
        Hace: Prueba posiciones 0-25
        Devuelve: Nada
        """
        posiciones_validas = list(range(0, 26))
        
        for pos in posiciones_validas:
            self.__ficha_blanca__.set_posicion(pos)
            self.assertEqual(self.__ficha_blanca__.get_posicion(), pos)
            
            # verificar estados especiales
            if pos == 0:
                self.assertTrue(self.__ficha_blanca__.esta_en_barra())
            elif pos == 25:
                self.assertTrue(self.__ficha_blanca__.esta_sacada())
            else:
                self.assertFalse(self.__ficha_blanca__.esta_en_barra())
                self.assertFalse(self.__ficha_blanca__.esta_sacada())


if __name__ == "__main__":
    unittest.main()