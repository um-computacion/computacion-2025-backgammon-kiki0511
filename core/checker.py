class Checker:
   
   def __init__(self, color):
      
       self.__color__ = color
       self.__posicion__ = None
  
   def get_color(self):
       
       return self.__color__
  
   def get_posicion(self):
      
       return self.__posicion__
   
   def set_posicion(self, nueva_posicion):
       
       self.__posicion__ = nueva_posicion
  
   def esta_en_barra(self):
       
       return self.__posicion__ == 0
  
   def esta_sacada(self):
      
       return self.__posicion__ == 25
   
   def __str__(self):
      
       if self.__color__ == 'blanco':
           simbolo = 'B'
       else:
           simbolo = 'N'
      
       return f"{simbolo}"

