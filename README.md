# Contador de ganado bovino

Software ideado para contar cabezas de ganado mediante fotografías aéreas tomadas por un dron.

## Contexto

Software creado durante el curso de Visión Artificial de la carrera Ingeniería Mecatrónica Agrícola en la Universidad Autónoma Chapingo por un equipo de trabajo de tres personas:

- Victoria Gallegos
- Manuel Bautista
- Manuel López

## Nota
- Por el momento la idea es refactorizar el código pero sin cambiar nada de la funcionalidad base, simplemente escribir lo mismo pero con mejores prácticas de programación.

- Hasta ahora se crearon dos módulos para separar todo lo relacionado con procesamiento de imágenes con OpenCV y la interfaz gráfica con Tkinter, sin embargo, es trabajo en proceso y realmente no hacen nada todavía, el **programa funcional sigue estando en el archivo main.py**

## Módulo gui.py
Genera una copia exacta de la interfaz creada en el archivo main.py pero usando **ttk** en vez de tk para crear los widgets, hasta ahora simplemente construye la GUI pero no tiene funcionalidad.