import unittest
from unittest.mock import Mock
from unittest.mock import patch
from cli.cli import CLI


class TestCLI(unittest.TestCase):
    """
    Clase que testea la interfaz CLI de Backgammon.
    
    Recibe: Nada
    Hace: Ejecuta tests para verificar la LOGICA de CLI
    Devuelve: Nada
    """
    
    def setUp(self):
        """
        Configura el ambiente antes de cada test.
        
        Recibe: Nada
        Hace: Crea una instancia de CLI para usar en los tests
        Devuelve: Nada
        """
        self.__cli__ = CLI()
    
    def tearDown(self):
        """
        Limpia después de cada test.
        
        Recibe: Nada
        Hace: Elimina la instancia de CLI
        Devuelve: Nada
        """
        self.__cli__ = None
    
    def test_inicializacion(self):
        """
        Verifica que CLI se inicialice correctamente.
        
        Recibe: Nada
        Hace: Verifica que el atributo juego sea None al inicio
        Devuelve: Nada
        """
        # crear una nueva instancia
        cli_nueva = CLI()
        
        # verificar que juego es None
        juego_inicial = cli_nueva._CLI__juego__
        self.assertEqual(juego_inicial, None)
    
    @patch('builtins.print')
    def test_mostrar_bienvenida(self, mock_print):
        """
        Verifica que mostrar_bienvenida ejecute sin errores.
        
        Recibe: mock_print para no llenar consola
        Hace: Llama a mostrar_bienvenida
        Devuelve: Nada
        """
        # llamar al metodo - debe ejecutar sin errores
        self.__cli__.mostrar_bienvenida()
        
        # verificar que se ejecuto (llamo a print al menos una vez)
        self.assertGreater(mock_print.call_count, 0)
    
    @patch('builtins.input')
    def test_obtener_nombres_jugadores_con_nombres(self, mock_input):
        """
        Verifica que se obtengan los nombres cuando el usuario los ingresa.
        
        Recibe: mock_input para simular entrada de usuario
        Hace: Simula que el usuario ingresa dos nombres
        Devuelve: Nada
        """
        # configurar los valores que devolvera input
        mock_input.side_effect = ["Juan", "Maria"]
        
        # llamar al metodo
        nombre1, nombre2 = self.__cli__.obtener_nombres_jugadores()
        
        # verificar los nombres
        self.assertEqual(nombre1, "Juan")
        self.assertEqual(nombre2, "Maria")
    
    @patch('builtins.input')
    def test_obtener_nombres_jugadores_sin_nombres(self, mock_input):
        """
        Verifica que se usen nombres por defecto cuando no se ingresa nada.
        
        Recibe: mock_input para simular entrada de usuario
        Hace: Simula que el usuario no ingresa nombres (string vacio)
        Devuelve: Nada
        """
        # configurar valores vacios
        mock_input.side_effect = ["", ""]
        
        # llamar al metodo
        nombre1, nombre2 = self.__cli__.obtener_nombres_jugadores()
        
        # verificar que se usen los nombres por defecto
        self.assertEqual(nombre1, "Jugador 1")
        self.assertEqual(nombre2, "Jugador 2")
    
    @patch('builtins.input')
    def test_obtener_nombres_jugadores_un_nombre_vacio(self, mock_input):
        """
        Verifica el caso mixto: un nombre ingresado y otro vacio.
        
        Recibe: mock_input para simular entrada de usuario
        Hace: Simula que solo se ingresa un nombre
        Devuelve: Nada
        """
        # primer nombre con valor, segundo vacio
        mock_input.side_effect = ["Pedro", ""]
        
        # llamar al metodo
        nombre1, nombre2 = self.__cli__.obtener_nombres_jugadores()
        
        # verificar resultados
        self.assertEqual(nombre1, "Pedro")
        self.assertEqual(nombre2, "Jugador 2")
    
    @patch('builtins.print')
    @patch('builtins.input')
    @patch('cli.cli.BackgammonGame')
    def test_crear_juego(self, mock_game_class, mock_input, mock_print):
        """
        Verifica que se cree correctamente un nuevo juego.
        
        Recibe: mocks para BackgammonGame, input y print
        Hace: Simula la creacion de un juego
        Devuelve: Nada
        """
        # configurar nombres
        mock_input.side_effect = ["Ana", "Luis"]
        
        # crear un juego simulado
        juego_simulado = Mock()
        mock_game_class.return_value = juego_simulado
        
        # llamar al metodo
        self.__cli__.crear_juego()
        
        # verificar que se creo el juego
        juego_creado = self.__cli__._CLI__juego__
        self.assertEqual(juego_creado, juego_simulado)
        
        # verificar que se llamo al constructor con los nombres correctos
        mock_game_class.assert_called_once_with("Ana", "Luis")
    
    @patch('builtins.print')
    def test_mostrar_tablero_sin_juego(self, mock_print):
        """
        Verifica que mostrar_tablero maneje el caso sin juego.
        
        Recibe: mock_print para no llenar consola
        Hace: Llama a mostrar_tablero sin juego
        Devuelve: Nada
        """
        # asegurar que no hay juego
        self.__cli__._CLI__juego__ = None
        
        # llamar al metodo - debe ejecutar sin errores
        self.__cli__.mostrar_tablero()
        
        # verificar que se ejecuto
        self.assertGreater(mock_print.call_count, 0)
    
    @patch('builtins.print')
    def test_mostrar_tablero_con_juego(self, mock_print):
        """
        Verifica que se muestre el tablero cuando hay juego.
        
        Recibe: mock_print para no llenar consola
        Hace: Crea un juego simulado y muestra el tablero
        Devuelve: Nada
        """
        # crear un juego simulado
        juego_simulado = Mock()
        juego_simulado.__str__ = Mock(return_value="TABLERO DE PRUEBA")
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.mostrar_tablero()
        
        # verificar que se llamo a str del juego
        juego_simulado.__str__.assert_called_once()
    
    @patch('builtins.print')
    def test_mostrar_ayuda(self, mock_print):
        """
        Verifica que mostrar_ayuda ejecute sin errores.
        
        Recibe: mock_print para no llenar consola
        Hace: Llama a mostrar_ayuda
        Devuelve: Nada
        """
        # llamar al metodo - debe ejecutar sin errores
        self.__cli__.mostrar_ayuda()
        
        # verificar que se ejecuto
        self.assertGreater(mock_print.call_count, 0)
    
    @patch('builtins.print')
    def test_mostrar_estado_sin_juego(self, mock_print):
        """
        Verifica que mostrar_estado maneje el caso sin juego.
        
        Recibe: mock_print para no llenar consola
        Hace: Llama a mostrar_estado sin juego
        Devuelve: Nada
        """
        # asegurar que no hay juego
        self.__cli__._CLI__juego__ = None
        
        # llamar al metodo - debe ejecutar sin errores
        self.__cli__.mostrar_estado()
        
        # verificar que se ejecuto
        self.assertGreater(mock_print.call_count, 0)
    
    @patch('builtins.print')
    def test_mostrar_estado_con_juego(self, mock_print):
        """
        Verifica que se llame a get_estado_juego correctamente.
        
        Recibe: mock_print para no llenar consola
        Hace: Crea un juego simulado con estado completo
        Devuelve: Nada
        """
        # crear jugadores simulados
        jugador1_mock = Mock()
        jugador1_mock.get_nombre = Mock(return_value="Jugador 1")
        
        jugador2_mock = Mock()
        jugador2_mock.get_nombre = Mock(return_value="Jugador 2")
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_estado_juego = Mock(return_value={
            "jugador_actual": "Jugador 1",
            "color_actual": "B",
            "movimientos_disponibles": [3, 5],
            "fichas_sacadas_j1": 5,
            "fichas_sacadas_j2": 3,
            "fichas_en_barra_j1": True,
            "fichas_en_barra_j2": False
        })
        juego_simulado.get_jugador1 = Mock(return_value=jugador1_mock)
        juego_simulado.get_jugador2 = Mock(return_value=jugador2_mock)
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.mostrar_estado()
        
        # verificar que se llamo a get_estado_juego
        juego_simulado.get_estado_juego.assert_called_once()
        juego_simulado.get_jugador1.assert_called()
        juego_simulado.get_jugador2.assert_called()
    
    @patch('builtins.print')
    def test_mostrar_estado_con_juego_sin_movimientos(self, mock_print):
        """
        Verifica el estado cuando no hay movimientos disponibles.
        
        Recibe: mock_print para no llenar consola
        Hace: Crea un juego sin movimientos
        Devuelve: Nada
        """
        # crear jugadores simulados
        jugador1_mock = Mock()
        jugador1_mock.get_nombre = Mock(return_value="Jugador 1")
        
        jugador2_mock = Mock()
        jugador2_mock.get_nombre = Mock(return_value="Jugador 2")
        
        # crear juego simulado sin movimientos
        juego_simulado = Mock()
        juego_simulado.get_estado_juego = Mock(return_value={
            "jugador_actual": "Jugador 1",
            "color_actual": "B",
            "movimientos_disponibles": [],
            "fichas_sacadas_j1": 0,
            "fichas_sacadas_j2": 0,
            "fichas_en_barra_j1": False,
            "fichas_en_barra_j2": False
        })
        juego_simulado.get_jugador1 = Mock(return_value=jugador1_mock)
        juego_simulado.get_jugador2 = Mock(return_value=jugador2_mock)
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.mostrar_estado()
        
        # verificar que se llamo a get_estado_juego
        juego_simulado.get_estado_juego.assert_called_once()
    
    @patch('builtins.print')
    def test_comando_tirar_ya_tiraron_dados(self, mock_print):
        """
        Verifica que no se tiren dados dos veces (logica de control).
        
        Recibe: mock_print para no llenar consola
        Hace: Intenta tirar dados cuando ya hay movimientos
        Devuelve: Nada
        """
        # crear juego simulado con movimientos disponibles
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[3, 5])
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_tirar()
        
        # verificar que NO se llamaron otros metodos del juego
        juego_simulado.tirar_dados.assert_not_called()
    
    @patch('builtins.print')
    def test_comando_tirar_sin_dobles(self, mock_print):
        """
        Verifica la logica de tirar dados normales.
        
        Recibe: mock_print para no llenar consola
        Hace: Simula tirar dados normales
        Devuelve: Nada
        """
        # crear dados simulados (no dobles)
        dados_simulados = Mock()
        dados_simulados.es_doble = Mock(return_value=False)
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[])
        juego_simulado.tirar_dados = Mock(return_value=[3, 5])
        juego_simulado.get_dados = Mock(return_value=dados_simulados)
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=True)
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_tirar()
        
        # verificar que se llamaron los metodos correctos
        juego_simulado.tirar_dados.assert_called_once()
        juego_simulado.get_dados.assert_called_once()
        dados_simulados.es_doble.assert_called_once()
        juego_simulado.puede_hacer_algun_movimiento.assert_called_once()
    
    @patch('builtins.print')
    def test_comando_tirar_con_dobles(self, mock_print):
        """
        Verifica la logica de tirar dados dobles.
        
        Recibe: mock_print para no llenar consola
        Hace: Simula tirar dados dobles
        Devuelve: Nada
        """
        # crear dados simulados (dobles)
        dados_simulados = Mock()
        dados_simulados.es_doble = Mock(return_value=True)
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[])
        juego_simulado.tirar_dados = Mock(return_value=[4, 4])
        juego_simulado.get_dados = Mock(return_value=dados_simulados)
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=True)
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_tirar()
        
        # verificar que se verifico si es doble
        dados_simulados.es_doble.assert_called_once()
    
    @patch('builtins.print')
    def test_comando_tirar_sin_movimientos_validos(self, mock_print):
        """
        Verifica que se termine el turno cuando no hay movimientos.
        
        Recibe: mock_print para no llenar consola
        Hace: Simula tirar dados sin movimientos posibles
        Devuelve: Nada
        """
        # crear dados simulados
        dados_simulados = Mock()
        dados_simulados.es_doble = Mock(return_value=False)
        
        # crear juego simulado sin movimientos posibles
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[])
        juego_simulado.tirar_dados = Mock(return_value=[3, 5])
        juego_simulado.get_dados = Mock(return_value=dados_simulados)
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=False)
        juego_simulado.terminar_turno = Mock()
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_tirar()
        
        # verificar que se termino el turno (LOGICA IMPORTANTE)
        juego_simulado.terminar_turno.assert_called_once()
    
    @patch('builtins.print')
    def test_comando_mover_sin_argumentos_suficientes(self, mock_print):
        """
        Verifica validacion de argumentos.
        
        Recibe: mock_print para no llenar consola
        Hace: Llama a mover con menos de 3 argumentos
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar con comando incompleto
        self.__cli__.comando_mover("mover 13")
        
        # verificar que NO se intento hacer movimiento
        juego_simulado.hacer_movimiento.assert_not_called()
    
    @patch('builtins.print')
    def test_comando_mover_con_argumentos_invalidos(self, mock_print):
        """
        Verifica validacion de tipos de datos.
        
        Recibe: mock_print para no llenar consola
        Hace: Llama a mover con texto en lugar de numeros
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar con argumentos no numericos
        self.__cli__.comando_mover("mover abc def")
        
        # verificar que NO se intento hacer movimiento
        juego_simulado.hacer_movimiento.assert_not_called()
    
    @patch('builtins.print')
    def test_comando_mover_exitoso_sin_terminar_juego(self, mock_print):
        """
        Verifica logica de movimiento exitoso.
        
        Recibe: mock_print para no llenar consola
        Hace: Simula un movimiento valido
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.hacer_movimiento = Mock(return_value=True)
        juego_simulado.esta_terminado = Mock(return_value=False)
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[3])
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=True)
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_mover("mover 13 5")
        
        # verificar que se hizo el movimiento con los parametros correctos
        juego_simulado.hacer_movimiento.assert_called_once_with(13, 5)
        
        # verificar que se verifico si el juego termino
        juego_simulado.esta_terminado.assert_called_once()
    
    @patch('builtins.print')
    def test_comando_mover_exitoso_termina_juego(self, mock_print):
        """
        Verifica logica cuando un movimiento termina el juego.
        
        Recibe: mock_print para no llenar consola
        Hace: Simula un movimiento que gana el juego
        Devuelve: Nada
        """
        # crear ganador simulado
        ganador_mock = Mock()
        ganador_mock.get_nombre = Mock(return_value="Campeon")
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.hacer_movimiento = Mock(return_value=True)
        juego_simulado.esta_terminado = Mock(return_value=True)
        juego_simulado.get_ganador = Mock(return_value=ganador_mock)
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_mover("mover 6 2")
        
        # verificar que se detecto el fin del juego
        juego_simulado.esta_terminado.assert_called_once()
        juego_simulado.get_ganador.assert_called_once()
    
    @patch('builtins.print')
    def test_comando_mover_sin_movimientos_restantes(self, mock_print):
        """
        Verifica que se termine el turno cuando se agotan movimientos.
        
        Recibe: mock_print para no llenar consola
        Hace: Simula movimiento que agota los dados
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.hacer_movimiento = Mock(return_value=True)
        juego_simulado.esta_terminado = Mock(return_value=False)
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[])
        juego_simulado.terminar_turno = Mock()
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_mover("mover 8 3")
        
        # verificar que se termino el turno automaticamente
        juego_simulado.terminar_turno.assert_called_once()
    
    @patch('builtins.print')
    def test_comando_mover_sin_mas_movimientos_validos(self, mock_print):
        """
        Verifica logica cuando hay movimientos pero no son validos.
        
        Recibe: mock_print para no llenar consola
        Hace: Simula caso donde hay movimientos pero ninguno es jugable
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.hacer_movimiento = Mock(return_value=True)
        juego_simulado.esta_terminado = Mock(return_value=False)
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[6])
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=False)
        juego_simulado.terminar_turno = Mock()
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_mover("mover 12 3")
        
        # verificar que se termino el turno
        juego_simulado.terminar_turno.assert_called_once()
    
    @patch('builtins.print')
    def test_comando_mover_invalido(self, mock_print):
        """
        Verifica manejo de movimiento invalido.
        
        Recibe: mock_print para no llenar consola
        Hace: Simula un movimiento rechazado por el juego
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.hacer_movimiento = Mock(return_value=False)
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_mover("mover 24 5")
        
        # verificar que se intento hacer el movimiento
        juego_simulado.hacer_movimiento.assert_called_once()
        
        # verificar que NO se llamo a esta_terminado (porque fallo)
        juego_simulado.esta_terminado.assert_not_called()
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_comando_pasar_sin_movimientos(self, mock_print, mock_input):
        """
        Verifica logica de pasar sin movimientos.
        
        Recibe: mocks para print e input
        Hace: Pasa el turno sin movimientos
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[])
        juego_simulado.terminar_turno = Mock()
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_pasar()
        
        # verificar que se termino el turno directamente
        juego_simulado.terminar_turno.assert_called_once()
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_comando_pasar_con_movimientos_confirmado(self, mock_print, mock_input):
        """
        Verifica logica de confirmacion para pasar con movimientos.
        
        Recibe: mocks para print e input
        Hace: Pasa con movimientos disponibles, usuario dice si
        Devuelve: Nada
        """
        # configurar respuesta afirmativa
        mock_input.return_value = "s"
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[3, 5])
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=True)
        juego_simulado.terminar_turno = Mock()
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_pasar()
        
        # verificar que se pidio confirmacion
        mock_input.assert_called_once()
        
        # verificar que se termino el turno
        juego_simulado.terminar_turno.assert_called_once()
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_comando_pasar_con_movimientos_no_confirmado(self, mock_print, mock_input):
        """
        Verifica que no se pase si el usuario cancela.
        
        Recibe: mocks para print e input
        Hace: Intenta pasar, usuario dice no
        Devuelve: Nada
        """
        # configurar respuesta negativa
        mock_input.return_value = "n"
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[3, 5])
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=True)
        juego_simulado.terminar_turno = Mock()
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_pasar()
        
        # verificar que NO se termino el turno (LOGICA IMPORTANTE)
        juego_simulado.terminar_turno.assert_not_called()
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_comando_pasar_con_movimientos_no_validos(self, mock_print, mock_input):
        """
        Verifica pasar cuando los movimientos no son jugables.
        
        Recibe: mocks para print e input
        Hace: Pasa cuando los movimientos no son jugables
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[6])
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=False)
        juego_simulado.terminar_turno = Mock()
        
        # asignar el juego
        self.__cli__._CLI__juego__ = juego_simulado
        
        # llamar al metodo
        self.__cli__.comando_pasar()
        
        # verificar que NO se pidio confirmacion
        mock_input.assert_not_called()
        
        # verificar que se termino el turno directamente
        juego_simulado.terminar_turno.assert_called_once()
    
    @patch('builtins.print')
    def test_procesar_comando_vacio(self, mock_print):
        """
        Verifica que los comandos vacios se ignoren correctamente.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa un comando vacio
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando vacio
        resultado = self.__cli__.procesar_comando("")
        
        # verificar que retorna True para continuar
        self.assertEqual(resultado, True)
    
    @patch('builtins.print')
    def test_procesar_comando_salir(self, mock_print):
        """
        Verifica logica del comando salir.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa el comando salir
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando salir
        resultado = self.__cli__.procesar_comando("salir")
        
        # verificar que retorna False para terminar (LOGICA IMPORTANTE)
        self.assertEqual(resultado, False)
    
    @patch('builtins.print')
    def test_procesar_comando_ayuda(self, mock_print):
        """
        Verifica procesamiento del comando ayuda.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa el comando ayuda
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.__str__ = Mock(return_value="tablero")
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando ayuda
        resultado = self.__cli__.procesar_comando("ayuda")
        
        # verificar que retorna True para continuar
        self.assertEqual(resultado, True)
    
    @patch('builtins.print')
    def test_procesar_comando_tablero(self, mock_print):
        """
        Verifica procesamiento del comando tablero.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa el comando tablero
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.__str__ = Mock(return_value="tablero")
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando tablero
        resultado = self.__cli__.procesar_comando("tablero")
        
        # verificar que retorna True
        self.assertEqual(resultado, True)
        
        # verificar que se llamo a __str__
        juego_simulado.__str__.assert_called()
    
    @patch('builtins.print')
    def test_procesar_comando_estado(self, mock_print):
        """
        Verifica procesamiento del comando estado.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa el comando estado
        Devuelve: Nada
        """
        # crear jugadores simulados
        jugador1_mock = Mock()
        jugador1_mock.get_nombre = Mock(return_value="J1")
        
        jugador2_mock = Mock()
        jugador2_mock.get_nombre = Mock(return_value="J2")
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_estado_juego = Mock(return_value={
            "jugador_actual": "J1",
            "color_actual": "B",
            "movimientos_disponibles": [],
            "fichas_sacadas_j1": 0,
            "fichas_sacadas_j2": 0,
            "fichas_en_barra_j1": False,
            "fichas_en_barra_j2": False
        })
        juego_simulado.get_jugador1 = Mock(return_value=jugador1_mock)
        juego_simulado.get_jugador2 = Mock(return_value=jugador2_mock)
        juego_simulado.__str__ = Mock(return_value="tablero")
        
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando estado
        resultado = self.__cli__.procesar_comando("estado")
        
        # verificar que retorna True
        self.assertEqual(resultado, True)
        
        # verificar que se llamo a get_estado_juego
        juego_simulado.get_estado_juego.assert_called_once()
    
    @patch('builtins.print')
    def test_procesar_comando_tirar(self, mock_print):
        """
        Verifica procesamiento del comando tirar.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa el comando tirar
        Devuelve: Nada
        """
        # crear dados simulados
        dados_simulados = Mock()
        dados_simulados.es_doble = Mock(return_value=False)
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[])
        juego_simulado.tirar_dados = Mock(return_value=[2, 4])
        juego_simulado.get_dados = Mock(return_value=dados_simulados)
        juego_simulado.puede_hacer_algun_movimiento = Mock(return_value=True)
        
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando tirar
        resultado = self.__cli__.procesar_comando("tirar")
        
        # verificar que retorna True
        self.assertEqual(resultado, True)
        
        # verificar que se llamo a tirar_dados
        juego_simulado.tirar_dados.assert_called_once()
    
    @patch('builtins.print')
    def test_procesar_comando_mover(self, mock_print):
        """
        Verifica procesamiento del comando mover.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa el comando mover
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.hacer_movimiento = Mock(return_value=True)
        juego_simulado.esta_terminado = Mock(return_value=False)
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[])
        juego_simulado.terminar_turno = Mock()
        
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando mover
        resultado = self.__cli__.procesar_comando("mover 6 3")
        
        # verificar que retorna True
        self.assertEqual(resultado, True)
        
        # verificar que se llamo a hacer_movimiento
        juego_simulado.hacer_movimiento.assert_called_once_with(6, 3)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_procesar_comando_pasar(self, mock_print, mock_input):
        """
        Verifica procesamiento del comando pasar.
        
        Recibe: mocks para print e input
        Hace: Procesa el comando pasar
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_movimientos_disponibles = Mock(return_value=[])
        juego_simulado.terminar_turno = Mock()
        
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando pasar
        resultado = self.__cli__.procesar_comando("pasar")
        
        # verificar que retorna True
        self.assertEqual(resultado, True)
        
        # verificar que se llamo a terminar_turno
        juego_simulado.terminar_turno.assert_called_once()
    
    @patch('builtins.print')
    def test_procesar_comando_no_reconocido(self, mock_print):
        """
        Verifica manejo de comandos invalidos.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa un comando inventado
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.__str__ = Mock(return_value="tablero")
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando invalido
        resultado = self.__cli__.procesar_comando("comando_inventado")
        
        # verificar que retorna True (continua el juego)
        self.assertEqual(resultado, True)
    
    @patch('builtins.print')
    def test_procesar_comando_mayusculas(self, mock_print):
        """
        Verifica que los comandos en mayusculas se procesen correctamente.
        
        Recibe: mock_print para no llenar consola
        Hace: Procesa comando en mayusculas
        Devuelve: Nada
        """
        # crear juego simulado
        juego_simulado = Mock()
        self.__cli__._CLI__juego__ = juego_simulado
        
        # procesar comando en mayusculas
        resultado = self.__cli__.procesar_comando("SALIR")
        
        # verificar que retorna False (se convierte a minusculas)
        self.assertEqual(resultado, False)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_ejecutar_juego_termina_inmediatamente(self, mock_game_class, mock_print, mock_input):
        """
        Verifica logica de ejecutar cuando el usuario sale de inmediato.
        
        Recibe: mocks para BackgammonGame, print e input
        Hace: Simula que el usuario escribe salir al inicio
        Devuelve: Nada
        """
        # configurar nombres y comando salir
        mock_input.side_effect = ["Jugador1", "Jugador2", "salir"]
        
        # crear jugador simulado
        jugador_mock = Mock()
        jugador_mock.get_nombre = Mock(return_value="Jugador1")
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_jugador_actual = Mock(return_value=jugador_mock)
        juego_simulado.esta_terminado = Mock(return_value=False)
        
        mock_game_class.return_value = juego_simulado
        
        # ejecutar
        self.__cli__.ejecutar()
        
        # verificar que se creo el juego
        self.assertIsNotNone(self.__cli__._CLI__juego__)
        
        # verificar que se creo con los nombres correctos
        mock_game_class.assert_called_once_with("Jugador1", "Jugador2")
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_ejecutar_juego_completo(self, mock_game_class, mock_print, mock_input):
        """
        Verifica logica de ejecutar con varios comandos.
        
        Recibe: mocks para BackgammonGame, print e input
        Hace: Simula una secuencia de comandos
        Devuelve: Nada
        """
        # configurar secuencia de comandos
        mock_input.side_effect = [
            "Ana",
            "Luis",
            "ayuda",
            "tablero",
            "salir"
        ]
        
        # crear jugador simulado
        jugador_mock = Mock()
        jugador_mock.get_nombre = Mock(return_value="Ana")
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_jugador_actual = Mock(return_value=jugador_mock)
        juego_simulado.esta_terminado = Mock(return_value=False)
        juego_simulado.__str__ = Mock(return_value="tablero")
        
        mock_game_class.return_value = juego_simulado
        
        # ejecutar
        self.__cli__.ejecutar()
        
        # verificar que se creo el juego
        self.assertIsNotNone(self.__cli__._CLI__juego__)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_ejecutar_juego_termina_por_victoria(self, mock_game_class, mock_print, mock_input):
        """
        Verifica logica cuando el juego termina por victoria.
        
        Recibe: mocks para BackgammonGame, print e input
        Hace: Simula que el juego se termina
        Devuelve: Nada
        """
        # configurar nombres
        mock_input.side_effect = ["Victor", "Perdedor"]
        
        # crear jugador simulado
        jugador_mock = Mock()
        jugador_mock.get_nombre = Mock(return_value="Victor")
        
        # crear juego simulado que termina
        juego_simulado = Mock()
        juego_simulado.get_jugador_actual = Mock(return_value=jugador_mock)
        juego_simulado.esta_terminado = Mock(return_value=True)
        
        mock_game_class.return_value = juego_simulado
        
        # ejecutar
        self.__cli__.ejecutar()
        
        # verificar que se detecto el fin del juego
        juego_simulado.esta_terminado.assert_called()
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_iniciar_juego(self, mock_game_class, mock_print, mock_input):
        """
        Verifica el metodo iniciar_juego.
        
        Recibe: mocks para BackgammonGame, print e input
        Hace: Llama a iniciar_juego
        Devuelve: Nada
        """
        # configurar entrada
        mock_input.side_effect = ["J1", "J2", "salir"]
        
        # crear jugador simulado
        jugador_mock = Mock()
        jugador_mock.get_nombre = Mock(return_value="J1")
        
        # crear juego simulado
        juego_simulado = Mock()
        juego_simulado.get_jugador_actual = Mock(return_value=jugador_mock)
        juego_simulado.esta_terminado = Mock(return_value=False)
        
        mock_game_class.return_value = juego_simulado
        
        # iniciar juego
        self.__cli__.iniciar_juego()
        
        # verificar que se ejecuto y se creo el juego
        self.assertIsNotNone(self.__cli__._CLI__juego__)


if __name__ == '__main__':
    unittest.main()