# Pipelines Project

<p style="background-color:#e6e6e6;font-style:italic;padding:15px;">Este repositorio es un proyecto realizado como tarea durante el bootcamp de Data Analytics de <a href="https://www.ironhack.com/" title="Ironhack">Ironhack</a>.</p>

Este proyecto permite al usuario elegir entre una compañía del IBEX35 y un dato financiero de la misma. El script devuelve un informe comparando dicho dato con el precio histórico de la acción.

Además ofrece en tablas información financiera adicional de la empresa.

## Archivos

Los archivos que contiene el proyecto son (por orden de ejecución):

* `main.py`: Archivo principal que llama a todas las funciones para ejecutar el programa.
* `getQuery.py`: Archivo con la librería de Python `argparse` que solicita los inputs al usuario.
* `downloadDataset.py`: Archivo que utiliza Selenium para descargar el dataset de la web oficial de la CNMV a través de *web scraping*.
* `unzip.py`: Pequeño script para descomprimir los archivos descargados.
* `cleanDataset.py`: Limpieza del dataset. Los archivos descargados tienen formato XBRL, un formato basado en XML para intercambio de información financiera. Por tanto, para poder obtener los datos que necesitamos, lo hemos hecho con BeautifulSoup
* `readAPI.py`: Obtención de la cotización de la empresa a través de una API.
* `drawPlot.py`: Dibujamos una gráfica y tres tablas con la información con la librería de Python `matplotlib`. Las 
* `createPDF.py`: Crea, a través de las imágenes creadas.
* `sendMail.py`: Envía el pdf creado a una dirección de correo electrónico.

Las carpetas `data`, `data-download` y `outputs` son necesarias para guardar información durante la ejecución del programa. Sin embargo, para no subir demasiados archivos se ha ignorado su contenido a través del .gitignore.
