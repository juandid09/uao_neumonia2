import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import backend as K
from preprocess_img import preprocess
from load_model import load_model


# Desactivar ejecución ansiosa de TensorFlow para evitar errores de ejecución
tf.compat.v1.disable_eager_execution()
tf.compat.v1.experimental.output_all_intermediates(True)


def grad_cam(array):
    """
    Genera un heatmap de gradiente con la técnica Grad-CAM.

    Args:
        array (numpy.ndarray): Imagen a procesar para generar el heatmap.

    Returns:
        numpy.ndarray: Imagen con el heatmap de Grad-CAM superpuesto.
    """
    img = preprocess(array)
    model = load_model()
    preds = model.predict(img)
    argmax = np.argmax(preds[0])
    output = model.output[:, argmax]
    last_conv_layer = model.get_layer("conv10_thisone")  
    grads = K.gradients(output, last_conv_layer.output)[0]
    pooled_grads = K.mean(grads, axis=(0, 1, 2))
    iterate = K.function([model.input], [pooled_grads, last_conv_layer.output[0]])
    pooled_grads_value, conv_layer_output_value = iterate(img)
    
    for filters in range(64):
        conv_layer_output_value[:, :, filters] *= pooled_grads_value[filters]
    
    heatmap = np.mean(conv_layer_output_value, axis=-1)
    heatmap = np.maximum(heatmap, 0)
    heatmap /= np.max(heatmap)
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[2]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    
    img2 = cv2.resize(array, (512, 512))
    transparency = heatmap * 0.8
    transparency = transparency.astype(np.uint8)
    superimposed_img = cv2.add(transparency, img2)
    
    print("Hola, grad_cam")
    return superimposed_img[:, :, ::-1]
