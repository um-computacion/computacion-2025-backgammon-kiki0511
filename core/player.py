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