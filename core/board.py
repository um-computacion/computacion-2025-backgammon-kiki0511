from core.checker import Checker


class Board:
    """
    Clase que representa el tablero de Backgammon.
    
    Recibe: Nada
    Hace: Crea un tablero con 26 puntos y coloca las fichas iniciales
    Devuelve: Nada
    """
    
    def __init__(self):
        """
        Inicializa el tablero con 26 puntos vacios.
        
        Recibe: Nada
        Hace: Crea 26 listas vacias y coloca las fichas iniciales
        Devuelve: Nada
        """
        # crear 26 puntos vacios (0 es la barra, 25 es fichas sacadas)
        self.__puntos__ = []
        contador = 0
        while contador < 26:
            self.__puntos__.append([])
            contador = contador + 1
        
        # colocar las fichas en posicion inicial
        self.colocar_fichas_iniciales()
    
    def colocar_fichas_iniciales(self):
        """
        Coloca las 15 fichas de cada jugador en posición inicial.
        
        Recibe: Nada
        Hace: Pone las fichas blancas y negras en sus posiciones iniciales
        Devuelve: Nada
        """
        # fichas blancas - 2 en punto 24
        contador = 0
        while contador < 2:
            ficha = Checker('blanco')
            ficha.set_posicion(24)
            self.__puntos__[24].append(ficha)
            contador = contador + 1
        
        # fichas blancas - 5 en punto 13
        contador = 0
        while contador < 5:
            ficha = Checker('blanco')
            ficha.set_posicion(13)
            self.__puntos__[13].append(ficha)
            contador = contador + 1
        
        # fichas blancas - 3 en punto 8
        contador = 0
        while contador < 3:
            ficha = Checker('blanco')
            ficha.set_posicion(8)
            self.__puntos__[8].append(ficha)
            contador = contador + 1
        
        # fichas blancas - 5 en punto 6
        contador = 0
        while contador < 5:
            ficha = Checker('blanco')
            ficha.set_posicion(6)
            self.__puntos__[6].append(ficha)
            contador = contador + 1
        
        # fichas negras - 2 en punto 1
        contador = 0
        while contador < 2:
            ficha = Checker('negro')
            ficha.set_posicion(1)
            self.__puntos__[1].append(ficha)
            contador = contador + 1
        
        # fichas negras - 5 en punto 12
        contador = 0
        while contador < 5:
            ficha = Checker('negro')
            ficha.set_posicion(12)
            self.__puntos__[12].append(ficha)
            contador = contador + 1
        
        # fichas negras - 3 en punto 17
        contador = 0
        while contador < 3:
            ficha = Checker('negro')
            ficha.set_posicion(17)
            self.__puntos__[17].append(ficha)
            contador = contador + 1
        
        # fichas negras - 5 en punto 19
        contador = 0
        while contador < 5:
            ficha = Checker('negro')
            ficha.set_posicion(19)
            self.__puntos__[19].append(ficha)
            contador = contador + 1
    
    def get_fichas_en_punto(self, punto):
        """
        Obtiene las fichas en un punto específico.
        
        Recibe: Número del punto (int)
        Hace: Busca las fichas en ese punto
        Devuelve: Lista de fichas en el punto
        """
        if punto < 0:
            return []
        if punto > 25:
            return []
        
        return self.__puntos__[punto]
    
    def contar_fichas_en_punto(self, punto):
        """
        Cuenta cuántas fichas hay en un punto.
        
        Recibe: Número del punto (int)
        Hace: Cuenta las fichas en ese punto
        Devuelve: Cantidad de fichas (int)
        """
        fichas = self.get_fichas_en_punto(punto)
        return len(fichas)
    
    def punto_esta_vacio(self, punto):
        """
        Verifica si un punto está vacío.
        
        Recibe: Número del punto (int)
        Hace: Verifica si no hay fichas en el punto
        Devuelve: True si está vacío, False si tiene fichas
        """
        cantidad = self.contar_fichas_en_punto(punto)
        if cantidad == 0:
            return True
        else:
            return False
    
    def get_color_en_punto(self, punto):
        """
        Obtiene el color de las fichas en un punto.
        
        Recibe: Número del punto (int)
        Hace: Busca el color de la primera ficha
        Devuelve: String con el color o None si está vacío
        """
        fichas = self.get_fichas_en_punto(punto)
        
        if len(fichas) == 0:
            return None
        
        primera_ficha = fichas[0]
        color = primera_ficha.get_color()
        return color
    
    def puede_mover_a_punto(self, punto, color_jugador):
        """
        Verifica si se puede mover a un punto.
        
        Recibe: Número del punto (int) y color del jugador (string)
        Hace: Verifica según las reglas si el movimiento es válido
        Devuelve: True si puede mover, False si no puede
        """
        # verificar que el punto sea valido
        if punto < 1:
            return False
        if punto > 24:
            return False
        
        cantidad_fichas = self.contar_fichas_en_punto(punto)
        
        # si esta vacio, siempre se puede
        if cantidad_fichas == 0:
            return True
        
        color_punto = self.get_color_en_punto(punto)
        
        # si es del mismo color, siempre se puede
        if color_punto == color_jugador:
            return True
        
        # si es del color contrario y hay solo 1, se puede capturar
        if color_punto != color_jugador:
            if cantidad_fichas == 1:
                return True
        
        # en cualquier otro caso, no se puede
        return False
    
    def mover_ficha(self, punto_origen, punto_destino, color_jugador):
        """
        Mueve una ficha de un punto a otro.
        
        Recibe: Punto origen (int), punto destino (int), color jugador (string)
        Hace: Mueve la ficha si es válido, captura si corresponde
        Devuelve: True si movió, False si no pudo
        """
        # verificar que hay fichas en el origen
        cantidad_origen = self.contar_fichas_en_punto(punto_origen)
        if cantidad_origen == 0:
            return False
        
        # verificar que la ficha es del color correcto
        color_origen = self.get_color_en_punto(punto_origen)
        if color_origen != color_jugador:
            return False
        
        # verificar que se puede mover al destino
        puede_mover = self.puede_mover_a_punto(punto_destino, color_jugador)
        if puede_mover == False:
            return False
        
        # sacar la ultima ficha del origen
        ficha = self.__puntos__[punto_origen].pop()
        
        # verificar si hay que capturar
        cantidad_destino = self.contar_fichas_en_punto(punto_destino)
        color_destino = self.get_color_en_punto(punto_destino)
        
        if cantidad_destino == 1:
            if color_destino != color_jugador:
                # capturar la ficha enemiga
                ficha_capturada = self.__puntos__[punto_destino].pop()
                ficha_capturada.set_posicion(0)
                self.__puntos__[0].append(ficha_capturada)
        
        # mover la ficha al destino
        ficha.set_posicion(punto_destino)
        self.__puntos__[punto_destino].append(ficha)
        
        return True
    
    def reingresar_desde_barra(self, color_jugador, destino):
        """
        Reingresa una ficha desde la barra al tablero.
        
        Recibe: Color del jugador (string) y punto destino (int)
        Hace: Mueve una ficha de la barra al destino si es válido
        Devuelve: True si reingresó, False si no pudo
        """
        # verificar que el destino es valido
        if destino < 1:
            return False
        if destino > 24:
            return False
        
        # verificar que se puede mover al destino
        puede_mover = self.puede_mover_a_punto(destino, color_jugador)
        if puede_mover == False:
            return False
        
        # buscar una ficha del jugador en la barra
        ficha = self.sacar_ficha_de_barra(color_jugador)
        if ficha == None:
            return False
        
        # verificar si hay que capturar
        cantidad_destino = self.contar_fichas_en_punto(destino)
        color_destino = self.get_color_en_punto(destino)
        
        if cantidad_destino == 1:
            if color_destino != color_jugador:
                # capturar la ficha enemiga
                ficha_capturada = self.__puntos__[destino].pop()
                ficha_capturada.set_posicion(0)
                self.__puntos__[0].append(ficha_capturada)
        
        # poner la ficha en el destino
        ficha.set_posicion(destino)
        self.__puntos__[destino].append(ficha)
        
        return True
    
    def jugador_tiene_fichas_en_barra(self, color_jugador):
        """
        Verifica si el jugador tiene fichas en la barra.
        
        Recibe: Color del jugador (string)
        Hace: Busca fichas del color en el punto 0 (barra)
        Devuelve: True si tiene fichas, False si no tiene
        """
        fichas_barra = self.get_fichas_en_punto(0)
        
        i = 0
        while i < len(fichas_barra):
            if fichas_barra[i].get_color() == color_jugador:
                return True
            i = i + 1
        
        return False
    
    def sacar_ficha_de_barra(self, color_jugador):
        """
        Saca una ficha del jugador de la barra.
        
        Recibe: Color del jugador (string)
        Hace: Busca y extrae una ficha del color de la barra
        Devuelve: Objeto Checker si encontró, None si no hay
        """
        fichas_barra = self.get_fichas_en_punto(0)
        
        i = 0
        while i < len(fichas_barra):
            if fichas_barra[i].get_color() == color_jugador:
                # sacar esta ficha de la lista
                ficha = self.__puntos__[0].pop(i)
                return ficha
            i = i + 1
        
        return None
    
    def puede_sacar_fichas(self, color_jugador):
        """
        Verifica si el jugador puede empezar a sacar fichas del tablero.
        
        Recibe: Color del jugador (string)
        Hace: Verifica que no tenga fichas en barra y todas estén en cuadrante final
        Devuelve: True si puede sacar, False si no puede
        """
        # no puede sacar si tiene fichas en barra
        if self.jugador_tiene_fichas_en_barra(color_jugador) == True:
            return False
        
        # verificar que todas las fichas esten en el cuadrante final
        if color_jugador == 'blanco':
            # blancos deben estar en puntos 1-6
            punto = 7
            while punto <= 24:
                fichas = self.get_fichas_en_punto(punto)
                i = 0
                while i < len(fichas):
                    if fichas[i].get_color() == color_jugador:
                        return False
                    i = i + 1
                punto = punto + 1
        else:
            # negros deben estar en puntos 19-24
            punto = 1
            while punto <= 18:
                fichas = self.get_fichas_en_punto(punto)
                i = 0
                while i < len(fichas):
                    if fichas[i].get_color() == color_jugador:
                        return False
                    i = i + 1
                punto = punto + 1
        
        return True
    
    def sacar_ficha_del_tablero(self, punto, color_jugador):
        """
        Saca una ficha del tablero (la mueve al punto 25).
        
        Recibe: Punto de origen (int) y color del jugador (string)
        Hace: Mueve la ficha al punto 25 si es válido
        Devuelve: True si sacó la ficha, False si no pudo
        """
        # verificar que puede sacar fichas
        if self.puede_sacar_fichas(color_jugador) == False:
            return False
        
        # verificar que hay fichas en el punto
        cantidad = self.contar_fichas_en_punto(punto)
        if cantidad == 0:
            return False
        
        # verificar que la ficha es del color correcto
        color_punto = self.get_color_en_punto(punto)
        if color_punto != color_jugador:
            return False
        
        # sacar la ficha y moverla al punto 25
        ficha = self.__puntos__[punto].pop()
        ficha.set_posicion(25)
        self.__puntos__[25].append(ficha)
        
        return True
    
    def contar_fichas_sacadas(self, color_jugador):
        """
        Cuenta cuántas fichas ha sacado un jugador.
        
        Recibe: Color del jugador (string)
        Hace: Cuenta las fichas del color en el punto 25
        Devuelve: Cantidad de fichas sacadas (int)
        """
        fichas_sacadas = self.get_fichas_en_punto(25)
        
        contador = 0
        i = 0
        while i < len(fichas_sacadas):
            if fichas_sacadas[i].get_color() == color_jugador:
                contador = contador + 1
            i = i + 1
        
        return contador
    
    def __str__(self):
        """
        Convierte el tablero a texto para mostrar en consola.
        
        Recibe: Nada
        Hace: Crea una representación visual del tablero
        Devuelve: String con el tablero dibujado
        """
        resultado = "\n=== TABLERO DE BACKGAMMON ===\n"
        
        # parte superior (puntos 13-24)
        resultado = resultado + "13 14 15 16 17 18   19 20 21 22 23 24\n"
        
        # dibujar 5 filas para la parte superior
        fila = 0
        while fila < 5:
            linea = ""
            punto = 13
            while punto <= 24:
                fichas = self.get_fichas_en_punto(punto)
                if fila < len(fichas):
                    linea = linea + " " + str(fichas[fila]) + " "
                else:
                    linea = linea + " . "
                
                # separador en el medio
                if punto == 18:
                    linea = linea + " | "
                
                punto = punto + 1
            
            resultado = resultado + linea + "\n"
            fila = fila + 1
        
        # mostrar la barra
        resultado = resultado + "                    BAR                   \n"
        
        # mostrar fichas en la barra si hay
        fichas_barra = self.get_fichas_en_punto(0)
        if len(fichas_barra) > 0:
            linea_barra = "BARRA: "
            i = 0
            while i < len(fichas_barra):
                linea_barra = linea_barra + str(fichas_barra[i]) + " "
                i = i + 1
            resultado = resultado + linea_barra + "\n"
        
        resultado = resultado + "                    BAR                   \n"
        
        # parte inferior (puntos 12-1)
        fila = 4
        while fila >= 0:
            linea = ""
            punto = 12
            while punto >= 1:
                fichas = self.get_fichas_en_punto(punto)
                if fila < len(fichas):
                    linea = linea + " " + str(fichas[fila]) + " "
                else:
                    linea = linea + " . "
                
                # separador en el medio
                if punto == 7:
                    linea = linea + " | "
                
                punto = punto - 1
            
            resultado = resultado + linea + "\n"
            fila = fila - 1
        
        resultado = resultado + "12 11 10  9  8  7    6  5  4  3  2  1\n"
        
        # mostrar fichas sacadas si hay
        fichas_sacadas = self.get_fichas_en_punto(25)
        if len(fichas_sacadas) > 0:
            linea_sacadas = "SACADAS: "
            i = 0
            while i < len(fichas_sacadas):
                linea_sacadas = linea_sacadas + str(fichas_sacadas[i]) + " "
                i = i + 1
            resultado = resultado + linea_sacadas + "\n"
        
        return resultado