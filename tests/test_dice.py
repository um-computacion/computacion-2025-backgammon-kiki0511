import unittest
import random
from core.dice import Dice


class TestDice(unittest.TestCase):
    """
    Clase de pruebas para la clase Dice.
    
    Recibe: Nada
    Hace: Prueba todos los métodos de los dados
    Devuelve: Nada
    """
    
    def setUp(self):
        """
        Prepara el ambiente antes de cada prueba.
        
        Recibe: Nada
        Hace: Crea un objeto Dice nuevo para cada test
        Devuelve: Nada
        """
        self.__dice__ = Dice()
    
    def test_crear_dice(self):
        """
        Prueba crear un objeto Dice.
        
        Recibe: Nada
        Hace: Verifica que se crea correctamente
        Devuelve: Nada
        """
        dados = Dice()
        self.assertNotEqual(dados, None)
        ultima = dados.get_ultima_tirada()
        self.assertEqual(ultima, None)
    
    def test_tirar_dados_normal(self):
        """
        Prueba tirar dados con resultado normal.
        
        Recibe: Nada
        Hace: Fuerza una tirada normal y verifica el resultado
        Devuelve: Nada
        """
        # guardar el random original
        randint_original = random.randint
        
        # crear una funcion que simula tirada normal
        valores = [3, 5]  # diferentes
        contador = [0]
        
        def mi_randint(a, b):
            resultado = valores[contador[0]]
            contador[0] = contador[0] + 1
            return resultado
        
        # reemplazar temporalmente
        random.randint = mi_randint
        
        try:
            resultado = self.__dice__.tirar()
            self.assertEqual(resultado, [3, 5])
            self.assertEqual(len(resultado), 2)
            
            # verificar que se guardó
            ultima = self.__dice__.get_ultima_tirada()
            self.assertEqual(ultima, [3, 5])
            
            # verificar que no es doble
            es_doble = self.__dice__.es_doble()
            self.assertEqual(es_doble, False)
        finally:
            # restaurar el random original
            random.randint = randint_original
    
    def test_tirar_dados_dobles(self):
        """
        Prueba tirar dados con dobles.
        
        Recibe: Nada
        Hace: Fuerza una tirada doble y verifica el resultado
        Devuelve: Nada
        """
        # guardar el random original
        randint_original = random.randint
        
        # crear una funcion que simula dobles
        def mi_randint(a, b):
            return 4  # siempre devuelve 4
        
        # reemplazar temporalmente
        random.randint = mi_randint
        
        try:
            resultado = self.__dice__.tirar()
            self.assertEqual(resultado, [4, 4, 4, 4])
            self.assertEqual(len(resultado), 4)
            
            # verificar que se guardó
            ultima = self.__dice__.get_ultima_tirada()
            self.assertEqual(ultima, [4, 4, 4, 4])
            
            # verificar que es doble
            es_doble = self.__dice__.es_doble()
            self.assertEqual(es_doble, True)
        finally:
            # restaurar el random original
            random.randint = randint_original
    
    def test_get_ultima_tirada_sin_tirar(self):
        """
        Prueba obtener última tirada sin haber tirado.
        
        Recibe: Nada
        Hace: Verifica que devuelve None
        Devuelve: Nada
        """
        ultima = self.__dice__.get_ultima_tirada()
        self.assertEqual(ultima, None)
    
    def test_es_doble_sin_tirar(self):
        """
        Prueba es_doble sin haber tirado.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        es_doble = self.__dice__.es_doble()
        self.assertEqual(es_doble, False)
    
    def test_multiples_tiradas_seguidas(self):
        """
        Prueba varias tiradas seguidas.
        
        Recibe: Nada
        Hace: Verifica que cada tirada actualiza el estado
        Devuelve: Nada
        """
        # guardar el random original
        randint_original = random.randint
        
        # primera tirada: normal
        valores1 = [2, 5]
        contador1 = [0]
        
        def mi_randint1(a, b):
            resultado = valores1[contador1[0]]
            contador1[0] = contador1[0] + 1
            return resultado
        
        random.randint = mi_randint1
        
        try:
            resultado1 = self.__dice__.tirar()
            self.assertEqual(resultado1, [2, 5])
            self.assertEqual(self.__dice__.es_doble(), False)
        finally:
            random.randint = randint_original
        
        # segunda tirada: dobles
        def mi_randint2(a, b):
            return 6
        
        random.randint = mi_randint2
        
        try:
            resultado2 = self.__dice__.tirar()
            self.assertEqual(resultado2, [6, 6, 6, 6])
            self.assertEqual(self.__dice__.es_doble(), True)
        finally:
            random.randint = randint_original
        
        # tercera tirada: normal de nuevo
        valores3 = [1, 3]
        contador3 = [0]
        
        def mi_randint3(a, b):
            resultado = valores3[contador3[0]]
            contador3[0] = contador3[0] + 1
            return resultado
        
        random.randint = mi_randint3
        
        try:
            resultado3 = self.__dice__.tirar()
            self.assertEqual(resultado3, [1, 3])
            self.assertEqual(self.__dice__.es_doble(), False)
        finally:
            random.randint = randint_original
    
    def test_todos_los_valores_dobles_posibles(self):
        """
        Prueba todos los dobles posibles (1-1 hasta 6-6).
        
        Recibe: Nada
        Hace: Verifica que funciona con todos los valores
        Devuelve: Nada
        """
        # guardar el random original
        randint_original = random.randint
        
        valor = 1
        while valor <= 6:
            def hacer_mi_randint(v):
                def mi_randint(a, b):
                    return v
                return mi_randint
            
            random.randint = hacer_mi_randint(valor)
            
            try:
                resultado = self.__dice__.tirar()
                esperado = []
                i = 0
                while i < 4:
                    esperado.append(valor)
                    i = i + 1
                
                self.assertEqual(resultado, esperado)
                self.assertEqual(self.__dice__.es_doble(), True)
            finally:
                random.randint = randint_original
            
            valor = valor + 1
    
    def test_valores_extremos(self):
        """
        Prueba con valores extremos 1 y 6.
        
        Recibe: Nada
        Hace: Verifica que funciona con los límites
        Devuelve: Nada
        """
        # guardar el random original
        randint_original = random.randint
        
        # probar 1 y 6
        valores = [1, 6]
        contador = [0]
        
        def mi_randint(a, b):
            resultado = valores[contador[0]]
            contador[0] = contador[0] + 1
            return resultado
        
        random.randint = mi_randint
        
        try:
            resultado = self.__dice__.tirar()
            self.assertEqual(resultado, [1, 6])
            
            # verificar cada valor
            self.assertEqual(resultado[0], 1)
            self.assertEqual(resultado[1], 6)
        finally:
            random.randint = randint_original


if __name__ == "__main__":
    unittest.main()