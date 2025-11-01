# Prompts de IA - Desarrollo

Este archivo documenta todos los prompts utilizados con herramientas de IA durante el desarrollo del código del proyecto Backgammon.

---

## Prompt 1: Inicio del Proyecto - Estructura Base

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 12/09/2024

### Instrucciones del Sistema
Ninguna (configuración por defecto)

### Prompt Exacto
```
hola necesito hacer un proyecto de backgammon para la facultad. Tengo que hacer las clases principales pero no se como empezar. 

me piden que tenga:
- clase para fichas
- clase para dados
- clase para jugadores
- clase para el tablero
- clase principal del juego

todo tiene que estar en una carpeta core/ y despues la interfaz en otra carpeta. Me ayudas a pensar como organizar esto?
```

### Respuesta Completa de la IA
```
¡Claro! Te ayudo a organizar tu proyecto de Backgammon. Aquí está una estructura recomendada:

Estructura de carpetas:
```
backgammon/
├── core/
│   ├── __init__.py
│   ├── checker.py      # Clase para las fichas
│   ├── dice.py         # Clase para los dados
│   ├── player.py       # Clase para jugadores
│   ├── board.py        # Clase para el tablero
│   ├── game.py         # Clase principal del juego
│   └── exceptions.py   # Excepciones personalizadas
├── cli/
│   ├── __init__.py
│   └── cli.py          # Interfaz de línea de comandos
├── tests/
│   ├── __init__.py
│   └── ...             # Tests unitarios
└── requirements.txt
```

Empecemos por lo más simple:

**1. Clase Checker (checker.py):**
```python
class Checker:
    def __init__(self, color):
        self.color = color  # 'blanco' o 'negro'
        self.posicion = None
    
    def get_color(self):
        return self.color
```

Te recomiendo empezar implementando las clases más simples primero (Checker, Dice, Player) y luego las más complejas (Board, Game).

¿Quieres que te ayude con alguna clase específica?
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
Cambié:
- Formato de atributos a `__nombre__` (requisito de la materia)
- Agregué más métodos a Checker
- Agregué docstrings
- No usé `self.color` directamente, sino `self.__color__`

Código final muy diferente al sugerido, pero la estructura de carpetas sí la usé.

### Archivos Finales Afectados
- Estructura completa del proyecto (carpetas core/, cli/, tests/)
- core/__init__.py
- cli/__init__.py
- tests/__init__.py

---

## Prompt 2: Implementación de Clase Player

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 12/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
necesito hacer la clase Player. Tiene que tener:
- nombre del jugador
- direccion (1 o -1 para saber hacia donde se mueve)
- fichas en la barra (cuando te capturan)
- fichas sacadas (bear off)

importante: todos los atributos tienen q tener formato __nombre__ adelante y atras.
no puedo usar for ni range() solo while
y necesito docstrings
```

### Respuesta Completa de la IA
```
Entendido. Aquí está la clase Player con tus requisitos:

```python
class Player:
    """Representa un jugador de Backgammon."""
    
    def __init__(self, nombre, direccion):
        """
        Inicializa un jugador.
        
        Args:
            nombre (str): Nombre del jugador
            direccion (int): 1 para blanco, -1 para negro
        """
        self.__nombre__ = nombre
        self.__direccion__ = direccion
        self.__fichas_en_barra__ = 0
        self.__fichas_sacadas__ = 0
    
    def get_nombre(self):
        """Retorna el nombre del jugador."""
        return self.__nombre__
    
    def get_direccion(self):
        """Retorna la dirección de movimiento."""
        return self.__direccion__
    
    def agregar_ficha_a_barra(self):
        """Incrementa el contador de fichas en la barra."""
        self.__fichas_en_barra__ += 1
    
    def quitar_ficha_de_barra(self):
        """Decrementa el contador de fichas en la barra."""
        if self.__fichas_en_barra__ > 0:
            self.__fichas_en_barra__ -= 1
    
    def ha_ganado(self):
        """Verifica si el jugador ganó (15 fichas sacadas)."""
        return self.__fichas_sacadas__ >= 15
