import unittest
from core.board import Board
from core.checker import Checker


class TestBoard(unittest.TestCase):
    """
    Clase de pruebas para la clase Board.
    
    Recibe: Nada
    Hace: Prueba todos los métodos del tablero de Backgammon
    Devuelve: Nada
    """
    
    def setUp(self):
        """
        Prepara el ambiente antes de cada prueba.
        
        Recibe: Nada
        Hace: Crea un tablero nuevo para cada test
        Devuelve: Nada
        """
        self.__board__ = Board()
    
    def test_board_se_inicializa_correctamente(self):
        """
        Prueba que el tablero se inicializa con las fichas correctas.
        
        Recibe: Nada
        Hace: Verifica posiciones iniciales de todas las fichas
        Devuelve: Nada
        """
        # verificar fichas blancas
        cantidad_24 = self.__board__.contar_fichas_en_punto(24)
        self.assertEqual(cantidad_24, 2)
        
        cantidad_13 = self.__board__.contar_fichas_en_punto(13)
        self.assertEqual(cantidad_13, 5)
        
        cantidad_8 = self.__board__.contar_fichas_en_punto(8)
        self.assertEqual(cantidad_8, 3)
        
        cantidad_6 = self.__board__.contar_fichas_en_punto(6)
        self.assertEqual(cantidad_6, 5)
        
        # verificar fichas negras
        cantidad_1 = self.__board__.contar_fichas_en_punto(1)
        self.assertEqual(cantidad_1, 2)
        
        cantidad_12 = self.__board__.contar_fichas_en_punto(12)
        self.assertEqual(cantidad_12, 5)
        
        cantidad_17 = self.__board__.contar_fichas_en_punto(17)
        self.assertEqual(cantidad_17, 3)
        
        cantidad_19 = self.__board__.contar_fichas_en_punto(19)
        self.assertEqual(cantidad_19, 5)
        
        # verificar colores
        color_24 = self.__board__.get_color_en_punto(24)
        self.assertEqual(color_24, "blanco")
        
        color_1 = self.__board__.get_color_en_punto(1)
        self.assertEqual(color_1, "negro")
    
    def test_puntos_vacios_inicialmente(self):
        """
        Prueba que los puntos correctos están vacíos al inicio.
        
        Recibe: Nada
        Hace: Verifica puntos que deben estar vacíos
        Devuelve: Nada
        """
        # verificar punto 2
        vacio_2 = self.__board__.punto_esta_vacio(2)
        self.assertEqual(vacio_2, True)
        color_2 = self.__board__.get_color_en_punto(2)
        self.assertEqual(color_2, None)
        
        # verificar punto 3
        vacio_3 = self.__board__.punto_esta_vacio(3)
        self.assertEqual(vacio_3, True)
        color_3 = self.__board__.get_color_en_punto(3)
        self.assertEqual(color_3, None)
        
        # verificar punto 4
        vacio_4 = self.__board__.punto_esta_vacio(4)
        self.assertEqual(vacio_4, True)
        
        # verificar punto 5
        vacio_5 = self.__board__.punto_esta_vacio(5)
        self.assertEqual(vacio_5, True)
        
        # verificar punto 7
        vacio_7 = self.__board__.punto_esta_vacio(7)
        self.assertEqual(vacio_7, True)
        
        # verificar punto 9
        vacio_9 = self.__board__.punto_esta_vacio(9)
        self.assertEqual(vacio_9, True)
        
        # verificar punto 10
        vacio_10 = self.__board__.punto_esta_vacio(10)
        self.assertEqual(vacio_10, True)
        
        # verificar punto 11
        vacio_11 = self.__board__.punto_esta_vacio(11)
        self.assertEqual(vacio_11, True)
    
    def test_barra_y_sacado_vacios_inicialmente(self):
        """
        Prueba que barra y zona de sacado empiezan vacías.
        
        Recibe: Nada
        Hace: Verifica puntos 0 y 25 vacíos
        Devuelve: Nada
        """
        vacio_0 = self.__board__.punto_esta_vacio(0)
        self.assertEqual(vacio_0, True)
        
        vacio_25 = self.__board__.punto_esta_vacio(25)
        self.assertEqual(vacio_25, True)
    
    def test_get_fichas_en_punto_fuera_de_rango(self):
        """
        Prueba get_fichas_en_punto con valores fuera de rango.
        
        Recibe: Nada
        Hace: Verifica que devuelve lista vacía para puntos inválidos
        Devuelve: Nada
        """
        fichas_negativo = self.__board__.get_fichas_en_punto(-1)
        self.assertEqual(len(fichas_negativo), 0)
        
        fichas_mayor = self.__board__.get_fichas_en_punto(26)
        self.assertEqual(len(fichas_mayor), 0)
    
    def test_get_color_en_punto_vacio(self):
        """
        Prueba get_color_en_punto cuando no hay fichas.
        
        Recibe: Nada
        Hace: Verifica que devuelve None para punto vacío
        Devuelve: Nada
        """
        color = self.__board__.get_color_en_punto(2)
        self.assertEqual(color, None)
    
    def test_puede_mover_a_punto_casos(self):
        """
        Prueba todos los casos de puede_mover_a_punto.
        
        Recibe: Nada
        Hace: Verifica fuera de rango, vacío, propio, enemigo
        Devuelve: Nada
        """
        # fuera de rango
        puede_0 = self.__board__.puede_mover_a_punto(0, "blanco")
        self.assertEqual(puede_0, False)
        
        puede_25 = self.__board__.puede_mover_a_punto(25, "blanco")
        self.assertEqual(puede_25, False)
        
        # punto vacio
        puede_2 = self.__board__.puede_mover_a_punto(2, "blanco")
        self.assertEqual(puede_2, True)
        
        # punto propio
        puede_24 = self.__board__.puede_mover_a_punto(24, "blanco")
        self.assertEqual(puede_24, True)
        
        # preparar una ficha sola enemiga
        movio = self.__board__.mover_ficha(24, 23, "blanco")
        self.assertEqual(movio, True)
        
        # enemigo con 1 ficha - se puede capturar
        puede_23 = self.__board__.puede_mover_a_punto(23, "negro")
        self.assertEqual(puede_23, True)
        
        # enemigo con muchas fichas - bloqueado
        puede_12 = self.__board__.puede_mover_a_punto(12, "blanco")
        self.assertEqual(puede_12, False)
    
    def test_mover_ficha_a_punto_vacio(self):
        """
        Prueba mover ficha a un punto vacío.
        
        Recibe: Nada
        Hace: Verifica movimiento simple a punto vacío
        Devuelve: Nada
        """
        resultado = self.__board__.mover_ficha(24, 23, "blanco")
        self.assertEqual(resultado, True)
        
        cantidad_24 = self.__board__.contar_fichas_en_punto(24)
        self.assertEqual(cantidad_24, 1)
        
        cantidad_23 = self.__board__.contar_fichas_en_punto(23)
        self.assertEqual(cantidad_23, 1)
        
        color_23 = self.__board__.get_color_en_punto(23)
        self.assertEqual(color_23, "blanco")
    
    def test_mover_ficha_a_punto_propio(self):
        """
        Prueba mover ficha a un punto con fichas propias.
        
        Recibe: Nada
        Hace: Verifica que se suma correctamente
        Devuelve: Nada
        """
        cantidad_antes = self.__board__.contar_fichas_en_punto(13)
        
        resultado = self.__board__.mover_ficha(24, 13, "blanco")
        self.assertEqual(resultado, True)
        
        cantidad_despues = self.__board__.contar_fichas_en_punto(13)
        self.assertEqual(cantidad_despues, cantidad_antes + 1)
    
    def test_mover_ficha_casos_negativos(self):
        """
        Prueba casos donde no se puede mover.
        
        Recibe: Nada
        Hace: Verifica origen vacío, color incorrecto, destino bloqueado
        Devuelve: Nada
        """
        # origen vacio
        resultado1 = self.__board__.mover_ficha(2, 3, "blanco")
        self.assertEqual(resultado1, False)
        
        # color incorrecto
        resultado2 = self.__board__.mover_ficha(1, 2, "blanco")
        self.assertEqual(resultado2, False)
        
        # destino bloqueado
        resultado3 = self.__board__.mover_ficha(8, 12, "blanco")
        self.assertEqual(resultado3, False)
    
    def test_capturar_ficha_enemiga_solitaria(self):
        """
        Prueba captura de ficha enemiga sola.
        
        Recibe: Nada
        Hace: Verifica que la ficha capturada va a la barra
        Devuelve: Nada
        """
        # dejar una negra sola en punto 3
        movio1 = self.__board__.mover_ficha(1, 3, "negro")
        self.assertEqual(movio1, True)
        
        # capturar con blanca
        movio2 = self.__board__.mover_ficha(8, 3, "blanco")
        self.assertEqual(movio2, True)
        
        # verificar que punto 3 ahora es blanco
        color_3 = self.__board__.get_color_en_punto(3)
        self.assertEqual(color_3, "blanco")
        
        # verificar que hay una negra en la barra
        fichas_barra = self.__board__.get_fichas_en_punto(0)
        self.assertEqual(len(fichas_barra), 1)
        self.assertEqual(fichas_barra[0].get_color(), "negro")
    
    def test_detectar_fichas_en_barra(self):
        """
        Prueba detección de fichas en la barra.
        
        Recibe: Nada
        Hace: Verifica jugador_tiene_fichas_en_barra
        Devuelve: Nada
        """
        # al inicio nadie tiene fichas en barra
        tiene_blanco = self.__board__.jugador_tiene_fichas_en_barra("blanco")
        self.assertEqual(tiene_blanco, False)
        
        tiene_negro = self.__board__.jugador_tiene_fichas_en_barra("negro")
        self.assertEqual(tiene_negro, False)
        
        # capturar una negra
        self.__board__.mover_ficha(1, 3, "negro")
        self.__board__.mover_ficha(8, 3, "blanco")
        
        # ahora negro tiene ficha en barra
        tiene_negro2 = self.__board__.jugador_tiene_fichas_en_barra("negro")
        self.assertEqual(tiene_negro2, True)
        
        tiene_blanco2 = self.__board__.jugador_tiene_fichas_en_barra("blanco")
        self.assertEqual(tiene_blanco2, False)
    
    def test_sacar_ficha_de_barra_por_color(self):
        """
        Prueba sacar ficha de la barra.
        
        Recibe: Nada
        Hace: Verifica que saca la ficha correcta o None
        Devuelve: Nada
        """
        # no hay fichas en barra
        ficha1 = self.__board__.sacar_ficha_de_barra("blanco")
        self.assertEqual(ficha1, None)
        
        # poner una negra en barra
        self.__board__.mover_ficha(1, 3, "negro")
        self.__board__.mover_ficha(8, 3, "blanco")
        
        # no hay blancas en barra
        ficha2 = self.__board__.sacar_ficha_de_barra("blanco")
        self.assertEqual(ficha2, None)
        
        # si hay negra
        ficha3 = self.__board__.sacar_ficha_de_barra("negro")
        self.assertNotEqual(ficha3, None)
        self.assertEqual(ficha3.get_color(), "negro")
    
    def test_reingresar_desde_barra_casos_falla(self):
        """
        Prueba casos donde reingresar desde barra falla.
        
        Recibe: Nada
        Hace: Verifica destino inválido, bloqueado, sin ficha
        Devuelve: Nada
        """
        # destino fuera de rango
        resultado1 = self.__board__.reingresar_desde_barra("blanco", 0)
        self.assertEqual(resultado1, False)
        
        resultado2 = self.__board__.reingresar_desde_barra("blanco", 25)
        self.assertEqual(resultado2, False)
        
        # sin ficha en barra
        resultado3 = self.__board__.reingresar_desde_barra("blanco", 2)
        self.assertEqual(resultado3, False)
        
        # meter una blanca a la barra
        self.__board__.mover_ficha(24, 23, "blanco")
        self.__board__.mover_ficha(1, 23, "negro")
        
        # intentar reingresar a punto bloqueado (12 tiene 5 negras)
        resultado4 = self.__board__.reingresar_desde_barra("blanco", 12)
        self.assertEqual(resultado4, False)
    
    def test_reingresar_desde_barra_exito(self):
        """
        Prueba reingresar desde barra exitosamente.
        
        Recibe: Nada
        Hace: Verifica reingreso a punto vacío y con captura
        Devuelve: Nada
        """
        # meter una blanca a la barra
        self.__board__.mover_ficha(24, 23, "blanco")
        self.__board__.mover_ficha(1, 23, "negro")
        
        # reingresar a punto vacio
        resultado = self.__board__.reingresar_desde_barra("blanco", 2)
        self.assertEqual(resultado, True)
        
        color_2 = self.__board__.get_color_en_punto(2)
        self.assertEqual(color_2, "blanco")
        
        # preparar otra blanca en barra
        self.__board__.mover_ficha(24, 23, "blanco")
        self.__board__.mover_ficha(1, 23, "negro")
        
        # poner una negra sola en punto 4
        puntos_4 = self.__board__.get_fichas_en_punto(4)
        while len(puntos_4) > 0:
            puntos_4.pop()
        
        ficha_negra = Checker("negro")
        ficha_negra.set_posicion(4)
        self.__board__.get_fichas_en_punto(4).append(ficha_negra)
        
        # reingresar capturando
        resultado2 = self.__board__.reingresar_desde_barra("blanco", 4)
        self.assertEqual(resultado2, True)
        
        color_4 = self.__board__.get_color_en_punto(4)
        self.assertEqual(color_4, "blanco")
        
        # verificar que la negra fue a la barra
        tiene_negra = self.__board__.jugador_tiene_fichas_en_barra("negro")
        self.assertEqual(tiene_negra, True)
    
    def test_puede_sacar_fichas_negativos(self):
        """
        Prueba casos donde NO se puede sacar fichas.
        
        Recibe: Nada
        Hace: Verifica que con fichas fuera del cuadrante final no se puede
        Devuelve: Nada
        """
        # al inicio nadie puede sacar
        puede_blanco = self.__board__.puede_sacar_fichas("blanco")
        self.assertEqual(puede_blanco, False)
        
        puede_negro = self.__board__.puede_sacar_fichas("negro")
        self.assertEqual(puede_negro, False)
    
    def test_puede_sacar_fichas_positivo_blanco(self):
        """
        Prueba cuando blanco SÍ puede sacar fichas.
        
        Recibe: Nada
        Hace: Pone todas las blancas en cuadrante final y verifica
        Devuelve: Nada
        """
        # limpiar tablero
        punto = 0
        while punto < 26:
            puntos_lista = self.__board__.get_fichas_en_punto(punto)
            while len(puntos_lista) > 0:
                puntos_lista.pop()
            punto = punto + 1
        
        # poner 15 blancas en puntos 1-6
        # 3 en punto 1
        contador = 0
        while contador < 3:
            ficha = Checker("blanco")
            ficha.set_posicion(1)
            self.__board__.get_fichas_en_punto(1).append(ficha)
            contador = contador + 1
        
        # 3 en punto 2
        contador = 0
        while contador < 3:
            ficha = Checker("blanco")
            ficha.set_posicion(2)
            self.__board__.get_fichas_en_punto(2).append(ficha)
            contador = contador + 1
        
        # 3 en punto 3
        contador = 0
        while contador < 3:
            ficha = Checker("blanco")
            ficha.set_posicion(3)
            self.__board__.get_fichas_en_punto(3).append(ficha)
            contador = contador + 1
        
        # 2 en punto 4
        contador = 0
        while contador < 2:
            ficha = Checker("blanco")
            ficha.set_posicion(4)
            self.__board__.get_fichas_en_punto(4).append(ficha)
            contador = contador + 1
        
        # 2 en punto 5
        contador = 0
        while contador < 2:
            ficha = Checker("blanco")
            ficha.set_posicion(5)
            self.__board__.get_fichas_en_punto(5).append(ficha)
            contador = contador + 1
        
        # 2 en punto 6
        contador = 0
        while contador < 2:
            ficha = Checker("blanco")
            ficha.set_posicion(6)
            self.__board__.get_fichas_en_punto(6).append(ficha)
            contador = contador + 1
        
        # ahora si puede
        puede = self.__board__.puede_sacar_fichas("blanco")
        self.assertEqual(puede, True)
    
    def test_puede_sacar_fichas_positivo_negro(self):
        """
        Prueba cuando negro SÍ puede sacar fichas.
        
        Recibe: Nada
        Hace: Pone todas las negras en cuadrante final y verifica
        Devuelve: Nada
        """
        # limpiar tablero
        punto = 0
        while punto < 26:
            puntos_lista = self.__board__.get_fichas_en_punto(punto)
            while len(puntos_lista) > 0:
                puntos_lista.pop()
            punto = punto + 1
        
        # poner 15 negras en puntos 19-24
        # 3 en punto 19
        contador = 0
        while contador < 3:
            ficha = Checker("negro")
            ficha.set_posicion(19)
            self.__board__.get_fichas_en_punto(19).append(ficha)
            contador = contador + 1
        
        # 3 en punto 20
        contador = 0
        while contador < 3:
            ficha = Checker("negro")
            ficha.set_posicion(20)
            self.__board__.get_fichas_en_punto(20).append(ficha)
            contador = contador + 1
        
        # 3 en punto 21
        contador = 0
        while contador < 3:
            ficha = Checker("negro")
            ficha.set_posicion(21)
            self.__board__.get_fichas_en_punto(21).append(ficha)
            contador = contador + 1
        
        # 3 en punto 22
        contador = 0
        while contador < 3:
            ficha = Checker("negro")
            ficha.set_posicion(22)
            self.__board__.get_fichas_en_punto(22).append(ficha)
            contador = contador + 1
        
        # 2 en punto 23
        contador = 0
        while contador < 2:
            ficha = Checker("negro")
            ficha.set_posicion(23)
            self.__board__.get_fichas_en_punto(23).append(ficha)
            contador = contador + 1
        
        # 1 en punto 24
        ficha = Checker("negro")
        ficha.set_posicion(24)
        self.__board__.get_fichas_en_punto(24).append(ficha)
        
        # ahora si puede
        puede = self.__board__.puede_sacar_fichas("negro")
        self.assertEqual(puede, True)
    
    def test_sacar_ficha_del_tablero_casos(self):
        """
        Prueba todos los casos de sacar_ficha_del_tablero.
        
        Recibe: Nada
        Hace: Verifica no puede, punto vacío, color incorrecto, éxito
        Devuelve: Nada
        """
        # caso 1: no puede sacar (fichas fuera del cuadrante)
        resultado1 = self.__board__.sacar_ficha_del_tablero(24, "blanco")
        self.assertEqual(resultado1, False)
        
        # caso 2: puede sacar pero punto vacio
        # limpiar tablero
        punto = 0
        while punto < 26:
            puntos_lista = self.__board__.get_fichas_en_punto(punto)
            while len(puntos_lista) > 0:
                puntos_lista.pop()
            punto = punto + 1
        
        # poner una blanca en punto 2
        ficha1 = Checker("blanco")
        ficha1.set_posicion(2)
        self.__board__.get_fichas_en_punto(2).append(ficha1)
        
        puede_sacar = self.__board__.puede_sacar_fichas("blanco")
        self.assertEqual(puede_sacar, True)
        
        # intentar sacar de punto 3 (vacio)
        resultado2 = self.__board__.sacar_ficha_del_tablero(3, "blanco")
        self.assertEqual(resultado2, False)
        
        # caso 3: color incorrecto
        # limpiar tablero de nuevo
        punto = 0
        while punto < 26:
            puntos_lista = self.__board__.get_fichas_en_punto(punto)
            while len(puntos_lista) > 0:
                puntos_lista.pop()
            punto = punto + 1
        
        # poner una negra en punto 24
        ficha2 = Checker("negro")
        ficha2.set_posicion(24)
        self.__board__.get_fichas_en_punto(24).append(ficha2)
        
        puede_negro = self.__board__.puede_sacar_fichas("negro")
        self.assertEqual(puede_negro, True)
        
        # intentar sacar como blanco
        resultado3 = self.__board__.sacar_ficha_del_tablero(24, "blanco")
        self.assertEqual(resultado3, False)
        
        # caso 4: exito
        # limpiar y poner una blanca en punto 1
        punto = 0
        while punto < 26:
            puntos_lista = self.__board__.get_fichas_en_punto(punto)
            while len(puntos_lista) > 0:
                puntos_lista.pop()
            punto = punto + 1
        
        ficha3 = Checker("blanco")
        ficha3.set_posicion(1)
        self.__board__.get_fichas_en_punto(1).append(ficha3)
        
        puede_blanco = self.__board__.puede_sacar_fichas("blanco")
        self.assertEqual(puede_blanco, True)
        
        resultado4 = self.__board__.sacar_ficha_del_tablero(1, "blanco")
        self.assertEqual(resultado4, True)
        
        # verificar que se saco
        cantidad_1 = self.__board__.contar_fichas_en_punto(1)
        self.assertEqual(cantidad_1, 0)
        
        sacadas = self.__board__.contar_fichas_sacadas("blanco")
        self.assertEqual(sacadas, 1)
    
    def test_contar_fichas_sacadas_cero(self):
        """
        Prueba contar fichas sacadas cuando no hay ninguna.
        
        Recibe: Nada
        Hace: Verifica que devuelve 0 para ambos colores
        Devuelve: Nada
        """
        cantidad_blanco = self.__board__.contar_fichas_sacadas("blanco")
        self.assertEqual(cantidad_blanco, 0)
        
        cantidad_negro = self.__board__.contar_fichas_sacadas("negro")
        self.assertEqual(cantidad_negro, 0)
    
    def test_str_inicial(self):
        """
        Prueba la representación en texto del tablero inicial.
        
        Recibe: Nada
        Hace: Verifica que el string contiene elementos esperados
        Devuelve: Nada
        """
        texto = str(self.__board__)
        
        # verificar que contiene los elementos basicos
        if "=== TABLERO DE BACKGAMMON ===" in texto:
            contiene_titulo = True
        else:
            contiene_titulo = False
        self.assertEqual(contiene_titulo, True)
        
        if "13 14 15 16 17 18   19 20 21 22 23 24" in texto:
            contiene_superior = True
        else:
            contiene_superior = False
        self.assertEqual(contiene_superior, True)
        
        if "12 11 10  9  8  7    6  5  4  3  2  1" in texto:
            contiene_inferior = True
        else:
            contiene_inferior = False
        self.assertEqual(contiene_inferior, True)
        
        if "BAR" in texto:
            contiene_bar = True
        else:
            contiene_bar = False
        self.assertEqual(contiene_bar, True)
        
        # no debe mostrar barra ni sacadas si estan vacias
        if "BARRA:" in texto:
            muestra_barra = True
        else:
            muestra_barra = False
        self.assertEqual(muestra_barra, False)
        
        if "SACADAS:" in texto:
            muestra_sacadas = True
        else:
            muestra_sacadas = False
        self.assertEqual(muestra_sacadas, False)
    
    def test_str_con_barra_y_sacadas(self):
        """
        Prueba el string cuando hay fichas en barra y sacadas.
        
        Recibe: Nada
        Hace: Verifica que muestra BARRA: y SACADAS: cuando corresponde
        Devuelve: Nada
        """
        # poner una ficha en la barra
        self.__board__.mover_ficha(1, 3, "negro")
        self.__board__.mover_ficha(8, 3, "blanco")
        
        texto1 = str(self.__board__)
        if "BARRA:" in texto1:
            muestra_barra = True
        else:
            muestra_barra = False
        self.assertEqual(muestra_barra, True)
        
        # sacar una ficha
        # limpiar tablero
        punto = 0
        while punto < 26:
            puntos_lista = self.__board__.get_fichas_en_punto(punto)
            while len(puntos_lista) > 0:
                puntos_lista.pop()
            punto = punto + 1
        
        # poner una blanca y sacarla
        ficha = Checker("blanco")
        ficha.set_posicion(1)
        self.__board__.get_fichas_en_punto(1).append(ficha)
        
        puede = self.__board__.puede_sacar_fichas("blanco")
        self.assertEqual(puede, True)
        
        saco = self.__board__.sacar_ficha_del_tablero(1, "blanco")
        self.assertEqual(saco, True)
        
        texto2 = str(self.__board__)
        if "SACADAS:" in texto2:
            muestra_sacadas = True
        else:
            muestra_sacadas = False
        self.assertEqual(muestra_sacadas, True)


if __name__ == "__main__":
    unittest.main()