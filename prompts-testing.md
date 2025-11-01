# Prompts de IA - Testing

Este archivo documenta todos los prompts utilizados con herramientas de IA durante el desarrollo de tests unitarios del proyecto Backgammon.

---

## Prompt 1: Como Empezar con Testing

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 23/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
nunca hice tests unitarios. tengo q hacer tests para mi proyecto de backgammon usando unittest (no pytest)

necesito alcanzar 90% de cobertura en core/

como empiezo? que instalo? como se estructura?
```

### Respuesta Completa de la IA
```
¡Perfecto! Te explico paso a paso cómo empezar con unittest.

**1. Instalar coverage:**
```bash
pip install coverage
```

**2. Estructura de tests:**
```
tests/
├── __init__.py
├── test_checker.py
├── test_dice.py
├── test_player.py
├── test_board.py
├── test_game.py
└── test_exceptions.py
```

**3. Estructura básica de un test:**
```python
import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test."""
        self.ficha = Checker('blanco')
    
    def test_algo(self):
        """Prueba algo específico."""
        self.assertEqual(self.ficha.get_color(), 'blanco')

if __name__ == '__main__':
    unittest.main()
```

**4. Ejecutar tests:**
```bash
# Todos los tests
python -m unittest discover

# Con cobertura
coverage run -m unittest discover
coverage report
```

**Assertions más usados:**
- `assertEqual(a, b)` - a == b
- `assertTrue(x)` - x es True
- `assertFalse(x)` - x es False
- `assertIsNone(x)` - x es None

Empieza testeando las clases más simples primero (Checker, Dice, Player).

¿Quieres que te ayude con el primer test?
```

### Estado de Uso
- [X] Usada sin cambios

### Modificaciones Realizadas
Ninguna, seguí exactamente esta estructura.

### Archivos Finales Afectados
- tests/__init__.py
- Instalé coverage
- Estructura de archivos test_*.py

---

## Prompt 2: Tests para Dice con Random

### Modelo/Herramienta
**Nombre:** Claude 3.5 Sonnet (claude.ai)  
**Versión:** claude-sonnet-3-5-20240620  
**Fecha:** 23/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
necesito testear mi clase Dice pero usa random.randint() y no se como testear algo aleatorio

la clase tiene:
- tirar() que devuelve [d1, d2] o [d, d, d, d] si son dobles
- get_ultima_tirada()
- es_doble()

como hago para controlar el random en los tests?
```

### Respuesta Completa de la IA
```
Excelente pregunta. Para testear código con random, necesitas usar **mocking** para controlar los valores.

Aquí está cómo hacerlo con unittest:

```python
import unittest
import random
from core.dice import Dice

class TestDice(unittest.TestCase):
    
    def setUp(self):
        self.dice = Dice()
    
    def test_tirar_no_dobles(self):
        """Prueba tirada normal (no dobles)."""
        # Guardar random original
        original = random.randint
        
        # Crear mock que devuelve valores controlados
        valores = [2, 5]
        indice = [0]
        
        def mock_randint(a, b):
            resultado = valores[indice[0]]
            indice[0] += 1
            return resultado
        
        # Reemplazar random
        random.randint = mock_randint
        
        try:
            resultado = self.dice.tirar()
            
            # Verificar resultado
            self.assertEqual(len(resultado), 2)
            self.assertEqual(resultado[0], 2)
            self.assertEqual(resultado[1], 5)
            self.assertFalse(self.dice.es_doble())
        
        finally:
            # Restaurar random original
            random.randint = original
    
    def test_tirar_dobles(self):
        """Prueba tirada de dobles."""
        original = random.randint
        
        # Mock que siempre devuelve 3
        random.randint = lambda a, b: 3
        
        try:
            resultado = self.dice.tirar()
            
            self.assertEqual(len(resultado), 4)
            self.assertEqual(resultado, [3, 3, 3, 3])
            self.assertTrue(self.dice.es_doble())
        
        finally:
            random.randint = original
