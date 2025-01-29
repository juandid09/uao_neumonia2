# Usa una imagen oficial de Python
FROM python:3.8-slim

# Instalar dependencias del sistema necesarias para Tkinter y OpenCV
RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    libglib2.0-0 \
    libgtk-3-0 \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    libxrender1 && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias necesarias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Definir el comando para ejecutar el archivo de inicio
CMD ["python", "/app/src/view.py"]
