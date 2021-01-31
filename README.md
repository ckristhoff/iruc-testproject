# iruc-testproject
Proyecto de demostración para la automatización de pruebas en la electiva de Ingeniería de Requisitos de la Universidad del Cauca.

## Requerimientos

* Python 3.8

Si ejecuta el proyecto en un sistema Windows, recuerde activar la casilla para agregar python al las variables del sistema (`Add Python 3.8 to PATH`) en el programa de instalación.

## Instalación
Ejecute el archivo `install.bat` desde el administrador de archivos o desde una terminal. El script de instalación es compatible para todos los sistemas operativos. El script de instalación ejecutará las siguientes tareas:

* Instalar gestor de entornos virtuales (pipenv)
* Instalar las dependencias del proyecto (django framework)
* Crear la base de datos del proyecto (SQLite)
* Cargar los datos de prueba

## Ejecución
Ejecute el archivo `start.bat` desde el administrador de archivos o desde una terminal. El script de inicio del servidor es compatible con todos los sistemas operativos. El script abrirá una ventana de terminal que debe mantenerse abierta mientras quiera que se ejecute el servidor. Cuando desee terminar la ejecución simplemente cierre la ventana de terminal.

URL de acceso: http://127.0.0.1:8000
URL de administración: http://127.0.0.1:8000/admin
Nombre de usuario: admin
Contraseña: admin
