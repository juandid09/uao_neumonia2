import os
import csv
from tkinter import *
from tkinter import ttk, font, filedialog, Text
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import Image, ImageTk, ImageGrab
import pydicom
from integrator import process_image  # Se utiliza el integrador para obtener el resultado
import numpy as np


class PneumoniaApp:

    def __init__(self):
        """Inicializa la aplicación y configura la interfaz gráfica ."""
        self.root = Tk()
        self.root.title("Herramienta para la detección rápida de neumonía")
        self.font = font.Font(weight="bold")
        self.root.geometry("815x560")
        self.root.resizable(0, 0)

        # Widgets de la interfaz
        self.setup_widgets()

        # Inicializar variables de imagen y resultados
        self.image_path = None  # Guardar la ruta del archivo
        self.array = None  # Guardar la imagen en formato de arreglo
        self.report_id = 0

        # Verificar o crear el directorio de salida
        self.output_dir = "/app/outputs"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Iniciar la interfaz gráfica
        self.root.mainloop()

    def setup_widgets(self):
        """Configura los widgets de la interfaz grafica"""
        # Etiquetas
        self.lab1 = ttk.Label(self.root, text="Imagen Radiográfica", font=self.font)
        self.lab2 = ttk.Label(self.root, text="Imagen con Heatmap", font=self.font)
        self.lab3 = ttk.Label(self.root, text="Resultado:", font=self.font)
        self.lab4 = ttk.Label(self.root, text="Cédula Paciente:", font=self.font)
        self.lab5 = ttk.Label(self.root, text="SOFTWARE PARA EL APOYO AL DIAGNÓSTICO MÉDICO DE NEUMONÍA", font=self.font)
        self.lab6 = ttk.Label(self.root, text="Probabilidad:", font=self.font)

        # Variables de texto
        self.ID = StringVar()
        self.result = StringVar()

        # Entradas de texto
        self.text1 = ttk.Entry(self.root, textvariable=self.ID, width=10)
        self.text_img1 = Text(self.root, width=31, height=15)
        self.text_img2 = Text(self.root, width=31, height=15)
        self.text2 = Text(self.root)
        self.text3 = Text(self.root)

        # Botones
        self.button1 = ttk.Button(self.root, text="Predecir", state="disabled", command=self.run_model)
        self.button2 = ttk.Button(self.root, text="Cargar Imagen", command=self.load_img_file)
        self.button3 = ttk.Button(self.root, text="Borrar", command=self.delete)
        self.button4 = ttk.Button(self.root, text="PDF", command=self.create_pdf)
        self.button6 = ttk.Button(self.root, text="Guardar", command=self.save_results_csv)

        # Posicion de los widgets
        self.position_widgets()

    def position_widgets(self):
        """Posiciona los widgets en la ventana."""
        self.lab1.place(x=110, y=65)
        self.lab2.place(x=545, y=65)
        self.lab3.place(x=500, y=350)
        self.lab4.place(x=65, y=350)
        self.lab5.place(x=122, y=25)
        self.lab6.place(x=500, y=400)
        self.button1.place(x=220, y=460)
        self.button2.place(x=70, y=460)
        self.button3.place(x=670, y=460)
        self.button4.place(x=520, y=460)
        self.button6.place(x=370, y=460)
        self.text1.place(x=200, y=350)
        self.text2.place(x=610, y=350, width=90, height=30)
        self.text3.place(x=610, y=400, width=90, height=30)
        self.text_img1.place(x=65, y=90)
        self.text_img2.place(x=500, y=90)

    def load_img_file(self):
        """Carga una imagen DICOM o JPG/JPEG y la muestra en la interfaz."""
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select image",
            filetypes=(("DICOM", "*.dcm"), ("JPEG", "*.jpeg"), ("JPG", "*.jpg"), ("PNG", "*.png"))
        )
        if filepath:
            # Guardar la ruta del archivo
            self.image_path = filepath

            # Verificar si el archivo es DICOM
            if filepath.lower().endswith('.dcm'):
                # Cargar imagen DICOM usando pydicom
                dicom_data = pydicom.dcmread(filepath)
                img_array = dicom_data.pixel_array

                # Convertir la imagen DICOM a formato compatible con PIL
                img = Image.fromarray(img_array)

            else:
                # Para imagenes JPEG, JPG, PNG
                img = Image.open(filepath)

            # Redimensionar la imagen para la previsualizacin
            img = img.resize((250, 250), Image.ANTIALIAS)  # Redimensionar para visualización
            self.img1 = ImageTk.PhotoImage(img)

            # Mostrar la imagen cargada
            self.text_img1.image_create(END, image=self.img1)

            # Habilitar el botón de predicción
            self.button1["state"] = "normal"

            # Guardar la imagen cargada en formato de arreglo
            self.array = np.array(img)  # Guardar la imagen en formato de arreglo

            # Limpiar los resultados anteriores
            self.text2.delete(1.0, "end")
            self.text3.delete(1.0, "end")

    def run_model(self):
        """Ejecuta el modelo de predicción y muestra el resultado."""
        if self.image_path is not None:
            # Procesar la imagen cargada y generar el heatmap
            label, proba, heatmap = process_image(self.image_path)  # Pasamos la ruta de la imagen

            # Mostrar el heatmap generado
            img_array = heatmap  # El heatmap generado es una imagen para mostrar
            img2 = Image.fromarray(img_array)
            img2 = img2.resize((250, 250), Image.ANTIALIAS)
            self.img2 = ImageTk.PhotoImage(img2)
            self.text_img2.image_create(END, image=self.img2)

            # Mostrar los resultados
            self.text2.delete(1.0, "end")
            self.text3.delete(1.0, "end")
            self.text2.insert(END, label)
            self.text3.insert(END, f"{proba:.2f}%")

    def save_results_csv(self):
        """Guarda los resultados en un archivo CSV en la carpeta 'outputs'."""
        try:
            csv_path = os.path.join(self.output_dir, "historial.csv")
            with open(csv_path, "a", newline='') as csvfile:
                w = csv.writer(csvfile, delimiter=",")
                w.writerow([self.text1.get(), self.text2.get("1.0", "end-1c"), self.text3.get("1.0", "end-1c")])
                showinfo(title="Guardar", message=f"Los datos se guardaron con éxito en {csv_path}.")
        except Exception as e:
            showinfo(title="Error", message=f"Error al guardar el archivo CSV: {e}")

    def create_pdf(self):
        """Genera un archivo PDF con la captura de la interfaz en la carpeta 'outputs'."""
        try:
            x1 = self.root.winfo_rootx()
            y1 = self.root.winfo_rooty()
            x2 = x1 + self.root.winfo_width()
            y2 = y1 + self.root.winfo_height()

            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))  # Captura el área de la ventana
            pdf_path = os.path.join(self.output_dir, f"Reporte_{self.report_id}.pdf")
            img.save(pdf_path, "PDF")
            self.report_id += 1
            showinfo(title="PDF", message=f"El PDF fue generado con éxito: {pdf_path}")
        except Exception as e:
            showinfo(title="Error", message=f"Error al crear el PDF: {e}")

    def delete(self):
        """Borra todos los datos en la interfaz"""
        answer = askokcancel(
            title="Confirmación", message="Se borrarán todos los datos.", icon=WARNING
        )
        if answer:
            self.text1.delete(0, "end")
            self.text2.delete(1.0, "end")
            self.text3.delete(1.0, "end")
            self.text_img1.delete(1.0, "end")
            self.text_img2.delete(1.0, "end")
            showinfo(title="Borrar", message="Los datos se borraron con éxito")


def main():
    PneumoniaApp()


if __name__ == "__main__":
    main()
