
# Prueba Técnica para el puesto de Fullstack en Silent4Business

![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/app_preview.png)

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

![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/env_file.png)

## Activar Entorno Virtual

Abre una consola de comandos y activa el entorno virtual en el directorio raíz con el siguiente comando:

```

.\venv\Scripts\activate

```

## Iniciar Servidor Backend

Una vez que el **entorno virtual** esté activado, inicia el servidor backend en el mismo directorio con el siguiente comando:

```

python .\manage.py runserver

```

## Iniciar Servidor Frontend

Con el backend iniciado, navega al directorio **./frontend/** e inicia el servidor frontend con el siguiente comando:

```

npm run start

```

Y listo, puede comenzar a interactuar con la página

  

## Explicación de funciones

### - Filtrado de valores
Con estos campos es posible filtrar los paises para obtener los registros deseados para su futura inserción en una lista .csv. Se pueden filtrar en base a su capital, nombre y población.
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/filtrar.png)

### - Eliminar aleatoriamente
Ingresamos dentro del campo un valor númerico menor o igual a la cantidad de paises recolectados y eliminara aleatoriamente valores dentro de la base datos. Esta función nos permite poder activar la función de hacer Webscrapping. Su efecto es inmmediato.
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/randel1.png)
Como podemos ver en la siguiente imagen, se han borrado satisfactoriamente 60 registros  y uno más que se realizó enseguida.
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/randel2.png)


### - Funciones relacionadas a la generación del archivo CSV
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv1.png)
#### - Webscrapping
Esta función se encarga de recorrer la siguiente página <https://www.scrapethissite.com/pages/simple/> y de obtener los datos de los paises. Su diseño es tal que previene la duplicación de datos por lo que verifica cada linea obtenida en la base de datos en búsqueda de una redundancia. Este proceso es lento y se ejecuta en el background. 

###### \* *En retrospectiva, ahora me doy cuenta de que hay una mejor solución para evitar duplicados y a la vez hacer del proceso mas rápido*
Se presiono el botón para iniciar el webscrapping
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-w-1.png)
Primer refresh pasado 30 segundos
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-w-2.png)

