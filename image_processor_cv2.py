import cv2
import numpy as np
from PIL import Image
from PIL import ImageTk


def obtener_imagen_y_mascara_binarizada(image_path):

    imagen_original = cv2.imread(image_path)
    imagen_para_tkinter = _convertir_imagen_para_mostrar_en_tk(imagen_original,(400,400))
    image_in_hsv = cv2.cvtColor(imagen_original,cv2.COLOR_BGR2HSV)



    limiteInferior = np.array([20,50,50], np.uint8)
    limiteSuperior = np.array([65,255,255], np.uint8)

    mascara = cv2.inRange(image_in_hsv,limiteInferior,limiteSuperior)
    mascara_binarizada = cv2.bitwise_not(mascara)

    return imagen_original, mascara_binarizada, imagen_para_tkinter


def _dibujar_contorno(imagen,numero_vacas,controno):

    x,y,w,h = cv2.boundingRect(controno)
    cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(imagen  ,str(numero_vacas),(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,200,0),2)



def contar_contornos(imagen,imagen_binarizada,densidad_de_pixeles):

    contornos_encontrados,_ = cv2.findContours(imagen_binarizada,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cabezas_de_ganado = 0
    for contorno in contornos_encontrados:
        area = cv2.contourArea(contorno)
        if(area > densidad_de_pixeles):
            cabezas_de_ganado = cabezas_de_ganado +1 
            _dibujar_contorno(imagen,cabezas_de_ganado,contorno)
    
    imagen_para_tkinter = _convertir_imagen_para_mostrar_en_tk(imagen,(700,500))
    
    return cabezas_de_ganado, imagen_para_tkinter
    

def _convertir_imagen_para_mostrar_en_tk(imagen, size):

    imagen = cv2.resize(imagen,size,interpolation=cv2.INTER_AREA)
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

    imagen_para_tkinter = ImageTk.PhotoImage(image=Image.fromarray(imagen))
    
    return imagen_para_tkinter