```

¿Necesitas más métodos?
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
- Cambié docstrings al formato "Recibe/Hace/Devuelve" (más simple)
- Agregué más métodos: `get_fichas_en_barra()`, `get_fichas_sacadas()`, `sacar_ficha_del_tablero()`, `tiene_fichas_en_barra()`, `__str__()`
- Cambié `+=` por `= variable + 1` (estilo más explícito)

### Archivos Finales Afectados
- core/player.py

---

## Prompt 3: Clase Dice con Random

### Modelo/Herramienta
**Nombre:** Claude 3.5 Sonnet (claude.ai)  
**Versión:** claude-sonnet-3-5-20240620  
**Fecha:** 13/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
tengo q hacer la clase Dice para tirar dados en backgammon

reglas:
- tira 2 dados de 6 caras
- si salen iguales (dobles) entonces tenes 4 movimientos con ese numero
- si salen distintos tenes 2 movimientos

tiene q usar random.randint
formato __atributo__
no usar for
agregar docstrings
```

### Respuesta Completa de la IA
```
Perfecto, aquí está la clase Dice para tu juego de Backgammon:

```python
import random

class Dice:
    """Clase que representa los dados del juego."""
    
    def __init__(self):
        """Inicializa los dados."""
        self.__ultima_tirada__ = None
    
    def tirar(self):
        """
        Realiza una tirada de dos dados.
        
        Returns:
            list: Lista con valores de dados (2 o 4 elementos)
        """
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        
        if dado1 == dado2:
            # Dobles: 4 movimientos
            resultado = [dado1, dado1, dado1, dado1]
        else:
            # Normal: 2 movimientos
            resultado = [dado1, dado2]
        
        self.__ultima_tirada__ = resultado
        return resultado
    
    def get_ultima_tirada(self):
        """Retorna la última tirada realizada."""
        return self.__ultima_tirada__
    
    def es_doble(self):
        """Verifica si la última tirada fue dobles."""
        if self.__ultima_tirada__ is None:
            return False
        return len(self.__ultima_tirada__) == 4
```

La lógica es simple: si los dados son iguales, crea una lista con 4 veces ese valor. Si son diferentes, devuelve los 2 valores.

¿Necesitas algo más para esta clase?
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
- Cambié la forma de construir la lista (usando append en lugar de lista literal)
- Agregué más explicación en docstrings
- Cambié `is None` por comparación con `== None`
- Usé while para construir lista de 4 elementos (para evitar lista literal que podría verse como "avanzado")

### Archivos Finales Afectados
- core/dice.py

---

## Prompt 4: Clase Checker Simple

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 14/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
clase Checker para una ficha de backgammon

atributos:
- color (blanco o negro)
- posicion (0-25, donde 0=barra y 25=sacada)

metodos:
- esta_en_barra() devuelve true si posicion es 0
- esta_sacada() devuelve true si posicion es 25
- __str__() devuelve 'B' o 'N'

formato __atributo__
docstrings
sin for
```

### Respuesta Completa de la IA
```
Aquí está la clase Checker:

```python
class Checker:
    """Representa una ficha de Backgammon."""
    
    def __init__(self, color):
        """Inicializa una ficha con su color."""
        self.__color__ = color
        self.__posicion__ = None
    
    def get_color(self):
        """Retorna el color de la ficha."""
        return self.__color__
    
    def get_posicion(self):
        """Retorna la posición actual."""
        return self.__posicion__
    
    def set_posicion(self, nueva_posicion):
        """Establece una nueva posición."""
        self.__posicion__ = nueva_posicion
    
    def esta_en_barra(self):
        """Verifica si está en la barra (posición 0)."""
        return self.__posicion__ == 0
    
    def esta_sacada(self):
        """Verifica si está sacada del tablero (posición 25)."""
        return self.__posicion__ == 25
    
    def __str__(self):
        """Representación en string."""
        if self.__color__ == 'blanco':
            return 'B'
        else:
            return 'N'
