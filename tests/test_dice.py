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
    
   