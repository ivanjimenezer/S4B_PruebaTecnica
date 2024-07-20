# Prueba Técnica para el puesto de Fullstack en Silent4Business
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/tree/main/media/app_preview.png)
## Instalación

Antes que nada, creamos un entorno virtual de python para hacer instalaciones de librerias locales. Esto se realiza con el siguiente comando en la carpeta raíz:
```
python -m venv venv
```
### Instalar Dependencias de Python
Instala los módulos necesarios para Django ejecutando el siguiente comando en la carpeta raíz:
```
pip install -r requirements.txt
```
## Instalar Dependencias de Node
Para instalar las dependencias de Node para React, ejecuta el siguiente comando en la carpeta ./frontend/:
```
npm install
```
## Configurar Variables de Entorno
Crea un archivo .env en el directorio scrappingApp y pega el contenido enviado por correo dentro de este archivo. Este archivo contendrá las credenciales necesarias para conectarse a la base de datos.
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/tree/main/media/env_file.png)
## Activar Entorno Virtual
Abre una consola de comandos y activa el entorno virtual en el directorio raíz con el siguiente comando:
```
.\venv\Scripts\activate  
```
## Iniciar Servidor Backend
Una vez que el entorno virtual esté activado, inicia el servidor backend en el mismo directorio con el siguiente comando:
```
python .\manage.py runserver
```
## Iniciar Servidor Frontend
Con el backend iniciado, navega al directorio ./frontend/ e inicia el servidor frontend con el siguiente comando:
```
npm run start
```
Y listo, puede comenzar a interactuar con la página

## Explicación de funciones




