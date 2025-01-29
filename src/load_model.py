import tensorflow as tf


def load_model():
    """
    Carga el modelo previamente entrenado.

    Returns:
        tensorflow.keras.Model: El modelo cargado desde el archivo.
    """
    model = tf.keras.models.load_model('/app/src/conv_MLP_84.h5')

    return model


