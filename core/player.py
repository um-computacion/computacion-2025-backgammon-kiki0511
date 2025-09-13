class Player:
   def __init__(self, nombre, direccion):
       self.__nombre__ = nombre
       self.__direccion__ = direccion
       self.__fichas_en_barra__ = 0
       self.__fichas_sacadas__ = 0


   def get_nombre(self):
       return self.__nombre__
 
   def get_direccion(self):
       return self.__direccion__
  
   def get_fichas_en_barra(self):
       return self.__fichas_en_barra__
   
   def get_fichas_sacadas(self):
        return self.__fichas_sacadas__
  
   def agregar_ficha_a_barra(self):
       self.__fichas_en_barra__ = self.__fichas_en_barra__ + 1
  
   def quitar_ficha_de_barra(self):
       if self.__fichas_en_barra__ > 0:
           self.__fichas_en_barra__ = self.__fichas_en_barra__ - 1



   def sacar_ficha_del_tablero(self):
       self.__fichas_sacadas__ = self.__fichas_sacadas__ + 1
  
   def tiene_fichas_en_barra(self):
       return self.__fichas_en_barra__ > 0
  
   def ha_ganado(self):
       return self.__fichas_sacadas__ >= 15

   def __str__(self):
       if self.__direccion__ == 1:
           direccion_texto = "derecha"
       else:
           direccion_texto = "izquierda"
       return f"Jugador: {self.__nombre__} (mueve hacia {direccion_texto})"    