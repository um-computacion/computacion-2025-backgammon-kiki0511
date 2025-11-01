# JUSTIFICACION.md

---

**Universidad de Mendoza – Facultad de Ingeniería**  
**Carrera:** Ingeniería en Informática  
**Materia:** Computación 1
**Proyecto:** Backgammon Computación 2025  
**Autor:** Joaquín Tejada Pareja  
**Fecha de entrega:** 01/11/2025  

---

## 1. Resumen del diseño general

El proyecto **Backgammon Computación 2025** implementa un juego de Backgammon desarrollado en **Python**, cumpliendo con todos los requisitos establecidos por la cátedra.  
El diseño se estructura bajo un enfoque **orientado a objetos (POO)** y sigue estrictamente los principios **SOLID**, promoviendo bajo acoplamiento y alta cohesión.  

La arquitectura se divide en tres capas principales:
1. **Core:** contiene la lógica central del juego (reglas, movimientos, validaciones).  
2. **CLI:** interfaz de línea de comandos obligatoria.  
3. **PygameUI:** interfaz gráfica opcional que utiliza la biblioteca `pygame`.  

Cada módulo es independiente y comunicable a través de clases bien definidas. El núcleo lógico (core) no depende de las interfaces, lo cual garantiza testabilidad y reutilización.

---

## 2. Justificación de las clases elegidas

### 2.1. `Checker`
Representa una **ficha individual**. Su responsabilidad es mantener su color y posición en el tablero.  
No contiene lógica de movimiento; delega esa responsabilidad al `Board` y al `Game`.  
Se eligió una clase separada para las fichas porque permite manipularlas como objetos (no simples enteros), lo que facilita operaciones como capturas, reingresos y bear-off.

**Atributos principales:**
- `__color__`: almacena el color ("blanco" o "negro").  
- `__posicion__`: indica su punto actual (0 = barra, 25 = fuera).  

**Decisión de diseño:** encapsular el color y la posición permite mantener consistencia en todo momento y evitar errores de asignación externa.

---

### 2.2. `Dice`
Encapsula la **lógica de tiradas de dados** del juego.  
Genera los valores aleatorios y gestiona los movimientos disponibles según las reglas (dobles, normales).

**Atributos:**
- `__ultima_tirada__`: guarda la tirada más reciente.

**Justificación:** separar la aleatoriedad en una clase independiente mejora la testabilidad y evita mezclar lógica de juego con generación de números aleatorios.  
Se implementaron todos los métodos sin usar `for` ni `range`, cumpliendo la restricción académica.

---

### 2.3. `Player`
Representa a un **jugador** y administra sus estados: fichas en la barra, fichas sacadas y dirección de movimiento.  
Cada jugador sabe hacia qué lado se mueve y cuántas fichas tiene fuera del tablero.

**Atributos:**
- `__nombre__`: nombre del jugador.  
- `__direccion__`: indica si el jugador avanza de 1 a 24 o viceversa.  
- `__fichas_en_barra__`: cantidad de fichas capturadas.  
- `__fichas_sacadas__`: fichas ya retiradas (bear off).

**Justificación:** esta estructura permite a la clase `Game` consultar el estado de cada jugador sin almacenar lógica redundante.  
Además, facilita la validación de condiciones de victoria.

---

### 2.4. `Board`
Modela el **tablero de Backgammon**, compuesto por 26 puntos (0–25).  
Guarda la distribución de las fichas y valida movimientos según las reglas del juego.

**Atributos:**
- `__puntos__`: lista de listas de fichas (`Checker`) que representan cada punto.

**Justificación de diseño:**
- Mantener la lógica de validación (movimientos válidos, capturas, bloqueos) dentro del `Board` promueve separación de responsabilidades.  
- Cada posición es una lista para poder apilar fichas y acceder a la del tope con facilidad.  

**Métodos clave:**
- `_colocar_fichas_iniciales`: configura la disposición inicial estándar.  
- `puede_mover_a_punto`: valida movimientos siguiendo las reglas de ocupación.  

---

### 2.5. `Game` (BackgammonGame)
Actúa como **coordinador principal** del juego, uniendo tablero, jugadores y dados.  
Controla turnos, verifica condiciones de victoria y aplica movimientos.

