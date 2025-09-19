import cv2
import numpy as np


def obtener_imagen_y_mascara_binarizada(image_path):

    imagen_original = cv2.imread(image_path)

    limiteInferior = np.array([20,50,50], np.uint8)
    limiteSuperior = np.array([65,255,255], np.uint8)

    imagen_en_hsv = cv2.cvtColor(imagen_original,cv2.COLOR_BGR2HSV)

    mascara = cv2.inRange(imagen_en_hsv,limiteInferior,limiteSuperior)
    mascara_binarizada = cv2.bitwise_not(mascara)

    return imagen_original, mascara_binarizada


def _dibujar_contorno(imagen,numero_vacas,controno):

    x,y,w,h = cv2.boundingRect(controno)
    cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(imagen  ,str(numero_vacas),(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,200,0),2)



def contar_contornos(imagen_original,imagen_binarizada, densidad_de_pixeles):


    contornos_encontrados,_ = cv2.findContours(imagen_binarizada,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cabezas_de_ganado = 0
    for contorno in contornos_encontrados:
        area = cv2.contourArea(contorno)
        if(area > densidad_de_pixeles):
            cabezas_de_ganado = cabezas_de_ganado +1
            _dibujar_contorno(imagen_original,cabezas_de_ganado,contorno)

    return cabezas_de_ganado, imagen_original