```
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
- Agregué más docstrings explicativos
- Cambié los return directos por if/else más explícitos
- Agregué validación en esta_en_barra() y esta_sacada() para manejar None

### Archivos Finales Afectados
- core/checker.py

---

## Prompt 5: Inicio de Clase Board

### Modelo/Herramienta
**Nombre:** Claude 3.5 Sonnet (claude.ai)  
**Versión:** claude-sonnet-3-5-20240620  
**Fecha:** 14/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
necesito empezar a hacer la clase Board para el tablero de backgammon

el tablero tiene:
- 26 puntos (0=barra, 1-24=tablero, 25=sacadas)
- cada punto tiene una lista de fichas

al inicio tiene q poner las fichas en las posiciones iniciales de backgammon:
- blancas: 2 en punto 24, 5 en punto 13, 3 en punto 8, 5 en punto 6
- negras: 2 en punto 1, 5 en punto 12, 3 en punto 17, 5 en punto 19

como arranco? formato __atributo__ y sin for
```

### Respuesta Completa de la IA
```
Excelente, empecemos con la estructura base de Board. Aquí está la inicialización:

```python
from core.checker import Checker

class Board:
    """Representa el tablero de Backgammon."""
    
    def __init__(self):
        """
        Inicializa el tablero con 26 puntos y coloca las fichas
        en sus posiciones iniciales.
        """
        # Crear 26 listas vacías (una por punto)
        self.__puntos__ = []
        i = 0
        while i < 26:
            self.__puntos__.append([])
            i += 1
        
        # Colocar fichas blancas
        self._colocar_fichas_iniciales('blanco', 24, 2)
        self._colocar_fichas_iniciales('blanco', 13, 5)
        self._colocar_fichas_iniciales('blanco', 8, 3)
        self._colocar_fichas_iniciales('blanco', 6, 5)
        
        # Colocar fichas negras
        self._colocar_fichas_iniciales('negro', 1, 2)
        self._colocar_fichas_iniciales('negro', 12, 5)
        self._colocar_fichas_iniciales('negro', 17, 3)
        self._colocar_fichas_iniciales('negro', 19, 5)
    
    def _colocar_fichas_iniciales(self, color, punto, cantidad):
        """Helper para colocar fichas en la inicialización."""
        i = 0
        while i < cantidad:
            ficha = Checker(color)
            ficha.set_posicion(punto)
            self.__puntos__[punto].append(ficha)
            i += 1
```

Este es el esqueleto básico. Ahora necesitarás agregar métodos para:
- get_fichas_en_punto(punto)
- mover_ficha(origen, destino, color)
- puede_mover_a_punto(destino, color)
- etc.

¿Quieres que te ayude con alguno de estos métodos?
```

### Estado de Uso
- [X] Usada sin cambios

### Modificaciones Realizadas
Ninguna, el código de inicialización quedó tal cual.

### Archivos Finales Afectados
- core/board.py (método __init__ y _colocar_fichas_iniciales)

---

## Prompt 6: Validación de Movimientos en Board

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 15/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
board.py

necesito el metodo puede_mover_a_punto(punto_destino, color) q valide si se puede mover a ese punto segun las reglas

reglas:
- si el punto esta vacio -> se puede
- si hay fichas del mismo color -> se puede
- si hay 1 ficha del otro color -> se puede (captura)
- si hay 2+ fichas del otro color -> NO se puede (bloqueado)

sin for, con while
```

### Respuesta Completa de la IA
```
Aquí está el método de validación:

```python
def puede_mover_a_punto(self, punto_destino, color):
    """
    Verifica si se puede mover una ficha al punto destino.
    
    Args:
        punto_destino (int): Punto destino (1-24)
        color (str): Color de la ficha que se quiere mover
    
    Returns:
        bool: True si el movimiento es válido, False si no
    """
    # Verificar rango válido
    if punto_destino < 1 or punto_destino > 24:
        return False
    
    fichas_en_destino = self.__puntos__[punto_destino]
    
    # Punto vacío: siempre se puede
    if len(fichas_en_destino) == 0:
        return True
    
    # Obtener color del punto
    color_punto = fichas_en_destino[0].get_color()
    
    # Mismo color: siempre se puede
    if color_punto == color:
        return True
    
    # Otro color: solo si hay 1 ficha (captura)
    if len(fichas_en_destino) == 1:
        return True  # Captura permitida
    
    # 2+ fichas del otro color: bloqueado
    return False
```
```

### Estado de Uso
- [X] Usada sin cambios

### Modificaciones Realizadas
Ninguna, la lógica es exacta.

### Archivos Finales Afectados
- core/board.py (método puede_mover_a_punto)

---

## Prompt 7: Sistema de Excepciones

### Modelo/Herramienta
**Nombre:** Claude 3.5 Sonnet (claude.ai)  
**Versión:** claude-sonnet-3-5-20240620  
**Fecha:** 23/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
necesito crear excepciones personalizadas para backgammon

las q necesito:
- BackgammonError (base)
- MovimientoInvalidoError
- PuntoInvalidoError
- ValorDadoInvalidoError
- JuegoTerminadoError
- TurnoIncorrectoError
- FichaEnBarraError
- BearOffInvalidoError

todas tienen q heredar de la base y tener mensajes por defecto

formato __atributo__
docstrings
```

