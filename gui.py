import tkinter as tk
from tkinter import ttk, filedialog

class App:

    def __init__(self,root):
        self.root = root
        self.root.title("Contador de ganado")
        self.root.geometry("1280x720")
        self.root.resizable(0,0)

        #Configuración global
        self._setup_styles()
        self._create_widgets()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

    def _create_widgets(self):
        #Contenedor de la imagen original
        labelImagenEntrada = ttk.Label(self.root)
        labelImagenEntrada.grid(column=0,row=2,padx=50)

        #Seleccinar densidad de pixeles para contornos
        sliderToleracia = ttk.Scale(self.root, from_=50, to=300, orient="horizontal")
        sliderToleracia.grid(column=0, row=5,padx=5)

        labelSlider = ttk.Label(self.root, text="Selecciona la densidad de pixeles")
        labelSlider.grid(column=0, row=4,padx=5)

        #Imagen con conteo
        labelImagenSalida = ttk.Label(self.root)
        labelImagenSalida.grid(column=1,row=1, rowspan=6)


        btn = ttk.Button(self.root, text="Seleccionar imagen", width=25, command=self._get_image_path)
        btn.grid(column=0, row=0,padx=5,pady=5)


        btnConteo = ttk.Button(self.root, text="Contar Vacas", width=25, command=self._count_cows)
        btnConteo.grid(column=0, row=3,padx=5,pady=10)

    def _get_image_path(self):
        pass

    def _count_cows(self):
        pass

def run_app():
    root = tk.Tk()
    app = App(root)
    root.mainloop()