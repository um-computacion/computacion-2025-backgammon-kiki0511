# Backgammon - Proyecto Computación 2025

Implementación completa del juego de Backgammon en Python con interfaz de línea de comandos (CLI) y interfaz gráfica (Pygame).

---

##  Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
  - [Modo CLI](#modo-cli)
  - [Modo Pygame](#modo-pygame)
- [Tests](#tests)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías](#tecnologías)
- [Documentación Adicional](#documentación-adicional)
- [Autor](#autor)

---

##  Descripción

Este proyecto implementa el juego clásico de Backgammon siguiendo las reglas tradicionales. El diseño separa completamente la lógica de negocio (módulo `core/`) de las interfaces de usuario (CLI y Pygame), permitiendo mantener, testear y extender el código fácilmente.

El proyecto fue desarrollado como parte de la materia Computación 2025 en la Universidad de Mendoza, aplicando principios SOLID y buenas prácticas de desarrollo orientado a objetos.

###  Objetivo

Desarrollar un juego de Backgammon completo y funcional que demuestre:
- Aplicación correcta del paradigma orientado a objetos
- Separación de responsabilidades
- Testing exhaustivo (cobertura ≥90%)
- Código limpio y bien documentado
- Múltiples interfaces de usuario

---

##  Características

### Reglas Completas de Backgammon
-  Tablero con 24 puntos
-  15 fichas por jugador
-  Movimiento según dados (1-6)
-  Tiradas dobles (4 movimientos)
-  Captura de fichas
-  Barra (fichas capturadas deben reingresar)
-  Bear off (sacar fichas del tablero)
-  Detección de victoria
-  Validación completa de movimientos según reglas oficiales

### Dos Modos de Juego
-  **CLI:** Interfaz de texto en consola (modo comando)
-  **Pygame:** Interfaz gráfica interactiva con mouse y teclado

### Arquitectura Limpia
-  Separación total core/UI
-  Principios SOLID aplicados
-  Cobertura de tests ≥90%
-  Código completamente documentado con docstrings
-  Excepciones específicas para cada tipo de error

---

## 📦 Requisitos

### Requisitos del Sistema
- **Python:** 3.8 o superior
- **pip:** Gestor de paquetes de Python
- **Sistema operativo:** Windows, Linux, o macOS

### Dependencias Python
Las principales dependencias del proyecto son:

```
pygame>=2.0.0
coverage>=6.0
```

Ver archivo `requirements.txt` para lista completa de dependencias.

---

## 🚀 Instalación

### Paso 1: Clonar el Repositorio

```bash
git clone <https://github.com/um-computacion/computacion-2025-backgammon-kiki0511.git>
cd backgammon
```

### Paso 2: Crear Entorno Virtual (Recomendado)


**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Verificar Instalación

```bash
python -m unittest discover
```

Si todos los tests pasan, ¡la instalación fue exitosa! 

---

## Uso

### Modo CLI

El modo CLI permite jugar Backgammon directamente desde la terminal.

**Iniciar el juego:**

```bash
python -m main
```

**Comandos disponibles:**

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `tirar` | Tirar los dados | `tirar` |
| `mover <origen> <dado>` | Mover ficha del punto origen usando valor del dado | `mover 24 3` |
| `reingresar <dado>` | Reingresar ficha desde la barra | `reingresar 2` |
| `sacar <origen> <dado>` | Sacar ficha del tablero (bear off) | `sacar 6 4` |
| `pasar` | Pasar el turno | `pasar` |
| `estado` | Mostrar estado del juego | `estado` |
| `ayuda` | Mostrar comandos disponibles | `ayuda` |
| `salir` | Salir del juego | `salir` |

**Ejemplo de partida:**

```
=== BACKGAMMON ===
Turno de: Jugador 1 (Blanco)

Tablero actual:
[Visualización ASCII del tablero]

> tirar
 Dados: [3, 5]
Movimientos disponibles: [3, 5]

> mover 24 3
 Ficha movida de punto 24 a punto 21

> mover 13 5
 Ficha movida de punto 13 a punto 8

Turno completado. Cambiando de jugador...
```

**Notas importantes:**
- Los puntos van del 1 al 24
- El punto 0 es la barra (fichas capturadas)
- El punto 25 es donde van las fichas sacadas
- Debes usar todos los dados disponibles antes de pasar turno
- Si tienes fichas en la barra, debes reingresarlas primero

---

### Modo Pygame

El modo Pygame ofrece una interfaz gráfica completa e interactiva.

**Iniciar el juego:**

```bash
python -m pygame_ui 
```

**Controles:**

| Control | Acción |
|---------|--------|
| **Click izquierdo** | Seleccionar ficha |
| **Click en destino** | Mover ficha seleccionada |
| **Botón "Tirar Dados"** | Tirar los dados |
| **Botón "Pasar Turno"** | Pasar el turno |
| **ESC** | Salir del juego |



**Instrucciones de juego:**
1. Presiona "Tirar Dados" al inicio de tu turno
2. Click en una ficha que quieras mover
3. Click en el punto destino
4. Repite hasta usar todos los dados
5. Presiona "Pasar Turno" cuando termines

---

##  Tests

El proyecto mantiene una cobertura de tests ≥90% en el módulo `core/`.

### Ejecutar Todos los Tests

```bash
python3 -m unittest 
```


### Ejecutar Test Específico

```bash
# Test de una clase específica
python -m unittest tests.test_checker

# Test de un método específico
python -m unittest tests.test_checker.TestChecker.test_crear_ficha_blanca
```

### Análisis de Cobertura

**Ver reporte en terminal:**
```bash
python3 -m coverage report  
```

**Generar reporte HTML:**
```bash
coverage html
```


### Cobertura por Archivo

| Archivo | Cobertura | Tests |
|---------|-----------|-------|
| `checker.py` | 100% | test_checker.py |
| `dice.py` | 100% | test_dice.py |
| `player.py` | 100% | test_player.py |
| `board.py` | 98.84% | test_board.py |
| `game.py` | 99.22%% | test_game.py |
| `exceptions.py` | 100% | test_exceptions.py |
| `cli.py` | 100% | test_cli.py |

**Total módulo core/:** ≥90% 

---

##  Estructura del Proyecto

```
backgammon/
│
├── core/                          # Lógica del juego (core)
│   ├── __init__.py
│   ├── board.py                   # Tablero de juego
│   ├── checker.py                 # Ficha individual
│   ├── dice.py                    # Dados
│   ├── exceptions.py              # Excepciones personalizadas
│   ├── game.py                    # Coordinador principal (BackgammonGame)
│   └── player.py                  # Jugador
│
├── cli/                           # Interfaz de línea de comandos
│   ├── __init__.py
│   └── cli.py                     # CLI principal
│
├── pygame_ui.py                   # Interfaz gráfica
│                                  # UI con Pygame
│
├── tests/                         # Tests unitarios
│   ├── __init__.py
│   ├── test_board.py              # Tests de Board
│   ├── test_checker.py            # Tests de Checker
│   ├── test_cli.py                # Tests de CLI
│   ├── test_dice.py               # Tests de Dice
│   ├── test_exceptions.py         # Tests de Excepciones
│   ├── test_game.py               # Tests de BackgammonGame
│   └── test_player.py             # Tests de Player
│
├── requirements.txt               # Dependencias Python
├── README.md                      # Este archivo
├── CHANGELOG.md                   # Historial de cambios
├── JUSTIFICACION.md               # Justificación técnica del diseño
├── prompts-desarrollo.md          # Prompts de IA (desarrollo)
├── prompts-testing.md             # Prompts de IA (testing)
└── prompts-documentacion.md       # Prompts de IA (documentación)
```

---

## Tecnologías

### Lenguajes y Frameworks
- **Python 3.8+** - Lenguaje principal
- **Pygame** - Interfaz gráfica
- **unittest** - Framework de testing

### Herramientas de Desarrollo
- **coverage** - Análisis de cobertura de tests
- **Git** - Control de versiones

### Principios y Patrones
- **SOLID** - Principios de diseño orientado a objetos
- **Separación de responsabilidades** - Core independiente de UI
- **Excepciones específicas** - Manejo de errores robusto
- **Testing exhaustivo** - TDD y cobertura ≥90%

---

## Documentación Adicional

### Archivos de Documentación

- **[CHANGELOG.md](CHANGELOG.md)** - Historial completo de cambios del proyecto
- **[JUSTIFICACION.md](JUSTIFICACION.md)** - Análisis técnico detallado:
  - Justificación de clases y atributos
  - Decisiones de diseño
  - Análisis de cumplimiento de SOLID
  - Estrategias de testing
  - Diagramas UML

- **Archivos de prompts de IA:**
  - [prompts-desarrollo.md](prompts-desarrollo.md) - Prompts usados en código
  - [prompts-testing.md](prompts-testing.md) - Prompts usados en tests
  - [prompts-documentacion.md](prompts-documentacion.md) - Prompts usados en docs

### Referencias Externas

- [Reglas de Backgammon (Wikipedia)](https://es.wikipedia.org/wiki/Backgammon)
- [Jugar Backgammon online](https://www.ludoteka.com/clasika/backgammon-es.html)
- [Documentación de Pygame](https://www.pygame.org/docs/)
- [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
- [Principios SOLID](https://en.wikipedia.org/wiki/SOLID)
- [Python docstrings](https://realpython.com/documenting-python-code/)

---

##  Contexto Académico

### Materia
- **Nombre:** Computación 1  
- **Universidad:** Universidad de Mendoza
- **Año:** 2025


### Requisitos Cumplidos
-  Separación core/UI completa
-  Principios SOLID aplicados
-  Cobertura de tests ≥90%
-  Formato de atributos `__nombre__`
-  Docstrings en todo el código
-  CLI funcional
-  Pygame funcional
-  Sistema de excepciones robusto
-  CHANGELOG.md actualizado
-  JUSTIFICACION.md completa
-  Documentación de prompts de IA

---

## Autor

**Joaquin Tejada Pareja**

- **Universidad:** Universidad de Mendoza
- **Materia:** Computación 1
- **Año:** 2025

---

##  Licencia

Este proyecto fue desarrollado con fines educativos para la materia Computación 2025 de la Universidad de Mendoza.

---

##  Contribuciones

Este es un proyecto académico individual. No se aceptan contribuciones externas.

---


##  Estado del Proyecto

**Versión actual:** 0.4.8  
**Estado:** Completo y funcional  
**Última actualización:** Noviembre 2025

### Funcionalidades Implementadas
-  Lógica completa del juego
-  Interfaz CLI
-  Interfaz Pygame
-  Tests exhaustivos
-  Documentación completa

---

**¡Disfrutá el juego!** 

---

## Tips para Jugar

### Para Principiantes
1. **Objetivo:** Sacar las 15 fichas del tablero antes que tu oponente
2. **Movimiento:** Las fichas se mueven según los valores de los dados
3. **Captura:** Si caes en un punto con una sola ficha enemiga, la capturas
4. **Barra:** Fichas capturadas van a la barra y deben reingresar
5. **Bear off:** Solo puedes sacar fichas cuando todas estén en tu cuadrante final (puntos 1-6)

### Estrategias Básicas
-  Intenta controlar puntos clave (especialmente el punto 5 y 7)
-  Mantén dos o más fichas juntas para protegerlas
-  Mueve fichas de la barra lo antes posible
-  Usa tiradas dobles estratégicamente
-  Agrupa fichas en tu cuadrante final para bear off rápido

---

