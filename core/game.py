from core.board import Board
from core.player import Player
from core.dice import Dice


class BackgammonGame:
    """
    Clase principal del juego de Backgammon.
    
    Recibe:
        Nada directamente (se usa en __init__).
    Hace:
        Maneja todo el flujo del juego, los turnos y las reglas.
    Devuelve:
        Nada (es una clase).
    """

    def __init__(self, nombre_jugador1, nombre_jugador2):
        """
        Crea un nuevo juego de Backgammon con dos jugadores.
        
        Recibe:
            nombre_jugador1 (str): nombre del primer jugador
            nombre_jugador2 (str): nombre del segundo jugador
        Hace:
            Crea el tablero, los jugadores, los dados y prepara todo para jugar.
        Devuelve:
            Nada (es el constructor).
        """
        # creo el tablero del juego
        self.__tablero__ = Board()
        
        # creo el primer jugador con fichas blancas (direccion 1)
        self.__jugador1__ = Player(nombre_jugador1, 1)
        
        # creo el segundo jugador con fichas negras (direccion -1)
        self.__jugador2__ = Player(nombre_jugador2, -1)
        
        # el jugador 1 empieza jugando primero
        self.__jugador_actual__ = self.__jugador1__
        
        # creo los dados para tirar
        self.__dados__ = Dice()
        
        # lista vacia para guardar los valores de dados que puedo usar
        self.__movimientos_disponibles__ = []
        
        # al principio el juego no esta terminado
        self.__juego_terminado__ = False
        
        # al principio no hay ganador
        self.__ganador__ = None
        
        # variable para saber si el turno cambio solo
        self.__turno_paso_automatico__ = False

    def get_tablero(self):
        """
        Devuelve el tablero del juego.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el tablero actual.
        Devuelve:
            Board: el tablero del juego.
        """
        return self.__tablero__

    def get_jugador_actual(self):
        """
        Devuelve el jugador que esta jugando ahora.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el jugador que tiene el turno actual.
        Devuelve:
            Player: el jugador actual.
        """
        return self.__jugador_actual__

    def get_jugador1(self):
        """
        Devuelve el primer jugador.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el jugador 1.
        Devuelve:
            Player: el primer jugador.
        """
        return self.__jugador1__

    def get_jugador2(self):
        """
        Devuelve el segundo jugador.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el jugador 2.
        Devuelve:
            Player: el segundo jugador.
        """
        return self.__jugador2__

    def get_dados(self):
        """
        Devuelve los dados del juego.
        
        Recibe:
            Nada.
        Hace:
            Obtiene los dados.
        Devuelve:
            Dice: los dados del juego.
        """
        return self.__dados__

    def get_movimientos_disponibles(self):
        """
        Devuelve la lista de movimientos disponibles.
        
        Recibe:
            Nada.
        Hace:
            Obtiene los valores de dados que todavia no se usaron.
        Devuelve:
            list: lista con los valores de dados disponibles.
        """
        return self.__movimientos_disponibles__

    def esta_terminado(self):
        """
        Verifica si el juego termino.
        
        Recibe:
            Nada.
        Hace:
            Chequea si el juego ya tiene un ganador.
        Devuelve:
            bool: True si el juego termino, False si todavia se esta jugando.
        """
        return self.__juego_terminado__

    def get_ganador(self):
        """
        Devuelve el ganador del juego.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el jugador que gano (si hay).
        Devuelve:
            Player: el jugador ganador, o None si no hay ganador todavia.
        """
        return self.__ganador__

    def turno_paso_automaticamente(self):
        """
        Verifica si el turno paso automaticamente.
        
        Recibe:
            Nada.
        Hace:
            Chequea si el turno cambio solo porque no habia movimientos.
        Devuelve:
            bool: True si el turno paso automaticamente, False si no.
        """
        return self.__turno_paso_automatico__

    def get_color_jugador_actual(self):
        """
        Devuelve el color del jugador que esta jugando.
        
        Recibe:
            Nada.
        Hace:
            Obtiene el color segun la direccion del jugador actual.
        Devuelve:
            str: 'blanco' si direccion es 1, 'negro' si direccion es -1.
        """
        # obtengo la direccion del jugador actual
        direccion_jugador = self.__jugador_actual__.get_direccion()
        
        # si la direccion es 1, el jugador tiene fichas blancas
        if direccion_jugador == 1:
            color = 'blanco'
        else:
            # si no es 1, entonces es -1 y tiene fichas negras
            color = 'negro'
        
        return color

    def tirar_dados(self):
        """
        Tira los dados para empezar un turno.
        
        Recibe:
            Nada.
        Hace:
            Tira los dados y guarda los valores como movimientos disponibles.
        Devuelve:
            list: lista con los valores que salieron en los dados.
        """
        # tiro los dados
        resultado_dados = self.__dados__.tirar()
        
        # copio los valores a movimientos disponibles (hago una lista nueva)
        self.__movimientos_disponibles__ = []
        for valor in resultado_dados:
            self.__movimientos_disponibles__.append(valor)
        
        return resultado_dados

    def puede_hacer_movimiento(self, punto_origen, valor_dado):
        """
        Verifica si un movimiento es valido segun las reglas.
        
        Recibe:
            punto_origen (int): punto desde donde quiero mover (0 significa barra)
            valor_dado (int): valor del dado que quiero usar
        Hace:
            Chequea todas las reglas: dado disponible, fichas en barra, 
            color correcto, destino valido.
        Devuelve:
            bool: True si el movimiento es valido, False si no lo es.
        """
        # primero verifico si tengo ese dado disponible
        dado_disponible = False
        for dado in self.__movimientos_disponibles__:
            if dado == valor_dado:
                dado_disponible = True
                break
        
        # si no tengo el dado, no puedo mover
        if dado_disponible == False:
            return False
        
        # obtengo el color del jugador actual
        color = self.get_color_jugador_actual()
        
        # obtengo el tablero
        tablero = self.__tablero__
        
        # verifico si tengo fichas en la barra
        tiene_fichas_en_barra = tablero.jugador_tiene_fichas_en_barra(color)
        
        # si tengo fichas en la barra, solo puedo mover desde la barra
        if tiene_fichas_en_barra == True:
            # si intento mover desde otro punto que no sea la barra, es invalido
            if punto_origen != 0:
                return False
            
            # calculo a donde iria desde la barra
            if color == 'blanco':
                # blanco entra por arriba (25 - dado)
                destino = 25 - valor_dado
            else:
                # negro entra por abajo (dado)
                destino = valor_dado
            
            # verifico que el destino este dentro del tablero
            if destino < 1 or destino > 24:
                return False
            
            # verifico si puedo mover a ese punto
            puedo_mover_ahi = tablero.puede_mover_a_punto(destino, color)
            
            if puedo_mover_ahi == True:
                return True
            else:
                return False
        
        # si llego aca es un movimiento normal (no desde barra)
        
        # verifico que haya fichas en el punto de origen
        cantidad_fichas_origen = tablero.contar_fichas_en_punto(punto_origen)
        if cantidad_fichas_origen == 0:
            return False
        
        # verifico que las fichas sean de mi color
        color_origen = tablero.get_color_en_punto(punto_origen)
        if color_origen != color:
            return False
        
        # calculo el punto de destino
        if color == 'blanco':
            # blanco se mueve hacia abajo (resta)
            destino = punto_origen - valor_dado
            
            if destino < 1:
                # intento sacar ficha del tablero (bear off)
                puede_sacar = tablero.puede_sacar_fichas(color)
                if puede_sacar == False:
                    return False
                
                if destino == 0:
                    return True
                
                # dado mayor al necesario: solo si no hay fichas en puntos superiores
                punto_revision = punto_origen + 1
                while punto_revision <= 6:
                    fichas_revision = tablero.get_fichas_en_punto(punto_revision)
                    indice_revision = 0
                    while indice_revision < len(fichas_revision):
                        if fichas_revision[indice_revision].get_color() == color:
                            return False
                        indice_revision = indice_revision + 1
                    punto_revision = punto_revision + 1
                
                return True
        else:
            # negro se mueve hacia arriba (suma)
            destino = punto_origen + valor_dado
            
            if destino > 24:
                # intento sacar ficha del tablero (bear off)
                puede_sacar = tablero.puede_sacar_fichas(color)
                if puede_sacar == False:
                    return False
                
                if destino == 25:
                    return True
                
                # dado mayor al necesario: solo si no hay fichas en puntos superiores
                punto_revision = punto_origen + 1
                while punto_revision <= 24:
                    fichas_revision = tablero.get_fichas_en_punto(punto_revision)
                    indice_revision = 0
                    while indice_revision < len(fichas_revision):
                        if fichas_revision[indice_revision].get_color() == color:
                            return False
                        indice_revision = indice_revision + 1
                    punto_revision = punto_revision + 1
                
                return True
        
        # verifico que el destino este dentro del tablero
        if destino < 1 or destino > 24:
            return False
        
        # verifico si puedo mover a ese punto
        puedo_mover_ahi = tablero.puede_mover_a_punto(destino, color)
        
        if puedo_mover_ahi == True:
            return True
        else:
            return False

    def puede_hacer_algun_movimiento(self):
        """
        Verifica si el jugador puede hacer al menos un movimiento.
        
        Recibe:
            Nada.
        Hace:
            Chequea todos los movimientos posibles con los dados disponibles.
        Devuelve:
            bool: True si hay al menos un movimiento valido, False si no.
        """
        # si no tengo dados disponibles, no puedo mover
        if len(self.__movimientos_disponibles__) == 0:
            return False
        
        # obtengo el color del jugador actual
        color = self.get_color_jugador_actual()
        
        # obtengo el tablero
        tablero = self.__tablero__
        
        # verifico si tengo fichas en la barra
        tiene_fichas_en_barra = tablero.jugador_tiene_fichas_en_barra(color)
        
        # pruebo cada dado disponible
        for dado in self.__movimientos_disponibles__:
            # si tengo fichas en la barra, solo puedo mover desde ahi
            if tiene_fichas_en_barra == True:
                # verifico si puedo mover desde la barra con este dado
                if self.puede_hacer_movimiento(0, dado) == True:
                    return True
            else:
                # no tengo fichas en la barra, pruebo todos los puntos
                for punto in range(1, 25):
                    # verifico si puedo mover desde este punto
                    if self.puede_hacer_movimiento(punto, dado) == True:
                        return True
        
        # si llego aca, no encontre ningun movimiento valido
        return False

    def hacer_movimiento(self, punto_origen, valor_dado):
        """
        Ejecuta un movimiento en el tablero.
        
        Recibe:
            punto_origen (int): punto desde donde mover (0 significa barra)
            valor_dado (int): valor del dado que quiero usar
        Hace:
            Verifica que sea valido, mueve la ficha, consume el dado usado,
            y cambia el turno si no quedan mas dados.
        Devuelve:
            bool: True si el movimiento se hizo exitosamente, False si no.
        """
        # obtengo el color del jugador actual
        color = self.get_color_jugador_actual()
        
        # obtengo el tablero
        tablero = self.__tablero__
        
        # guardo si este es el ultimo dado disponible antes de intentar mover
        ultimo_dado_disponible = (
            len(self.__movimientos_disponibles__) == 1
            and valor_dado in self.__movimientos_disponibles__
        )

        # primero verifico si el movimiento es valido
        movimiento_valido = self.puede_hacer_movimiento(punto_origen, valor_dado)
        if movimiento_valido == False:
            # si era el ultimo dado y no se pudo usar, igual termino el turno
            if ultimo_dado_disponible:
                self.__movimientos_disponibles__.pop()
                self.terminar_turno()
            return False
        
        # calculo el punto de destino
        if punto_origen == 0:
            # estoy moviendo desde la barra
            if color == 'blanco':
                destino = 25 - valor_dado
            else:
                destino = valor_dado
        else:
            # estoy moviendo desde un punto normal
            if color == 'blanco':
                destino = punto_origen - valor_dado
            else:
                destino = punto_origen + valor_dado
        
        # ejecuto el movimiento en el tablero
        if punto_origen == 0:
            # es un reingreso desde la barra
            movimiento_exitoso = tablero.reingresar_desde_barra(color, destino)
        else:
            # determinar si es un bear off
            es_bear_off = False
            if color == 'blanco' and destino < 1:
                es_bear_off = True
            if color == 'negro' and destino > 24:
                es_bear_off = True

            if es_bear_off:
                movimiento_exitoso = tablero.sacar_ficha_del_tablero(punto_origen, color)
                if movimiento_exitoso == True:
                    jugador_actual = self.get_jugador_actual()
                    jugador_actual.sacar_ficha_del_tablero()
            else:
                # es un movimiento normal
                movimiento_exitoso = tablero.mover_ficha(punto_origen, destino, color)
        
        # si el movimiento no se pudo hacer, devuelvo False
        if movimiento_exitoso == False:
            return False
        
        # el movimiento se hizo, ahora consumo el dado usado
        # busco el dado en la lista y lo saco
        indice_encontrado = -1
        for i in range(len(self.__movimientos_disponibles__)):
            valor_actual = self.__movimientos_disponibles__[i]
            if valor_actual == valor_dado:
                indice_encontrado = i
                break
        
        # si encontre el dado, lo saco de la lista
        if indice_encontrado >= 0:
            self.__movimientos_disponibles__.pop(indice_encontrado)
        
        # verifico si ya no quedan dados disponibles
        cantidad_dados_restantes = len(self.__movimientos_disponibles__)
        if cantidad_dados_restantes == 0:
            # si no quedan dados, termino el turno
            self.terminar_turno()
        
        return True

    def terminar_turno(self):
        """
        Termina el turno actual y pasa al siguiente jugador.
        
        Recibe:
            Nada.
        Hace:
            Cambia al otro jugador, limpia dados y verifica victoria.
        Devuelve:
            Nada.
        """
        # primero verifico si alguien gano
        self.verificar_victoria()
        
        # si el juego no termino, cambio de jugador
        if self.__juego_terminado__ == False:
            # verifico quien es el jugador actual y cambio al otro
            if self.__jugador_actual__ == self.__jugador1__:
                # si era el jugador 1, paso al jugador 2
                self.__jugador_actual__ = self.__jugador2__
            else:
                # si era el jugador 2, paso al jugador 1
                self.__jugador_actual__ = self.__jugador1__
        
        # limpio la lista de movimientos disponibles
        self.__movimientos_disponibles__ = []
        
        # reseteo el flag de turno automatico
        self.__turno_paso_automatico__ = False

    def verificar_victoria(self):
        """
        Verifica si algun jugador gano el juego.
        
        Recibe:
            Nada.
        Hace:
            Chequea si algun jugador saco todas sus fichas.
        Devuelve:
            Nada.
        """
        # obtengo el tablero
        tablero = self.__tablero__
        
        # verifico si el jugador 1 (blanco) gano
        fichas_blancas_en_tablero = 0
        fichas_blancas_en_barra = tablero.contar_fichas_en_barra('blanco')
        
        # cuento las fichas blancas en todos los puntos
        for punto in range(1, 25):
            color_punto = tablero.get_color_en_punto(punto)
            if color_punto == 'blanco':
                cantidad = tablero.contar_fichas_en_punto(punto)
                fichas_blancas_en_tablero = fichas_blancas_en_tablero + cantidad
        
        # sumo las fichas en la barra
        total_fichas_blancas = fichas_blancas_en_tablero + fichas_blancas_en_barra
        
        # si no tiene fichas y el rival no tiene fichas en la barra, gano
        if total_fichas_blancas == 0:
            fichas_negras_en_barra = tablero.contar_fichas_en_barra('negro')
            if fichas_negras_en_barra == 0:
                self.__juego_terminado__ = True
                self.__ganador__ = self.__jugador1__
                return
        
        # verifico si el jugador 2 (negro) gano
        fichas_negras_en_tablero = 0
        fichas_negras_en_barra = tablero.contar_fichas_en_barra('negro')
        
        # cuento las fichas negras en todos los puntos
        for punto in range(1, 25):
            color_punto = tablero.get_color_en_punto(punto)
            if color_punto == 'negro':
                cantidad = tablero.contar_fichas_en_punto(punto)
                fichas_negras_en_tablero = fichas_negras_en_tablero + cantidad
        
        # sumo las fichas en la barra
        total_fichas_negras = fichas_negras_en_tablero + fichas_negras_en_barra
        
        # si no tiene fichas, gano
        if total_fichas_negras == 0:
            fichas_blancas_en_barra = tablero.contar_fichas_en_barra('blanco')
            if fichas_blancas_en_barra == 0:
                self.__juego_terminado__ = True
                self.__ganador__ = self.__jugador2__

    def pasar_turno_si_no_hay_movimientos(self):
        """
        Pasa el turno automaticamente si no hay movimientos disponibles.
        
        Recibe:
            Nada.
        Hace:
            Verifica si puede hacer algun movimiento y si no, pasa el turno.
        Devuelve:
            bool: True si el turno paso automaticamente, False si no.
        """
        # verifico si puedo hacer algun movimiento
        puedo_mover = self.puede_hacer_algun_movimiento()
        
        # si no puedo mover, paso el turno automaticamente
        if puedo_mover == False:
            self.__turno_paso_automatico__ = True

            # cambiar manualmente de jugador
            if self.__jugador_actual__ == self.__jugador1__:
                self.__jugador_actual__ = self.__jugador2__
            else:
                self.__jugador_actual__ = self.__jugador1__

            # limpiar movimientos para el nuevo turno
            self.__movimientos_disponibles__ = []

            # resetear flag para reflejar el estado final
            self.__turno_paso_automatico__ = False
            return True
        
        # si puedo mover, no paso el turno
        return False

    def get_estado_juego(self):
        """
        Devuelve el estado actual del juego.
        
        Recibe:
            Nada.
        Hace:
            Recopila toda la informacion del estado actual en un diccionario.
        Devuelve:
            dict: diccionario con el estado del juego (jugador actual, color,
                  movimientos disponibles, si termino, ganador).
        """
        # creo un diccionario vacio para guardar el estado
        estado = {}
        
        # guardo el nombre del jugador actual
        nombre_actual = self.__jugador_actual__.get_nombre()
        estado['jugador_actual'] = nombre_actual
        
        # guardo el color del jugador actual
        color_actual = self.get_color_jugador_actual()
        estado['color_actual'] = color_actual
        
        # guardo una copia de los movimientos disponibles
        movimientos_copia = []
        for movimiento in self.__movimientos_disponibles__:
            movimientos_copia.append(movimiento)
        estado['movimientos_disponibles'] = movimientos_copia
        
        # guardo si el juego esta terminado
        estado['juego_terminado'] = self.__juego_terminado__
        
        # guardo el ganador (si hay)
        if self.__ganador__ != None:
            nombre_ganador = self.__ganador__.get_nombre()
            estado['ganador'] = nombre_ganador
        else:
            estado['ganador'] = None
        
        # guardo si el turno paso automaticamente
        estado['turno_paso_automatico'] = self.__turno_paso_automatico__
        
        return estado

    def __str__(self):
        """
        Crea una representacion en texto del juego.
        
        Recibe:
            Nada.
        Hace:
            Genera un string con los nombres de los jugadores y el tablero.
        Devuelve:
            str: texto que representa el estado del juego.
        """
        # obtengo el nombre del jugador 1
        nombre_jugador1 = self.__jugador1__.get_nombre()
        
        # obtengo el nombre del jugador 2
        nombre_jugador2 = self.__jugador2__.get_nombre()
        
        # creo el encabezado con los nombres
        encabezado = "Backgammon: " + nombre_jugador1 + " vs " + nombre_jugador2
        
        # obtengo la representacion del tablero
        texto_tablero = str(self.__tablero__)
        
        # uno todo con un salto de linea
        texto_completo = encabezado + "\n" + texto_tablero
        
        return texto_completo
