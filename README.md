# Proyecto UAO Neumonía!

Hola, en este proyecto se desarrollo una herramienta de diagnóstico médico que utiliza técnicas de aprendizaje profundo para detectar neumonía en imágenes radiográficas. La aplicación permite cargar imágenes, tanto en formato DICOM como JPG, procesarlas y generar predicciones sobre si la neumonía es de tipo bacteriana, viral o si no está presente. Además, muestra un mapa de calor heatmap para resaltar las áreas de la imagen relevantes para la predicción.
  

## Estructura del Proyecto

la estructura del proyecto a tener en cuenta al implementar es la siguiente: 

uao-neumonia/

├── src/          # Código fuente de la aplicación

│   ├── view.py            # Interfaz gráfica y lógica de la aplicación

│   ├── read_img.py        # Funciones para leer imágenes DICOM y JPG

│   ├── preprocess_img.py  # Preprocesamiento de las imágenes para la predicción

│   ├── load_model.py      # Carga del modelo previamente entrenado

│   ├── integrator.py      # Integración de funciones para el flujo completo de predicción

│   ├── grad_cam.py        # Generación de mapas de calor usando Grad-CAM

│   └── ... 

├── tests/                 # Archivos de prueba

│   ├── test_integrator.py # Pruebas para el integrador de imágenes y modelo

│   ├── test_process_img.py# Pruebas para el preprocesamiento y generación de mapas de calor

│   └── ...

├── requirements.txt       # Dependencias del proyecto


cabe aclarar que a la estructura hace referencia solo a la parte funcional del proyecto porque tambien se pueden encontrar directorios como outputs que es donde se estan almacenando los archivos generados. 


## Observaciones 

El codigo esta con rutas /app/src al ejecutarse debido a la estructura de docker, si requiere correr el programa de manera nativa tendria que bajar el proyecto y quitar /app/ y dejar src esto resolvería cualquier conflicto dado que encontraría los archivos desde el disco local y no desde la imagen de docker. si ejecutar una imagen de doket no tendría ningún problema. 
tambien tener en cuenta incluir el archivo .h5
la carpeta donde se guardan los archivos se general al ejecutar el proyecto de igual forma se mantiene validando se se debe crear, es decir si no existe la crea y si existe la utiliza para guardar los archivos pdf y csv

## Recursos del Proyecto
Archivo Docker: https://drive.google.com/file/d/1chGgNVcmmttn91aTSeMWXxskpGCMoboR/view

Tutorial: https://drive.google.com/file/d/1VQizObXTqtse7I4XWPI4w33etj-lkmSv/view?usp=sharing

Repositorio GitHub: https://github.com/juandid09/uao_neumonia2/tree/main?tab=readme-ov-file

Documentación: https://drive.google.com/file/d/14oyb4NtME74qY13t2nDZDT-qGnz2TOGf/view?usp=drive_link


## Requisitos

Este proyecto requiere Python 3.x y las siguientes bibliotecas. Puedes instalarlas usando el archivo requirements.txt

tensorflow==2.10.*

 pyautogui==0.9.52 
 
 pillow==8.4.0 
 
 tkcap==0.0.4 
 
 pydicom==2.2.2 
 
 img2pdf==0.4.4
 
  opencv-python==4.5.5.64 
  
  matplotlib==3.5.1 
  
  pandas==1.3.5 
  
  python-xlib==0.31 
  
  protobuf==3.19.6 
  
  keras==2.10.* 
  
  pytest==7.2.2
  
  se pueden instalar las dependencias utilizando: pip install -r requirements.txt o si crea un entorno virtual en su editor de código seria seleccionando el mismo. 

## Instalación

Clona el repositorio: 
git clone https://github.com/juandid09/uao_neumonia2.git

Instala las dependencias:
Asegúrate de tener Python 3.8 y tener el pip instalado y habilitado 
pip install -r requirements.txt
este punto tambien se puede realizar utilizando la virtualización del entorno de desarrollo. 

Ejecuta la aplicación

python src/view.py

## Uso

### Cargar una imagen

Carga una imagen: en formato utilizando el botón "Cargar Imagen".
    
Realiza la predicción: haciendo clic en "Predecir". El modelo mostrará la clase Bacteriana, Viral o Normal y la probabilidad asociada a la predicción esto se mostrara en la GUI en los campos a la derecha.
    
Visualiza el mapa de calor: generado por el modelo utilizando la técnica Grad-CAM, el cual se superpone sobre la imagen para resaltar las áreas relevantes para la predicción.

### Guardar resultados
Los resultados pueden guardarse en un archivo CSV para su posterior análisis o como un archivo PDF de la captura de la interfaz, estos estarán ubicados en la carpeta outputs dado que se debe respetar el patron de diseño MVC y el orden  que esta en el árbol de las reglas del juego. 

### Borrar los datos
Puedes borrar todos los datos de la aplicación (como las imágenes y resultados) usando el botón "Borrar".

# Tests
El proyecto incluye pruebas unitarias para garantizar que el sistema funcione correctamente. Los tests están en la carpeta tests/ y se pueden ejecutar con pytest. 
Para ejecutar las pruebas, simplemente usa el siguiente comando: pytest tests/test_integrator.py o el nombre del archivo que se quiera probar. 


## Explicación de los Archivos

### view. py: 
Es el archivo principal que maneja la interfaz gráfica usando Tkinter. Permite cargar imágenes, realizar predicciones, mostrar resultados y generar reportes.
### read_img. py: 
Contiene funciones para leer imágenes DICOM y JPG, convirtiéndolas a un formato adecuado para el procesamiento.
### preprocess_img. py
Preprocesa las imágenes para la predicción, ajustando su tamaño y normalizándolas.
### load_model. py
Carga el modelo previamente entrenado que se usará para realizar las predicciones.
### integrator. py
Integra las funciones de carga de imagen, preprocesamiento, predicción y generación de mapas de calor.
### grad_cam. py
Implementa la técnica Grad-CAM para generar mapas de calor que visualizan las áreas relevantes de la imagen para la predicción.

internamente estos archivos respetan el patrón de desarrollo MVC modelo vistas controlador. 

## Licencia
se publica bajo la licencia la cual esta disponible aqui: [LICENSE.py](https://github.com/juandid09/uao_neumonia2/blob/main/LICENSE)

## Contribuciones
si se ve producente hacer alguna observación, corrección  o contribución el proyecto esta en disponibilidad  de hacer fork y abrir un pull request. 
