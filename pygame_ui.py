import pygame
import sys

# importar desde core y game
from core.game import BackgammonGame


class PygameUI:
    """
    Clase que representa la interfaz grafica del juego.
    
    Recibe: Nada
    Hace: Maneja toda la visualizacion y interaccion con pygame
    Devuelve: Nada
    """
    
    def __init__(self):
        """
        Inicializa la interfaz grafica.
        
        Recibe: Nada
        Hace: Configura pygame y crea el juego
        Devuelve: Nada
        """
        # inicializar pygame
        pygame.init()
        
        # configuracion de la ventana
        self.__ancho__ = 1300
        self.__alto__ = 900
        self.__pantalla__ = pygame.display.set_mode((self.__ancho__, self.__alto__))
        pygame.display.set_caption("Backgammon")
        self.__margen_x__ = 70
        self.__margen_y__ = 110
        
        # reloj para controlar fps
        self.__reloj__ = pygame.time.Clock()
        
        # colores - paleta con tonos madera y contraste claro/oscuro
        self.__color_fondo__ = (233, 224, 207)  # beige suave de fondo
        self.__color_tablero__ = (181, 136, 99)  # madera media para tablero
        self.__color_tablero_claro__ = (205, 170, 125)  # realce interior del tablero
        self.__color_punto_claro__ = (243, 228, 202)  # triángulo claro
        self.__color_punto_oscuro__ = (143, 94, 60)  # triángulo oscuro
        self.__color_borde__ = (92, 64, 51)  # borde marrón oscuro
        self.__color_panel__ = (250, 244, 230)  # paneles laterales
        self.__color_sombra__ = (70, 55, 40)
        self.__color_blanco__ = (250, 250, 250)  # fichas blancas
        self.__color_negro__ = (15, 15, 15)  # fichas negras
        self.__color_texto__ = (60, 45, 32)  # texto marrón oscuro
        self.__color_texto_secundario__ = (90, 72, 55)
        self.__color_boton__ = (65, 105, 225)  # royal blue
        self.__color_boton_hover__ = (48, 87, 190)
        self.__color_seleccion__ = (212, 172, 13)  # dorado
        self.__color_error__ = (192, 57, 43)
        
        # fuentes
        self.__fuente_grande__ = pygame.font.SysFont('Arial', 32, bold=True)
        self.__fuente_mediana__ = pygame.font.SysFont('Arial', 24)
        self.__fuente_pequena__ = pygame.font.SysFont('Arial', 18)
        
        # el juego
        self.__juego__ = None
        
        # estado de seleccion
        self.__punto_seleccionado__ = None
        self.__dados_tirados__ = False
        
        # mensaje de error
        self.__mensaje_error__ = ""
        self.__tiempo_error__ = 0
        
        # ejecutando
        self.__ejecutando__ = True
        self.__areas_botones__ = {}

    def __geom_tablero__(self):
        """
        Devuelve la geometría actual del tablero (márgenes y dimensiones).
        """
        ancho_tablero = self.__ancho__ - 2 * self.__margen_x__
        alto_tablero = self.__alto__ - 2 * self.__margen_y__
        return self.__margen_x__, self.__margen_y__, ancho_tablero, alto_tablero
    
    def iniciar_juego(self):
        """
        Inicia un nuevo juego.
        
        Recibe: Nada
        Hace: Crea un nuevo juego y reinicia el estado
        Devuelve: Nada
        """
        # pedir nombres de jugadores
        nombre1 = self.pedir_nombre("Ingrese nombre del Jugador 1 (Blanco)")
        nombre2 = self.pedir_nombre("Ingrese nombre del Jugador 2 (Negro)")
        
        # crear el juego
        self.__juego__ = BackgammonGame(nombre1, nombre2)
        
        # reiniciar estado
        self.__punto_seleccionado__ = None
        self.__dados_tirados__ = False
        self.__mensaje_error__ = ""
        self.__tiempo_error__ = 0
    
    def pedir_nombre(self, mensaje):
        """
        Pide el nombre de un jugador.
        
        Recibe: String con el mensaje a mostrar
        Hace: Muestra un campo de texto para ingresar el nombre
        Devuelve: String con el nombre ingresado
        """
        nombre = ""
        ingresando = True
        
        while ingresando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if nombre != "":
                            ingresando = False
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre = nombre[0:len(nombre)-1]
                    else:
                        if len(nombre) < 20:
                            nombre = nombre + evento.unicode
            
            # dibujar pantalla
            self.__pantalla__.fill(self.__color_fondo__)
            
            # dibujar cuadro para el input
            ancho_cuadro = 520
            alto_cuadro = 260
            x_cuadro = self.__ancho__ // 2 - ancho_cuadro // 2
            y_cuadro = self.__alto__ // 2 - alto_cuadro // 2
            
            pygame.draw.rect(self.__pantalla__, self.__color_tablero__, 
                           (x_cuadro + 8, y_cuadro + 12, ancho_cuadro, alto_cuadro), border_radius=20)
            pygame.draw.rect(self.__pantalla__, self.__color_borde__, 
                           (x_cuadro + 8, y_cuadro + 12, ancho_cuadro, alto_cuadro), 3, border_radius=20)
            pygame.draw.rect(self.__pantalla__, self.__color_panel__, 
                           (x_cuadro, y_cuadro, ancho_cuadro, alto_cuadro), border_radius=22)
            
            # dibujar mensaje
            titulo = self.__fuente_grande__.render("Configuración de jugadores", True, self.__color_texto__)
            rect_titulo = titulo.get_rect(center=(self.__ancho__ // 2, y_cuadro + 55))
            self.__pantalla__.blit(titulo, rect_titulo)
            
            texto_mensaje = self.__fuente_mediana__.render(mensaje, True, self.__color_texto_secundario__)
            rectangulo_mensaje = texto_mensaje.get_rect(center=(self.__ancho__ // 2, y_cuadro + 110))
            self.__pantalla__.blit(texto_mensaje, rectangulo_mensaje)
            
            # dibujar campo de texto
            ancho_campo = 360
            alto_campo = 50
            x_campo = self.__ancho__ // 2 - ancho_campo // 2
            y_campo = y_cuadro + 150
            
            pygame.draw.rect(self.__pantalla__, self.__color_blanco__, 
                           (x_campo, y_campo, ancho_campo, alto_campo), border_radius=12)
            pygame.draw.rect(self.__pantalla__, self.__color_seleccion__, 
                           (x_campo, y_campo, ancho_campo, alto_campo), 3, border_radius=12)
            
            # dibujar nombre
            if nombre == "":
                texto_nombre = self.__fuente_mediana__.render("_", True, (150, 150, 150))
            else:
                texto_nombre = self.__fuente_mediana__.render(nombre + "_", True, self.__color_borde__)
            
            rectangulo_nombre = texto_nombre.get_rect()
            rectangulo_nombre.midleft = (x_campo + 16, y_campo + alto_campo // 2)
            self.__pantalla__.blit(texto_nombre, rectangulo_nombre)
            
            pygame.display.flip()
            self.__reloj__.tick(30)
        
        return nombre
    
    def dibujar_tablero(self):
        """
        Dibuja el tablero de backgammon.
        
        Recibe: Nada
        Hace: Dibuja el tablero con todos los puntos
        Devuelve: Nada
        """
        # fondo
        self.__pantalla__.fill(self.__color_fondo__)
        
        # rectangulo del tablero
        margen_x, margen_y, ancho_tablero, alto_tablero = self.__geom_tablero__()
        ancho_punto = ancho_tablero / 14.0
        alto_punto = alto_tablero / 2.0 - 40
        
        pygame.draw.rect(self.__pantalla__, self.__color_sombra__, 
                        (margen_x + 6, margen_y + 10, ancho_tablero, alto_tablero), border_radius=20)
        pygame.draw.rect(self.__pantalla__, self.__color_tablero__, 
                        (margen_x, margen_y, ancho_tablero, alto_tablero), border_radius=22)
        pygame.draw.rect(self.__pantalla__, self.__color_tablero_claro__, 
                        (margen_x + 14, margen_y + 14, ancho_tablero - 28, alto_tablero - 28), border_radius=18)
        pygame.draw.rect(self.__pantalla__, self.__color_borde__, 
                        (margen_x, margen_y, ancho_tablero, alto_tablero), 4, border_radius=22)

        # sombreado lateral para efecto 3D
        sombra_rect = pygame.Rect(margen_x - 8, margen_y + 20, 16, alto_tablero - 40)
        pygame.draw.ellipse(self.__pantalla__, self.__color_sombra__, sombra_rect)
        cuerpo_rect = pygame.Rect(margen_x - 4, margen_y + 12, 12, alto_tablero - 24)
        pygame.draw.rect(self.__pantalla__, (120, 96, 70), cuerpo_rect, border_radius=8)
        
        # puntos superiores (12 a 1)
        posicion = 0
        while posicion < 12:
            x = margen_x + posicion * ancho_punto
            if posicion >= 6:
                x += ancho_punto
            base_izq = int(x)
            base_der = int(x + ancho_punto)
            punta = int(x + ancho_punto / 2)
            alto = int(alto_punto)
            # alternar colores
            if posicion % 2 == 0:
                color = self.__color_punto_claro__
            else:
                color = self.__color_punto_oscuro__
            
            # dibujar triangulo
            punto_1 = (base_izq + 3, margen_y + 8)
            punto_2 = (base_der - 3, margen_y + 8)
            punto_3 = (punta, margen_y + alto + 2)
            pygame.draw.polygon(self.__pantalla__, color, [punto_1, punto_2, punto_3])
            pygame.draw.polygon(self.__pantalla__, self.__color_borde__, 
                              [punto_1, punto_2, punto_3], 2)
            
            # numero del punto
            numero = 12 - posicion
            texto = self.__fuente_pequena__.render(str(numero), True, self.__color_texto_secundario__)
            rect_texto = texto.get_rect()
            rect_texto.center = (punta, margen_y + alto + 20)
            self.__pantalla__.blit(texto, rect_texto)
            
            posicion = posicion + 1
        
        # puntos inferiores (13 a 24)
        posicion = 0
        while posicion < 12:
            x = margen_x + posicion * ancho_punto
            if posicion >= 6:
                x += ancho_punto
            base_izq = int(x)
            base_der = int(x + ancho_punto)
            punta = int(x + ancho_punto / 2)
            alto = int(alto_punto)
            # alternar colores
            if posicion % 2 == 0:
                color = self.__color_punto_oscuro__
            else:
                color = self.__color_punto_claro__
            
            # dibujar triangulo
            punto_1 = (base_izq + 3, int(margen_y + alto_tablero) - 8)
            punto_2 = (base_der - 3, int(margen_y + alto_tablero) - 8)
            punto_3 = (punta, int(margen_y + alto_tablero - alto) - 2)
            pygame.draw.polygon(self.__pantalla__, color, [punto_1, punto_2, punto_3])
            pygame.draw.polygon(self.__pantalla__, self.__color_borde__, 
                              [punto_1, punto_2, punto_3], 2)
            
            # numero del punto
            numero = 13 + posicion
            texto = self.__fuente_pequena__.render(str(numero), True, self.__color_texto_secundario__)
            rect_texto = texto.get_rect()
            rect_texto.center = (punta, margen_y + alto_tablero - alto - 20)
            self.__pantalla__.blit(texto, rect_texto)
            
            posicion = posicion + 1
        
        # barra central
        x_barra = margen_x + 6 * ancho_punto
        pygame.draw.rect(self.__pantalla__, self.__color_borde__, 
                        (x_barra, margen_y, ancho_punto, alto_tablero))
        pygame.draw.rect(self.__pantalla__, (120, 90, 65), 
                        (x_barra + 6, margen_y + 6, ancho_punto - 12, alto_tablero - 12), border_radius=6)
        
        # zona de salida para fichas (bear off)
        x_salida = margen_x + 13 * ancho_punto
        ancho_salida = ancho_punto
        pygame.draw.rect(self.__pantalla__, self.__color_borde__,
                         (x_salida, margen_y, ancho_salida, alto_tablero), border_radius=10)
        pygame.draw.rect(self.__pantalla__, (214, 198, 171),
                         (x_salida + 4, margen_y + 8, ancho_salida - 8, alto_tablero - 16), border_radius=12)
        # linea divisoria para separar zona superior e inferior
        pygame.draw.line(self.__pantalla__, (196, 172, 140),
                         (x_salida + 6, margen_y + alto_tablero // 2),
                         (x_salida + ancho_salida - 6, margen_y + alto_tablero // 2), 3)
    
    def dibujar_fichas(self):
        """
        Dibuja todas las fichas en el tablero.
        
        Recibe: Nada
        Hace: Dibuja cada ficha en su posicion correspondiente
        Devuelve: Nada
        """
        if self.__juego__ == None:
            return
        
        margen_x, margen_y, ancho_tablero, alto_tablero = self.__geom_tablero__()
        ancho_punto = ancho_tablero / 14.0
        radio = int(ancho_punto * 0.42)
        altura_punto = alto_tablero / 2.0 - 40

        def centro_x(punto_tablero):
            if punto_tablero <= 12:
                posicion = 12 - punto_tablero
            else:
                posicion = punto_tablero - 13
            x_base = margen_x + posicion * ancho_punto
            if posicion >= 6:
                x_base += ancho_punto
            return x_base + ancho_punto / 2.0
        
        tablero = self.__juego__.get_tablero()
        
        # dibujar fichas en cada punto (1 a 24)
        punto = 1
        while punto <= 24:
            fichas = tablero.get_fichas_en_punto(punto)
            
            if len(fichas) > 0:
                # determinar posicion x del punto
                if punto <= 12:
                    x = centro_x(punto)
                    altura_disponible = max(altura_punto - 52, radio)
                    paso = 0 if len(fichas) <= 1 else min(radio * 2 + 6, altura_disponible / (len(fichas) - 1))
                    base_y = margen_y + 26 + radio
                    sentido = 1
                else:
                    x = centro_x(punto)
                    altura_disponible = max(altura_punto - 52, radio)
                    paso = 0 if len(fichas) <= 1 else min(radio * 2 + 6, altura_disponible / (len(fichas) - 1))
                    base_y = margen_y + alto_tablero - 26 - radio
                    sentido = -1
                
                # dibujar cada ficha
                indice = 0
                while indice < len(fichas):
                    ficha = fichas[indice]
                    
                    # determinar color
                    if ficha.get_color() == 'blanco':
                        color = self.__color_blanco__
                    else:
                        color = self.__color_negro__
                    
                    y = int(round(base_y + sentido * paso * indice))
                    x_int = int(round(x))
                    
                    # dibujar ficha con pequeña sombra
                    pygame.draw.circle(self.__pantalla__, self.__color_sombra__, (x_int + 2, y + 3), radio)
                    pygame.draw.circle(self.__pantalla__, color, (x_int, y), radio)
                    pygame.draw.circle(self.__pantalla__, self.__color_borde__, (x_int, y), radio, 3)
                    
                    # si hay muchas fichas, mostrar numero
                    if len(fichas) > 7 and indice == 6:
                        texto = self.__fuente_pequena__.render(str(len(fichas) - 6), True, 
                                                               self.__color_negro__ if color == self.__color_blanco__ else self.__color_blanco__)
                        rect_texto = texto.get_rect()
                        rect_texto.center = (x_int, y)
                        self.__pantalla__.blit(texto, rect_texto)
                        break
                    
                    indice = indice + 1
            
            punto = punto + 1
        
        # dibujar fichas en la barra (punto 0)
        fichas_barra = tablero.get_fichas_en_punto(0)
        if len(fichas_barra) > 0:
            x_barra = margen_x + 6 * ancho_punto + ancho_punto / 2.0
            
            # separar por color
            fichas_blancas = []
            fichas_negras = []
            i = 0
            while i < len(fichas_barra):
                if fichas_barra[i].get_color() == 'blanco':
                    fichas_blancas.append(fichas_barra[i])
                else:
                    fichas_negras.append(fichas_barra[i])
                i = i + 1
            
            def dibujar_stack_barra(fichas_color, arriba=True):
                if not fichas_color:
                    return
                altura_disponible = alto_tablero - 80
                paso = 0 if len(fichas_color) <= 1 else min(radio * 2 + 8, altura_disponible / (len(fichas_color) - 1))
                if arriba:
                    base_y = margen_y + 55 + radio
                    sentido = 1
                    color_ficha = self.__color_blanco__
                    color_texto = self.__color_negro__
                else:
                    base_y = margen_y + alto_tablero - 55 - radio
                    sentido = -1
                    color_ficha = self.__color_negro__
                    color_texto = self.__color_blanco__
                for idx in range(len(fichas_color)):
                    y = int(round(base_y + sentido * paso * idx))
                    x_centro = int(round(x_barra))
                    pygame.draw.circle(self.__pantalla__, self.__color_sombra__, (x_centro + 2, y + 3), radio)
                    pygame.draw.circle(self.__pantalla__, color_ficha, (x_centro, y), radio)
                    pygame.draw.circle(self.__pantalla__, self.__color_borde__, (x_centro, y), radio, 3)
                    if len(fichas_color) > 7 and idx == 6:
                        texto = self.__fuente_pequena__.render(str(len(fichas_color) - 6), True, color_texto)
                        rect_texto = texto.get_rect()
                        rect_texto.center = (x_centro, y)
                        self.__pantalla__.blit(texto, rect_texto)
                        break
            
            dibujar_stack_barra(fichas_blancas, arriba=True)
            dibujar_stack_barra(fichas_negras, arriba=False)
        
        # dibujar fichas sacadas (a la derecha del tablero)
        fichas_fuera = tablero.get_fichas_en_punto(25)
        if len(fichas_fuera) > 0:
            fichas_fuera_blancas = []
            fichas_fuera_negras = []
            indice_fuera = 0
            while indice_fuera < len(fichas_fuera):
                ficha = fichas_fuera[indice_fuera]
                if ficha.get_color() == 'blanco':
                    fichas_fuera_blancas.append(ficha)
                else:
                    fichas_fuera_negras.append(ficha)
                indice_fuera = indice_fuera + 1
            
            x_salida = margen_x + 13 * ancho_punto + ancho_punto / 2.0
            altura_salida = alto_tablero / 2 - 60
            paso_base = radio * 2 + 10
            
            if len(fichas_fuera_negras) > 0:
                paso = 0 if len(fichas_fuera_negras) <= 1 else min(paso_base, altura_salida / (len(fichas_fuera_negras) - 1))
                base_y = margen_y + 36 + radio
                idx = 0
                while idx < len(fichas_fuera_negras):
                    y = int(round(base_y + paso * idx))
                    x_centro = int(round(x_salida))
                    pygame.draw.circle(self.__pantalla__, self.__color_sombra__, (x_centro + 2, y + 3), radio)
                    pygame.draw.circle(self.__pantalla__, self.__color_negro__, (x_centro, y), radio)
                    pygame.draw.circle(self.__pantalla__, self.__color_borde__, (x_centro, y), radio, 3)
                    if len(fichas_fuera_negras) > 6 and idx == 5:
                        texto = self.__fuente_pequena__.render(str(len(fichas_fuera_negras) - 5), True, self.__color_blanco__)
                        rect_texto = texto.get_rect(center=(x_centro, y))
                        self.__pantalla__.blit(texto, rect_texto)
                        break
                    idx = idx + 1
            
            if len(fichas_fuera_blancas) > 0:
                paso = 0 if len(fichas_fuera_blancas) <= 1 else min(paso_base, altura_salida / (len(fichas_fuera_blancas) - 1))
                base_y = margen_y + alto_tablero - 36 - radio
                idx = 0
                while idx < len(fichas_fuera_blancas):
                    y = int(round(base_y - paso * idx))
                    x_centro = int(round(x_salida))
                    pygame.draw.circle(self.__pantalla__, self.__color_sombra__, (x_centro + 2, y + 3), radio)
                    pygame.draw.circle(self.__pantalla__, self.__color_blanco__, (x_centro, y), radio)
                    pygame.draw.circle(self.__pantalla__, self.__color_borde__, (x_centro, y), radio, 3)
                    if len(fichas_fuera_blancas) > 6 and idx == 5:
                        texto = self.__fuente_pequena__.render(str(len(fichas_fuera_blancas) - 5), True, self.__color_negro__)
                        rect_texto = texto.get_rect(center=(x_centro, y))
                        self.__pantalla__.blit(texto, rect_texto)
                        break
                    idx = idx + 1
        
        jugador1 = self.__juego__.get_jugador1()
        jugador2 = self.__juego__.get_jugador2()
        
        x_sacadas = self.__ancho__ - 40
        
        # fichas blancas sacadas (arriba)
        fichas_sacadas_blanco = jugador1.get_fichas_sacadas()
        if fichas_sacadas_blanco > 0:
            texto = self.__fuente_mediana__.render(f"Sacadas: {fichas_sacadas_blanco}", True, self.__color_texto__)
            rect_texto = texto.get_rect()
            rect_texto.midright = (x_sacadas, 50)
            self.__pantalla__.blit(texto, rect_texto)
        
        # fichas negras sacadas (abajo)
        fichas_sacadas_negro = jugador2.get_fichas_sacadas()
        if fichas_sacadas_negro > 0:
            texto = self.__fuente_mediana__.render(f"Sacadas: {fichas_sacadas_negro}", True, self.__color_texto__)
            rect_texto = texto.get_rect()
            rect_texto.midright = (x_sacadas, self.__alto__ - 50)
            self.__pantalla__.blit(texto, rect_texto)
    
    def dibujar_seleccion(self):
        """
        Dibuja el indicador de punto seleccionado.
        
        Recibe: Nada
        Hace: Resalta el punto que esta seleccionado
        Devuelve: Nada
        """
        if self.__punto_seleccionado__ == None:
            return
        
        punto = self.__punto_seleccionado__
        
        # si es barra
        margen_x, margen_y, ancho_tablero, alto_tablero = self.__geom_tablero__()
        ancho_punto = int(ancho_tablero / 14)
        alto_punto = int(alto_tablero / 2 - 40)

        if punto == 0:
            x_barra = margen_x + 6 * ancho_punto
            pygame.draw.rect(self.__pantalla__, self.__color_seleccion__, 
                           (x_barra, margen_y, ancho_punto, alto_tablero), 5)
            return
        
        # punto normal
        if punto <= 12:
            posicion = 12 - punto
            base = margen_x + posicion * ancho_punto
            if posicion >= 6:
                base += ancho_punto
            base_izq = int(base)
            base_der = int(base + ancho_punto)
            punta = int(base + ancho_punto / 2)
            pygame.draw.polygon(self.__pantalla__, self.__color_seleccion__,
                              [(base_izq, margen_y), (base_der, margen_y), (punta, margen_y + alto_punto)], 5)
        else:
            posicion = punto - 13
            base = margen_x + posicion * ancho_punto
            if posicion >= 6:
                base += ancho_punto
            base_izq = int(base)
            base_der = int(base + ancho_punto)
            punta = int(base + ancho_punto / 2)
            pygame.draw.polygon(self.__pantalla__, self.__color_seleccion__,
                              [(base_izq, margen_y + alto_tablero),
                               (base_der, margen_y + alto_tablero),
                               (punta, margen_y + alto_tablero - alto_punto)], 5)
    
    def dibujar_info(self):
        """
        Dibuja la informacion del juego.
        
        Recibe: Nada
        Hace: Muestra turno, dados, jugadores
        Devuelve: Nada
        """
        if self.__juego__ == None:
            return
        
        # turno actual
        jugador_actual = self.__juego__.get_jugador_actual()
        color_actual = self.__juego__.get_color_jugador_actual()
        
        texto_turno = f"Turno: {jugador_actual.get_nombre()} ({color_actual})"
        margen_x, _, ancho_tablero, _ = self.__geom_tablero__()
        ancho_info = max(int(ancho_tablero * 0.55), 360)
        panel_rect = pygame.Rect(margen_x, 26, ancho_info, 64)
        pygame.draw.rect(self.__pantalla__, self.__color_panel__, panel_rect, border_radius=18)
        pygame.draw.rect(self.__pantalla__, self.__color_borde__, panel_rect, 2, border_radius=18)
        decor = pygame.Rect(panel_rect.x + 12, panel_rect.y + 12, panel_rect.width - 24, 40)
        pygame.draw.rect(self.__pantalla__, (244, 236, 221), decor, border_radius=12)
        pygame.draw.rect(self.__pantalla__, (210, 190, 160), decor, 1, border_radius=12)
        
        texto = self.__fuente_mediana__.render(texto_turno, True, self.__color_texto__)
        self.__pantalla__.blit(texto, (decor.x + 14, decor.y + 6))

        dados = self.__juego__.get_movimientos_disponibles()
        if dados:
            texto_dados = "Dados: " + ", ".join(str(d) for d in dados)
            texto = self.__fuente_pequena__.render(texto_dados, True, self.__color_texto_secundario__)
            
            # calcular espacio disponible entre la info del turno y el panel de acciones
            ancho_botones = max(int(ancho_tablero - 360), 320)
            inicio_botones = margen_x + ancho_botones + 30
            separacion = 16
            espacio_disponible = inicio_botones - (panel_rect.right + separacion)

            if espacio_disponible >= 120:
                ancho_panel_dados = min(max(texto.get_width() + 32, 140), espacio_disponible)
                dados_rect = pygame.Rect(panel_rect.right + separacion,
                                         panel_rect.y,
                                         ancho_panel_dados,
                                         panel_rect.height)
                pygame.draw.rect(self.__pantalla__, self.__color_panel__, dados_rect, border_radius=18)
                pygame.draw.rect(self.__pantalla__, self.__color_borde__, dados_rect, 2, border_radius=18)

                decor_dados = pygame.Rect(dados_rect.x + 12, dados_rect.y + 12,
                                          dados_rect.width - 24, dados_rect.height - 24)
                pygame.draw.rect(self.__pantalla__, (244, 236, 221), decor_dados, border_radius=12)
                pygame.draw.rect(self.__pantalla__, (210, 190, 160), decor_dados, 1, border_radius=12)

                rect_dados = texto.get_rect(center=decor_dados.center)
                self.__pantalla__.blit(texto, rect_dados)
            else:
                rect_dados = texto.get_rect()
                rect_dados.centery = decor.centery
                rect_dados.right = decor.right - 12
                self.__pantalla__.blit(texto, rect_dados)
        
        # fichas en barra
        jugador1 = self.__juego__.get_jugador1()
        jugador2 = self.__juego__.get_jugador2()
        
        if jugador1.get_fichas_en_barra() > 0:
            texto = self.__fuente_pequena__.render(
                f"{jugador1.get_nombre()} - fichas en barra: {jugador1.get_fichas_en_barra()}", 
                True, self.__color_texto_secundario__)
            self.__pantalla__.blit(texto, (panel_rect.x + 320, panel_rect.y + 12))
        
        if jugador2.get_fichas_en_barra() > 0:
            texto = self.__fuente_pequena__.render(
                f"{jugador2.get_nombre()} - fichas en barra: {jugador2.get_fichas_en_barra()}", 
                True, self.__color_texto_secundario__)
            self.__pantalla__.blit(texto, (panel_rect.x + 320, panel_rect.y + 40))
    
    def dibujar_botones(self):
        """
        Dibuja los botones de accion.
        
        Recibe: Nada
        Hace: Dibuja botones de tirar dados, pasar turno, nuevo juego
        Devuelve: Nada
        """
        margen_x, _, ancho_tablero, _ = self.__geom_tablero__()
        ancho_info = max(int(ancho_tablero - 360), 320)
        panel_rect = pygame.Rect(margen_x + ancho_info + 30, 26, ancho_tablero - ancho_info - 40, 64)
        pygame.draw.rect(self.__pantalla__, self.__color_panel__, panel_rect, border_radius=18)
        pygame.draw.rect(self.__pantalla__, self.__color_borde__, panel_rect, 2, border_radius=18)
        titulo = self.__fuente_pequena__.render("Acciones", True, self.__color_texto_secundario__)
        self.__pantalla__.blit(titulo, (panel_rect.centerx - titulo.get_width() // 2, panel_rect.y + 8))

        botones = []
        # Tirar dados
        botones.append({
            "id": "tirar",
            "texto": "Tirar Dados",
            "activo": not self.__dados_tirados__
        })
        # Pasar turno
        botones.append({
            "id": "pasar",
            "texto": "Pasar Turno",
            "activo": self.__dados_tirados__
        })
        # Nuevo juego
        botones.append({
            "id": "nuevo",
            "texto": "Nuevo Juego",
            "activo": True
        })

        ancho_boton = 110
        alto_boton = 40
        espacio = 18
        total_ancho = len(botones) * ancho_boton + (len(botones) - 1) * espacio
        inicio_x = panel_rect.x + (panel_rect.width - total_ancho) // 2
        centro_y = panel_rect.y + panel_rect.height // 2 + 2

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.__areas_botones__ = {}

        for idx, boton in enumerate(botones):
            rect = pygame.Rect(inicio_x + idx * (ancho_boton + espacio),
                               centro_y - alto_boton // 2,
                               ancho_boton, alto_boton)
            self.__areas_botones__[boton["id"]] = rect

            if not boton["activo"]:
                color_relleno = (189, 195, 199)
                color_texto = (120, 120, 120)
            else:
                if rect.collidepoint(mouse_x, mouse_y):
                    color_relleno = self.__color_boton_hover__
                else:
                    color_relleno = self.__color_boton__
                color_texto = self.__color_blanco__

            pygame.draw.rect(self.__pantalla__, color_relleno, rect, border_radius=12)
            pygame.draw.rect(self.__pantalla__, self.__color_borde__, rect, 2, border_radius=12)

            texto = self.__fuente_pequena__.render(boton["texto"], True, color_texto)
            rect_texto = texto.get_rect(center=rect.center)
            self.__pantalla__.blit(texto, rect_texto)
    
    def dibujar_mensaje_error(self):
        """
        Dibuja el mensaje de error si hay alguno.
        
        Recibe: Nada
        Hace: Muestra mensaje de error temporalmente
        Devuelve: Nada
        """
        if self.__mensaje_error__ != "":
            # verificar si paso el tiempo
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.__tiempo_error__ < 3000:
                # dibujar recuadro
                ancho_recuadro = 520
                alto_recuadro = 60
                margen_x, margen_y, _, alto_tablero = self.__geom_tablero__()
                panel_top = margen_y + alto_tablero + 20
                x_recuadro = self.__ancho__ // 2 - ancho_recuadro // 2
                y_recuadro = max(panel_top - 80, margen_y + alto_tablero // 2)
                
                pygame.draw.rect(self.__pantalla__, self.__color_error__, 
                               (x_recuadro, y_recuadro, ancho_recuadro, alto_recuadro), border_radius=8)
                pygame.draw.rect(self.__pantalla__, self.__color_borde__, 
                               (x_recuadro, y_recuadro, ancho_recuadro, alto_recuadro), 3, border_radius=8)
                
                # dibujar texto
                texto = self.__fuente_pequena__.render(self.__mensaje_error__, True, self.__color_blanco__)
                rect_texto = texto.get_rect()
                rect_texto.center = (self.__ancho__ // 2, y_recuadro + alto_recuadro // 2)
                self.__pantalla__.blit(texto, rect_texto)
            else:
                self.__mensaje_error__ = ""
    
    def dibujar_ganador(self):
        """
        Dibuja el mensaje de ganador.
        
        Recibe: Nada
        Hace: Muestra quien gano el juego
        Devuelve: Nada
        """
        if not self.__juego__.esta_terminado():
            return
        
        # dibujar recuadro
        ancho_recuadro = 450
        alto_recuadro = 180
        x_recuadro = self.__ancho__ // 2 - ancho_recuadro // 2
        y_recuadro = self.__alto__ // 2 - alto_recuadro // 2
        
        pygame.draw.rect(self.__pantalla__, self.__color_sombra__, 
                       (x_recuadro + 6, y_recuadro + 8, ancho_recuadro, alto_recuadro), border_radius=18)
        pygame.draw.rect(self.__pantalla__, self.__color_panel__, 
                       (x_recuadro, y_recuadro, ancho_recuadro, alto_recuadro), border_radius=18)
        pygame.draw.rect(self.__pantalla__, self.__color_seleccion__, 
                       (x_recuadro, y_recuadro, ancho_recuadro, alto_recuadro), 4, border_radius=18)
        
        # texto ganador
        texto1 = self.__fuente_grande__.render("JUEGO TERMINADO", True, self.__color_texto__)
        rect_texto1 = texto1.get_rect()
        rect_texto1.center = (self.__ancho__ // 2, y_recuadro + 50)
        self.__pantalla__.blit(texto1, rect_texto1)
        
        ganador = self.__juego__.get_ganador()
        nombre_ganador = ganador.get_nombre()
        
        texto2 = self.__fuente_mediana__.render(f"Ganador: {nombre_ganador}", True, self.__color_texto__)
        rect_texto2 = texto2.get_rect()
        rect_texto2.center = (self.__ancho__ // 2, y_recuadro + 110)
        self.__pantalla__.blit(texto2, rect_texto2)
    
    def obtener_punto_click(self, x, y):
        """
        Obtiene el numero de punto clickeado.
        
        Recibe: Integer x, Integer y (coordenadas del click)
        Hace: Calcula que punto fue clickeado
        Devuelve: Integer con el numero de punto o None
        """
        margen_x, margen_y, ancho_tablero, alto_tablero = self.__geom_tablero__()
        ancho_punto = int(ancho_tablero / 14)
        
        # verificar si click esta en tablero
        if x < margen_x or x > margen_x + ancho_tablero:
            return None
        if y < margen_y or y > margen_y + alto_tablero:
            return None
        
        # calcular columna
        x_relativo = x - margen_x
        
        # verificar si es la barra
        if 6 * ancho_punto <= x_relativo <= 7 * ancho_punto:
            return 0
        
        # verificar si es la zona de salida (bear off) en la ultima columna
        if x_relativo >= 13 * ancho_punto:
            if self.__juego__ != None:
                mitad = margen_y + alto_tablero // 2
                color_actual = self.__juego__.get_color_jugador_actual()
                if color_actual == 'blanco' and y >= mitad:
                    return 25
                if color_actual == 'negro' and y <= mitad:
                    return 25
            return None
        
        # calcular columna sin la barra
        if x_relativo > 7 * ancho_punto:
            x_relativo = x_relativo - ancho_punto
        
        columna = x_relativo // ancho_punto
        
        # verificar si es parte superior o inferior
        mitad = margen_y + alto_tablero // 2
        
        if y < mitad:
            # parte superior (puntos 12 a 1)
            punto = 12 - columna
        else:
            # parte inferior (puntos 13 a 24)
            punto = 13 + columna
        
        return punto
    
    def calcular_valor_dado_necesario(self, origen, destino):
        """
        Calcula que valor de dado se necesita para mover de origen a destino.
        
        Recibe: Integer origen, Integer destino
        Hace: Calcula la diferencia segun el color del jugador
        Devuelve: Integer con el valor del dado o None si no es posible
        """
        color = self.__juego__.get_color_jugador_actual()
        
        dados_disponibles = self.__juego__.get_movimientos_disponibles()
        
        # probar cada dado disponible y ver si alcanza el destino deseado
        i = 0
        while i < len(dados_disponibles):
            valor_dado = dados_disponibles[i]
            
            if origen == 0:
                # reingreso desde la barra
                if color == 'blanco':
                    destino_calculado = 25 - valor_dado
                else:
                    destino_calculado = valor_dado
            else:
                if color == 'blanco':
                    destino_calculado = origen - valor_dado
                else:
                    destino_calculado = origen + valor_dado
            
            if destino == 25:
                # intento sacar ficha
                if color == 'blanco' and destino_calculado < 1:
                    if self.__juego__.puede_hacer_movimiento(origen, valor_dado):
                        return valor_dado
                elif color == 'negro' and destino_calculado > 24:
                    if self.__juego__.puede_hacer_movimiento(origen, valor_dado):
                        return valor_dado
            else:
                if destino_calculado == destino and self.__juego__.puede_hacer_movimiento(origen, valor_dado):
                    return valor_dado
            
            i = i + 1
        
        return None
    
    def manejar_click_tablero(self, x, y):
        """
        Maneja el click en el tablero.
        
        Recibe: Integer x, Integer y (coordenadas del click)
        Hace: Procesa la seleccion de origen y destino
        Devuelve: Nada
        """
        if not self.__dados_tirados__:
            return
        
        if self.__juego__.esta_terminado():
            return
        
        punto = self.obtener_punto_click(x, y)
        
        if punto == None:
            return
        
        # la zona de salida no puede ser un origen
        if punto == 25 and self.__punto_seleccionado__ == None:
            return
        
        # si no hay punto seleccionado, seleccionar origen
        if self.__punto_seleccionado__ == None:
            # verificar que tenga fichas del jugador actual
            if punto == 0:
                # barra
                color_actual = self.__juego__.get_color_jugador_actual()
                tablero = self.__juego__.get_tablero()
                if tablero.jugador_tiene_fichas_en_barra(color_actual):
                    self.__punto_seleccionado__ = punto
            else:
                # punto normal
                tablero = self.__juego__.get_tablero()
                fichas = tablero.get_fichas_en_punto(punto)
                
                if len(fichas) > 0:
                    color_esperado = self.__juego__.get_color_jugador_actual()
                    if fichas[0].get_color() == color_esperado:
                        self.__punto_seleccionado__ = punto
        else:
            # ya hay origen seleccionado, este es el destino
            origen = self.__punto_seleccionado__
            destino = punto
            color_actual = self.__juego__.get_color_jugador_actual()

            # si sale desde la barra, permitir clicks en numeración local (1-6 / 24-19)
            if origen == 0:
                if color_actual == 'blanco':
                    if 1 <= destino <= 6:
                        destino = 25 - destino
                else:
                    if 19 <= destino <= 24:
                        destino = destino - 18

            jugador_antes = self.__juego__.get_jugador_actual()
            
            # calcular valor de dado necesario
            valor_dado = self.calcular_valor_dado_necesario(origen, destino)
            
            if valor_dado == None:
                self.__mensaje_error__ = "Dado no disponible para ese movimiento"
                self.__tiempo_error__ = pygame.time.get_ticks()
                self.__punto_seleccionado__ = None
                return
            
            # intentar hacer el movimiento
            movimiento_exitoso = self.__juego__.hacer_movimiento(origen, valor_dado)
            
            if movimiento_exitoso:
                self.__punto_seleccionado__ = None
                # si se agotaron los dados (o cambió el turno), habilitar nuevo tiro
                if len(self.__juego__.get_movimientos_disponibles()) == 0 or \
                        self.__juego__.get_jugador_actual() != jugador_antes:
                    self.__dados_tirados__ = False
                elif self.__juego__.puede_hacer_algun_movimiento() == False:
                    self.__mensaje_error__ = "Sin movimientos válidos. El turno pasa automáticamente."
                    self.__tiempo_error__ = pygame.time.get_ticks()
                    self.__juego__.pasar_turno_si_no_hay_movimientos()
                    self.__dados_tirados__ = False
                    self.__punto_seleccionado__ = None
            else:
                self.__mensaje_error__ = "Movimiento no valido"
                self.__tiempo_error__ = pygame.time.get_ticks()
                self.__punto_seleccionado__ = None
    
    def manejar_click_boton(self, x, y):
        """
        Maneja el click en los botones.
        
        Recibe: Integer x, Integer y (coordenadas del click)
        Hace: Ejecuta la accion del boton clickeado
        Devuelve: Nada
        """
        rects = self.__areas_botones__
        if not rects:
            return
        if "tirar" in rects and rects["tirar"].collidepoint(x, y) and not self.__dados_tirados__:
            self.__juego__.tirar_dados()
            self.__dados_tirados__ = True
            self.__punto_seleccionado__ = None
            if self.__juego__.puede_hacer_algun_movimiento() == False:
                self.__mensaje_error__ = "Sin movimientos válidos. El turno pasa automáticamente."
                self.__tiempo_error__ = pygame.time.get_ticks()
                self.__juego__.pasar_turno_si_no_hay_movimientos()
                self.__dados_tirados__ = False
                self.__punto_seleccionado__ = None
            return
        if "pasar" in rects and rects["pasar"].collidepoint(x, y) and self.__dados_tirados__:
            self.__juego__.terminar_turno()
            self.__dados_tirados__ = False
            self.__punto_seleccionado__ = None
            return
        if "nuevo" in rects and rects["nuevo"].collidepoint(x, y):
            self.iniciar_juego()
            return
    
    def ejecutar(self):
        """
        Ejecuta el loop principal del juego.
        
        Recibe: Nada
        Hace: Maneja eventos y dibuja la pantalla
        Devuelve: Nada
        """
        # iniciar primer juego
        self.iniciar_juego()
        
        # loop principal
        while self.__ejecutando__:
            # manejar eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.__ejecutando__ = False
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        x, y = evento.pos
                        self.manejar_click_tablero(x, y)
                        self.manejar_click_boton(x, y)
            
            # dibujar todo
            self.dibujar_tablero()
            self.dibujar_fichas()
            self.dibujar_seleccion()
            self.dibujar_info()
            self.dibujar_botones()
            self.dibujar_mensaje_error()
            self.dibujar_ganador()
            
            # actualizar pantalla
            pygame.display.flip()
            self.__reloj__.tick(30)
        
        # cerrar pygame
        pygame.quit()
        sys.exit()


# punto de entrada
if __name__ == "__main__":
    interfaz = PygameUI()
    interfaz.ejecutar()
