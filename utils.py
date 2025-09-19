import cv2
from PIL import Image, ImageTk


def cv2_a_imagenTk(imagen_cv2):

    imagen_pil = Image.fromarray(imagen_cv2)
    imagen_tk = ImageTk.PhotoImage(image=imagen_pil)

    return imagen_tk


def redimensionar_imagen_cv2(imagen_cv2, size):

   imagen_cv2_redimensionada = cv2.resize(imagen_cv2,size,interpolation=cv2.INTER_AREA)
   imagen_cv2_redimensionada = cv2.cvtColor(imagen_cv2_redimensionada,cv2.COLOR_BGR2RGB)

   return imagen_cv2_redimensionada
