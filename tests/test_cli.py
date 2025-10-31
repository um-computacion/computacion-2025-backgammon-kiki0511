import unittest
from unittest.mock import patch
from cli.cli import CLI


class JugadorStub:
    """
    Representa un jugador simple para usar en los tests.
    
    Recibe: Nombre del jugador
    Hace: Guarda el nombre y lo expone con get_nombre
    Devuelve: Nada
    """
    def __init__(self, nombre):
        self.__nombre__ = nombre
    
    def get_nombre(self):
        return self.__nombre__


class JuegoStub:
    """
    Juego muy simple para simular BackgammonGame en los tests.
    
    Recibe: Nada
    Hace: Permite configurar respuestas para cada metodo usado por CLI
    Devuelve: Nada
    """
    def __init__(self):
        self.movimientos = []
        self.tirada_resultado = [1, 2]
        self.dados_es_doble = False
        self.puede_mover_respuesta = True
        self.hacer_movimiento_respuesta = True
        self.auto_consumir = True
        self.esta_terminado_respuesta = False
        self.ganador = JugadorStub("Ganador")
        self.terminar_turno_llamadas = 0
        self.hacer_llamadas = []
        self.estado = {
            "jugador_actual": "Ana",
            "color_actual": "blanco",
            "movimientos_disponibles": [],
            "juego_terminado": False,
            "ganador": None,
            "turno_paso_automatico": False,
            "fichas_sacadas_j1": 3,
            "fichas_sacadas_j2": 5,
            "fichas_en_barra_j1": True,
            "fichas_en_barra_j2": False,
        }
        self.tablero_texto = "TABLERO SIMPLIFICADO"
        self.jugador1 = JugadorStub("Ana")
        self.jugador2 = JugadorStub("Luis")
        self.jugador_actual = self.jugador1
    
    def tirar_dados(self):
        self.movimientos = list(self.tirada_resultado)
        return list(self.tirada_resultado)
    
    def get_dados(self):
        return self
    
    def es_doble(self):
        return self.dados_es_doble
    
    def puede_hacer_algun_movimiento(self):
        return self.puede_mover_respuesta
    
    def terminar_turno(self):
        self.terminar_turno_llamadas = self.terminar_turno_llamadas + 1
    
    def get_movimientos_disponibles(self):
        return self.movimientos
    
    def hacer_movimiento(self, punto, dado):
        self.hacer_llamadas.append((punto, dado))
        if self.hacer_movimiento_respuesta == False:
            return False
        if self.auto_consumir == True:
            if dado in self.movimientos:
                self.movimientos.remove(dado)
        return True
    
    def esta_terminado(self):
        return self.esta_terminado_respuesta
    
    def get_ganador(self):
        return self.ganador
    
    def get_estado_juego(self):
        return dict(self.estado)
    
    def __str__(self):
        return self.tablero_texto
    
    def get_jugador_actual(self):
        return self.jugador_actual
    
    def get_jugador1(self):
        return self.jugador1
    
    def get_jugador2(self):
        return self.jugador2


