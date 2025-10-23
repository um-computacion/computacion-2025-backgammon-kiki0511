import unittest
import random
from core.dice import Dice


class TestDiceCobertura100(unittest.TestCase):
    """
    Tests para cubrir el 100% del codigo original.
    
    Recibe: Nada
    Hace: Cubre todas las lineas y ramas del codigo
    Devuelve: Nada
    """
    
    def setUp(self):
        """
        Prepara el ambiente antes de cada prueba.
        
        Recibe: Nada
        Hace: Crea un objeto Dice nuevo
        Devuelve: Nada
        """
        self.dice = Dice()
    
    def test_init_crea_objeto(self):
        """
        Prueba que __init__ crea el objeto correctamente.
        
        Recibe: Nada
        Hace: Verifica la inicializacion
        Devuelve: Nada
        """
        # crear un dado nuevo
        dado_nuevo = Dice()
        # verificar que se inicializa con None
        self.assertIsNone(dado_nuevo.get_ultima_tirada())
        # verificar que no es doble al inicio
        self.assertFalse(dado_nuevo.es_doble())
    
    def test_tirar_caso_no_dobles(self):
        """
        Prueba tirar cuando NO son dobles.
        
        Recibe: Nada
        Hace: Cubre la rama else del metodo tirar
        Devuelve: Nada
        """
        # guardar el original
        original = random.randint
        
        # hacer que devuelva valores diferentes
        valores = [2, 5]
        indice = [0]
        
        def mock_randint(a, b):
            # verificar parametros
            self.assertEqual(a, 1)
            self.assertEqual(b, 6)
            resultado = valores[indice[0]]
            indice[0] = indice[0] + 1
            return resultado
        
        random.randint = mock_randint
        
        try:
            # tirar los dados
            resultado = self.dice.tirar()
            
            # verificar que se ejecuto el else (no dobles)
            self.assertEqual(len(resultado), 2)
            self.assertEqual(resultado[0], 2)
            self.assertEqual(resultado[1], 5)
            
            # verificar que se guardo
            self.assertEqual(self.dice.get_ultima_tirada(), resultado)
            
            # verificar que no es doble
            self.assertFalse(self.dice.es_doble())
        finally:
            random.randint = original
    
    def test_tirar_caso_dobles(self):
        """
        Prueba tirar cuando SI son dobles.
        
        Recibe: Nada
        Hace: Cubre la rama if del metodo tirar
        Devuelve: Nada
        """
        # guardar el original
        original = random.randint
        
        # hacer que devuelva valores iguales
        def mock_randint(a, b):
            # verificar parametros
            self.assertEqual(a, 1)
            self.assertEqual(b, 6)
            return 3  # siempre 3
        
        random.randint = mock_randint
        
        try:
            # tirar los dados
            resultado = self.dice.tirar()
            
            # verificar que se ejecuto el if (dobles)
            self.assertEqual(len(resultado), 4)
            # verificar cada append
            self.assertEqual(resultado[0], 3)
            self.assertEqual(resultado[1], 3)
            self.assertEqual(resultado[2], 3)
            self.assertEqual(resultado[3], 3)
            
            # verificar que se guardo
            self.assertEqual(self.dice.get_ultima_tirada(), resultado)
            
            # verificar que es doble
            self.assertTrue(self.dice.es_doble())
        finally:
            random.randint = original
    
    def test_get_ultima_tirada_devuelve_none(self):
        """
        Prueba get_ultima_tirada cuando es None.
        
        Recibe: Nada
        Hace: Cubre el return de get_ultima_tirada
        Devuelve: Nada
        """
        # sin tirar, debe ser None
        resultado = self.dice.get_ultima_tirada()
        self.assertIsNone(resultado)
    
    def test_get_ultima_tirada_devuelve_valor(self):
        """
        Prueba get_ultima_tirada cuando hay valor.
        
        Recibe: Nada
        Hace: Cubre el return con valor
        Devuelve: Nada
        """
        # hacer una tirada primero
        original = random.randint
        random.randint = lambda a, b: 4
        
        try:
            self.dice.tirar()
            # ahora debe devolver la tirada
            resultado = self.dice.get_ultima_tirada()
            self.assertIsNotNone(resultado)
            self.assertEqual(len(resultado), 4)  # dobles
        finally:
            random.randint = original
    
    def test_es_doble_cuando_none(self):
        """
        Prueba es_doble cuando ultima_tirada es None.
        
        Recibe: Nada
        Hace: Cubre la rama if == None
        Devuelve: Nada
        """
        # sin tirar debe ser False
        resultado = self.dice.es_doble()
        self.assertFalse(resultado)
        # verificar que entro al if
        self.assertIsNone(self.dice.get_ultima_tirada())
    
    def test_es_doble_cuando_len_es_4(self):
        """
        Prueba es_doble cuando len es 4.
        
        Recibe: Nada
        Hace: Cubre la rama if len == 4
        Devuelve: Nada
        """
        # hacer tirada de dobles
        original = random.randint
        random.randint = lambda a, b: 5  # siempre 5
        
        try:
            self.dice.tirar()
            # debe ser True porque len es 4
            resultado = self.dice.es_doble()
            self.assertTrue(resultado)
            # verificar que len es 4
            self.assertEqual(len(self.dice.get_ultima_tirada()), 4)
        finally:
            random.randint = original
    
    def test_es_doble_cuando_len_no_es_4(self):
        """
        Prueba es_doble cuando len no es 4.
        
        Recibe: Nada
        Hace: Cubre la rama else de es_doble
        Devuelve: Nada
        """
        # hacer tirada normal (no dobles)
        original = random.randint
        valores = [1, 2]
        indice = [0]
        
        def mock_randint(a, b):
            resultado = valores[indice[0]]
            indice[0] = indice[0] + 1
            return resultado
        
        random.randint = mock_randint
        
        try:
            self.dice.tirar()
            # debe ser False porque len es 2
            resultado = self.dice.es_doble()
            self.assertFalse(resultado)
            # verificar que len es 2
            self.assertEqual(len(self.dice.get_ultima_tirada()), 2)
        finally:
            random.randint = original
    
    def test_todas_las_lineas_del_append_dobles(self):
        """
        Prueba que se ejecutan todos los append en dobles.
        
        Recibe: Nada  
        Hace: Asegura que cada append se ejecuta
        Devuelve: Nada
        """
        original = random.randint
        
        # probar con diferentes valores de dobles
        valores_dobles = [1, 2, 3, 4, 5, 6]
        
        for valor in valores_dobles:
            random.randint = lambda a, b: valor
            
            try:
                resultado = self.dice.tirar()
                # verificar que se hicieron 4 appends
                self.assertEqual(len(resultado), 4)
                # verificar cada posicion
                self.assertEqual(resultado[0], valor)
                self.assertEqual(resultado[1], valor)
                self.assertEqual(resultado[2], valor)
                self.assertEqual(resultado[3], valor)
            finally:
                random.randint = original
    
    def test_todas_las_lineas_del_append_no_dobles(self):
        """
        Prueba que se ejecutan los append en no dobles.
        
        Recibe: Nada
        Hace: Asegura que cada append se ejecuta
        Devuelve: Nada
        """
        original = random.randint
        
        # diferentes combinaciones
        combinaciones = [
            [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
            [2, 3], [2, 4], [2, 5], [2, 6],
            [3, 4], [3, 5], [3, 6],
            [4, 5], [4, 6],
            [5, 6]
        ]
        
        for combo in combinaciones:
            indice = [0]
            
            def hacer_mock(valores):
                idx = [0]
                def mock_randint(a, b):
                    resultado = valores[idx[0]]
                    idx[0] = idx[0] + 1
                    return resultado
                return mock_randint
            
            random.randint = hacer_mock(combo)
            
            try:
                resultado = self.dice.tirar()
                # verificar que se hicieron 2 appends
                self.assertEqual(len(resultado), 2)
                # verificar cada posicion
                self.assertEqual(resultado[0], combo[0])
                self.assertEqual(resultado[1], combo[1])
            finally:
                random.randint = original
    
    def test_asignacion_ultima_tirada(self):
        """
        Prueba que se asigna correctamente ultima_tirada.
        
        Recibe: Nada
        Hace: Verifica la linea de asignacion
        Devuelve: Nada
        """
        original = random.randint
        
        # primer caso: dobles
        random.randint = lambda a, b: 6
        
        try:
            resultado1 = self.dice.tirar()
            guardado1 = self.dice.get_ultima_tirada()
            # verificar que son el mismo objeto
            self.assertEqual(resultado1, guardado1)
            self.assertIs(resultado1, guardado1)
        finally:
            random.randint = original
        
        # segundo caso: no dobles
        valores = [3, 4]
        indice = [0]
        
        def mock_randint(a, b):
            resultado = valores[indice[0]]
            indice[0] = indice[0] + 1
            return resultado
        
        random.randint = mock_randint
        
        try:
            resultado2 = self.dice.tirar()
            guardado2 = self.dice.get_ultima_tirada()
            # verificar que son el mismo objeto
            self.assertEqual(resultado2, guardado2)
            self.assertIs(resultado2, guardado2)
        finally:
            random.randint = original
    
    def test_flujo_completo_multiples_tiradas(self):
        """
        Prueba flujo completo con varias tiradas.
        
        Recibe: Nada
        Hace: Ejecuta todas las ramas en secuencia
        Devuelve: Nada
        """
        original = random.randint
        
        # empezar sin tirada
        self.assertIsNone(self.dice.get_ultima_tirada())
        self.assertFalse(self.dice.es_doble())
        
        # primera tirada: no dobles
        valores1 = [2, 6]
        indice1 = [0]
        
        def mock1(a, b):
            resultado = valores1[indice1[0]]
            indice1[0] = indice1[0] + 1
            return resultado
        
        random.randint = mock1
        
        try:
            resultado1 = self.dice.tirar()
            self.assertEqual(resultado1, [2, 6])
            self.assertFalse(self.dice.es_doble())
        finally:
            random.randint = original
        
        # segunda tirada: dobles
        random.randint = lambda a, b: 1
        
        try:
            resultado2 = self.dice.tirar()
            self.assertEqual(resultado2, [1, 1, 1, 1])
            self.assertTrue(self.dice.es_doble())
        finally:
            random.randint = original
        
        # tercera tirada: no dobles otra vez
        valores3 = [5, 3]
        indice3 = [0]
        
        def mock3(a, b):
            resultado = valores3[indice3[0]]
            indice3[0] = indice3[0] + 1
            return resultado
        
        random.randint = mock3
        
        try:
            resultado3 = self.dice.tirar()
            self.assertEqual(resultado3, [5, 3])
            self.assertFalse(self.dice.es_doble())
        finally:
            random.randint = original


if __name__ == "__main__":
    # ejecutar con mas detalle
    unittest.main(verbosity=2)