### Respuesta Completa de la IA
```
Perfecto, aquí está el sistema completo de excepciones:

```python
class BackgammonError(Exception):
    """Excepción base para errores del juego."""
    
    def __init__(self, mensaje="Error en el juego de Backgammon"):
        self.__mensaje__ = mensaje
        super().__init__(self.__mensaje__)


class MovimientoInvalidoError(BackgammonError):
    """Error cuando se intenta un movimiento inválido."""
    
    def __init__(self, mensaje="Movimiento no es valido"):
        super().__init__(mensaje)


class PuntoInvalidoError(BackgammonError):
    """Error cuando se especifica un punto fuera de rango."""
    
    def __init__(self, mensaje="Punto fuera del rango valido"):
        super().__init__(mensaje)


class ValorDadoInvalidoError(BackgammonError):
    """Error cuando el valor del dado es inválido."""
    
    def __init__(self, mensaje="Valor de dado fuera del rango valido"):
        super().__init__(mensaje)


class JuegoTerminadoError(BackgammonError):
    """Error cuando se intenta jugar en un juego terminado."""
    
    def __init__(self, mensaje="El juego ya esta terminado"):
        super().__init__(mensaje)


class TurnoIncorrectoError(BackgammonError):
    """Error cuando se hace una acción fuera de turno."""
    
    def __init__(self, mensaje="Accion fuera del turno correspondiente"):
        super().__init__(mensaje)


class FichaEnBarraError(BackgammonError):
    """Error cuando hay fichas en barra sin resolver."""
    
    def __init__(self, mensaje="Debe mover fichas de la barra primero"):
        super().__init__(mensaje)


class BearOffInvalidoError(BackgammonError):
    """Error cuando se intenta bear off inválido."""
    
    def __init__(self, mensaje="No puede sacar fichas del cuadrante final"):
        super().__init__(mensaje)
```

Todas heredan de BackgammonError, así puedes capturarlas todas con un solo `except BackgammonError` o capturar específicas según necesites.
```

### Estado de Uso
- [X] Usada sin cambios

### Modificaciones Realizadas
Ninguna, quedó tal cual.

### Archivos Finales Afectados
- core/exceptions.py

---

## Prompt 8: Clase BackgammonGame - Coordinador

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 24/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
necesito la clase BackgammonGame que coordine todo el juego

tiene q tener:
- un tablero (Board)
- dos jugadores (Player)
- dados (Dice)
- jugador actual
- lista de movimientos disponibles (los dados que todavia no use)
- flag si el juego termino
- ganador

metodos principales:
- tirar_dados() -> tira y guarda en movimientos disponibles
- hacer_movimiento(origen, dado) -> mueve y consume el dado
- terminar_turno() -> cambia de jugador
- verificar_victoria() -> checkea si alguien gano

formato __atributo__
sin for
docstrings
```

### Respuesta Completa de la IA
```
Aquí está la estructura base de BackgammonGame:

