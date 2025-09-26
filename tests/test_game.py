import unittest
from unittest.mock import patch, MagicMock
from core.game import BackgammonGame
from core.exceptions import *


class TestBackgammonGame(unittest.TestCase):
  
   def setUp(self):
       #configuracion inicial para cada test
       self.juego = BackgammonGame("Jugador1", "Jugador2")
  
   # ===== TESTS DE INICIALIZACION =====
  
   def test_crear_juego_correctamente(self):
       #Un juego nuevo debe crearse con todos los componentes
       self.assertEqual(self.juego.get_jugador1().get_nombre(), "Jugador1")
       self.assertEqual(self.juego.get_jugador2().get_nombre(), "Jugador2")
       self.assertEqual(self.juego.get_jugador_actual(), self.juego.get_jugador1())
       self.assertFalse(self.juego.esta_terminado())
       self.assertIsNone(self.juego.get_ganador())
  
   def test_jugadores_tienen_direcciones_correctas(self):
       #Los jugadores deben tener direcciones opuestas
       self.assertEqual(self.juego.get_jugador1().get_direccion(), 1)  # Derecha
       self.assertEqual(self.juego.get_jugador2().get_direccion(), -1)  # Izquierda
  
   def test_tablero_inicializado_correctamente(self):
       # El tablero debe estar en posicion inicial
       tablero = self.juego.get_tablero()
       # Verificar algunas posiciones iniciales
       self.assertEqual(tablero.contar_fichas_en_punto(24), 2)  # Fichas blancas
       self.assertEqual(tablero.contar_fichas_en_punto(1), 2)   # Fichas negras
  
   def test_sin_movimientos_disponibles_inicialmente(self):
       #No debe haber movimientos disponibles antes de tirar dados
       self.assertEqual(len(self.juego.get_movimientos_disponibles()), 0)
  
 # ===== TESTS DE TIRADA DE DADOS =====
  
   @patch('core.dice.random.randint')
   def test_tirar_dados_normal(self, mock_randint):
       #Debe poder tirar dados y obtener movimientos normales
       mock_randint.side_effect = [3, 5]
      
       resultado = self.juego.tirar_dados()
      
       self.assertEqual(resultado, [3, 5])
       self.assertEqual(self.juego.get_movimientos_disponibles(), [3, 5])
  
   @patch('core.dice.random.randint')
   def test_tirar_dados_dobles(self, mock_randint):
       #Debe poder tirar dobles y obtener 4 movimientos
       mock_randint.side_effect = [4, 4]
      
       resultado = self.juego.tirar_dados()
      
       self.assertEqual(resultado, [4, 4, 4, 4])
       self.assertEqual(self.juego.get_movimientos_disponibles(), [4, 4, 4, 4])
  
   def test_no_puede_tirar_dados_si_ya_tiro(self):
       #No debe poder tirar dados si ya tirÃ³ en este turno
       with patch('core.dice.random.randint', side_effect=[2, 6]):
           self.juego.tirar_dados()
          
           # Intentar tirar de nuevo debera fallar
           with self.assertRaises(TurnoIncorrectoError):
               self.juego.tirar_dados()
  
   # ===== TESTS DE COLORES DE JUGADORES =====
  
   def test_color_jugador_actual_inicial(self):
       #El primer jugador debe ser blanco
       self.assertEqual(self.juego.get_color_jugador_actual(), 'blanco')
  
   def test_color_jugador_cambia_con_turno(self):
       #El color debe cambiar cuando cambia el turno
       self.assertEqual(self.juego.get_color_jugador_actual(), 'blanco')
      
       self.juego.terminar_turno()
       self.assertEqual(self.juego.get_color_jugador_actual(), 'negro')
      
       self.juego.terminar_turno()
       self.assertEqual(self.juego.get_color_jugador_actual(), 'blanco')
  
 # ===== TESTS DE CALCULO DE DESTINOS =====
  
   def test_calcular_punto_destino_jugador_blanco(self):
       #Jugador blanco debe mover hacia numeros menores
       # Jugador 1 (blanco) mueve hacia la derecha (numeros decrecientes)
       destino = self.juego.calcular_punto_destino(13, 5)
       self.assertEqual(destino, 8)  # 13 - 5 = 8
  
   def test_calcular_punto_destino_jugador_negro(self):
       #Jugador negro debe mover hacia numeros mayores
       # Cambiar al jugador 2 (negro)
       self.juego.terminar_turno()
      
       destino = self.juego.calcular_punto_destino(12, 3)
       self.assertEqual(destino, 15)  # 12 + 3 = 15
  
   # ===== TESTS DE VALIDACION DE MOVIMIENTOS =====
  
   @patch('core.dice.random.randint')
   def test_puede_hacer_movimiento_valido(self, mock_randint):
       #Debe poder validar movimientos correctos
       mock_randint.side_effect = [2, 3]
       self.juego.tirar_dados()
      
       # Mover ficha blanca del punto 24
       self.assertTrue(self.juego.puede_hacer_movimiento(24, 2))
       self.assertTrue(self.juego.puede_hacer_movimiento(24, 3))
  
   @patch('core.dice.random.randint')
   def test_no_puede_hacer_movimiento_sin_dados(self, mock_randint):
       # No debe poder hacer movimientos sin dados disponibles
       # No tirar dados
       self.assertFalse(self.juego.puede_hacer_movimiento(24, 3))
  
   @patch('core.dice.random.randint')
   def test_no_puede_usar_valor_no_disponible(self, mock_randint):
       #No debe poder usar un valor de dado que no tiene
       mock_randint.side_effect = [2, 3]
       self.juego.tirar_dados()
      
       # Intentar usar un 5 cuando solo tiene 2 y 3
       self.assertFalse(self.juego.puede_hacer_movimiento(24, 5))
  
   @patch('core.dice.random.randint')
   def test_no_puede_mover_desde_punto_vacio(self, mock_randint):
       # No debe poder mover desde un punto sin fichas
       mock_randint.side_effect = [2, 3]
       self.juego.tirar_dados()
      
       # Punto 2 esta vacio inicialmente
       self.assertFalse(self.juego.puede_hacer_movimiento(2, 2))
  
   @patch('core.dice.random.randint')
   def test_no_puede_mover_ficha_enemiga(self, mock_randint):
       # No debe poder mover fichas del oponente
       mock_randint.side_effect = [2, 3]
       self.juego.tirar_dados()
      
       # Punto 1 tiene fichas negras, jugador actual es blanco
       self.assertFalse(self.juego.puede_hacer_movimiento(1, 2))
        
    # ===== TESTS DE EJECUCIÃ“N DE MOVIMIENTOS =====
  
   @patch('core.dice.random.randint')
   def test_hacer_movimiento_exitoso(self, mock_randint):
       #Debe poder ejecutar movimientos validos
       mock_randint.side_effect = [1, 2]
       self.juego.tirar_dados()
      
       # Mover ficha del punto 24
       resultado = self.juego.hacer_movimiento(24, 1)
      
       self.assertTrue(resultado)
       self.assertEqual(self.juego.get_movimientos_disponibles(), [2])  # Solo queda el 2
  
   @patch('core.dice.random.randint')
   def test_hacer_movimiento_invalido(self, mock_randint):
       #Movimientos invalidos deben fallar
       mock_randint.side_effect = [1, 2]
       self.juego.tirar_dados()
      
       # Intentar mover desde punto vacio
       resultado = self.juego.hacer_movimiento(3, 1)
      
       self.assertFalse(resultado)
       self.assertEqual(self.juego.get_movimientos_disponibles(), [1, 2])  # No se consume
  
   @patch('core.dice.random.randint')
   def test_movimiento_agota_dados(self, mock_randint):
       #Usar todos los dados debe terminar el turno automaticamente
       mock_randint.side_effect = [1, 1]  # Movimientos pequeños
       self.juego.tirar_dados()
      
       # Hacer ambos movimientos
       self.juego.hacer_movimiento(24, 1)
       self.juego.hacer_movimiento(24, 1)
      
       # Debe cambiar automÃ¡ticamente al siguiente jugador
       self.assertEqual(self.juego.get_jugador_actual(), self.juego.get_jugador2())
  
   # ===== TESTS DE TURNOS =====
  
   def test_terminar_turno_cambia_jugador(self):
       #Terminar turno debe cambiar al otro jugador
       jugador_inicial = self.juego.get_jugador_actual()
      
       self.juego.terminar_turno()
      
       self.assertNotEqual(self.juego.get_jugador_actual(), jugador_inicial)
       self.assertEqual(len(self.juego.get_movimientos_disponibles()), 0)
  
   def test_terminar_turno_limpia_movimientos(self):
       #Terminar turno debe limpiar movimientos disponibles
       with patch('core.dice.random.randint', side_effect=[3, 5]):
           self.juego.tirar_dados()
           self.assertEqual(len(self.juego.get_movimientos_disponibles()), 2)
          
           self.juego.terminar_turno()
           self.assertEqual(len(self.juego.get_movimientos_disponibles()), 0)
  
   # ===== TESTS DE DETECCION DE MOVIMIENTOS DISPONIBLES =====
  
   @patch('core.dice.random.randint')
   def test_puede_hacer_algun_movimiento_true(self, mock_randint):
       #Debe detectar cuando hay movimientos disponibles
       mock_randint.side_effect = [1, 2]
       self.juego.tirar_dados()
      
       self.assertTrue(self.juego.puede_hacer_algun_movimiento())
  
   def test_puede_hacer_algun_movimiento_false_sin_dados(self):
       #Sin dados no debe poder hacer movimientos
       # No tirar dados
       self.assertFalse(self.juego.puede_hacer_algun_movimiento())
  
   # ===== TESTS DE ESTADO DEL JUEGO =====
  
   def test_get_estado_juego_inicial(self):
       #El estado inicial debe ser correcto
       estado = self.juego.get_estado_juego()
      
       self.assertEqual(estado['jugador_actual'], "Jugador1")
       self.assertEqual(estado['color_actual'], 'blanco')
       self.assertEqual(estado['movimientos_disponibles'], [])
       self.assertFalse(estado['juego_terminado'])
       self.assertIsNone(estado['ganador'])
  
   @patch('core.dice.random.randint')
   def test_get_estado_juego_con_movimientos(self, mock_randint):
       #El estado debe reflejar movimientos disponibles
       mock_randint.side_effect = [4, 6]
       self.juego.tirar_dados()
      
       estado = self.juego.get_estado_juego()
      
       self.assertEqual(estado['movimientos_disponibles'], [4, 6])
  
   # ===== TESTS DE VICTORIA =====
  
   def test_verificar_victoria_no_ganador_inicial(self):
       #Al inicio no debe haber ganador
       self.juego.verificar_victoria()
      
       self.assertFalse(self.juego.esta_terminado())
       self.assertIsNone(self.juego.get_ganador())
  
   def test_detectar_victoria_simulada(self):
       #Debe detectar victoria cuando un jugador saca 15 fichas
       # Simular que el jugador blanco saca todas las fichas
       tablero = self.juego.get_tablero()
      
       # Limpiar tablero y poner todas las fichas como sacadas
       for punto in range(26):
           tablero.get_fichas_en_punto(punto).clear()
      
       # Agregar 15 fichas blancas a la zona de sacado
       from core.checker import Checker
       for i in range(15):
           ficha = Checker('blanco')
           ficha.set_posicion(25)
           tablero.get_fichas_en_punto(25).append(ficha)
      
       # Verificar victoria
       self.juego.verificar_victoria()
      
       self.assertTrue(self.juego.esta_terminado())
       self.assertEqual(self.juego.get_ganador(), self.juego.get_jugador1())
  
   # ===== TESTS DE REPRESENTACION =====
  
   def test_str_juego_contiene_info_basica(self):
       #La representacion string debe contener informacion basica
       resultado = str(self.juego)
      
       self.assertIn("BACKGAMMON", resultado)
       self.assertIn("Jugador1", resultado)
       self.assertIn("Jugador2", resultado)
       self.assertIn("Blancas", resultado)
       self.assertIn("Negras", resultado)
  
   @patch('core.dice.random.randint')
   def test_str_juego_con_movimientos(self, mock_randint):
       # Debe mostrar movimientos cuando estan disponibles
       mock_randint.side_effect = [3, 5]
       self.juego.tirar_dados()
      
       resultado = str(self.juego)
      
       self.assertIn("Movimientos disponibles", resultado)
       self.assertIn("[3, 5]", resultado)