```

**Cómo funciona:**
1. Guardas la función `random.randint` original
2. La reemplazas con tu propia función que devuelve valores controlados
3. Ejecutas el test
4. En el `finally` restauras el random original

Esto te da control total sobre qué valores "salen" en los dados.

¿Necesitas más ejemplos?
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
- Cambié `indice[0] +=1` por `indice[0] = indice[0] + 1` (evitar +=)
- Agregué más tests para cubrir todas las combinaciones
- Agregué test para estado inicial (ultima_tirada = None)

### Archivos Finales Afectados
- tests/test_dice.py

---

## Prompt 3: Tests Completos para Checker

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 24/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
necesito tests para Checker

la clase tiene:
- __init__(color)
- get_color()
- get_posicion() / set_posicion()
- esta_en_barra() - true si pos==0
- esta_sacada() - true si pos==25
- __str__() - devuelve 'B' o 'N'

necesito 100% de cobertura. como saber q esta todo cubierto?
```

### Respuesta Completa de la IA
```
Para 100% de cobertura necesitas probar:
1. Todas las líneas de código
2. Todas las ramas (if/else)
3. Todos los casos límite

Aquí están los tests que necesitas:

```python
import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):
    
    def setUp(self):
        self.ficha_blanca = Checker('blanco')
        self.ficha_negra = Checker('negro')
    
    # Tests de inicialización
    def test_crear_ficha_blanca(self):
        self.assertEqual(self.ficha_blanca.get_color(), 'blanco')
        self.assertIsNone(self.ficha_blanca.get_posicion())
    
    def test_crear_ficha_negra(self):
        self.assertEqual(self.ficha_negra.get_color(), 'negro')
        self.assertIsNone(self.ficha_negra.get_posicion())
    
    # Tests de posición
    def test_set_posicion(self):
        self.ficha_blanca.set_posicion(13)
        self.assertEqual(self.ficha_blanca.get_posicion(), 13)
    
    # Tests de esta_en_barra() - AMBAS RAMAS
    def test_esta_en_barra_true(self):
        self.ficha_blanca.set_posicion(0)
        self.assertTrue(self.ficha_blanca.esta_en_barra())
    
    def test_esta_en_barra_false(self):
        self.ficha_blanca.set_posicion(5)
        self.assertFalse(self.ficha_blanca.esta_en_barra())
    
    # Tests de esta_sacada() - AMBAS RAMAS
    def test_esta_sacada_true(self):
        self.ficha_blanca.set_posicion(25)
        self.assertTrue(self.ficha_blanca.esta_sacada())
    
    def test_esta_sacada_false(self):
        self.ficha_blanca.set_posicion(10)
        self.assertFalse(self.ficha_blanca.esta_sacada())
    
    # Tests de __str__() - AMBAS RAMAS
    def test_str_blanca(self):
        self.assertEqual(str(self.ficha_blanca), 'B')
    
    def test_str_negra(self):
        self.assertEqual(str(self.ficha_negra), 'N')
    
    # Casos límite
    def test_todas_posiciones_validas(self):
        """Probar posiciones 0-25."""
        posiciones = [0, 1, 12, 24, 25]
        for pos in posiciones:
            self.ficha_blanca.set_posicion(pos)
            self.assertEqual(self.ficha_blanca.get_posicion(), pos)
```

**Para ver cobertura:**
```bash
coverage run -m unittest discover
coverage report -m
```

El `-m` te muestra qué líneas NO están cubiertas. Agrega tests hasta que todo esté al 100%.
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
- Cambié el for del caso límite por while
- Agregué más tests de casos límite
- Agregué tests de posición None
- Separé más los tests para mejor granularidad
- Cambié nombres de variables (self.ficha_blanca -> self.__ficha_blanca__)

### Archivos Finales Afectados
- tests/test_checker.py

---

## Prompt 4: Tests para Player

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 26/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
tests para Player

la clase tiene:
- nombre, direccion
- fichas_en_barra (se incrementa con agregar_ficha_a_barra)
- fichas_sacadas (se incrementa con agregar_ficha_sacada)
- quitar_ficha_de_barra (solo si hay fichas)
- tiene_fichas_en_barra() - bool
- ha_ganado() - true si 15 fichas sacadas

dame estructura de tests
```

