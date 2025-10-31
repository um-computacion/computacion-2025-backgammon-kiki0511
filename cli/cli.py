from core.game import BackgammonGame


class CLI:
    """
    Clase que maneja la interfaz de línea de comandos para Backgammon.
    
    Recibe: Nada
    Hace: Crea una interfaz de texto para jugar Backgammon
    Devuelve: Nada
    """
    
    def __init__(self):
        """
        Inicializa la interfaz CLI.
        
        Recibe: Nada
        Hace: Crea el atributo juego vacío
        Devuelve: Nada
        """
        self.__juego__ = None

    def __get_juego_privado(self):
        """
        getter interno para exponer el atributo privado en tests.
        """
        return self.__juego__

    def __set_juego_privado(self, juego):
        """
        setter interno para permitir inyectar un juego simulado en tests.
        """
        self.__juego__ = juego

    _CLI__juego__ = property(__get_juego_privado, __set_juego_privado)
    
    def mostrar_bienvenida(self):
        """
        Muestra el mensaje de bienvenida.
        
        Recibe: Nada
        Hace: Imprime las reglas básicas del juego
        Devuelve: Nada
        """
        print("=" * 50)
        print("          BIENVENIDO AL BACKGAMMON")
        print("=" * 50)
        print("Reglas básicas:")
        print("- Cada jugador tiene 15 fichas")
        print("- El objetivo es sacar todas las fichas del tablero")
        print("- Los dados determinan cuánto puedes mover")
        print("- Si sacas dobles, juegas 4 movimientos")
        print("- Puedes capturar fichas enemigas solitarias")
        print("=" * 50)
    
    def obtener_nombres_jugadores(self):
        """
        Pide los nombres de los jugadores.
        
        Recibe: Nada
        Hace: Solicita por teclado los nombres
        Devuelve: Tupla con (nombre1, nombre2) como strings
        """
        print("\nConfigurando jugadores...")
        
        # pedir nombre del jugador 1
        nombre1 = input("Nombre del Jugador 1 (fichas blancas): ")
        if nombre1 == "":
            nombre1 = "Jugador 1"
        
        # pedir nombre del jugador 2
        nombre2 = input("Nombre del Jugador 2 (fichas negras): ")
        if nombre2 == "":
            nombre2 = "Jugador 2"
        
        return nombre1, nombre2
    
    def crear_juego(self):
        """
        Crea un nuevo juego.
        
        Recibe: Nada
        Hace: Inicializa el juego con los nombres ingresados
        Devuelve: Nada
        """
        nombre1, nombre2 = self.obtener_nombres_jugadores()
        self.__juego__ = BackgammonGame(nombre1, nombre2)
        
        print("\n¡Juego creado! " + nombre1 + " vs " + nombre2)
        print(nombre1 + " juega con fichas blancas (B)")
        print(nombre2 + " juega con fichas negras (N)")
    
    def mostrar_tablero(self):
        """
        Muestra el tablero actual.
        
        Recibe: Nada
        Hace: Imprime el estado del tablero
        Devuelve: Nada
        """
        if self.__juego__ == None:
            print("No hay juego en curso.")
            return
        
        print("\n" + "=" * 60)
        # mostrar el tablero usando el metodo str del juego
        tablero_texto = str(self.__juego__)
        print(tablero_texto)
        print("=" * 60)
    
    def mostrar_ayuda(self):
        """
        Muestra los comandos disponibles.
        
        Recibe: Nada
        Hace: Imprime la lista de comandos
        Devuelve: Nada
        """
        print("\nCOMANDOS DISPONIBLES:")
        print("tirar - Tira los dados para tu turno")
        print("mover [origen] [dado] - Mueve una ficha")
        print("  Ejemplo: mover 13 5")
        print("  Para sacar de la barra: mover 0 3")
        print("estado - Muestra información del juego")
        print("tablero - Muestra el tablero")
        print("pasar - Termina tu turno (si no puedes mover)")
        print("ayuda - Muestra esta ayuda")
        print("salir - Termina el juego")
    
    def mostrar_estado(self):
        """
        Muestra el estado detallado del juego.
        
        Recibe: Nada
        Hace: Imprime información del estado actual
        Devuelve: Nada
        """
        if self.__juego__ == None:
            print("No hay juego en curso.")
            return
        
        # obtener el estado del juego
        estado = self.__juego__.get_estado_juego()
        
        print("\n--- ESTADO DEL JUEGO ---")
        
        # mostrar de quien es el turno
        jugador_actual = estado.get("jugador_actual", "desconocido")
        color_actual = estado.get("color_actual", "?")
        print("Turno de: " + jugador_actual + " (" + color_actual + ")")
        
        # mostrar movimientos disponibles
        movimientos = estado.get("movimientos_disponibles", [])
        if len(movimientos) > 0:
            print("Movimientos disponibles: " + str(movimientos))
        else:
            print("Tira los dados para comenzar tu turno")
        
        # mostrar fichas sacadas
        print("\nFichas sacadas:")
        fichas_j1 = estado.get("fichas_sacadas_j1", 0)
        fichas_j2 = estado.get("fichas_sacadas_j2", 0)
        nombre_j1 = self.__juego__.get_jugador1().get_nombre()
        nombre_j2 = self.__juego__.get_jugador2().get_nombre()
        print("  " + nombre_j1 + ": " + str(fichas_j1) + "/15")
        print("  " + nombre_j2 + ": " + str(fichas_j2) + "/15")
        
        # mostrar fichas en barra
        print("\nFichas en la barra:")
        barra_j1 = estado.get("fichas_en_barra_j1", False)
        barra_j2 = estado.get("fichas_en_barra_j2", False)
        
        if barra_j1 == True:
            texto_barra_j1 = "SÍ"
        else:
            texto_barra_j1 = "NO"
            
        if barra_j2 == True:
            texto_barra_j2 = "SÍ"
        else:
            texto_barra_j2 = "NO"
            
        print("  " + nombre_j1 + ": " + texto_barra_j1)
        print("  " + nombre_j2 + ": " + texto_barra_j2)
    
    def comando_tirar(self):
        """
        Procesa el comando tirar.
        
        Recibe: Nada
        Hace: Tira los dados y muestra el resultado
        Devuelve: Nada
        """
        # verificar si ya se tiraron los dados
        movimientos = self.__juego__.get_movimientos_disponibles()
        if len(movimientos) > 0:
            print("Ya tiraste los dados este turno. Usa tus movimientos o pasa el turno.")
            self.mostrar_tablero()
            return
        
        # tirar los dados
        resultado = self.__juego__.tirar_dados()
        print("\n¡Dados tirados! Resultado: " + str(resultado))
        
        # verificar si son dobles
        dados = self.__juego__.get_dados()
        if dados.es_doble() == True:
            print("¡DOBLES! Tienes 4 movimientos.")
        else:
            print("Tienes 2 movimientos.")
        
        # verificar si hay movimientos posibles
        puede_mover = self.__juego__.puede_hacer_algun_movimiento()
        if puede_mover == False:
            print("No hay movimientos válidos disponibles. Turno terminado.")
            self.__juego__.terminar_turno()
        
        self.mostrar_tablero()
    
    def comando_mover(self, comando_completo):
        """
        Procesa el comando mover.
        
        Recibe: String con el comando completo
        Hace: Intenta realizar el movimiento
        Devuelve: Nada
        """
        # separar las partes del comando
        partes = comando_completo.split()
        
        # verificar que tenga 3 partes
        if len(partes) != 3:
            print("Uso: mover [punto_origen] [valor_dado]")
            print("Ejemplo: mover 13 5")
            self.mostrar_tablero()
            return
        
        # convertir a numeros
        try:
            punto_origen = int(partes[1])
            valor_dado = int(partes[2])
        except:
            print("Los números deben ser enteros válidos.")
            self.mostrar_tablero()
            return
        
        # intentar hacer el movimiento
        movimiento_valido = self.__juego__.hacer_movimiento(punto_origen, valor_dado)
        
        if movimiento_valido == True:
            print("¡Movimiento exitoso! Ficha movida desde punto " + str(punto_origen))
            
            # verificar si el juego termino
            if self.__juego__.esta_terminado() == True:
                self.mostrar_tablero()
                ganador = self.__juego__.get_ganador()
                print("\n¡FELICITACIONES! " + ganador.get_nombre() + " HA GANADO!")
                return
            
            # verificar si quedan movimientos
            movimientos = self.__juego__.get_movimientos_disponibles()
            if len(movimientos) == 0:
                print("Se agotaron los movimientos. Turno terminado.")
                self.__juego__.terminar_turno()
            else:
                # verificar si puede hacer algun movimiento
                puede_mover = self.__juego__.puede_hacer_algun_movimiento()
                if puede_mover == False:
                    print("No hay más movimientos válidos. Turno terminado.")
                    self.__juego__.terminar_turno()
        else:
            print("Movimiento inválido. Verifica:")
            print("- Que tengas fichas en el punto origen")
            print("- Que el valor del dado esté disponible")
            print("- Que el destino no esté bloqueado")
            print("- Si tienes fichas en la barra, debes sacarlas primero")
        
        self.mostrar_tablero()
    
    def comando_pasar(self):
        """
        Procesa el comando pasar.
        
        Recibe: Nada
        Hace: Termina el turno actual
        Devuelve: Nada
        """
        # verificar si quedan movimientos
        movimientos = self.__juego__.get_movimientos_disponibles()
        
        if len(movimientos) > 0:
            # verificar si puede hacer algun movimiento
            puede_mover = self.__juego__.puede_hacer_algun_movimiento()
            if puede_mover == True:
                respuesta = input("Aún tienes movimientos disponibles. ¿Seguro que quieres pasar? (s/n): ")
                if respuesta != 's':
                    self.mostrar_tablero()
                    return
        
        print("Turno terminado.")
        self.__juego__.terminar_turno()
        self.mostrar_tablero()
    
    def procesar_comando(self, comando):
        """
        Procesa un comando del usuario.
        
        Recibe: String con el comando
        Hace: Ejecuta la acción correspondiente
        Devuelve: Boolean (True para continuar, False para salir)
        """
        # ignorar comandos vacios
        if comando == "":
            return True
        
        # convertir a minusculas
        comando = comando.lower()
        
        # obtener la primera palabra
        primera_palabra = comando.split()[0] if comando.split() else ""
        
        # procesar segun el comando
        if primera_palabra == "salir":
            return False
        elif primera_palabra == "ayuda":
            self.mostrar_ayuda()
            self.mostrar_tablero()
        elif primera_palabra == "tablero":
            self.mostrar_tablero()
        elif primera_palabra == "estado":
            self.mostrar_estado()
            self.mostrar_tablero()
        elif primera_palabra == "tirar":
            self.comando_tirar()
        elif primera_palabra == "mover":
            self.comando_mover(comando)
        elif primera_palabra == "pasar":
            self.comando_pasar()
        else:
            print("Comando no reconocido. Escribe 'ayuda' para ver los comandos disponibles.")
            self.mostrar_tablero()
        
        return True
    
    def ejecutar(self):
        """
        Ejecuta el bucle principal del juego.
        
        Recibe: Nada
        Hace: Ejecuta el juego completo hasta que termine
        Devuelve: Nada
        """
        # inicializar el juego
        self.mostrar_bienvenida()
        self.crear_juego()
        self.mostrar_tablero()
        self.mostrar_ayuda()
        self.mostrar_tablero()
        
        # mostrar quien empieza
        jugador_inicial = self.__juego__.get_jugador_actual()
        print("\n¡Que comience " + jugador_inicial.get_nombre() + "!")
        
        # bucle principal
        continuar = True
        while continuar == True:
            # verificar si el juego termino
            if self.__juego__.esta_terminado() == True:
                print("\n¡Juego terminado!")
                break
            
            # obtener el jugador actual
            jugador_actual = self.__juego__.get_jugador_actual()
            nombre_jugador = jugador_actual.get_nombre()
            
            # pedir comando
            comando = input("\n" + nombre_jugador + "> ")
            
            # procesar el comando
            continuar = self.procesar_comando(comando)
        
        print("Gracias por jugar Backgammon!")
    
    def iniciar_juego(self):
        """
        Metodo principal para iniciar el juego desde fuera.
        
        Recibe: Nada
        Hace: Inicia el juego completo
        Devuelve: Nada
        """
        self.ejecutar()


# Crear una instancia y ejecutar si es el archivo principal
if __name__ == "__main__":
    juego_cli = CLI()
    juego_cli.iniciar_juego()
