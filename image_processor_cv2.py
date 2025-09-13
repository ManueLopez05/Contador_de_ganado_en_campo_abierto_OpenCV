import cv2
import numpy as np


def procesar_imagen(image_path):
    original_image = cv2.imread(image_path)

    image_in_hsv = cv2.cvtColor(original_image,cv2.COLOR_RGB2HSV)
    limiteInferior = np.array([20,50,50], np.uint8)
    limiteSuperior = np.array([65,255,255], np.uint8)

    mascara = cv2.inRange(image_in_hsv,limiteInferior,limiteSuperior)
    mascaraNot = cv2.bitwise_not(mascara)

    return mascaraNot

def count_contours():
    pass

