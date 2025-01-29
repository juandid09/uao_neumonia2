from read_img import read_dicom_file, read_jpg_file
from preprocess_img import preprocess
from load_model import load_model
from grad_cam import grad_cam
import numpy as np


def process_image(image_path):
    """
    Procesa la imagen y devuelve la clase, la probabilidad y el mapa de calor.

    Args:
        image_path (str): Ruta del archivo de imagen.

    Returns:
        tuple: Una tupla que contiene:
            - label (str): La etiqueta predicha
            - prob (float): La probabilidad de la prediccion
            - heatmap (numpy.ndarray): El mapa de calor, generado por Grad-CAM.
    """
    if image_path.lower().endswith('.dcm'):
        # Si la imagen es DICOM
        img_array, _ = read_dicom_file(image_path)
    else:
        # Si la imagen es JPG/JPEG/PNG
        img_array, _ = read_jpg_file(image_path)
    
    # Preprocesamiento
    processed_img = preprocess(img_array)

    # Cargar el modelo y realizar predicción
    model = load_model()
    prediction = np.argmax(model.predict(processed_img))
    prob = np.max(model.predict(processed_img)) * 100

    # Etiquetas para la predicción
    if prediction == 0:
        label = "Bacteriana"
    elif prediction == 1:
        label = "Normal"
    elif prediction == 2:
        label = "Viral"
    
    # Generar mapa de calor con Grad-CAM
    heatmap = grad_cam(img_array)
    
    print("Hola, integrator")
    return label, prob, heatmap
