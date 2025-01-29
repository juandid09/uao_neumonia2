# tests/test_integrator.py
import sys
from pathlib import Path

# Establecer la ruta del directorio src
src_path = Path(__file__).resolve().parent.parent / "src"
sys.path.append(str(src_path))

from integrator import process_image  # Importamos la función a probar
import pytest

def test_process_image():
    # Ruta de la imagen de prueba 
    image_path = 'tests/test_image.jpg'  # Cambia esto al nombre y ubicación de tu imagen

    # Llamamos a la función `process_image`
    label, prob, heatmap = process_image(image_path)

    # Verificamos que la etiqueta esté en las opciones válidas
    assert label in ['Bacteriana', 'Normal', 'Viral'], f"Etiqueta inválida: {label}"

    # Verificamos que la probabilidad esté entre 0 y 100
    assert 0 <= prob <= 100, f"Probabilidad fuera de rango: {prob}"

    # Aseguramos que el mapa de calor no sea None
    assert heatmap is not None, "El mapa de calor es None"
