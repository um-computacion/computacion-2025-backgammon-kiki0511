## Dice: logica de tiradas de dados .

import random


class Dice:
   def __init__(self):
       self.ultima_tirada = None


   def tirar(self):
       dado1 = random.randint(1, 6)
       dado2 = random.randint(1, 6)

       if dado1 == dado2:
           resultado = [dado1]*4
       else:
           resultado = [dado1, dado2]
       self.ultima_tirada = resultado

       return resultado


   def get_ultima_tirada(self):
       
       return self.ultima_tirada


   def es_doble(self):
       
       if self.ultima_tirada is None:
           return False
       return len(self.ultima_tirada) == 4