```python
from core.board import Board
from core.player import Player
from core.dice import Dice

class BackgammonGame:
    """Coordinador principal del juego de Backgammon."""
    
    def __init__(self, nombre1, nombre2):
        """Inicializa una nueva partida."""
        self.__tablero__ = Board()
        self.__jugador1__ = Player(nombre1, 1)   # Blanco
        self.__jugador2__ = Player(nombre2, -1)  # Negro
        self.__jugador_actual__ = self.__jugador1__
        self.__dados__ = Dice()
        self.__movimientos_disponibles__ = []
        self.__juego_terminado__ = False
        self.__ganador__ = None
    
    def tirar_dados(self):
        """Tira los dados y guarda movimientos disponibles."""
        resultado = self.__dados__.tirar()
        self.__movimientos_disponibles__ = []
        
        # Copiar valores a movimientos disponibles
        i = 0
        while i < len(resultado):
            self.__movimientos_disponibles__.append(resultado[i])
            i += 1
        
        return resultado
    
    def hacer_movimiento(self, origen, valor_dado):
        """
        Ejecuta un movimiento y consume el dado usado.
        
        Returns:
            bool: True si el movimiento fue exitoso
        """
        # Verificar que el dado esté disponible
        if valor_dado not in self.__movimientos_disponibles__:
            return False
        
        # Intentar hacer el movimiento en el tablero
        exito = self.__tablero__.mover_ficha(
            origen, 
            destino,  # calcular según dirección
            self.__jugador_actual__.get_color()
        )
        
        if exito:
            # Consumir el dado usado
            self.__movimientos_disponibles__.remove(valor_dado)
            return True
        
        return False
    
    def terminar_turno(self):
        """Cambia al siguiente jugador."""
        if self.__jugador_actual__ == self.__jugador1__:
            self.__jugador_actual__ = self.__jugador2__
        else:
            self.__jugador_actual__ = self.__jugador1__
        
        self.__movimientos_disponibles__ = []
    
    def verificar_victoria(self):
        """Verifica si algún jugador ganó."""
        if self.__jugador1__.ha_ganado():
            self.__juego_terminado__ = True
            self.__ganador__ = self.__jugador1__
        elif self.__jugador2__.ha_ganado():
            self.__juego_terminado__ = True
            self.__ganador__ = self.__jugador2__
```

Este es el esqueleto principal. Necesitarás completar los métodos y agregar validaciones adicionales.
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
- Completé el método hacer_movimiento con toda la lógica
- Agregué método _calcular_destino para calcular punto destino
- Agregué método puede_hacer_movimiento para validar antes de mover
- Agregué más validaciones
- Cambié .remove() por búsqueda con while y .pop()
- Agregué atributo __turno_paso_automatico__
- Mejoré verificar_victoria() con conteo real de fichas

### Archivos Finales Afectados
- core/game.py

---

## Prompt 9: Corrección de Formato - Sin For

### Modelo/Herramienta
**Nombre:** Claude 3.5 Sonnet (claude.ai)  
**Versión:** claude-sonnet-4-5-20250929  
**Fecha:** 01/11/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
revisa todo mi código y asegurate de que NO use for, range(), ni break en ninguna parte

tiene q ser todo con while

pasame las correcciones que tengo q hacer
```

### Respuesta Completa de la IA
```
Revisé tu código y encontré varios lugares donde usas `for`, `range()` o `break`. Aquí están las correcciones:

**En game.py - Método tirar_dados():**
Cambiar:
```python
for valor in resultado_dados:
    self.__movimientos_disponibles__.append(valor)
```

Por:
```python
i = 0
while i < len(resultado_dados):
    valor = resultado_dados[i]
    self.__movimientos_disponibles__.append(valor)
    i = i + 1
```

**En game.py - Método puede_hacer_movimiento():**
Cambiar:
```python
for dado in self.__movimientos_disponibles__:
    if dado == valor_dado:
        dado_disponible = True
        break
```

Por:
```python
i = 0
while i < len(self.__movimientos_disponibles__):
    dado = self.__movimientos_disponibles__[i]
    if dado == valor_dado:
        dado_disponible = True
        i = len(self.__movimientos_disponibles__)  # salir
    else:
        i = i + 1
```

[... más correcciones similares ...]
```

### Estado de Uso
- [X] Usada sin cambios

### Modificaciones Realizadas
Ninguna, apliqué todas las correcciones tal cual.

### Archivos Finales Afectados
- core/game.py (6 correcciones)
- core/player.py (formato docstrings)

---

## Notas Finales

### Estrategia General
1. Empecé por clases simples (Checker, Dice, Player)
2. Luego hice las complejas (Board, Game)
3. Sistema de excepciones al final
4. Corrección de formato al final

### Lecciones Aprendidas
- La IA genera código con `for` por defecto, hay que corregir
- Siempre revisar que cumpla con formato `__atributo__`
- Los docstrings generados son buenos pero los simplifiqué
- Mejor pedir ayuda paso a paso que todo junto

---

**Última actualización:** 01/11/2024