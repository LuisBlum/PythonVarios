"""
Este programa tiene como finalidad cambiar el tamaño de las imagenes agregadas al directorio img/
    basandose en el ancho deseado ingresado por el usuario. Las imagenes cambiadas se almacenarán
    con el mismo nombre en el directorio img_cambiadas/

Primero se debe almacenar las imágenes en un directorio, por ejemplo C:/img
Crear un directorio donde se almacenarán las nuevas imágenes.
"""
import os
import PIL
from PIL import Image

print("*******************************")
print("Cambiar Pixeles Imagenes")
print("*******************************")
print("\n")

dirOrigen = input("Ingrese el directorio de las imágenes a cambiar: ")
imagenes = os.listdir(f"{dirOrigen}/")
dirDestino = input("Ingrese el directorio donde desea que se almacenen las nuevas imágenes: ")
ancho = int(input("Ingrese el ancho deseado: "))

for i in imagenes:
    img = Image.open(f"{dirOrigen}/{i}")
    porcentaje_ancho = (float(ancho) / float(img.size[0]))
    alto = int((float(img.size[1]) * float(porcentaje_ancho)))
    img = img.resize((ancho, alto), PIL.Image.ANTIALIAS)
    img.save(f"{dirDestino}/{i}")
    print(f"La imagen {i} ha sido cambiada.")

print("\n\n")

salir_pantalla = input("Presione ENTER para salir...")