import os
import sys
import numpy as np
from pathlib import Path
from PIL import Image

# Establecer la ruta del directorio src
src_path = Path(__file__).resolve().parent.parent / "src"
sys.path.append(str(src_path))

from integrator import process_image  # Importamos la función a probar

def test_process_img():
    # Creamos una imagen simulada (por ejemplo, 100x100 con 3 canales)
    test_image_path = "test_image.jpg"
    test_image = np.ones((100, 100, 3), dtype=np.uint8)  # Imagen 100x100 con 3 canales (RGB)

    # Guardamos la imagen como archivo JPG temporal
    img = Image.fromarray(test_image)
    img.save(test_image_path)

    # Llamamos a la función process_image
    label, prob, heatmap = process_image(test_image_path)
    
    # Validamos que la etiqueta es una cadena
    assert isinstance(label, str), f"Expected label to be a string, but got {type(label)}"

    # Validamos que la probabilidad es un valor float
    assert isinstance(prob, (float, int)), f"Expected prob to be a float, but got {type(prob)}"

    # Validamos que el mapa de calor tiene la forma de una imagen de 512x512
    assert isinstance(heatmap, np.ndarray), f"Expected heatmap to be a numpy ndarray, but got {type(heatmap)}"
    assert heatmap.shape == (512, 512, 3), f"Expected heatmap shape to be (512, 512, 3), but got {heatmap.shape}"

    # Elimina la imagen temporal después de la prueba
    os.remove(test_image_path)
