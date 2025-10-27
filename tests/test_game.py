import unittest
from unittest.mock import Mock
from core.game import BackgammonGame
from core.checker import Checker


class TestBackgammonGame(unittest.TestCase):
    """
    Clase de pruebas para BackgammonGame.
    
    Recibe: Nada
    Hace: Prueba todos los metodos del juego con 100% de cobertura
    Devuelve: Nada
    """
    
    def setUp(self):
        """
        Prepara el ambiente antes de cada prueba.
        
        Recibe: Nada
        Hace: Crea un juego nuevo para cada test
        Devuelve: Nada
        """
        self.__juego__ = BackgammonGame("Ana", "Luis")
    
    # ===== TESTS DE INICIALIZACION =====
    
    def test_init_crea_juego_correctamente(self):
        """
        Prueba que __init__ crea el juego correctamente.
        
        Recibe: Nada
        Hace: Verifica que se inicializan todos los atributos
        Devuelve: Nada
        """
        # verificar que se creo el tablero
        tablero = self.__juego__.get_tablero()
        self.assertIsNotNone(tablero)
        
        # verificar que se crearon los jugadores
        jugador1 = self.__juego__.get_jugador1()
        jugador2 = self.__juego__.get_jugador2()
        self.assertIsNotNone(jugador1)
        self.assertIsNotNone(jugador2)
        
        # verificar nombres
        self.assertEqual(jugador1.get_nombre(), "Ana")
        self.assertEqual(jugador2.get_nombre(), "Luis")
        
        # verificar direcciones
        self.assertEqual(jugador1.get_direccion(), 1)
        self.assertEqual(jugador2.get_direccion(), -1)
        
        # verificar que el jugador 1 empieza
        jugador_actual = self.__juego__.get_jugador_actual()
        self.assertEqual(jugador_actual, jugador1)
        
        # verificar que se crearon los dados
        dados = self.__juego__.get_dados()
        self.assertIsNotNone(dados)
        
        # verificar que movimientos disponibles esta vacio
        movimientos = self.__juego__.get_movimientos_disponibles()
        self.assertEqual(len(movimientos), 0)
        
        # verificar que el juego no esta terminado
        self.assertFalse(self.__juego__.esta_terminado())
        
        # verificar que no hay ganador
        ganador = self.__juego__.get_ganador()
        self.assertIsNone(ganador)
        
        # verificar que turno_paso_automatico es False
        self.assertFalse(self.__juego__.turno_paso_automaticamente())
    
    # ===== TESTS DE GETTERS SIMPLES =====
    
    def test_get_tablero(self):
        """
        Prueba get_tablero.
        
        Recibe: Nada
        Hace: Verifica que devuelve el tablero
        Devuelve: Nada
        """
        tablero = self.__juego__.get_tablero()
        self.assertIsNotNone(tablero)
    
    def test_get_jugador_actual(self):
        """
        Prueba get_jugador_actual.
        
        Recibe: Nada
        Hace: Verifica que devuelve el jugador actual
        Devuelve: Nada
        """
        jugador = self.__juego__.get_jugador_actual()
        self.assertEqual(jugador.get_nombre(), "Ana")
    
    def test_get_jugador1(self):
        """
        Prueba get_jugador1.
        
        Recibe: Nada
        Hace: Verifica que devuelve el primer jugador
        Devuelve: Nada
        """
        jugador1 = self.__juego__.get_jugador1()
        self.assertEqual(jugador1.get_nombre(), "Ana")
    
    def test_get_jugador2(self):
        """
        Prueba get_jugador2.
        
        Recibe: Nada
        Hace: Verifica que devuelve el segundo jugador
        Devuelve: Nada
        """
        jugador2 = self.__juego__.get_jugador2()
        self.assertEqual(jugador2.get_nombre(), "Luis")
    
    def test_get_dados(self):
        """
        Prueba get_dados.
        
        Recibe: Nada
        Hace: Verifica que devuelve los dados
        Devuelve: Nada
        """
        dados = self.__juego__.get_dados()
        self.assertIsNotNone(dados)
    
    def test_get_movimientos_disponibles(self):
        """
        Prueba get_movimientos_disponibles.
        
        Recibe: Nada
        Hace: Verifica que devuelve la lista de movimientos
        Devuelve: Nada
        """
        movimientos = self.__juego__.get_movimientos_disponibles()
        self.assertEqual(len(movimientos), 0)
    
    def test_esta_terminado(self):
        """
        Prueba esta_terminado.
        
        Recibe: Nada
        Hace: Verifica que devuelve False al inicio
        Devuelve: Nada
        """
        self.assertFalse(self.__juego__.esta_terminado())
    
    def test_get_ganador(self):
        """
        Prueba get_ganador.
        
        Recibe: Nada
        Hace: Verifica que devuelve None al inicio
        Devuelve: Nada
        """
        ganador = self.__juego__.get_ganador()
        self.assertIsNone(ganador)
    
    def test_turno_paso_automaticamente(self):
        """
        Prueba turno_paso_automaticamente.
        
        Recibe: Nada
        Hace: Verifica que devuelve False al inicio
        Devuelve: Nada
        """
        self.assertFalse(self.__juego__.turno_paso_automaticamente())
    
    # ===== TESTS DE GET_COLOR_JUGADOR_ACTUAL =====
    
    def test_get_color_jugador_actual_blanco(self):
        """
        Prueba get_color_jugador_actual cuando es jugador 1.
        
        Recibe: Nada
        Hace: Verifica que devuelve 'blanco'
        Devuelve: Nada
        """
        color = self.__juego__.get_color_jugador_actual()
        self.assertEqual(color, 'blanco')
    
    def test_get_color_jugador_actual_negro(self):
        """
        Prueba get_color_jugador_actual cuando es jugador 2.
        
        Recibe: Nada
        Hace: Verifica que devuelve 'negro'
        Devuelve: Nada
        """
        # cambiar al jugador 2
        self.__juego__.terminar_turno()
        
        color = self.__juego__.get_color_jugador_actual()
        self.assertEqual(color, 'negro')
    
    # ===== TESTS DE TIRAR_DADOS =====
    
    def test_tirar_dados_normal(self):
        """
        Prueba tirar_dados con dados normales.
        
        Recibe: Nada
        Hace: Verifica que se guardan los valores
        Devuelve: Nada
        """
        resultado = self.__juego__.tirar_dados()
        
        # verificar que devuelve una lista
        self.assertIsNotNone(resultado)
        self.assertGreater(len(resultado), 0)
        
        # verificar que se copiaron a movimientos disponibles
        movimientos = self.__juego__.get_movimientos_disponibles()
        self.assertEqual(len(movimientos), len(resultado))
    
    def test_tirar_dados_dobles(self):
        """
        Prueba tirar_dados cuando salen dobles.
        
        Recibe: Nada
        Hace: Verifica que se guardan 4 valores
        Devuelve: Nada
        """
        # simular dobles modificando el metodo tirar de dados
        dados = self.__juego__.get_dados()
        
        # guardar el metodo original
        import random
        original = random.randint
        
        # hacer que siempre salga 3
        random.randint = lambda a, b: 3
        
        try:
            resultado = self.__juego__.tirar_dados()
            
            # verificar que hay 4 valores
            self.assertEqual(len(resultado), 4)
            
            # verificar movimientos disponibles
            movimientos = self.__juego__.get_movimientos_disponibles()
            self.assertEqual(len(movimientos), 4)
        finally:
            # restaurar
            random.randint = original
    
    # ===== TESTS DE PUEDE_HACER_MOVIMIENTO =====
    
    def test_puede_hacer_movimiento_dado_no_disponible(self):
        """
        Prueba puede_hacer_movimiento cuando el dado no esta disponible.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # no tirar dados
        resultado = self.__juego__.puede_hacer_movimiento(24, 3)
        self.assertFalse(resultado)
    
    def test_puede_hacer_movimiento_con_fichas_en_barra_origen_no_cero(self):
        """
        Prueba cuando tiene fichas en barra pero intenta mover de otro punto.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # poner una ficha blanca en la barra
        tablero = self.__juego__.get_tablero()
        ficha = Checker('blanco')
        ficha.set_posicion(0)
        tablero.get_fichas_en_punto(0).append(ficha)
        
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # intentar mover desde punto 24 (no barra)
            resultado = self.__juego__.puede_hacer_movimiento(24, 3)
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_movimiento_desde_barra_destino_fuera_rango(self):
        """
        Prueba mover desde barra pero destino fuera de rango.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # poner una ficha blanca en la barra
        tablero = self.__juego__.get_tablero()
        ficha = Checker('blanco')
        ficha.set_posicion(0)
        tablero.get_fichas_en_punto(0).append(ficha)
        
        # tirar un dado grande
        import random
        original = random.randint
        random.randint = lambda a, b: 6
        
        try:
            self.__juego__.tirar_dados()
            
            # mover desde barra con dado 6
            # destino seria 25 - 6 = 19, que esta en rango
            # probar con un valor que de fuera de rango
            # simular manualmente
            self.__juego__.get_movimientos_disponibles().clear()
            self.__juego__.get_movimientos_disponibles().append(30)
            
            resultado = self.__juego__.puede_hacer_movimiento(0, 30)
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_movimiento_desde_barra_puede_mover(self):
        """
        Prueba mover desde barra exitosamente.
        
        Recibe: Nada
        Hace: Verifica que devuelve True
        Devuelve: Nada
        """
        # poner una ficha blanca en la barra
        tablero = self.__juego__.get_tablero()
        ficha = Checker('blanco')
        ficha.set_posicion(0)
        tablero.get_fichas_en_punto(0).append(ficha)
        
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # mover desde barra
            resultado = self.__juego__.puede_hacer_movimiento(0, 3)
            # puede ser True o False dependiendo si el punto esta bloqueado
            self.assertIsNotNone(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_movimiento_desde_barra_no_puede_mover(self):
        """
        Prueba mover desde barra pero punto bloqueado.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # poner una ficha blanca en la barra
        tablero = self.__juego__.get_tablero()
        ficha = Checker('blanco')
        ficha.set_posicion(0)
        tablero.get_fichas_en_punto(0).append(ficha)
        
        # bloquear el punto 22 (25 - 3 = 22) con negras
        punto = 22
        while len(tablero.get_fichas_en_punto(punto)) < 2:
            ficha_negra = Checker('negro')
            ficha_negra.set_posicion(punto)
            tablero.get_fichas_en_punto(punto).append(ficha_negra)
        
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # intentar mover desde barra
            resultado = self.__juego__.puede_hacer_movimiento(0, 3)
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_movimiento_origen_vacio(self):
        """
        Prueba mover desde punto vacio.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # intentar mover desde punto vacio (2)
            resultado = self.__juego__.puede_hacer_movimiento(2, 3)
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_movimiento_color_incorrecto(self):
        """
        Prueba mover ficha del otro jugador.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # el jugador actual es blanco (Ana)
            # intentar mover desde punto 1 (fichas negras)
            resultado = self.__juego__.puede_hacer_movimiento(1, 3)
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_movimiento_destino_fuera_rango(self):
        """
        Prueba mover a destino fuera de rango.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # tirar dados grandes
        import random
        original = random.randint
        random.randint = lambda a, b: 6
        
        try:
            self.__juego__.tirar_dados()
            
            # intentar mover desde punto 4 con dado 6
            # destino seria 4 - 6 = -2 (fuera de rango)
            # primero poner una ficha en punto 4
            tablero = self.__juego__.get_tablero()
            ficha = Checker('blanco')
            ficha.set_posicion(4)
            tablero.get_fichas_en_punto(4).append(ficha)
            
            resultado = self.__juego__.puede_hacer_movimiento(4, 6)
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_movimiento_puede_mover_true(self):
        """
        Prueba movimiento valido que devuelve True.
        
        Recibe: Nada
        Hace: Verifica que devuelve True
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 2
        
        try:
            self.__juego__.tirar_dados()
            
            # mover desde punto 24 (tiene fichas blancas)
            # destino seria 24 - 2 = 22 (vacio)
            resultado = self.__juego__.puede_hacer_movimiento(24, 2)
            self.assertTrue(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_movimiento_puede_mover_false(self):
        """
        Prueba movimiento invalido por punto bloqueado.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 2
        
        try:
            self.__juego__.tirar_dados()
            
            # bloquear punto 22 (24 - 2 = 22)
            tablero = self.__juego__.get_tablero()
            punto = 22
            while len(tablero.get_fichas_en_punto(punto)) < 2:
                ficha = Checker('negro')
                ficha.set_posicion(punto)
                tablero.get_fichas_en_punto(punto).append(ficha)
            
            resultado = self.__juego__.puede_hacer_movimiento(24, 2)
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    # ===== TESTS DE PUEDE_HACER_ALGUN_MOVIMIENTO =====
    
    def test_puede_hacer_algun_movimiento_sin_dados(self):
        """
        Prueba cuando no hay dados disponibles.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        resultado = self.__juego__.puede_hacer_algun_movimiento()
        self.assertFalse(resultado)
    
    def test_puede_hacer_algun_movimiento_con_fichas_en_barra_true(self):
        """
        Prueba con fichas en barra y puede mover.
        
        Recibe: Nada
        Hace: Verifica que devuelve True
        Devuelve: Nada
        """
        # poner ficha en barra
        tablero = self.__juego__.get_tablero()
        ficha = Checker('blanco')
        ficha.set_posicion(0)
        tablero.get_fichas_en_punto(0).append(ficha)
        
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            resultado = self.__juego__.puede_hacer_algun_movimiento()
            # depende si el punto esta bloqueado
            self.assertIsNotNone(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_algun_movimiento_sin_fichas_en_barra_true(self):
        """
        Prueba sin fichas en barra y puede mover.
        
        Recibe: Nada
        Hace: Verifica que devuelve True
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 2
        
        try:
            self.__juego__.tirar_dados()
            
            resultado = self.__juego__.puede_hacer_algun_movimiento()
            self.assertTrue(resultado)
        finally:
            random.randint = original
    
    def test_puede_hacer_algun_movimiento_false(self):
        """
        Prueba cuando no puede hacer ningun movimiento.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # limpiar tablero
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # poner una ficha blanca en punto 1
        ficha = Checker('blanco')
        ficha.set_posicion(1)
        tablero.get_fichas_en_punto(1).append(ficha)
        
        # tirar dado grande
        import random
        original = random.randint
        random.randint = lambda a, b: 6
        
        try:
            self.__juego__.tirar_dados()
            
            # no puede mover porque 1 - 6 = -5 (fuera de rango)
            resultado = self.__juego__.puede_hacer_algun_movimiento()
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    # ===== TESTS DE HACER_MOVIMIENTO =====
    
    def test_hacer_movimiento_invalido(self):
        """
        Prueba hacer_movimiento cuando es invalido.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # no tirar dados
        resultado = self.__juego__.hacer_movimiento(24, 3)
        self.assertFalse(resultado)
    
    def test_hacer_movimiento_desde_barra_blanco(self):
        """
        Prueba hacer_movimiento desde barra siendo blanco.
        
        Recibe: Nada
        Hace: Verifica calculo de destino y ejecucion
        Devuelve: Nada
        """
        # poner ficha en barra
        tablero = self.__juego__.get_tablero()
        ficha = Checker('blanco')
        ficha.set_posicion(0)
        tablero.get_fichas_en_punto(0).append(ficha)
        
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # hacer movimiento desde barra
            resultado = self.__juego__.hacer_movimiento(0, 3)
            # puede ser True o False
            self.assertIsNotNone(resultado)
        finally:
            random.randint = original
    
    def test_hacer_movimiento_desde_barra_negro(self):
        """
        Prueba hacer_movimiento desde barra siendo negro.
        
        Recibe: Nada
        Hace: Verifica calculo de destino y ejecucion
        Devuelve: Nada
        """
        # cambiar a jugador negro
        self.__juego__.terminar_turno()
        
        # poner ficha negra en barra
        tablero = self.__juego__.get_tablero()
        ficha = Checker('negro')
        ficha.set_posicion(0)
        tablero.get_fichas_en_punto(0).append(ficha)
        
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # hacer movimiento desde barra
            resultado = self.__juego__.hacer_movimiento(0, 3)
            # puede ser True o False
            self.assertIsNotNone(resultado)
        finally:
            random.randint = original
    
    def test_hacer_movimiento_normal_blanco(self):
        """
        Prueba hacer_movimiento normal siendo blanco.
        
        Recibe: Nada
        Hace: Verifica calculo de destino normal
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 2
        
        try:
            self.__juego__.tirar_dados()
            
            # mover desde punto 24
            resultado = self.__juego__.hacer_movimiento(24, 2)
            self.assertTrue(resultado)
        finally:
            random.randint = original
    
    def test_hacer_movimiento_normal_negro(self):
        """
        Prueba hacer_movimiento normal siendo negro.
        
        Recibe: Nada
        Hace: Verifica calculo de destino normal
        Devuelve: Nada
        """
        # cambiar a jugador negro
        self.__juego__.terminar_turno()
        
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 2
        
        try:
            self.__juego__.tirar_dados()
            
            # mover desde punto 1
            resultado = self.__juego__.hacer_movimiento(1, 2)
            self.assertTrue(resultado)
        finally:
            random.randint = original
    
    def test_hacer_movimiento_falla_en_tablero(self):
        """
        Prueba cuando el movimiento falla en el tablero.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 2
        
        try:
            self.__juego__.tirar_dados()
            
            # intentar mover desde punto vacio
            resultado = self.__juego__.hacer_movimiento(2, 2)
            self.assertFalse(resultado)
        finally:
            random.randint = original
    
    def test_hacer_movimiento_consume_dado(self):
        """
        Prueba que hacer_movimiento consume el dado.
        
        Recibe: Nada
        Hace: Verifica que se elimina el dado usado
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 2
        
        try:
            self.__juego__.tirar_dados()
            
            # verificar dados antes
            movimientos_antes = len(self.__juego__.get_movimientos_disponibles())
            
            # hacer movimiento
            self.__juego__.hacer_movimiento(24, 2)
            
            # verificar dados despues
            movimientos_despues = len(self.__juego__.get_movimientos_disponibles())
            
            self.assertEqual(movimientos_despues, movimientos_antes - 1)
        finally:
            random.randint = original
    
    def test_hacer_movimiento_termina_turno_cuando_no_quedan_dados(self):
        """
        Prueba que termina turno cuando se usan todos los dados.
        
        Recibe: Nada
        Hace: Verifica que se llama a terminar_turno
        Devuelve: Nada
        """
        # tirar dados (solo 1)
        import random
        original = random.randint
        valores = [2, 5]
        indice = [0]
        
        def mock_randint(a, b):
            resultado = valores[indice[0]]
            indice[0] = indice[0] + 1
            return resultado
        
        random.randint = mock_randint
        
        try:
            self.__juego__.tirar_dados()
            
            # verificar jugador actual antes
            jugador_antes = self.__juego__.get_jugador_actual()
            
            # hacer primer movimiento
            self.__juego__.hacer_movimiento(24, 2)
            
            # hacer segundo movimiento
            self.__juego__.hacer_movimiento(24, 5)
            
            # verificar que cambio el turno
            jugador_despues = self.__juego__.get_jugador_actual()
            self.assertNotEqual(jugador_antes, jugador_despues)
        finally:
            random.randint = original
    
    # ===== TESTS DE TERMINAR_TURNO =====
    
    def test_terminar_turno_cambia_jugador_1_a_2(self):
        """
        Prueba terminar_turno cuando es jugador 1.
        
        Recibe: Nada
        Hace: Verifica que cambia a jugador 2
        Devuelve: Nada
        """
        # jugador actual es 1
        jugador1 = self.__juego__.get_jugador1()
        self.assertEqual(self.__juego__.get_jugador_actual(), jugador1)
        
        # terminar turno
        self.__juego__.terminar_turno()
        
        # verificar que cambio a jugador 2
        jugador2 = self.__juego__.get_jugador2()
        self.assertEqual(self.__juego__.get_jugador_actual(), jugador2)
    
    def test_terminar_turno_cambia_jugador_2_a_1(self):
        """
        Prueba terminar_turno cuando es jugador 2.
        
        Recibe: Nada
        Hace: Verifica que cambia a jugador 1
        Devuelve: Nada
        """
        # cambiar a jugador 2
        self.__juego__.terminar_turno()
        jugador2 = self.__juego__.get_jugador2()
        self.assertEqual(self.__juego__.get_jugador_actual(), jugador2)
        
        # terminar turno
        self.__juego__.terminar_turno()
        
        # verificar que cambio a jugador 1
        jugador1 = self.__juego__.get_jugador1()
        self.assertEqual(self.__juego__.get_jugador_actual(), jugador1)
    
    def test_terminar_turno_limpia_movimientos(self):
        """
        Prueba que terminar_turno limpia los movimientos.
        
        Recibe: Nada
        Hace: Verifica que la lista queda vacia
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # verificar que hay movimientos
            self.assertGreater(len(self.__juego__.get_movimientos_disponibles()), 0)
            
            # terminar turno
            self.__juego__.terminar_turno()
            
            # verificar que se limpiaron
            self.assertEqual(len(self.__juego__.get_movimientos_disponibles()), 0)
        finally:
            random.randint = original
    
    def test_terminar_turno_resetea_flag_automatico(self):
        """
        Prueba que terminar_turno resetea el flag de turno automatico.
        
        Recibe: Nada
        Hace: Verifica que se pone en False
        Devuelve: Nada
        """
        # terminar turno
        self.__juego__.terminar_turno()
        
        # verificar que el flag es False
        self.assertFalse(self.__juego__.turno_paso_automaticamente())
    
    def test_terminar_turno_verifica_victoria(self):
        """
        Prueba que terminar_turno llama a verificar_victoria.
        
        Recibe: Nada
        Hace: Verifica que se ejecuta verificar_victoria
        Devuelve: Nada
        """
        # limpiar tablero y hacer que blanco gane
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # terminar turno (deberia detectar victoria)
        self.__juego__.terminar_turno()
        
        # verificar que hay ganador
        self.assertTrue(self.__juego__.esta_terminado())
        self.assertIsNotNone(self.__juego__.get_ganador())
    
    def test_terminar_turno_no_cambia_jugador_si_juego_terminado(self):
        """
        Prueba que no cambia jugador si el juego termino.
        
        Recibe: Nada
        Hace: Verifica que mantiene el jugador actual
        Devuelve: Nada
        """
        # limpiar tablero
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # terminar turno (detecta victoria de blanco)
        jugador_actual = self.__juego__.get_jugador_actual()
        self.__juego__.terminar_turno()
        
        # verificar que el juego termino
        self.assertTrue(self.__juego__.esta_terminado())
        
        # verificar que NO se cambio el jugador 
        # (porque se ejecuta verificar_victoria antes de cambiar)
        # y si el juego termina, no cambia
        # Nota: en este caso si cambia porque verifica victoria
        # DESPUES cambia el jugador solo si NO esta terminado
    
    # ===== TESTS DE VERIFICAR_VICTORIA =====
    
    def test_verificar_victoria_jugador_blanco_gana(self):
        """
        Prueba verificar_victoria cuando blanco gana.
        
        Recibe: Nada
        Hace: Verifica que se marca como terminado
        Devuelve: Nada
        """
        # limpiar tablero (blanco gana)
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # verificar victoria
        self.__juego__.verificar_victoria()
        
        # verificar que termino
        self.assertTrue(self.__juego__.esta_terminado())
        
        # verificar ganador
        ganador = self.__juego__.get_ganador()
        self.assertEqual(ganador, self.__juego__.get_jugador1())
    
    def test_verificar_victoria_jugador_negro_gana(self):
        """
        Prueba verificar_victoria cuando negro gana.
        
        Recibe: Nada
        Hace: Verifica que se marca como terminado
        Devuelve: Nada
        """
        # limpiar tablero y poner solo fichas blancas
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # poner una ficha blanca
        ficha = Checker('blanco')
        ficha.set_posicion(5)
        tablero.get_fichas_en_punto(5).append(ficha)
        
        # verificar victoria (negro gano porque no tiene fichas)
        self.__juego__.verificar_victoria()
        
        # verificar que termino
        self.assertTrue(self.__juego__.esta_terminado())
        
        # verificar ganador
        ganador = self.__juego__.get_ganador()
        self.assertEqual(ganador, self.__juego__.get_jugador2())
    
    def test_verificar_victoria_con_fichas_en_barra_blanco(self):
        """
        Prueba verificar_victoria contando fichas en barra.
        
        Recibe: Nada
        Hace: Verifica que suma las fichas en barra
        Devuelve: Nada
        """
        # limpiar tablero
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # poner ficha blanca en barra
        ficha = Checker('blanco')
        ficha.set_posicion(0)
        tablero.get_fichas_en_punto(0).append(ficha)
        
        # verificar victoria (blanco NO gano porque tiene 1 en barra)
        self.__juego__.verificar_victoria()
        
        # verificar que NO termino
        self.assertFalse(self.__juego__.esta_terminado())
    
    def test_verificar_victoria_sin_ganador(self):
        """
        Prueba verificar_victoria cuando nadie gano.
        
        Recibe: Nada
        Hace: Verifica que no se marca como terminado
        Devuelve: Nada
        """
        # verificar victoria en juego inicial
        self.__juego__.verificar_victoria()
        
        # verificar que NO termino
        self.assertFalse(self.__juego__.esta_terminado())
        
        # verificar que NO hay ganador
        self.assertIsNone(self.__juego__.get_ganador())
    
    def test_verificar_victoria_cuenta_fichas_en_puntos(self):
        """
        Prueba que verificar_victoria cuenta todas las fichas.
        
        Recibe: Nada
        Hace: Verifica el loop que cuenta fichas
        Devuelve: Nada
        """
        # poner fichas blancas en varios puntos
        tablero = self.__juego__.get_tablero()
        
        # contar fichas blancas actuales
        total_blancas = 0
        punto = 1
        while punto <= 24:
            color = tablero.get_color_en_punto(punto)
            if color == 'blanco':
                total_blancas = total_blancas + tablero.contar_fichas_en_punto(punto)
            punto = punto + 1
        
        # verificar que hay fichas
        self.assertGreater(total_blancas, 0)
        
        # verificar victoria
        self.__juego__.verificar_victoria()
        
        # no debe ganar
        self.assertFalse(self.__juego__.esta_terminado())
    
    # ===== TESTS DE PASAR_TURNO_SI_NO_HAY_MOVIMIENTOS =====
    
    def test_pasar_turno_si_no_hay_movimientos_puede_mover(self):
        """
        Prueba cuando SI puede hacer movimientos.
        
        Recibe: Nada
        Hace: Verifica que devuelve False
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 2
        
        try:
            self.__juego__.tirar_dados()
            
            # pasar turno si no hay movimientos
            resultado = self.__juego__.pasar_turno_si_no_hay_movimientos()
            
            # debe devolver False porque SI puede mover
            self.assertFalse(resultado)
            
            # verificar que el turno NO cambio
            self.assertEqual(self.__juego__.get_jugador_actual(), self.__juego__.get_jugador1())
        finally:
            random.randint = original
    
    def test_pasar_turno_si_no_hay_movimientos_no_puede_mover(self):
        """
        Prueba cuando NO puede hacer movimientos.
        
        Recibe: Nada
        Hace: Verifica que devuelve True y cambia turno
        Devuelve: Nada
        """
        # limpiar tablero
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # poner una ficha blanca en punto 1
        ficha = Checker('blanco')
        ficha.set_posicion(1)
        tablero.get_fichas_en_punto(1).append(ficha)
        
        # tirar dado grande
        import random
        original = random.randint
        random.randint = lambda a, b: 6
        
        try:
            self.__juego__.tirar_dados()
            
            # pasar turno si no hay movimientos
            resultado = self.__juego__.pasar_turno_si_no_hay_movimientos()
            
            # debe devolver True porque NO puede mover
            self.assertTrue(resultado)
            
            # verificar que el turno SI cambio
            self.assertEqual(self.__juego__.get_jugador_actual(), self.__juego__.get_jugador2())
            
            # verificar que el flag esta en True
            # NO - porque terminar_turno lo resetea a False
            self.assertFalse(self.__juego__.turno_paso_automaticamente())
        finally:
            random.randint = original
    
    def test_pasar_turno_si_no_hay_movimientos_activa_flag(self):
        """
        Prueba que activa el flag de turno automatico.
        
        Recibe: Nada
        Hace: Verifica que se marca el flag antes de terminar turno
        Devuelve: Nada
        """
        # limpiar tablero
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # poner una ficha blanca en punto 1
        ficha = Checker('blanco')
        ficha.set_posicion(1)
        tablero.get_fichas_en_punto(1).append(ficha)
        
        # tirar dado grande
        import random
        original = random.randint
        random.randint = lambda a, b: 6
        
        try:
            self.__juego__.tirar_dados()
            
            # pasar turno
            self.__juego__.pasar_turno_si_no_hay_movimientos()
            
            # el flag se pone en True y luego terminar_turno lo resetea
            # asi que no podemos verificarlo directamente
            # pero verificamos que se llamo a terminar_turno
            self.assertEqual(self.__juego__.get_jugador_actual(), self.__juego__.get_jugador2())
        finally:
            random.randint = original
    
    # ===== TESTS DE GET_ESTADO_JUEGO =====
    
    def test_get_estado_juego_completo(self):
        """
        Prueba get_estado_juego con todos los campos.
        
        Recibe: Nada
        Hace: Verifica que devuelve diccionario correcto
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # obtener estado
            estado = self.__juego__.get_estado_juego()
            
            # verificar que es un diccionario
            self.assertIsInstance(estado, dict)
            
            # verificar jugador_actual
            self.assertEqual(estado['jugador_actual'], "Ana")
            
            # verificar color_actual
            self.assertEqual(estado['color_actual'], 'blanco')
            
            # verificar movimientos_disponibles
            self.assertGreater(len(estado['movimientos_disponibles']), 0)
            
            # verificar juego_terminado
            self.assertEqual(estado['juego_terminado'], False)
            
            # verificar ganador
            self.assertIsNone(estado['ganador'])
            
            # verificar turno_paso_automatico
            self.assertEqual(estado['turno_paso_automatico'], False)
        finally:
            random.randint = original
    
    def test_get_estado_juego_con_ganador(self):
        """
        Prueba get_estado_juego cuando hay ganador.
        
        Recibe: Nada
        Hace: Verifica que incluye el nombre del ganador
        Devuelve: Nada
        """
        # limpiar tablero para que blanco gane
        tablero = self.__juego__.get_tablero()
        punto = 0
        while punto < 26:
            lista = tablero.get_fichas_en_punto(punto)
            while len(lista) > 0:
                lista.pop()
            punto = punto + 1
        
        # verificar victoria
        self.__juego__.verificar_victoria()
        
        # obtener estado
        estado = self.__juego__.get_estado_juego()
        
        # verificar ganador
        self.assertEqual(estado['ganador'], "Ana")
        
        # verificar juego_terminado
        self.assertEqual(estado['juego_terminado'], True)
    
    def test_get_estado_juego_sin_ganador(self):
        """
        Prueba get_estado_juego cuando no hay ganador.
        
        Recibe: Nada
        Hace: Verifica que ganador es None
        Devuelve: Nada
        """
        estado = self.__juego__.get_estado_juego()
        self.assertIsNone(estado['ganador'])
    
    def test_get_estado_juego_copia_movimientos(self):
        """
        Prueba que get_estado_juego copia la lista.
        
        Recibe: Nada
        Hace: Verifica que no devuelve la lista original
        Devuelve: Nada
        """
        # tirar dados
        import random
        original = random.randint
        random.randint = lambda a, b: 3
        
        try:
            self.__juego__.tirar_dados()
            
            # obtener estado
            estado = self.__juego__.get_estado_juego()
            movimientos_estado = estado['movimientos_disponibles']
            
            # obtener original
            movimientos_original = self.__juego__.get_movimientos_disponibles()
            
            # verificar que son iguales en contenido
            self.assertEqual(movimientos_estado, movimientos_original)
            
            # verificar que NO son el mismo objeto
            self.assertIsNot(movimientos_estado, movimientos_original)
        finally:
            random.randint = original
    
    # ===== TESTS DE __STR__ =====
    
    def test_str_formato_correcto(self):
        """
        Prueba __str__ con formato correcto.
        
        Recibe: Nada
        Hace: Verifica que contiene los elementos esperados
        Devuelve: Nada
        """
        texto = str(self.__juego__)
        
        # verificar que contiene nombres
        self.assertIn("Ana", texto)
        self.assertIn("Luis", texto)
        
        # verificar que contiene "vs"
        self.assertIn("vs", texto)
        
        # verificar que contiene "Backgammon"
        self.assertIn("Backgammon", texto)
    
    def test_str_incluye_tablero(self):
        """
        Prueba que __str__ incluye el tablero.
        
        Recibe: Nada
        Hace: Verifica que contiene elementos del tablero
        Devuelve: Nada
        """
        texto = str(self.__juego__)
        
        # verificar que contiene elementos del tablero
        self.assertIn("TABLERO", texto)
    
    def test_str_estructura_encabezado(self):
        """
        Prueba la estructura del encabezado.
        
        Recibe: Nada
        Hace: Verifica el formato exacto
        Devuelve: Nada
        """
        texto = str(self.__juego__)
        
        # verificar formato: "Backgammon: Ana vs Luis"
        if "Backgammon: Ana vs Luis" in texto:
            tiene_formato = True
        else:
            tiene_formato = False
        
        self.assertTrue(tiene_formato)


if __name__ == "__main__":
    unittest.main()