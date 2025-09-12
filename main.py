import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import imutils

#Funciones

def seleccion_imagen():
    image_path = filedialog.askopenfilename(filetypes = [
        ("image", ".jpg"),
        ("iamge", ".jpeg"),
        ("image", ".png")])
    
    if len(image_path) > 0:
        global image
        image = cv2.imread(image_path)
        image = imutils.resize(image,height=380)

        #Mostramos la imagen en la ventana
        imageToShow = imutils.resize(image,width=400)
        imageToShow = cv2.cvtColor(imageToShow,cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        labelImagenEntrada.configure(image=img)
        labelImagenEntrada.image = img

        
        labelInfo = Label(mainWindow,text="Imagen Seleccionada")
        labelInfo.grid(column=0, row=1, padx=5)

        #Limpiamos imagen de salida
        labelImagenSalida.image = ""

def contar_vacas():
    global image
    imageToShowOutput = cv2.resize(image,(700,500),interpolation=cv2.INTER_AREA)
    imageToShowOutput = cv2.cvtColor(imageToShowOutput, cv2.COLOR_BGR2RGB)

    
    imagehsv = cv2.cvtColor(imageToShowOutput,cv2.COLOR_RGB2HSV)

    
    limiteInferior = np.array([20,50,50], np.uint8)
    limiteSuperior = np.array([65,255,255], np.uint8)

    mascara = cv2.inRange(imagehsv,limiteInferior,limiteSuperior)
    mascaraNot = cv2.bitwise_not(mascara)
    contorno,_ = cv2.findContours(mascaraNot,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    contador = 0
    for i in contorno:
        area = cv2.contourArea(i)
        if(area > sliderToleracia.get()):
            contador = contador +1 
            x,y,w,h = cv2.boundingRect(i)
            cv2.rectangle(imageToShowOutput,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(imageToShowOutput,str(contador),(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,200,0),2)

    cv2.putText(imageToShowOutput,str(contador),(600,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,230,206),5)

    #Mostramos resultado
    im = Image.fromarray(imageToShowOutput)
    img = ImageTk.PhotoImage(image=im)
    labelImagenSalida.configure(image=img)
    labelImagenSalida.image = img

    labelInfo = Label(mainWindow,text=f"Cantidad de vacas = {contador}")
    labelInfo.grid(column=1,row=0,padx=5,pady=5)

#Ventana principal
mainWindow = Tk()

mainWindow.geometry("1280x720")
mainWindow.resizable(0,0)

#Contenedor de la imagen original
labelImagenEntrada = Label(mainWindow)
labelImagenEntrada.grid(column=0,row=2,padx=50)

#Seleccinar densidad de pixeles para contornos
sliderToleracia = Scale(mainWindow, from_=50, to=300, orient=HORIZONTAL)
sliderToleracia.grid(column=0, row=5,padx=5)

labelSlider = Label(mainWindow, text="Selecciona la densidad de pixeles")
labelSlider.grid(column=0, row=4,padx=5)

#Imagen con conteo
labelImagenSalida = Label(mainWindow)
labelImagenSalida.grid(column=1,row=1, rowspan=6)


btn = Button(mainWindow, text="Seleccionar imagen", width=25, command=seleccion_imagen)
btn.grid(column=0, row=0,padx=5,pady=5)


btnConteo = Button(mainWindow, text="Contar Vacas", width=25, command=contar_vacas)
btnConteo.grid(column=0, row=3,padx=5,pady=10)


mainWindow.mainloop()