# Board: representa el tablero.


from core.checker import Checker


class Board:
    def __init__(self):
       # Crear 26 listas vacías (0 a 25)
       self.__puntos__ = []
       for _ in range(26):
           self.__puntos__.append([])
       # Colocar fichas en posición inicial
       self.colocar_fichas_iniciales()
  
    def colocar_fichas_iniciales(self):
       #Coloca las fichas en la posición inicial del Backgammon (15 blancas y 15 negras)
       # Fichas blancas (jugador que mueve hacia derecha)
       # 2 fichas en punto 24
       for _ in range(2):
           ficha = Checker('blanco')
           ficha.set_posicion(24)
           self.__puntos__[24].append(ficha)
      
       # 5 fichas en punto 13
       for _ in range(5):
           ficha = Checker('blanco')
           ficha.set_posicion(13)
           self.__puntos__[13].append(ficha)
      
       # 3 fichas en punto 8
       for _ in range(3):
           ficha = Checker('blanco')
           ficha.set_posicion(8)
           self.__puntos__[8].append(ficha)

         # 5 fichas en punto 6
       for _ in range(5):
           ficha = Checker('blanco')
           ficha.set_posicion(6)
           self.__puntos__[6].append(ficha)
      
       # Fichas negras (jugador que mueve hacia izquierda)
       # 2 fichas en punto 1
       for _ in range(2):
           ficha = Checker('negro')
           ficha.set_posicion(1)
           self.__puntos__[1].append(ficha)
      
       # 5 fichas en punto 12
       for _ in range(5):
           ficha = Checker('negro')
           ficha.set_posicion(12)
           self.__puntos__[12].append(ficha)
          # 3 fichas en punto 17
       for _ in range(3):
           ficha = Checker('negro')
           ficha.set_posicion(17)
           self.__puntos__[17].append(ficha)
      
       # 5 fichas en punto 19
       for _ in range(5):
           ficha = Checker('negro')
           ficha.set_posicion(19)
           self.__puntos__[19].append(ficha)

def get_fichas_en_punto(self, punto):
       
       if punto < 0 or punto > 25:
           return []
       return self.__puntos__[punto]
  
def contar_fichas_en_punto(self, punto):
       
       return len(self.get_fichas_en_punto(punto))
  
def punto_esta_vacio(self, punto):
       
       return self.contar_fichas_en_punto(punto) == 0
  
def get_color_en_punto(self, punto):
       
       fichas = self.get_fichas_en_punto(punto)
       if len(fichas) == 0:
           return None
       return fichas[0].get_color()

def puede_mover_a_punto(self, punto, color_jugador):
       
       if punto < 1 or punto > 24:
           return False
      
       fichas_en_punto = self.contar_fichas_en_punto(punto)
      
       # Punto vacío - siempre se puede mover
       if fichas_en_punto == 0:
           return True
      
       color_en_punto = self.get_color_en_punto(punto)
      
       # Punto propio - siempre se puede mover
       if color_en_punto == color_jugador:
           return True
      
       # Punto enemigo con 1 ficha - se puede capturar
       if color_en_punto != color_jugador and fichas_en_punto == 1:
           return True
      
       # Punto enemigo con 2 o más fichas - bloqueado
       return False
  
def mover_ficha(self, punto_origen, punto_destino, color_jugador):
       
       # Verificar que hay fichas en el origen
       if self.contar_fichas_en_punto(punto_origen) == 0:
           return False
      
       # Verificar que la ficha es del color correcto
       if self.get_color_en_punto(punto_origen) != color_jugador:
           return False
       
         # Verificar que se puede mover al destino
       if not self.puede_mover_a_punto(punto_destino, color_jugador):
           return False
      
       # Tomar la ficha del origen
       ficha = self.__puntos__[punto_origen].pop()
      
       # Verificar si hay captura
       if (self.contar_fichas_en_punto(punto_destino) == 1 and
           self.get_color_en_punto(punto_destino) != color_jugador):
           # Capturar la ficha enemiga (moverla a la barra)
           ficha_capturada = self.__puntos__[punto_destino].pop()
           ficha_capturada.set_posicion(0)
           self.__puntos__[0].append(ficha_capturada)
      
       # Mover la ficha al destino
       ficha.set_posicion(punto_destino)
       self.__puntos__[punto_destino].append(ficha)
      
       return True

def reingresar_desde_barra(self, color_jugador, destino):
       """
       Reingresa una ficha desde la barra (punto 0) al destino segun reglas.
       Maneja captura si hay 1 ficha enemiga.
       """
       if not (1 <= destino <= 24):
           return False
       if not self.puede_mover_a_punto(destino, color_jugador):
           return False


       ficha = self.sacar_ficha_de_barra(color_jugador)
       if ficha is None:
           return False

 # Captura si corresponde
       if (self.contar_fichas_en_punto(destino) == 1 and
           self.get_color_en_punto(destino) != color_jugador):
           ficha_capturada = self.__puntos__[destino].pop()
           ficha_capturada.set_posicion(0)
           self.__puntos__[0].append(ficha_capturada)


       ficha.set_posicion(destino)
       self.__puntos__[destino].append(ficha)
       return True
  
def jugador_tiene_fichas_en_barra(self, color_jugador):
       #Verifica si un jugador tiene fichas en la barra (punto 0).
       fichas_en_barra = self.get_fichas_en_punto(0)
       for ficha in fichas_en_barra:
           if ficha.get_color() == color_jugador:
               return True
       return False
  
def sacar_ficha_de_barra(self, color_jugador):
       #Saca una ficha del jugador desde la barra (punto 0).
       fichas_en_barra = self.get_fichas_en_punto(0)
       for i in range(len(fichas_en_barra)):
           if fichas_en_barra[i].get_color() == color_jugador:
               return self.__puntos__[0].pop(i)
       return None
  
def puede_sacar_fichas(self, color_jugador):
       """
       Verifica si un jugador puede empezar a sacar fichas del tablero .
       Requiere que no tenga fichas en barra y que todas estén en el cuadrante final.
       """
       if self.jugador_tiene_fichas_en_barra(color_jugador):
           return False
      
       # Definir cuadrante final según el color
       if color_jugador == 'blanco':
           cuadrante_final = range(1, 7)  # Puntos 1-6
       else:
           cuadrante_final = range(19, 25)  # Puntos 19-24