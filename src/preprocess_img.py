import cv2
import numpy as np


def preprocess(array):
    """
    Preprocesa una imagen para que sea adecuada para la prediccion.

    Args:
        array (numpy.ndarray): Imagen en formato numpy.

    Returns:
        numpy.ndarray: Imagen preprocesada lista para la predición.
    """
    array = cv2.resize(array, (512, 512))
    array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    array = clahe.apply(array)
    array = array / 255
    array = np.expand_dims(array, axis=-1)
    array = np.expand_dims(array, axis=0)

    print("Hola, preprocess_img.py")
    return array