### Respuesta Completa de la IA
```
Aquí está la estructura completa:

```python
import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.jugador_blanco = Player("Ana", 1)
        self.jugador_negro = Player("Luis", -1)
    
    # Getters básicos
    def test_get_nombre(self):
        self.assertEqual(self.jugador_blanco.get_nombre(), "Ana")
    
    def test_get_direccion(self):
        self.assertEqual(self.jugador_blanco.get_direccion(), 1)
        self.assertEqual(self.jugador_negro.get_direccion(), -1)
    
    # Fichas en barra
    def test_agregar_ficha_a_barra(self):
        self.jugador_blanco.agregar_ficha_a_barra()
        self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 1)
    
    def test_quitar_ficha_de_barra_cuando_hay(self):
        self.jugador_blanco.agregar_ficha_a_barra()
        self.jugador_blanco.quitar_ficha_de_barra()
        self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 0)
    
    def test_quitar_ficha_de_barra_cuando_no_hay(self):
        """Debe manejar bien el caso de 0 fichas."""
        self.jugador_blanco.quitar_ficha_de_barra()
        self.assertEqual(self.jugador_blanco.get_fichas_en_barra(), 0)
    
    def test_tiene_fichas_en_barra_true(self):
        self.jugador_blanco.agregar_ficha_a_barra()
        self.assertTrue(self.jugador_blanco.tiene_fichas_en_barra())
    
    def test_tiene_fichas_en_barra_false(self):
        self.assertFalse(self.jugador_blanco.tiene_fichas_en_barra())
    
    # Fichas sacadas y victoria
    def test_agregar_ficha_sacada(self):
        self.jugador_blanco.agregar_ficha_sacada()
        self.assertEqual(self.jugador_blanco.get_fichas_sacadas(), 1)
    
    def test_ha_ganado_false(self):
        # Con menos de 15 fichas
        for _ in range(10):
            self.jugador_blanco.agregar_ficha_sacada()
        self.assertFalse(self.jugador_blanco.ha_ganado())
    
    def test_ha_ganado_true(self):
        # Con 15 fichas
        for _ in range(15):
            self.jugador_blanco.agregar_ficha_sacada()
        self.assertTrue(self.jugador_blanco.ha_ganado())
```

Esto debería darte cerca del 100% de cobertura en Player.
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
- Cambié los `for` por `while`
- Cambié nombres de variables (self.jugador_blanco -> self.__jugador_blanco__)
- Agregué test de __str__()
- Agregué test de independencia entre jugadores
- Agregué docstrings más detallados

### Archivos Finales Afectados
- tests/test_player.py

---

## Prompt 5: Como Testear Board

### Modelo/Herramienta
**Nombre:** Claude 3.5 Sonnet (claude.ai)  
**Versión:** claude-sonnet-3-5-20240620  
**Fecha:** 27/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
board es la clase mas compleja, tiene muchos metodos

- inicialización con fichas en posiciones iniciales
- mover_ficha() con captura
- puede_mover_a_punto() con validaciones
- reingresar_desde_barra()
- sacar_ficha_del_tablero() (bear off)
- puede_sacar_fichas()

por donde empiezo? que cosas importantes testear?
```

### Respuesta Completa de la IA
```
Board es complejo, te recomiendo este orden:

**1. Tests de inicialización:**
```python
def test_tablero_inicializa_26_puntos(self):
    """Debe tener 26 puntos (0-25)."""
    # Verificar que existen 26 puntos
    
def test_fichas_blancas_posicion_inicial(self):
    """Fichas blancas en puntos correctos."""
    # Verificar punto 24: 2 fichas
    # Verificar punto 13: 5 fichas
    # etc.

def test_fichas_negras_posicion_inicial(self):
    """Fichas negras en puntos correctos."""
    # Similar para negras
```

**2. Tests de validación (puede_mover_a_punto):**
```python
def test_puede_mover_a_punto_vacio(self):
    """Punto vacío siempre se puede."""
    
