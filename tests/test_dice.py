import unittest
from unittest.mock import patch
from core.dice import Dice

class TestDice(unittest.TestCase):

    #Se ejecuta antes de cada test para preparar el dado
    def setUp(self):
        self.dice = Dice()
    
    #Verifica que con dados diferentes se devuelvan solo 2 valores
         # Simulamos dados con valores diferentes
    def test_tirar_retorna_valores_normales_sin_dobles(self):
        with patch('core.dice.random.randint', side_effect=[2, 5]):
            resultado = self.dice.tirar()
            
        self.assertEqual(resultado, [2, 5])
    
    #Verifica que con dados iguales se devuelvan 4 valores
        # Simulamos dados con valores iguales (dobles)
    def test_tirar_retorna_cuatro_valores_cuando_son_dobles(self):
        with patch('core.dice.random.randint', side_effect=[4, 4]):
            resultado = self.dice.tirar()
            
        self.assertEqual(resultado, [4, 4, 4, 4])
    
    #Verifica que se guarde correctamente la última tirada
    def test_ultima_tirada_se_actualiza_correctamente(self):
        with patch('core.dice.random.randint', side_effect=[3, 6]):
            self.dice.tirar()
        
        ultima_tirada = self.dice.get_ultima_tirada()
        self.assertEqual(ultima_tirada, [3, 6])
    
    #Verifica que sin tirar dados, es_doble() sea False
    def test_es_doble_retorna_false_sin_tirar_dados(self):
        resultado = self.dice.es_doble()
        self.assertFalse(resultado)
    
    #Verifica que con valores iguales, es_doble() sea True
    def test_es_doble_retorna_true_cuando_valores_son_iguales(self):
        with patch('core.dice.random.randint', side_effect=[1, 1]):
            self.dice.tirar()
        
        resultado = self.dice.es_doble()
        self.assertTrue(resultado)


class MockDice:
    """Mock simple que simula dados con valores predefinidos"""
    def __init__(self, valores_predefinidos):
        self.valores = valores_predefinidos
        self.indice = 0
    
    def tirar(self):
        if self.indice < len(self.valores):
            resultado = self.valores[self.indice]
            self.indice += 1
            return resultado
        return [1, 1]

def ejemplo_uso_mock_manual():
    """Muestra cómo usar un mock manual para tests predecibles"""
    mock_dice = MockDice([[2, 5], [4, 4, 4, 4]])
    
    resultado1 = mock_dice.tirar()
    print(f"Primera tirada: {resultado1}")
    
    resultado2 = mock_dice.tirar()
    print(f"Segunda tirada: {resultado2}")

if __name__ == '__main__':
    unittest.main()