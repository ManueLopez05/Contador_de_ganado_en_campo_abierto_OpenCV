import tkinter as tk
from tkinter import ttk, filedialog
from image_processor_cv2 import contar_contornos, obtener_imagen_y_mascara_binarizada

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
        self.labelImagenEntrada = ttk.Label(self.root)
        self.labelImagenEntrada.grid(column=0,row=2,padx=50)

        #Seleccinar densidad de pixeles para contornos
        self.sliderToleracia = ttk.Scale(self.root, from_=50, to=300, orient="horizontal")
        self.sliderToleracia.grid(column=0, row=5,padx=5)

        labelSlider = ttk.Label(self.root, text="Selecciona la densidad de pixeles")
        labelSlider.grid(column=0, row=4,padx=5)

        #Imagen con conteo
        self.labelImagenSalida = ttk.Label(self.root)
        self.labelImagenSalida.grid(column=1,row=1, rowspan=6)


        btn = ttk.Button(self.root, text="Seleccionar imagen", width=25, command=self._get_image_path)
        btn.grid(column=0, row=0,padx=5,pady=5)


        btnConteo = ttk.Button(self.root, text="Contar Vacas", width=25, command=self._count_cows)
        btnConteo.grid(column=0, row=3,padx=5,pady=10)

    def _get_image_path(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[
                ("image", ".jpg"),
                ("iamge", ".jpeg"),
                ("image", ".png")
            ]
        )
        print(str(type(self.image_path))+" - "+self.image_path + "modulo gui.py método _get_path()")


    def _count_cows(self):
        imagen, mascara_binarizada, self.imgaen_vista_previa = obtener_imagen_y_mascara_binarizada(self.image_path)

        self.cabezas_de_ganado, self.imagen_con_conteo = contar_contornos(imagen,mascara_binarizada,self.sliderToleracia.get())
        self._mostrar_imagenes()

    def _mostrar_imagenes(self):
        self.labelImagenEntrada.configure(image=self.imgaen_vista_previa)
        self.labelImagenSalida.configure(image=self.imagen_con_conteo)
        labelInfo = ttk.Label(self.root,text=f"Cantidad de vacas = {self.cabezas_de_ganado}")
        labelInfo.grid(column=1,row=0,padx=5,pady=5)
    
def run_app():
    root = tk.Tk()
    app = App(root)
    root.mainloop()