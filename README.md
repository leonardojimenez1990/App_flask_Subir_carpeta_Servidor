# App_flask_Subir_carpeta_Servidor
Aplicación Flask para subir y mostrar archivos  Este código representa una aplicación web desarrollada con Flask que permite a los usuarios seleccionar una carpeta en su disco local, subir los archivos permitidos contenidos en esa carpeta al servidor y mostrar los archivos subidos en una plantilla HTML.
El código se divide en varias secciones y utiliza varias bibliotecas y funciones para lograr su funcionalidad. A continuación se describe cada sección y sus funciones principales:

Importación de bibliotecas:

shutil: Se utiliza para copiar archivos en el servidor.
Flask, render_template, request, send_file: Importación de clases y funciones de Flask para el desarrollo de la aplicación web.
filedialog y tkinter: Importación de clases y funciones para mostrar un cuadro de diálogo para seleccionar una carpeta utilizando la biblioteca Tkinter.
Configuración de la aplicación:

Se crea una instancia de la clase Flask y se asigna a la variable app.
Se configura la carpeta de carga (UPLOAD_FOLDER) donde se guardarán los archivos subidos. Si la carpeta no existe, se crea utilizando os.makedirs().
Definición de variables y funciones de utilidad:

ALLOWED_EXTENSIONS: Lista de extensiones de archivos permitidas. Se utiliza para verificar si un archivo tiene una extensión válida.
allowed_file(filename): Función que verifica si un archivo tiene una extensión permitida. Se utiliza para filtrar los archivos a subir.
get_uploaded_files(): Función que obtiene la lista de archivos subidos en la carpeta de carga (UPLOAD_FOLDER) y devuelve las rutas absolutas y los nombres de los archivos.
upload_files(folder_path): Función que sube los archivos permitidos desde la carpeta seleccionada por el usuario al servidor. Utiliza la función shutil.copy() para copiar los archivos.
Ruta principal (/) y función index():

Esta ruta y función manejan tanto las solicitudes GET como las POST.
En una solicitud POST, se muestra un cuadro de diálogo para que el usuario seleccione una carpeta utilizando la biblioteca Tkinter. Si se selecciona una carpeta válida, se suben los archivos permitidos desde esa carpeta al servidor y se muestra una plantilla HTML con los archivos subidos.
En una solicitud GET, se obtiene la lista de archivos subidos y se muestra una plantilla HTML con los archivos existentes.
Ruta para leer archivos (/uploads/<nombre_archivo>) y función leer_archivo():

Esta ruta y función manejan las solicitudes para abrir archivos subidos en la aplicación.
La función leer_archivo(nombre_archivo) construye la ruta del archivo seleccionado y lo envía como respuesta utilizando send_file() de Flask.
Punto de entrada principal (__name__ == '__main__'):

Se ejecuta la aplicación Flask con la configuración de depuración habilitada.