def test_puede_mover_mismo_color(self):
    """Mismo color siempre se puede."""
    
def test_puede_capturar_1_ficha(self):
    """1 ficha enemiga se puede capturar."""
    
def test_no_puede_mover_2_fichas_enemigas(self):
    """2+ fichas enemigas bloquean."""
```

**3. Tests de movimiento:**
```python
def test_mover_ficha_simple(self):
    """Mover de punto A a punto B."""
    
def test_mover_con_captura(self):
    """Mover y capturar ficha enemiga."""
    # Verificar que ficha va a barra
```

**4. Tests de barra:**
```python
def test_reingresar_desde_barra(self):
    """Reingresar ficha desde barra."""
```

**5. Tests de bear off:**
```python
def test_puede_sacar_cuando_todas_en_home(self):
    """Bear off válido."""
    
def test_no_puede_sacar_con_fichas_afuera(self):
    """Bear off inválido."""
```

Empieza por inicialización (lo más simple) y ve avanzando. Cada grupo de tests debería darte ~15-20% de cobertura.
```

### Estado de Uso
- [X] Usada sin cambios

### Modificaciones Realizadas
Ninguna, seguí esta estructura exactamente.

### Archivos Finales Afectados
- tests/test_board.py

---

## Prompt 6: Tests para Excepciones

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 29/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
tengo 8 excepciones personalizadas que heredan de BackgammonError

como las testeo? q cosas verificar?
```

### Respuesta Completa de la IA
```
Para testear excepciones necesitas verificar:
1. Se pueden instanciar
2. Tienen el mensaje correcto
3. Heredan de la clase base
4. Se pueden capturar correctamente

Ejemplo:

```python
import unittest
from core.exceptions import (
    BackgammonError,
    MovimientoInvalidoError,
    PuntoInvalidoError
)

class TestExceptions(unittest.TestCase):
    
    def test_backgammon_error_creacion(self):
        """BackgammonError se puede crear."""
        error = BackgammonError("mensaje test")
        self.assertEqual(str(error), "mensaje test")
    
    def test_backgammon_error_mensaje_default(self):
        """Mensaje por defecto."""
        error = BackgammonError()
        self.assertIn("Backgammon", str(error))
    
    def test_movimiento_invalido_hereda_base(self):
        """MovimientoInvalidoError hereda de BackgammonError."""
        self.assertTrue(
            issubclass(MovimientoInvalidoError, BackgammonError)
        )
    
    def test_movimiento_invalido_se_puede_capturar(self):
        """Se puede capturar con except."""
        with self.assertRaises(MovimientoInvalidoError):
            raise MovimientoInvalidoError()
    
    def test_captura_polimorfica(self):
        """Se puede capturar con la clase base."""
        with self.assertRaises(BackgammonError):
            raise MovimientoInvalidoError()
```

Repite esto para cada excepción. Son tests simples pero necesarios para cobertura.
```

### Estado de Uso
- [X] Usada sin cambios

### Modificaciones Realizadas
Ninguna, implementé para todas las excepciones.

### Archivos Finales Afectados
- tests/test_exceptions.py

---

## Prompt 7: Mejorar Cobertura - Encontrar Líneas Faltantes

### Modelo/Herramienta
**Nombre:** Claude 3.5 Sonnet (claude.ai)  
**Versión:** claude-sonnet-3-5-20240620  
**Fecha:** 27/09/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
ejecute coverage report -m y me dice que me faltan estas lineas en checker.py:

linea 39: return False  (en else de esta_en_barra)
linea 62: return False  (en else de esta_sacada)

como cubro esas lineas?
```

### Respuesta Completa de la IA
```
Esas líneas son las ramas `else` que no has cubierto. Necesitas tests que ejecuten esos caminos:

**Para línea 39 (else de esta_en_barra):**
```python
def test_esta_en_barra_false_cuando_posicion_diferente(self):
    """Debe devolver False cuando posición no es 0."""
    self.ficha.set_posicion(5)   # Cualquier posición != 0
    self.assertFalse(self.ficha.esta_en_barra())
    
    self.ficha.set_posicion(25)  # Incluso posición 25
    self.assertFalse(self.ficha.esta_en_barra())