**Atributos:**
- `__tablero__`: instancia de `Board`.  
- `__jugador1__` y `__jugador2__`: instancias de `Player`.  
- `__jugador_actual__`: referencia al jugador en turno.  
- `__dados__`: instancia de `Dice`.  
- `__movimientos_disponibles__`: lista de valores de dados no usados.  
- `__juego_terminado__`: indica si alguien ganó.  
- `__ganador__`: guarda al jugador vencedor.  

**Justificación de diseño:**
- Centralizar el flujo de partida simplifica la interfaz (`CLI` y `PygameUI`).  
- La clase sigue el principio de **Responsabilidad Única**: sólo coordina, no ejecuta lógica de validación.  
- Permite ejecutar pruebas unitarias sobre reglas de turno, victoria y consumo de dados.

---

### 2.6. `Exceptions`
Contiene **todas las excepciones personalizadas** del sistema.  
Permite manejar errores semánticos del juego (por ejemplo, movimiento inválido, turno incorrecto, etc.) sin detener la ejecución.

**Ejemplos:**
- `MovimientoInvalidoError`  
- `PuntoInvalidoError`  
- `TurnoIncorrectoError`  
- `BearOffInvalidoError`  

**Justificación:** usar una jerarquía de errores específica mejora la legibilidad y la depuración, además de cumplir el principio **Open/Closed (O de SOLID)**.

---

### 2.7. `CLI`
Interfaz de línea de comandos obligatoria.  
Permite jugar directamente desde la consola, ingresando los movimientos manualmente.

**Justificación:**  
- Es la interfaz base exigida por la cátedra.  
- Sirve como entorno de pruebas para verificar la lógica sin depender de `pygame`.  
- Su implementación respeta el patrón de **separación de capas (MVC)**, conectando la presentación textual con la lógica del juego.

---

### 2.8. `PygameUI`
Interfaz gráfica opcional desarrollada con `pygame`.  
Ofrece una representación visual completa del tablero y las fichas, permitiendo interacciones con el ratón.

**Justificación:**  
- Proporciona una experiencia de usuario más atractiva sin alterar la lógica central.  
- Reutiliza todos los métodos de `Game`, lo que demuestra una arquitectura desacoplada.  

---

## 3. Justificación de atributos

Cada atributo sigue el formato `__nombre__`, obligatorio según el documento oficial, lo que:
- Evita conflictos de nombres.  
- Refuerza el encapsulamiento.  
- Obliga a acceder a los datos mediante getters y setters.  

Todos los atributos se declaran junto a `self`, asegurando coherencia y visibilidad controlada dentro de las clases.

---

## 4. Decisiones de diseño relevantes

1. **Separación Core / Interfaz:** garantiza independencia entre lógica y presentación.  
2. **Evitar bucles `for` o `range`:** se reemplazaron por estructuras `while` en cumplimiento del reglamento.  
3. **Excepciones personalizadas:** para mantener la robustez sin romper el flujo.  
4. **Uso de listas anidadas:** facilita el manejo dinámico de fichas en el tablero.  
5. **Testing modular:** cada clase cuenta con su propio archivo de pruebas en `tests/`.  


---

## 5. Manejo de errores y excepciones

El manejo de errores se centraliza en el módulo `exceptions.py`.  
Cada excepción comunica un tipo específico de error de juego y se usa para informar al usuario sin interrumpir el flujo.  
Esto permite capturar situaciones como:
- Movimiento inválido (`MovimientoInvalidoError`)  
- Intento de sacar ficha fuera de turno (`TurnoIncorrectoError`)  
- Jugador con fichas en la barra que intenta mover otra (`FichaEnBarraError`)  

---

## 6. Estrategia de testing y cobertura

La suite de tests se encuentra en la carpeta `tests/` e incluye más de 90% de cobertura sobre la lógica central (`core`).  
Cada clase posee su propio archivo de prueba (`test_game.py`, `test_board.py`, etc.).  
Las pruebas se ejecutan mediante `unittest` con el comando:
```bash
python3 -m coverage report "