class TestCLI(unittest.TestCase):
    """
    Pruebas unitarias para la clase CLI.
    
    Recibe: Nada
    Hace: Verifica cada comando y metodo de la interfaz
    Devuelve: Nada
    """
    
    def setUp(self):
        """
        Crea una instancia nueva de CLI antes de cada test.
        
        Recibe: Nada
        Hace: Guarda la instancia para reutilizar
        Devuelve: Nada
        """
        self.__cli__ = CLI()
        self._print_patcher = patch("builtins.print")
        self._print_mock = self._print_patcher.start()
    
    def tearDown(self):
        """
        Limpia los parches despues de cada prueba.
        
        Recibe: Nada
        Hace: Detiene el parche global de print
        Devuelve: Nada
        """
        self._print_patcher.stop()
    
    def _reiniciar_parcheo_print(self):
        """
        Reinicia el parche global de print.
        
        Recibe: Nada
        Hace: Vuelve a aplicar la sustitución para suprimir salidas
        Devuelve: Nada
        """
        self._print_patcher = patch("builtins.print")
        self._print_mock = self._print_patcher.start()
    
    def capturar_prints(self, funcion, *args, **kwargs):
        """
        Captura los mensajes impresos por una funcion.
        
        Recibe: La funcion y sus argumentos
        Hace: Reemplaza print por una lista temporal
        Devuelve: Lista de mensajes impresos
        """
        self._print_patcher.stop()
        mensajes = []
        def falso_print(*parms, **kparms):
            texto = " ".join(str(x) for x in parms)
            mensajes.append(texto)
        try:
            with patch("builtins.print", falso_print):
                funcion(*args, **kwargs)
        finally:
            self._reiniciar_parcheo_print()
        return mensajes
    
    def test_cli_init_empieza_sin_juego(self):
        """
        Verifica que al crear la CLI no haya juego cargado.
        
        Recibe: Nada
        Hace: Revisa el atributo interno
        Devuelve: Nada
        """
        self.assertIsNone(self.__cli__._CLI__juego__)
    
    def test_cli_propiedad_privada_permite_inyectar_juego(self):
        """
        Verifica que se pueda setear y leer el juego usando la propiedad.
        
        Recibe: Nada
        Hace: Asigna un valor y lo lee nuevamente
        Devuelve: Nada
        """
        stub = JuegoStub()
        self.__cli__._CLI__juego__ = stub
        self.assertEqual(self.__cli__._CLI__juego__, stub)
    
    def test_mostrar_bienvenida_imprime_encabezado(self):
        """
        Prueba mostrar_bienvenida.
        
        Recibe: Nada
        Hace: Captura la salida en pantalla
        Devuelve: Nada
        """
        mensajes = self.capturar_prints(self.__cli__.mostrar_bienvenida)
        self.assertTrue(any("BIENVENIDO AL BACKGAMMON" in linea for linea in mensajes))
    
    def test_obtener_nombres_jugadores_por_defecto(self):
        """
        Prueba obtener_nombres_jugadores cuando se dejan vacios.
        
        Recibe: Nada
        Hace: Simula dos entradas vacias
        Devuelve: Nada
        """
        with patch("builtins.input", side_effect=["", ""]):
            nombre1, nombre2 = self.__cli__.obtener_nombres_jugadores()
        self.assertEqual(nombre1, "Jugador 1")
        self.assertEqual(nombre2, "Jugador 2")
    
    def test_obtener_nombres_jugadores_personalizados(self):
        """
        Prueba obtener_nombres_jugadores con nombres reales.
        
        Recibe: Nada
        Hace: Simula dos entradas con texto
        Devuelve: Nada
        """
        with patch("builtins.input", side_effect=["Ana", "Luis"]):
            nombre1, nombre2 = self.__cli__.obtener_nombres_jugadores()
        self.assertEqual(nombre1, "Ana")
        self.assertEqual(nombre2, "Luis")
    
    def test_crear_juego_asigna_instancia(self):
        """
        Prueba crear_juego.
        
        Recibe: Nada
        Hace: Usa nombres simulados y verifica que __juego__ exista
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "obtener_nombres_jugadores", return_value=("Ana", "Luis")):
            mensajes = self.capturar_prints(self.__cli__.crear_juego)
        self.assertIsNotNone(self.__cli__._CLI__juego__)
        self.assertTrue(any("Juego creado" in linea for linea in mensajes))
    
    def test_mostrar_tablero_sin_juego(self):
        """
        Prueba mostrar_tablero cuando no hay juego.
        
        Recibe: Nada
        Hace: Llama al metodo sin juego cargado
        Devuelve: Nada
        """
        mensajes = self.capturar_prints(self.__cli__.mostrar_tablero)
        self.assertIn("No hay juego en curso.", mensajes[0])
    
    def test_mostrar_tablero_con_juego(self):
        """
        Prueba mostrar_tablero con un juego simulado.
        
        Recibe: Nada
        Hace: Inyecta un tablero falso y verifica la salida
        Devuelve: Nada
        """
        stub = JuegoStub()
        self.__cli__._CLI__juego__ = stub
        mensajes = self.capturar_prints(self.__cli__.mostrar_tablero)
        self.assertTrue(any(stub.tablero_texto in linea for linea in mensajes))
    
    def test_mostrar_ayuda_lista_comandos(self):
        """
        Prueba mostrar_ayuda.
        
        Recibe: Nada
        Hace: Captura los comandos impresos
        Devuelve: Nada
        """
        mensajes = self.capturar_prints(self.__cli__.mostrar_ayuda)
        self.assertTrue(any("tirar" in linea for linea in mensajes))
    
    def test_mostrar_estado_sin_juego(self):
        """
        Prueba mostrar_estado sin juego creado.
        
        Recibe: Nada
        Hace: Llama al metodo y verifica el mensaje
        Devuelve: Nada
        """
        mensajes = self.capturar_prints(self.__cli__.mostrar_estado)
        self.assertIn("No hay juego en curso.", mensajes[0])
    
    def test_mostrar_estado_con_datos(self):
        """
        Prueba mostrar_estado con un juego simulado.
        
        Recibe: Nada
        Hace: Usa JuegoStub para devolver información
        Devuelve: Nada
        """
        stub = JuegoStub()
        self.__cli__._CLI__juego__ = stub
        mensajes = self.capturar_prints(self.__cli__.mostrar_estado)
        self.assertTrue(any("Turno de" in linea for linea in mensajes))
        self.assertTrue(any("SÍ" in linea for linea in mensajes))
        self.assertTrue(any("NO" in linea for linea in mensajes))
    
    def test_mostrar_estado_con_movimientos_y_barra_contraria(self):
        """
        Prueba mostrar_estado cuando hay movimientos y las barras cambian.
        
        Recibe: Nada
        Hace: Configura el estado para recorrer las ramas restantes
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.estado["movimientos_disponibles"] = [1, 2]
        stub.estado["fichas_en_barra_j1"] = False
        stub.estado["fichas_en_barra_j2"] = True
        self.__cli__._CLI__juego__ = stub
        mensajes = self.capturar_prints(self.__cli__.mostrar_estado)
        self.assertTrue(any("Movimientos disponibles" in linea for linea in mensajes))
        self.assertTrue(any("NO" in linea for linea in mensajes))
        self.assertTrue(any("SÍ" in linea for linea in mensajes))
    
    def test_comando_tirar_con_movimientos_previos(self):
        """
        Prueba comando_tirar cuando ya hay movimientos cargados.
        
        Recibe: Nada
        Hace: Verifica que no vuelva a tirar
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = [3]
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            mensajes = self.capturar_prints(self.__cli__.comando_tirar)
        self.assertTrue(any("Ya tiraste los dados" in linea for linea in mensajes))
        mostrar_tablero.assert_called()
    
    def test_comando_tirar_con_dobles_sin_movimientos_validos(self):
        """
        Prueba comando_tirar sacando dobles y sin movimientos validos.
        
        Recibe: Nada
        Hace: Simula que no hay jugadas posibles y finaliza el turno
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = []
        stub.tirada_resultado = [4, 4, 4, 4]
        stub.dados_es_doble = True
        stub.puede_mover_respuesta = False
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            mensajes = self.capturar_prints(self.__cli__.comando_tirar)
        self.assertTrue(any("DOBLES" in linea for linea in mensajes))
        self.assertEqual(stub.terminar_turno_llamadas, 1)
        mostrar_tablero.assert_called()
    
    def test_comando_tirar_sin_dobles_con_movimientos(self):
        """
        Prueba comando_tirar con resultado normal.
        
        Recibe: Nada
        Hace: Simula que hay movimientos disponibles
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.dados_es_doble = False
        stub.movimientos = []
        stub.tirada_resultado = [1, 2]
        stub.puede_mover_respuesta = True
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            mensajes = self.capturar_prints(self.__cli__.comando_tirar)
        self.assertTrue(any("Tienes 2 movimientos." in linea for linea in mensajes))
        self.assertEqual(stub.terminar_turno_llamadas, 0)
        mostrar_tablero.assert_called()
    
    def test_comando_mover_formato_incorrecto(self):
        """
        Prueba comando_mover con cantidad de parametros invalida.
        
        Recibe: Nada
        Hace: Usa un comando incompleto
        Devuelve: Nada
        """
        stub = JuegoStub()
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            mensajes = self.capturar_prints(self.__cli__.comando_mover, "mover 1")
        self.assertTrue(any("Uso: mover" in linea for linea in mensajes))
        mostrar_tablero.assert_called()
    
    def test_comando_mover_argumentos_no_numericos(self):
        """
        Prueba comando_mover cuando los argumentos no son enteros.
        
        Recibe: Nada
        Hace: Usa texto en lugar de números
        Devuelve: Nada
        """
        stub = JuegoStub()
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            mensajes = self.capturar_prints(self.__cli__.comando_mover, "mover a b")
        self.assertTrue(any("deben ser enteros" in linea for linea in mensajes))
        mostrar_tablero.assert_called()
    
    def test_comando_mover_exitoso_sin_movimientos_restantes(self):
        """
        Prueba comando_mover cuando se agotan los movimientos.
        
        Recibe: Nada
        Hace: Simula un movimiento valido que consume el dado
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = [3]
        stub.puede_mover_respuesta = True
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero"):
            self.__cli__.comando_mover("mover 6 3")
        self.assertEqual(stub.terminar_turno_llamadas, 1)
        self.assertEqual(stub.movimientos, [])
    
    def test_comando_mover_exitoso_con_movimientos_sin_opciones(self):
        """
        Prueba comando_mover con movimientos restantes pero sin jugadas validas.
        
        Recibe: Nada
        Hace: Simula que queda un dado pero no hay jugadas
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = [4, 2]
        stub.puede_mover_respuesta = False
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero"):
            self.__cli__.comando_mover("mover 6 4")
        self.assertEqual(stub.terminar_turno_llamadas, 1)
        self.assertIn(2, stub.movimientos)
    
    def test_comando_mover_juego_terminado(self):
        """
        Prueba comando_mover cuando el juego termina con ese movimiento.
        
        Recibe: Nada
        Hace: Configura el juego para que indique ganador
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = [5]
        stub.esta_terminado_respuesta = True
        stub.ganador = JugadorStub("Ana")
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            mensajes = self.capturar_prints(self.__cli__.comando_mover, "mover 6 5")
        self.assertTrue(any("HA GANADO" in linea for linea in mensajes))
        mostrar_tablero.assert_called()
    
    def test_comando_mover_invalido(self):
        """
        Prueba comando_mover cuando el movimiento es invalido.
        
        Recibe: Nada
        Hace: Devuelve False desde el stub
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = [2]
        stub.hacer_movimiento_respuesta = False
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            mensajes = self.capturar_prints(self.__cli__.comando_mover, "mover 6 2")
        self.assertTrue(any("Movimiento inválido" in linea for linea in mensajes))
        mostrar_tablero.assert_called()
    
    def test_comando_pasar_con_movimientos_confirma_no(self):
        """
        Prueba comando_pasar cuando el jugador elige no pasar.
        
        Recibe: Nada
        Hace: Devuelve 'n' para mantener el turno
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = [2]
        stub.puede_mover_respuesta = True
        self.__cli__._CLI__juego__ = stub
        with patch("builtins.input", return_value="n"):
            with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
                self.__cli__.comando_pasar()
        self.assertEqual(stub.terminar_turno_llamadas, 0)
        mostrar_tablero.assert_called()
    
    def test_comando_pasar_con_movimientos_confirma_si(self):
        """
        Prueba comando_pasar cuando el jugador acepta pasar.
        
        Recibe: Nada
        Hace: Devuelve 's' para terminar el turno
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = [4]
        stub.puede_mover_respuesta = True
        self.__cli__._CLI__juego__ = stub
        with patch("builtins.input", return_value="s"):
            with patch.object(self.__cli__, "mostrar_tablero"):
                self.__cli__.comando_pasar()
        self.assertEqual(stub.terminar_turno_llamadas, 1)
    
    def test_comando_pasar_sin_movimientos(self):
        """
        Prueba comando_pasar sin movimientos disponibles.
        
        Recibe: Nada
        Hace: El turno debe terminar directamente
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.movimientos = []
        self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_tablero"):
            self.__cli__.comando_pasar()
        self.assertEqual(stub.terminar_turno_llamadas, 1)
    
    def test_procesar_comando_salir_detiene_bucle(self):
        """
        Prueba procesar_comando con la palabra salir.
        
        Recibe: Nada
        Hace: Verifica que retorna False
        Devuelve: Nada
        """
        resultado = self.__cli__.procesar_comando("salir")
        self.assertFalse(resultado)
    
    def test_procesar_comando_ayuda(self):
        """
        Prueba procesar_comando con ayuda.
        
        Recibe: Nada
        Hace: Verifica que muestra ayuda y tablero
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "mostrar_ayuda") as mostrar_ayuda:
            with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
                resultado = self.__cli__.procesar_comando("ayuda")
        self.assertTrue(resultado)
        mostrar_ayuda.assert_called()
        mostrar_tablero.assert_called()
    
    def test_procesar_comando_tablero(self):
        """
        Prueba procesar_comando con tablero.
        
        Recibe: Nada
        Hace: Verifica que se llama a mostrar_tablero
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            resultado = self.__cli__.procesar_comando("tablero")
        self.assertTrue(resultado)
        mostrar_tablero.assert_called()
    
    def test_procesar_comando_estado(self):
        """
        Prueba procesar_comando con estado.
        
        Recibe: Nada
        Hace: Valida que llame a mostrar_estado y al tablero
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "mostrar_estado") as mostrar_estado:
            with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
                resultado = self.__cli__.procesar_comando("estado")
        self.assertTrue(resultado)
        mostrar_estado.assert_called()
        mostrar_tablero.assert_called()
    
    def test_procesar_comando_tirar(self):
        """
        Prueba procesar_comando con tirar.
        
        Recibe: Nada
        Hace: Asegura que se llame a comando_tirar
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "comando_tirar") as comando_tirar:
            resultado = self.__cli__.procesar_comando("tirar")
        self.assertTrue(resultado)
        comando_tirar.assert_called()
    
    def test_procesar_comando_mover(self):
        """
        Prueba procesar_comando con mover.
        
        Recibe: Nada
        Hace: Asegura que se llame a comando_mover
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "comando_mover") as comando_mover:
            resultado = self.__cli__.procesar_comando("mover 6 3")
        self.assertTrue(resultado)
        comando_mover.assert_called_with("mover 6 3")
    
    def test_procesar_comando_pasar(self):
        """
        Prueba procesar_comando con pasar.
        
        Recibe: Nada
        Hace: Asegura que se llame a comando_pasar
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "comando_pasar") as comando_pasar:
            resultado = self.__cli__.procesar_comando("pasar")
        self.assertTrue(resultado)
        comando_pasar.assert_called()
    
    def test_procesar_comando_desconocido(self):
        """
        Prueba procesar_comando con un comando desconocido.
        
        Recibe: Nada
        Hace: Verifica que imprima mensaje de error
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "mostrar_tablero") as mostrar_tablero:
            mensajes = self.capturar_prints(self.__cli__.procesar_comando, "volar")
        self.assertTrue(any("Comando no reconocido" in linea for linea in mensajes))
        mostrar_tablero.assert_called()
    
    def test_procesar_comando_vacio(self):
        """
        Prueba procesar_comando con comando vacio.
        
        Recibe: Nada
        Hace: Entrega cadena vacía y espera True
        Devuelve: Nada
        """
        resultado = self.__cli__.procesar_comando("")
        self.assertTrue(resultado)
    
    def test_ejecutar_flujo_basico(self):
        """
        Prueba ejecutar con un bucle muy corto.
        
        Recibe: Nada
        Hace: Simula un comando y luego salir
        Devuelve: Nada
        """
        stub = JuegoStub()
        def crear_juego_stub():
            self.__cli__._CLI__juego__ = stub
        with patch.object(self.__cli__, "mostrar_bienvenida"):
            with patch.object(self.__cli__, "mostrar_tablero"):
                with patch.object(self.__cli__, "mostrar_ayuda"):
                    with patch("builtins.input", side_effect=["ayuda", "salir"]):
                        with patch.object(self.__cli__, "procesar_comando", side_effect=[True, False]) as procesar:
                            self.__cli__.crear_juego = crear_juego_stub
                            self.__cli__.ejecutar()
        self.assertEqual(procesar.call_count, 2)
    
    def test_ejecutar_juego_terminado_inmediatamente(self):
        """
        Prueba ejecutar cuando el juego ya esta terminado al entrar al bucle.
        
        Recibe: Nada
        Hace: Verifica que se muestre el mensaje de fin y no pida comando
        Devuelve: Nada
        """
        stub = JuegoStub()
        stub.esta_terminado_respuesta = True
        
        def crear_juego_stub():
            self.__cli__._CLI__juego__ = stub
        
        def ejecutar_envuelto():
            with patch.object(self.__cli__, "mostrar_bienvenida"):
                with patch.object(self.__cli__, "mostrar_tablero"):
                    with patch.object(self.__cli__, "mostrar_ayuda"):
                        with patch("builtins.input", side_effect=AssertionError("No deberia pedir comandos")):
                            self.__cli__.crear_juego = crear_juego_stub
                            self.__cli__.ejecutar()
        
        mensajes = self.capturar_prints(ejecutar_envuelto)
        self.assertTrue(any("Juego terminado" in linea for linea in mensajes))
    
    def test_iniciar_juego_llama_ejecutar(self):
        """
        Prueba iniciar_juego para asegurar que delega en ejecutar.
        
        Recibe: Nada
        Hace: Usa un mock para controlar la llamada
        Devuelve: Nada
        """
        with patch.object(self.__cli__, "ejecutar") as ejecutar:
            self.__cli__.iniciar_juego()
        ejecutar.assert_called_once()


if __name__ == "__main__":
    unittest.main()
