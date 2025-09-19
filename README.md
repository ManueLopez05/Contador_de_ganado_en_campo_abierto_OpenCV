# Contador de ganado bovino

Software ideado para contar cabezas de ganado mediante fotografías aéreas tomadas por un dron.

## Contexto

Software creado durante el curso de Visión Artificial de la carrera Ingeniería Mecatrónica Agrícola en la Universidad Autónoma Chapingo por un equipo de trabajo de tres personas:

- Victoria Gallegos
- Manuel Bautista
- Manuel López

## Nota
- Por el momento la idea es refactorizar el código pero sin cambiar nada de la funcionalidad base, simplemente escribir lo mismo pero con mejores prácticas de programación.

- La intención es realizar todas las modificaciones sin recurrir a la ayuda de la IA, mas allá de preguntas sobre funcionalidades de las librerías utilizadas, de las que no me acuerde, o sugerencias esporádicas en caso de que me quede atacascado en un problema.

### Módulo gui.py
Genera una copia exacta de la interfaz creada en el archivo main.py pero usando **ttk** en vez de tk para crear los widgets, hasta ahora simplemente construye la GUI pero no tiene funcionalidad.

## Novedades de desarrollo

### Viernes 19 de septiembre
**Primera entrada**
Respecto a la modularización del código, la idea principal era tener tres archivos: main.py, gui.py y image_processor.py. La cuestión es que para poder mostrar las imágenes en la interfaz creada por Tkinter se necesita un formato compatible, por lo que se deber hacer uso de la librería **PIL**, lo que complicó un poco la realización de la visión que se tenía la principio de como organizar el código.

Los últimos commits hechos realmente eran el intento de crear módulos funcionales, sin embargo, la implementación de **PIL** complicó las cosas mas de lo que debería, ya que estoy empeñado en dejar **gui.py** únicamente para construir la interfaz gráfica y no para procesar imágenes.

Por sugerencia de la IA Qwen crearé un módulo adicional llamado **utils.py** en el cuál dejar funciones para conversión de imágenes entre **PIL** y **OpenCV**. Bien.... ¡pues vamos a hacerlo!
