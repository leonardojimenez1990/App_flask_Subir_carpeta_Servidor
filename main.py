import shutil
from flask import Flask, render_template, request, send_file
from tkinter import filedialog
import tkinter as tk
import os

app = Flask(__name__)

# Configuración para almacenar los archivos subidos
app.config['UPLOAD_FOLDER'] = 'uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'jpg', 'jpeg', 'png', 'gif', 'pdf', 'txt']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_uploaded_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    ruta_archivos = [os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], file)) for file in files]
    return ruta_archivos, files

def upload_files(folder_path):
    ruta_archivos = []
    # Subir los archivos desde la carpeta seleccionada
    for raiz, dirs, archivos in os.walk(folder_path):
        for archivo in archivos:
            f = os.path.join(raiz, archivo)
            if allowed_file(archivo):
                destino = os.path.join(app.config['UPLOAD_FOLDER'], archivo)
                shutil.copy(f, destino)
                ruta_archivos.append(os.path.abspath(f))
    return ruta_archivos

# Ruta para la página principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Crear ventana tkinter
        root = tk.Tk()
        root.withdraw()

        # Mostrar diálogo para seleccionar carpeta
        folder_path = filedialog.askdirectory()

        if folder_path:
            # Guardar la ruta de la carpeta seleccionada
            folder_path = os.path.abspath(folder_path)

            # Verificar si la carpeta existe
            if os.path.exists(folder_path):
                ruta_archivos = upload_files(folder_path)
                folder, files = get_uploaded_files()
                return render_template('index.html', folder_path=folder_path, folder=folder, files=files)

    ruta_archivos, files = get_uploaded_files()
    return render_template('index.html', folder_path=None, folder=ruta_archivos, files=files)

@app.route('/' + app.config['UPLOAD_FOLDER'] + '/<nombre_archivo>')
def leer_archivo(nombre_archivo):
    ruta_file = os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo)
    return send_file(ruta_file, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
