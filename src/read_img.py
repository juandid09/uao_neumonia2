import pydicom as dicom
import cv2
from PIL import Image
import numpy as np


def read_dicom_file(path):
    """
    Lee un archivo DICOM y devuelve la imagen procesada.

    Args:
        path (str): Ruta del archivo DICOM.

    Returns:
        tuple: Una tupla con dos elementos:
            - img_rgb (numpy.ndarray): Imagn DICOM en formato RGB.
            - img2show (PIL.Image): Imagen en formato PIL para visualización.
    """
    img = dicom.read_file(path)
    img_array = img.pixel_array
    img2show = Image.fromarray(img_array)

    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    img_rgb = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)

    print("Hola, read_img.py 1")
    return img_rgb, img2show


def read_jpg_file(path):
    """
    Lee un archivo JPG y devuelve la imagen procesada.

    Args:
        path (str): Ruta del archivo JPG.

    Returns:
        tuple: Una tupla con dos elementos:
            - img2 (numpy.ndarray): Imagen JPG procesada.
            - img2show (PIL.Image): Imagen en formato PIL para visualización.
    """
    img = cv2.imread(path)
    img_array = np.asarray(img)
    img2show = Image.fromarray(img_array)

    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)

    return img2, img2show