```

**Para línea 62 (else de esta_sacada):**
```python
def test_esta_sacada_false_cuando_posicion_diferente(self):
    """Debe devolver False cuando posición no es 25."""
    self.ficha.set_posicion(0)   # Posición 0
    self.assertFalse(self.ficha.esta_sacada())
    
    self.ficha.set_posicion(10)  # Posición normal
    self.assertFalse(self.ficha.esta_sacada())
```

La clave es que necesitas tests que hagan que el `if` sea False, así entra al `else`.

Ejecuta `coverage report -m` después de agregar estos tests y las líneas deberían estar cubiertas.
```

### Estado de Uso
- [X] Usada sin cambios

### Modificaciones Realizadas
Ninguna, funcionó perfectamente.

### Archivos Finales Afectados
- tests/test_checker.py (agregados tests específicos)

---

## Prompt 8: Tests para CLI

### Modelo/Herramienta
**Nombre:** ChatGPT 4  
**Versión:** GPT-4  
**Fecha:** 25/10/2024

### Instrucciones del Sistema
Ninguna

### Prompt Exacto
```
tengo que testear mi CLI que usa input() del usuario

como mockeo input() para simular comandos?
```

### Respuesta Completa de la IA
```
Para mockear `input()` en tests, usa `unittest.mock.patch`:

```python
import unittest
from unittest.mock import patch
from cli.cli import CLI  # Tu clase CLI

class TestCLI(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['tirar', 'salir'])
    def test_comando_tirar(self, mock_input):
        """Test comando tirar dados."""
        # Tu test aquí
        # input() devolverá 'tirar' la primera vez
        # y 'salir' la segunda vez
    
    @patch('builtins.input', return_value='mover 24 3')
    def test_comando_mover(self, mock_input):
        """Test comando mover."""
        # input() siempre devolverá 'mover 24 3'
```

**Opciones:**
- `side_effect=[...]` - Lista de valores sucesivos
- `return_value='...'` - Valor único

También puedes mockear `print()` para verificar output:

```python
@patch('builtins.print')
def test_mensaje_victoria(self, mock_print):
    # Tu código
    mock_print.assert_called_with('¡Ganaste!')
```
```

### Estado de Uso
- [X] Usada con modificaciones

### Modificaciones Realizadas
- Adapté a mi estructura específica de CLI
- Agregué más tests de comandos
- Agregué tests de validación de input

### Archivos Finales Afectados
- tests/test_cli.py

---

## Resumen de Cobertura Final

### Comandos Usados
```bash
# Ejecutar tests
python -m unittest discover

# Con verbosidad
python -m unittest discover -v

# Con cobertura
coverage run -m unittest discover

# Ver reporte
coverage report

# Ver líneas faltantes
coverage report -m

# Generar HTML
coverage html
```



---

## Técnicas Aprendidas

### 1. Mocking de Random
```python
original = random.randint
random.randint = lambda a, b: 3
try:
    # test
finally:
    random.randint = original
```

### 2. setUp() para Fixtures
```python
def setUp(self):
    """Crear objetos fresh antes de cada test."""
    self.objeto = MiClase()
```

### 3. Assertions Comunes
- `assertEqual(a, b)` - Igualdad
- `assertTrue(x)` - Booleano True
- `assertFalse(x)` - Booleano False
- `assertIsNone(x)` - None
- `assertIn(x, lista)` - Contención

### 4. Coverage Report
- `-m` muestra líneas faltantes
- Enfocarme en ramas (if/else)
- Casos límite son importantes

---

## Lecciones Aprendidas

1. **Empezar por lo simple:** Checker, Dice, Player primero
2. **Mocking es esencial:** Random, input(), etc.
3. **Coverage guía el proceso:** Ver qué falta y agregar tests específicos
4. **Docstrings en tests:** Ayudan a entender qué se prueba
5. **setUp es tu amigo:** Evita repetir código de inicialización

---

**Última actualización:** 01/11/2024