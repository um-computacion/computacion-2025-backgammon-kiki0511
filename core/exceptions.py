


class BackgammonError(Exception):
   
   pass


class MovimientoInvalidoError(BackgammonError):
   """
   Error cuando se intenta hacer un movimiento que no es valido.
  
   Se lanza cuando:
   - El punto origen no tiene fichas del jugador
   - El punto destino esta bloqueado
   - No se tiene el valor del dado disponible
   - Se intenta mover cuando hay fichas en la barra
   """
   pass


class PuntoInvalidoError(BackgammonError):
   """
   Error cuando se especifica un punto que no existe en el tablero.
  
   Se lanza cuando:
   - El numero de punto es menor a 0
   - El numero de punto es mayor a 25
   """
   pass


class ValorDadoInvalidoError(BackgammonError):
   """
   Error cuando se especifica un valor de dado invalido.
   Se lanza cuando:
   - El valor no esta en la lista de movimientos disponibles
   - El valor esta fuera del rango 1-6
   """
   pass


class JuegoTerminadoError(BackgammonError):
   """
   Error cuando se intenta hacer una accion en un juego que ya termina
   Se lanza cuando:
   - Se intenta tirar dados en un juego terminado
   - Se intenta hacer movimientos cuando hay un ganador
   """
   pass


class TurnoIncorrectoError(BackgammonError):
   """
   Error cuando se intenta hacer una accion fuera del turno correspondiente.
   Se lanza cuando:
   - Se intenta tirar dados cuando ya se tiraron en el turno
   - Se intenta mover sin haber tirado dados
   """
   pass


class FichaEnBarraError(BackgammonError):
   """
   Error cuando se intenta mover fichas del tablero teniendo fichas en la barra.
  
   Se lanza cuando:
   - Se intenta mover desde un punto del tablero
   - El jugador tiene fichas capturadas en la barra
   """
   pass


class BearOffInvalidoError(BackgammonError):
   """
   Error cuando se intenta sacar fichas sin cumplir las condiciones.
  
   Se lanza cuando:
   - Se intenta sacar fichas sin tenerlas todas en el cuadrante final
   - Se intenta sacar fichas teniendo fichas en la barra
   """
   pass