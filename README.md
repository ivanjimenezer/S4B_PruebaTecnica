
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
Esta función se encarga de recorrer la siguiente página <https://www.scrapethissite.com/pages/simple/> y de obtener los datos de los paises. Solo se puede hacer WebScrapping cuando la cantidad total de registros de la BD sea menor a 250. Es por ello que se diseño la función de eliminación aleatoria, para poner a prueba el webscrapping de datos.

El diseño de la función es tal que previene la duplicación de datos por lo que verifica cada linea obtenida en la base de datos en búsqueda de una redundancia. Este proceso es lento y se ejecuta en el background. 

###### \* *En retrospectiva, ahora me doy cuenta de que hay una mejor solución para evitar duplicados y a la vez hacer del proceso mas rápido*
Se presiono el botón para iniciar el webscrapping

![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-w-1.png)

Primer refresh pasado 30 segundos

![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-w-2.png)

Segundo refresh pasado 1min. Aqui el webscrapping ha terminado porque hasta el momento la cantidad total de registros dentro del sitio web es de 250 elementos.

![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-w-3.png)

#### - Ordenar Alfabeticamente por nombre de País
Por si se desea ordenar los países alfabeticamente para darle mayor orden al archivo csv
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-o-1.png)

#### - Guardar archivo CSV
Agregue esta función porque a mi consideración este seria el **objetivo final** de dicho webscrapping. Poder obtener los datos de una página, filtrarlos y guardarlos para futuros análisis. 
A continuación podemos ver un ejemplo de datos filtrados siendo guardados para su almacenamiento en un archivo .csv : 
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-s-1.png)

Este es el resultado final del archivo

![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-s-2.png)

#### - Eliminación lógica de elementos
Esta función practicamente oculta elementos a simple vista, poniendolos al final de la tabla y también evita que aparezcan en el archivo .csv. En la siguiente imagen podemos ver como los elementos ocultos estan al final de la lista

![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/logdel1.png)

Y si vemos el archivo .csv generado no aparecen dentro de este
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/logdel2.png)

#### - Activacion de elementos

Es el opuesto a la funcionalidad anterior, en caso de que queramos desocultar un elemento entonces presionamos el botón verde:

![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-a-1.png)

Ahora los elementos activados pueden aparecer en el archivo .csv
![Image](https://github.com/ivanjimenezer/S4B_PruebaTecnica/blob/main/media/csv-a-2.png)
