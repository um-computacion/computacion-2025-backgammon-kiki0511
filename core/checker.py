class Checker:
   
   def __init__(self, color):
      
       self.__color__ = color
       self.__posicion__ = None
  
   def get_color(self):
       
       return self.__color__
  
   def get_posicion(self):
      
       return self.__posicion__