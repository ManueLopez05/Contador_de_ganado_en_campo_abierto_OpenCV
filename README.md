# Contador de ganado bovino

Software ideado para contar cabezas de ganado mediante fotografías aéreas tomadas por un dron.

## Contexto  🚀

Software creado durante el curso de Visión Artificial de la carrera Ingeniería Mecatrónica Agrícola en la Universidad Autónoma Chapingo por un equipo de trabajo de tres personas:

- Victoria Gallegos
- Manuel Bautista
- Manuel López

El progrma consta de una interfaz gráfica que en la que se cargan las imágenes y con un simple botón se realiza el conteo del ganado, sin embargo, este conteo se hace mediante meras técnicas de acondicionamiento de la imagen en cuestión, no se usa ningún modelo de IA para hacerlo ya que esa fue la instrucción para esta tarea en específico.

Por lo que se partió de una diea principal para construir la lógica de la aplicación:

- Las imágenes tienen que ser aéreas y hechas sobre pastisales verdes, o dicho de otra forma, se tiene que tener una fotografía complemtanete verde con puntos café, negros o blancos los cuáles representant al ganado, de manera ideal.

## Nota 📑
- Por el momento la idea es refactorizar el código pero sin cambiar nada de la funcionalidad base, simplemente escribir lo mismo pero con mejores prácticas de programación.

- La intención es realizar todas las modificaciones sin recurrir a la ayuda de la IA, mas allá de preguntas sobre funcionalidades de las librerías utilizadas, de las que no me acuerde, o sugerencias esporádicas en caso de que me quede atacascado en un problema.

### Módulo gui.py
Genera una copia exacta de la interfaz creada en el archivo main.py pero usando **ttk** en vez de tk para crear los widgets, hasta ahora simplemente construye la GUI pero no tiene funcionalidad.

## Novedades de desarrollo

### Viernes 19 de septiembre 📑
**Primera entrada 📋**  
Respecto a la modularización del código, la idea principal era tener tres archivos: main.py, gui.py y image_processor.py. La cuestión es que para poder mostrar las imágenes en la interfaz creada por Tkinter se necesita un formato compatible, por lo que se deber hacer uso de la librería **PIL**, lo que complicó un poco la realización de la visión que se tenía la principio de como organizar el código.

Los últimos commits hechos realmente eran el intento de crear módulos funcionales, sin embargo, la implementación de **PIL** complicó las cosas mas de lo que debería, ya que estoy empeñado en dejar **gui.py** únicamente para construir la interfaz gráfica y no para procesar imágenes.

Por sugerencia de la IA Qwen crearé un módulo adicional llamado **utils.py** en el cuál dejar funciones para conversión de imágenes entre **PIL** y **OpenCV**. Bien.... ¡pues vamos a hacerlo!

**Segunda entrada 📋**  
Bien, fianlmente se creó el módulo **utils.py** que tiene dentro dos funciones `ajustar_imagen_cv2()` retorna una imagen de OpenCV cambiando el formato de color de BGR (Usado por defecto en OpenCV) a RGB y modificando el tamaño a uno nuevo especificado. Luego está la función `cv2_a_imagenTk` que transforma la imagen retornada por la función anterior en el formato adecuado para mostrar en una interfaz de Tkinter, para luego ser retornada.

Con esta solución se tiene la necesidad de primero usar la función `ajustar_imagen_cv2()` y luego `cv2_a_imagenTk` dentro del módulo gui.py de lo contrario se mostrará una imagen con un color extraño y con dimensiones desproporcionadas. 

Ciertamente tengo dudas sobre si está bien dejar esto así o simplemente tener todo en una sola función, la idea de hacer dos es por el principio de responsabilidad única, sin embargo, se que pretender modularizar todo tampoco es conveniente.

Respecto a al módulo **image_processor.py** se eliminó toda funcionalidades que concierne a modifiacar las imgánes, funcionalidades que  se movieron a el módulo **utils.py**, de esta forma ahora solo se encuentra lo relacionado a procesar la imagen para realizar el conteo del ganado usando la librería **OpenCV**.

Por el momento estos módulos, así como **gui.py** no se encuentran integrados para funcionar como una unidad, todavía hay que hacer modificaciones en en este útimo para que el programa funcione correctamente.