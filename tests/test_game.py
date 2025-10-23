import unittest
from unittest.mock import MagicMock, patch
from core.game import BackgammonGame


class TestBackgammonGame(unittest.TestCase):
    """
    Clase para probar el juego de Backgammon.
    
    Recibe:
        Nada.
    Hace:
        Prueba todas las funciones del juego como tirar dados, mover fichas,
        validar movimientos y cambiar turnos.
    Devuelve:
        Nada.
    """

    def setUp(self):
        """
        Prepara cada prueba creando un juego nuevo.
        
        Recibe:
            Nada.
        Hace:
            Crea un juego con dos jugadores y reemplaza el tablero y dados
            por versiones falsas para poder controlarlas en las pruebas.
        Devuelve:
            Nada.
        """
        # Creo un juego nuevo con dos jugadores
        self.game = BackgammonGame("Alice", "Bob")
        
        # Creo versiones falsas del tablero y dados para controlarlas
        self.__tablero_falso__ = MagicMock()
        self.__dados_falsos__ = MagicMock()
        
        # Le pongo las versiones falsas al juego
        self.game._BackgammonGame__tablero__ = self.__tablero_falso__
        self.game._BackgammonGame__dados__ = self.__dados_falsos__

    def test_nombres_de_jugadores(self):
        """
        Prueba que los nombres de los jugadores sean correctos.
        
        Recibe:
            Nada.
        Hace:
            Verifica que el jugador 1 se llame Alice y el jugador 2 Bob.
        Devuelve:
            Nada.
        """
        # Obtengo el nombre del jugador 1
        nombre_jugador1 = self.game.get_jugador1().get_nombre()
        # Verifico que sea Alice
        self.assertEqual(nombre_jugador1, "Alice")
        
        # Obtengo el nombre del jugador 2
        nombre_jugador2 = self.game.get_jugador2().get_nombre()
        # Verifico que sea Bob
        self.assertEqual(nombre_jugador2, "Bob")

    def test_color_del_jugador_actual(self):
        """
        Prueba que el color del jugador actual sea valido.
        
        Recibe:
            Nada.
        Hace:
            Verifica que el color sea blanco o negro.
        Devuelve:
            Nada.
        """
        # Obtengo el color del jugador actual
        color_actual = self.game.get_color_jugador_actual()
        
        # El color debe ser blanco o negro
        self.assertIn(color_actual, ("blanco", "negro"))

    def test_tirar_dados_devuelve_lista(self):
        """
        Prueba que tirar dados devuelva una lista de numeros.
        
        Recibe:
            Nada.
        Hace:
            Configura los dados falsos para que devuelvan 3 y 5, luego
            verifica que el juego devuelva esos valores.
        Devuelve:
            Nada.
        """
        # Le digo a los dados falsos que devuelvan 3 y 5
        self.__dados_falsos__.tirar.return_value = [3, 5]
        
        # Tiro los dados
        resultado_dados = self.game.tirar_dados()
        
        # Verifico que haya devuelto 3 y 5
        self.assertEqual(resultado_dados, [3, 5])

    def test_tirar_dados_guarda_movimientos_disponibles(self):
        """
        Prueba que los dados tirados se guarden como movimientos disponibles.
        
        Recibe:
            Nada.
        Hace:
            Tira los dados y verifica que esos valores queden guardados
            en la lista de movimientos disponibles.
        Devuelve:
            Nada.
        """
        # Le digo a los dados falsos que devuelvan 3 y 5
        self.__dados_falsos__.tirar.return_value = [3, 5]
        
        # Tiro los dados
        self.game.tirar_dados()
        
        # Obtengo los movimientos disponibles
        movimientos = self.game.get_movimientos_disponibles()
        
        # Verifico que sean 3 y 5
        self.assertEqual(movimientos, [3, 5])

    def test_tirar_dados_hace_copia_de_lista(self):
        """
        Prueba que la lista de movimientos sea una copia y no la original.
        
        Recibe:
            Nada.
        Hace:
            Tira los dados, modifica la lista devuelta y verifica que
            los movimientos disponibles no cambien.
        Devuelve:
            Nada.
        """
        # Le digo a los dados falsos que devuelvan 3 y 5
        self.__dados_falsos__.tirar.return_value = [3, 5]
        
        # Tiro los dados y guardo el resultado
        resultado = self.game.tirar_dados()
        
        # Modifico la lista que me devolvio
        resultado.append(6)
        
        # Obtengo los movimientos disponibles
        movimientos = self.game.get_movimientos_disponibles()
        
        # Verifico que sigan siendo 3 y 5 (sin el 6 que agregue)
        self.assertEqual(movimientos, [3, 5])

    def test_no_puede_mover_si_dado_no_disponible(self):
        """
        Prueba que no se pueda usar un dado que no esta disponible.
        
        Recibe:
            Nada.
        Hace:
            Pone dados 2 y 4 disponibles, e intenta usar el dado 6.
        Devuelve:
            Nada.
        """
        # Pongo que solo hay dados 2 y 4 disponibles
        self.game._BackgammonGame__movimientos_disponibles__ = [2, 4]
        
        # Intento mover con el dado 6 (que no tengo)
        puede_mover = self.game.puede_hacer_movimiento(6, 3)
        
        # Verifico que no me deje
        self.assertFalse(puede_mover)

    def test_con_fichas_en_barra_solo_puede_salir_desde_barra(self):
        """
        Prueba que si hay fichas en la barra, solo se pueda mover desde ahi.
        
        Recibe:
            Nada.
        Hace:
            Configura el tablero para que haya fichas en barra y verifica
            que solo se pueda mover desde la posicion 0 (la barra).
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 4 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [4]
        
        # Creo funcion para simular jugador_tiene_fichas_en_barra
        def simular_fichas_barra(color):
            return True
        
        # Le digo al tablero falso que tengo fichas en la barra
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.side_effect = simular_fichas_barra
        
        # Le digo que el destino es valido (25-4=21 para blanco)
        self.__tablero_falso__.puede_mover_a_punto.return_value = True
        
        # Intento mover desde la barra (posicion 0)
        puede_desde_barra = self.game.puede_hacer_movimiento(0, 4)
        
        # Verifico que SI me deje
        self.assertTrue(puede_desde_barra)
        
        # Ahora intento mover desde otra posicion (no la barra)
        puede_desde_otro = self.game.puede_hacer_movimiento(6, 4)
        
        # Verifico que NO me deje
        self.assertFalse(puede_desde_otro)

    def test_no_puede_mover_desde_punto_vacio(self):
        """
        Prueba que no se pueda mover desde un punto sin fichas.
        
        Recibe:
            Nada.
        Hace:
            Configura un punto vacio e intenta mover desde ahi.
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 3 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [3]
        
        # Le digo al tablero que no tengo fichas en la barra
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        
        # Le digo que en el punto 6 hay 0 fichas
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 0
        
        # Intento mover desde el punto 6 (que esta vacio)
        puede_mover = self.game.puede_hacer_movimiento(6, 3)
        
        # Verifico que NO me deje
        self.assertFalse(puede_mover)

    def test_no_puede_mover_ficha_de_color_incorrecto(self):
        """
        Prueba que no se pueda mover una ficha del otro jugador.
        
        Recibe:
            Nada.
        Hace:
            Configura un punto con fichas negras cuando el jugador actual
            es blanco, e intenta mover desde ahi.
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 3 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [3]
        
        # Le digo al tablero que no tengo fichas en la barra
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        
        # Le digo que en el punto 6 hay 2 fichas
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 2
        
        # Le digo que esas fichas son negras (pero el jugador actual es blanco)
        self.__tablero_falso__.get_color_en_punto.return_value = "negro"
        
        # Intento mover desde el punto 6
        puede_mover = self.game.puede_hacer_movimiento(6, 3)
        
        # Verifico que NO me deje
        self.assertFalse(puede_mover)

    def test_no_puede_mover_fuera_del_tablero(self):
        """
        Prueba que no se pueda mover a una posicion fuera del tablero.
        
        Recibe:
            Nada.
        Hace:
            Intenta mover desde el punto 1 con un dado muy grande que
            saldria del tablero.
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 7 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [7]
        
        # Le digo al tablero que no tengo fichas en la barra
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        
        # Le digo que en el punto 1 hay fichas blancas
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 2
        self.__tablero_falso__.get_color_en_punto.return_value = "blanco"
        
        # Intento mover desde punto 1 con dado 7 (iria a 1-7 = -6, fuera del tablero)
        puede_mover = self.game.puede_hacer_movimiento(1, 7)
        
        # Verifico que NO me deje
        self.assertFalse(puede_mover)

    def test_puede_hacer_movimiento_valido_normal(self):
        """
        Prueba que SI se pueda hacer un movimiento valido normal.
        
        Recibe:
            Nada.
        Hace:
            Configura todo para que el movimiento sea valido y verifica
            que el juego lo permita.
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 2 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [2]
        
        # Le digo al tablero que no tengo fichas en la barra
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        
        # Le digo que en el punto 6 hay 1 ficha blanca
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 1
        self.__tablero_falso__.get_color_en_punto.return_value = "blanco"
        
        # Le digo que SI puedo mover al destino (6-2=4)
        self.__tablero_falso__.puede_mover_a_punto.return_value = True
        
        # Intento mover desde punto 6 con dado 2
        puede_mover = self.game.puede_hacer_movimiento(6, 2)
        
        # Verifico que SI me deje
        self.assertTrue(puede_mover)

    def test_hacer_movimiento_valido_consume_dado(self):
        """
        Prueba que al hacer un movimiento se consuma el dado usado.
        
        Recibe:
            Nada.
        Hace:
            Configura un movimiento valido, lo ejecuta y verifica que
            el dado usado ya no este disponible.
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 3 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [3]
        
        # Configuro el tablero para que el movimiento sea valido
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 1
        self.__tablero_falso__.get_color_en_punto.return_value = "blanco"
        self.__tablero_falso__.puede_mover_a_punto.return_value = True
        self.__tablero_falso__.mover_ficha.return_value = True
        
        # Configuro verificar_victoria para que no termine el juego
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 5
        
        # Hago el movimiento
        resultado = self.game.hacer_movimiento(8, 3)
        
        # Verifico que el movimiento se haya hecho
        self.assertTrue(resultado)
        
        # Obtengo los movimientos disponibles
        movimientos = self.game.get_movimientos_disponibles()
        
        # Verifico que ya no este el dado 3
        self.assertEqual(movimientos, [])

    def test_hacer_movimiento_cambia_turno_cuando_no_quedan_dados(self):
        """
        Prueba que el turno cambie cuando se usan todos los dados.
        
        Recibe:
            Nada.
        Hace:
            Hace un movimiento con el unico dado disponible y verifica
            que cambie el turno.
        Devuelve:
            Nada.
        """
        # Pongo que tengo solo el dado 3 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [3]
        
        # Configuro el tablero para que el movimiento sea valido
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 1
        self.__tablero_falso__.get_color_en_punto.return_value = "blanco"
        self.__tablero_falso__.puede_mover_a_punto.return_value = True
        self.__tablero_falso__.mover_ficha.return_value = True
        
        # Configuro verificar_victoria para que no termine el juego
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 5
        
        # Guardo quien es el jugador actual
        jugador_antes = self.game.get_jugador_actual()
        
        # Hago el movimiento
        self.game.hacer_movimiento(8, 3)
        
        # Obtengo el jugador actual despues del movimiento
        jugador_despues = self.game.get_jugador_actual()
        
        # Verifico que haya cambiado el jugador
        self.assertIsNot(jugador_antes, jugador_despues)

    def test_hacer_movimiento_desde_barra(self):
        """
        Prueba que se pueda reingresar una ficha desde la barra.
        
        Recibe:
            Nada.
        Hace:
            Configura fichas en barra y ejecuta un reingreso.
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 4 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [4]
        
        # Le digo al tablero que tengo fichas en la barra
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = True
        
        # Le digo que puedo mover al destino (25-4=21 para blanco)
        self.__tablero_falso__.puede_mover_a_punto.return_value = True
        
        # Le digo que el reingreso funciona
        self.__tablero_falso__.reingresar_desde_barra.return_value = True
        
        # Configuro para que no termine el juego
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 5
        
        # Hago el movimiento desde la barra (posicion 0)
        resultado = self.game.hacer_movimiento(0, 4)
        
        # Verifico que se haya hecho
        self.assertTrue(resultado)
        
        # Verifico que se haya consumido el dado 4
        movimientos = self.game.get_movimientos_disponibles()
        self.assertNotIn(4, movimientos)

    def test_hacer_movimiento_invalido_no_cambia_nada(self):
        """
        Prueba que si el movimiento es invalido no cambie nada.
        
        Recibe:
            Nada.
        Hace:
            Intenta hacer un movimiento invalido y verifica que los dados
            y el turno no cambien.
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 2 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [2]
        
        # Configuro el tablero para que el movimiento sea invalido (punto vacio)
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 0
        
        # Guardo el jugador actual
        jugador_antes = self.game.get_jugador_actual()
        
        # Intento hacer el movimiento invalido
        resultado = self.game.hacer_movimiento(6, 2)
        
        # Verifico que NO se haya hecho
        self.assertFalse(resultado)
        
        # Verifico que el dado siga disponible
        movimientos = self.game.get_movimientos_disponibles()
        self.assertEqual(movimientos, [2])
        
        # Verifico que el jugador no haya cambiado
        jugador_despues = self.game.get_jugador_actual()
        self.assertIs(jugador_antes, jugador_despues)

    def test_hacer_dos_movimientos_no_cambia_turno_hasta_consumir_todos(self):
        """
        Prueba que con dos dados, el turno NO cambie hasta usar ambos.
        
        Recibe:
            Nada.
        Hace:
            Hace dos movimientos con dos dados disponibles y verifica
            que el turno solo cambie despues del segundo movimiento.
        Devuelve:
            Nada.
        """
        # Pongo que tengo dos dados disponibles: 3 y 4
        self.game._BackgammonGame__movimientos_disponibles__ = [3, 4]
        
        # Configuro el tablero para que ambos movimientos sean validos
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 1
        self.__tablero_falso__.get_color_en_punto.return_value = "blanco"
        self.__tablero_falso__.puede_mover_a_punto.return_value = True
        self.__tablero_falso__.mover_ficha.return_value = True
        
        # Configuro para que no termine el juego
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 5
        
        # Guardo el jugador actual
        jugador_inicial = self.game.get_jugador_actual()
        
        # Hago el primer movimiento (uso el dado 3)
        resultado1 = self.game.hacer_movimiento(10, 3)
        self.assertTrue(resultado1)
        
        # Verifico que solo quede el dado 4
        movimientos_despues_primero = self.game.get_movimientos_disponibles()
        self.assertEqual(movimientos_despues_primero, [4])
        
        # Verifico que el jugador NO haya cambiado todavia
        jugador_despues_primero = self.game.get_jugador_actual()
        self.assertIs(jugador_inicial, jugador_despues_primero)
        
        # Hago el segundo movimiento (uso el dado 4)
        resultado2 = self.game.hacer_movimiento(9, 4)
        self.assertTrue(resultado2)
        
        # Verifico que ya no queden dados
        movimientos_despues_segundo = self.game.get_movimientos_disponibles()
        self.assertEqual(movimientos_despues_segundo, [])
        
        # Verifico que AHORA SI haya cambiado el jugador
        jugador_despues_segundo = self.game.get_jugador_actual()
        self.assertIsNot(jugador_inicial, jugador_despues_segundo)

    def test_puede_hacer_algun_movimiento_con_lista_vacia(self):
        """
        Prueba que sin dados disponibles no se pueda hacer movimientos.
        
        Recibe:
            Nada.
        Hace:
            Pone la lista de movimientos vacia y verifica que devuelva False.
        Devuelve:
            Nada.
        """
        # Pongo que no hay dados disponibles
        self.game._BackgammonGame__movimientos_disponibles__ = []
        
        # Pregunto si puedo hacer algun movimiento
        puede = self.game.puede_hacer_algun_movimiento()
        
        # Verifico que NO pueda
        self.assertFalse(puede)

    def test_puede_hacer_algun_movimiento_con_dados_disponibles(self):
        """
        Prueba que con dados disponibles SI se puedan hacer movimientos.
        
        Recibe:
            Nada.
        Hace:
            Pone un dado disponible y verifica que devuelva True.
        Devuelve:
            Nada.
        """
        # Pongo que tengo el dado 6 disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [6]
        
        # Configuro el tablero para que haya movimientos validos
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 2
        self.__tablero_falso__.get_color_en_punto.return_value = 'blanco'
        self.__tablero_falso__.puede_mover_a_punto.return_value = True
        
        # Pregunto si puedo hacer algun movimiento
        puede = self.game.puede_hacer_algun_movimiento()
        
        # Verifico que SI pueda
        self.assertTrue(puede)

    def test_terminar_turno_limpia_movimientos(self):
        """
        Prueba que al terminar turno se limpie la lista de movimientos.
        
        Recibe:
            Nada.
        Hace:
            Pone movimientos disponibles, termina el turno y verifica
            que la lista quede vacia.
        Devuelve:
            Nada.
        """
        # Pongo que tengo dados 1 y 2 disponibles
        self.game._BackgammonGame__movimientos_disponibles__ = [1, 2]
        
        # Configuro para que no termine el juego
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 5
        self.__tablero_falso__.get_color_en_punto.return_value = 'blanco'
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 3
        
        # Termino el turno
        self.game.terminar_turno()
        
        # Obtengo los movimientos disponibles
        movimientos = self.game.get_movimientos_disponibles()
        
        # Verifico que la lista este vacia
        self.assertEqual(movimientos, [])

    def test_terminar_turno_cambia_jugador(self):
        """
        Prueba que al terminar turno cambie el jugador actual.
        
        Recibe:
            Nada.
        Hace:
            Guarda el jugador actual, termina el turno y verifica que
            sea otro jugador.
        Devuelve:
            Nada.
        """
        # Configuro para que no termine el juego
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 5
        self.__tablero_falso__.get_color_en_punto.return_value = 'blanco'
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 3
        
        # Guardo el jugador actual
        jugador_antes = self.game.get_jugador_actual()
        
        # Termino el turno
        self.game.terminar_turno()
        
        # Obtengo el nuevo jugador actual
        jugador_despues = self.game.get_jugador_actual()
        
        # Verifico que haya cambiado
        self.assertIsNot(jugador_antes, jugador_despues)

    def test_get_estado_juego_tiene_todas_las_claves(self):
        """
        Prueba que el estado del juego contenga todas las claves necesarias.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el estado del juego y verifica que tenga las claves
            esperadas.
        Devuelve:
            Nada.
        """
        # Pongo algunos movimientos disponibles
        self.game._BackgammonGame__movimientos_disponibles__ = [5, 6]
        
        # Obtengo el estado del juego
        estado = self.game.get_estado_juego()
        
        # Verifico que tenga estas claves importantes
        self.assertIn("jugador_actual", estado)
        self.assertIn("color_actual", estado)
        self.assertIn("movimientos_disponibles", estado)
        self.assertIn("juego_terminado", estado)
        self.assertIn("ganador", estado)

    def test_get_estado_juego_movimientos_son_copia(self):
        """
        Prueba que los movimientos en el estado sean una copia.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el estado, guarda una copia, modifica los movimientos internos
            y verifica que la copia guardada no cambie.
        Devuelve:
            Nada.
        """
        # Pongo movimientos 5 y 6
        self.game._BackgammonGame__movimientos_disponibles__ = [5, 6]
        
        # Obtengo el estado
        estado = self.game.get_estado_juego()
        
        # Guardo los movimientos del estado en una variable
        movimientos_estado = estado["movimientos_disponibles"]
        
        # Verifico que sean 5 y 6
        self.assertEqual(movimientos_estado, [5, 6])
        
        # Modifico la lista interna del juego DESPUES de obtener el estado
        self.game._BackgammonGame__movimientos_disponibles__.append(1)
        
        # Verifico que los movimientos en el estado sigan siendo 5 y 6
        self.assertEqual(movimientos_estado, [5, 6])

    def test_str_contiene_nombres_de_jugadores(self):
        """
        Prueba que el string del juego contenga los nombres de los jugadores.
        
        Recibe:
            Nada.
        Hace:
            Obtiene la representacion en texto del juego y verifica que
            contenga ambos nombres.
        Devuelve:
            Nada.
        """
        # Obtengo el texto del juego
        texto_juego = str(self.game)
        
        # Verifico que contenga el nombre Alice
        self.assertIn("Alice", texto_juego)
        
        # Verifico que contenga el nombre Bob
        self.assertIn("Bob", texto_juego)

    def test_str_contiene_representacion_del_tablero(self):
        """
        Prueba que el string del juego contenga informacion del tablero.
        
        Recibe:
            Nada.
        Hace:
            Verifica que el string contenga la palabra Backgammon.
        Devuelve:
            Nada.
        """
        # Obtengo el texto del juego
        texto_juego = str(self.game)
        
        # Verifico que contenga la palabra Backgammon
        self.assertIn("Backgammon", texto_juego)

    def test_get_tablero_devuelve_tablero(self):
        """
        Prueba que get_tablero devuelva el tablero del juego.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el tablero y verifica que sea el mismo que tiene el juego.
        Devuelve:
            Nada.
        """
        # Obtengo el tablero usando el metodo
        tablero_obtenido = self.game.get_tablero()
        
        # Verifico que sea el tablero falso que puse en setUp
        self.assertEqual(tablero_obtenido, self.__tablero_falso__)

    def test_get_dados_devuelve_dados(self):
        """
        Prueba que get_dados devuelva los dados del juego.
        
        Recibe:
            Nada.
        Hace:
            Obtiene los dados y verifica que sean los mismos que tiene el juego.
        Devuelve:
            Nada.
        """
        # Obtengo los dados usando el metodo
        dados_obtenidos = self.game.get_dados()
        
        # Verifico que sean los dados falsos que puse en setUp
        self.assertEqual(dados_obtenidos, self.__dados_falsos__)

    def test_esta_terminado_devuelve_false_al_inicio(self):
        """
        Prueba que al inicio el juego no este terminado.
        
        Recibe:
            Nada.
        Hace:
            Verifica que el juego recien creado no este terminado.
        Devuelve:
            Nada.
        """
        # Pregunto si el juego esta terminado
        juego_terminado = self.game.esta_terminado()
        
        # Verifico que sea False
        self.assertFalse(juego_terminado)

    def test_get_ganador_devuelve_none_al_inicio(self):
        """
        Prueba que al inicio no haya ganador.
        
        Recibe:
            Nada.
        Hace:
            Verifica que el ganador sea None cuando el juego recien empieza.
        Devuelve:
            Nada.
        """
        # Obtengo el ganador
        ganador = self.game.get_ganador()
        
        # Verifico que sea None
        self.assertIsNone(ganador)

    def test_turno_paso_automaticamente_devuelve_false_al_inicio(self):
        """
        Prueba que al inicio el turno no haya pasado automaticamente.
        
        Recibe:
            Nada.
        Hace:
            Verifica que el flag de turno automatico sea False al inicio.
        Devuelve:
            Nada.
        """
        # Pregunto si el turno paso automaticamente
        paso_automatico = self.game.turno_paso_automaticamente()
        
        # Verifico que sea False
        self.assertFalse(paso_automatico)

    def test_verificar_victoria_cuando_blanco_gana(self):
        """
        Prueba que detecte cuando el jugador blanco gana.
        
        Recibe:
            Nada.
        Hace:
            Configura el tablero para que no haya fichas blancas y verifica
            que el juego termine y el jugador 1 sea el ganador.
        Devuelve:
            Nada.
        """
        # Le digo al tablero que no hay fichas blancas en la barra
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 0
        
        # Le digo al tablero que no hay fichas blancas en ningun punto
        self.__tablero_falso__.get_color_en_punto.return_value = 'negro'
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 0
        
        # Llamo a verificar victoria
        self.game.verificar_victoria()
        
        # Verifico que el juego este terminado
        self.assertTrue(self.game.esta_terminado())
        
        # Verifico que el ganador sea el jugador 1
        ganador = self.game.get_ganador()
        self.assertEqual(ganador, self.game.get_jugador1())

    def test_verificar_victoria_cuando_negro_gana(self):
        """
        Prueba que detecte cuando el jugador negro gana.
        
        Recibe:
            Nada.
        Hace:
            Configura el tablero para que no haya fichas negras y verifica
            que el juego termine y el jugador 2 sea el ganador.
        Devuelve:
            Nada.
        """
        # Creo una funcion que simule el tablero
        def simular_tablero(color):
            if color == 'blanco':
                # hay fichas blancas
                return 5
            else:
                # no hay fichas negras
                return 0
        
        # Le digo al tablero que use mi funcion simulada
        self.__tablero_falso__.contar_fichas_en_barra.side_effect = simular_tablero
        
        # Simulo que todos los puntos tienen fichas blancas
        self.__tablero_falso__.get_color_en_punto.return_value = 'blanco'
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 1
        
        # Llamo a verificar victoria
        self.game.verificar_victoria()
        
        # Verifico que el juego este terminado
        self.assertTrue(self.game.esta_terminado())
        
        # Verifico que el ganador sea el jugador 2
        ganador = self.game.get_ganador()
        self.assertEqual(ganador, self.game.get_jugador2())

    def test_verificar_victoria_cuando_nadie_gana(self):
        """
        Prueba que no detecte ganador cuando ambos tienen fichas.
        
        Recibe:
            Nada.
        Hace:
            Configura el tablero con fichas de ambos colores y verifica
            que el juego no termine.
        Devuelve:
            Nada.
        """
        # Le digo al tablero que hay fichas de ambos colores
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 1
        self.__tablero_falso__.get_color_en_punto.return_value = 'blanco'
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 5
        
        # Llamo a verificar victoria
        self.game.verificar_victoria()
        
        # Verifico que el juego NO este terminado
        self.assertFalse(self.game.esta_terminado())
        
        # Verifico que no haya ganador
        ganador = self.game.get_ganador()
        self.assertIsNone(ganador)

    def test_pasar_turno_si_no_hay_movimientos_pasa_el_turno(self):
        """
        Prueba que pase el turno si no hay movimientos disponibles.
        
        Recibe:
            Nada.
        Hace:
            Configura una situacion sin movimientos posibles y verifica
            que el turno pase automaticamente.
        Devuelve:
            Nada.
        """
        # Pongo que tengo un dado disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [3]
        
        # Configuro el tablero para que no haya movimientos validos
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 0
        
        # Configuro para que no termine el juego
        self.__tablero_falso__.contar_fichas_en_barra.return_value = 5
        self.__tablero_falso__.get_color_en_punto.return_value = 'blanco'
        
        # Guardo el jugador actual
        jugador_antes = self.game.get_jugador_actual()
        
        # Intento pasar el turno si no hay movimientos
        resultado = self.game.pasar_turno_si_no_hay_movimientos()
        
        # Verifico que haya pasado el turno
        self.assertTrue(resultado)
        
        # Verifico que el turno paso automaticamente
        self.assertTrue(self.game.turno_paso_automaticamente())
        
        # Verifico que el jugador haya cambiado
        jugador_despues = self.game.get_jugador_actual()
        self.assertIsNot(jugador_antes, jugador_despues)

    def test_pasar_turno_si_no_hay_movimientos_no_pasa_si_hay_movimientos(self):
        """
        Prueba que NO pase el turno si hay movimientos disponibles.
        
        Recibe:
            Nada.
        Hace:
            Configura una situacion con movimientos validos y verifica
            que el turno NO pase.
        Devuelve:
            Nada.
        """
        # Pongo que tengo un dado disponible
        self.game._BackgammonGame__movimientos_disponibles__ = [3]
        
        # Configuro el tablero para que haya movimientos validos
        self.__tablero_falso__.jugador_tiene_fichas_en_barra.return_value = False
        self.__tablero_falso__.contar_fichas_en_punto.return_value = 2
        self.__tablero_falso__.get_color_en_punto.return_value = 'blanco'
        self.__tablero_falso__.puede_mover_a_punto.return_value = True
        
        # Guardo el jugador actual
        jugador_antes = self.game.get_jugador_actual()
        
        # Intento pasar el turno si no hay movimientos
        resultado = self.game.pasar_turno_si_no_hay_movimientos()
        
        # Verifico que NO haya pasado el turno
        self.assertFalse(resultado)
        
        # Verifico que el jugador NO haya cambiado
        jugador_despues = self.game.get_jugador_actual()
        self.assertIs(jugador_antes, jugador_despues)

    def test_get_estado_juego_incluye_turno_paso_automatico(self):
        """
        Prueba que el estado incluya el flag de turno automatico.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el estado y verifica que tenga la clave turno_paso_automatico.
        Devuelve:
            Nada.
        """
        # Obtengo el estado del juego
        estado = self.game.get_estado_juego()
        
        # Verifico que tenga la clave turno_paso_automatico
        self.assertIn('turno_paso_automatico', estado)
        
        # Verifico que el valor sea False al inicio
        self.assertFalse(estado['turno_paso_automatico'])

    def test_get_estado_juego_con_ganador(self):
        """
        Prueba que el estado incluya el nombre del ganador.
        
        Recibe:
            Nada.
        Hace:
            Configura un ganador y verifica que aparezca en el estado.
        Devuelve:
            Nada.
        """
        # Marco el juego como terminado y pongo un ganador
        self.game._BackgammonGame__juego_terminado__ = True
        self.game._BackgammonGame__ganador__ = self.game.get_jugador1()
        
        # Obtengo el estado
        estado = self.game.get_estado_juego()
        
        # Verifico que tenga el nombre del ganador
        self.assertEqual(estado['ganador'], 'Alice')
        
        # Verifico que este marcado como terminado
        self.assertTrue(estado['juego_terminado'])


if __name__ == "__main__":
    unittest.main()