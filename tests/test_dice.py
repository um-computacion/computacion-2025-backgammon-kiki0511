import unittest
from unittest.mock import patch
from core.dice import Dice


class TestDice(unittest.TestCase):
    
    def setUp(self):
    #Configuración inicial para cada test
        self.dice = Dice()
    
    # Metodos helper para hacer los tests más legibles 
    
    def _simular_tirada_normal(self, valor1, valor2):
        #Helper: simula una tirada sin dobles
        with patch('core.dice.random.randint', side_effect=[valor1, valor2]):
            return self.dice.tirar()
    
    def _simular_tirada_doble(self, valor):
        #Helper: simula una tirada con dobles#
        with patch('core.dice.random.randint', side_effect=[valor, valor]):
            return self.dice.tirar()
    
    def _verificar_valores_en_rango(self, resultado):
        #Helper: verifica que todos los valores estén entre 1 y 6 #
        for valor in resultado:
            self.assertGreaterEqual(valor, 1, f"Valor {valor} es menor a 1")
            self.assertLessEqual(valor, 6, f"Valor {valor} es mayor a 6")
    
    #  Tests del estado inicial 
    
    def test_estado_inicial_es_correcto(self):
        #El dado debe empezar sin tiradas previas
        self.assertIsNone(self.dice.get_ultima_tirada())
        self.assertFalse(self.dice.es_doble())
    
    #  Tests de tiradas normales (sin dobles) 
    
    def test_tirada_normal_devuelve_dos_valores(self):
        #Una tirada normal debe devolver exactamente 2 valores
        resultado = self._simular_tirada_normal(2, 5)
        
        self.assertEqual(resultado, [2, 5])
        self.assertEqual(len(resultado), 2)
    
    def test_tirada_normal_actualiza_estado(self):
        #Una tirada normal debe actualizar correctamente el estado
        resultado = self._simular_tirada_normal(3, 6)
        
        self.assertEqual(self.dice.get_ultima_tirada(), [3, 6])
        self.assertFalse(self.dice.es_doble())
    
    def test_tirada_normal_valores_en_rango(self):
        #Los valores de una tirada normal deben estar entre 1 y 6
        resultado = self._simular_tirada_normal(1, 6)
        self._verificar_valores_en_rango(resultado)
    #  Tests de tiradas con dobles 
    
    def test_tirada_doble_devuelve_cuatro_valores(self):
        #Una tirada doble debe devolver exactamente 4 valores iguales
        resultado = self._simular_tirada_doble(4)
        
        self.assertEqual(resultado, [4, 4, 4, 4])
        self.assertEqual(len(resultado), 4)
    
    def test_tirada_doble_actualiza_estado(self):
        #Una tirada doble debe actualizar correctamente el estado
        resultado = self._simular_tirada_doble(2)
        
        self.assertEqual(self.dice.get_ultima_tirada(), [2, 2, 2, 2])
        self.assertTrue(self.dice.es_doble())
    
    def test_tirada_doble_valores_en_rango(self):
        #Los valores de una tirada doble deben estar entre 1 y 6
        resultado = self._simular_tirada_doble(6)
        self._verificar_valores_en_rango(resultado)
    
    #  Tests de transiciones entre estados 
    
    def test_transicion_normal_a_doble(self):
        #El estado debe cambiar correctamente de normal a doble.
        # Primera tirada normal
        self._simular_tirada_normal(3, 6)
        self.assertFalse(self.dice.es_doble())
        
        # Segunda tirada doble debe cambiar el estado
        self._simular_tirada_doble(5)
        self.assertTrue(self.dice.es_doble())
        self.assertEqual(self.dice.get_ultima_tirada(), [5, 5, 5, 5])
    
    def test_transicion_doble_a_normal(self):
        #El estado debe cambiar correctamente de doble a normal
        # Primera tirada doble
        self._simular_tirada_doble(1)
        self.assertTrue(self.dice.es_doble())
        
        # Segunda tirada normal debe cambiar el estado
        self._simular_tirada_normal(4, 2)
        self.assertFalse(self.dice.es_doble())
        self.assertEqual(self.dice.get_ultima_tirada(), [4, 2])
    
    def test_multiples_tiradas_mantienen_consistencia(self):
        #Múltiples tiradas deben mantener la consistencia del estado
        # Tirada normal
        self._simular_tirada_normal(1, 3)
        self.assertFalse(self.dice.es_doble())
        
        # Tirada doble
        self._simular_tirada_doble(6)
        self.assertTrue(self.dice.es_doble())
        
        # Otra tirada normal
        self._simular_tirada_normal(2, 4)
        self.assertFalse(self.dice.es_doble())
if __name__ == "__main__":
    unittest.main()