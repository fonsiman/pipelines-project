# Una pequeña función que descomprime los ZIP en una carpeta destino. Tras ello, borra el .zip.
# Si existe la carpeta destino, te crea una nueva (con un número al final)
# La gestión de archivos no es mu eficiente, ya que, por el momento, te crea una carpeta nueva con cada consulta.

import zipfile
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def unzip(query):
    try:
        print ("Descomprimiendo los archivos descargados...")
        zip_ref = zipfile.ZipFile(dir_path+"/download-data/Informes.zip", 'r')

        index = ""

        # Busca el nombre de la carpeta si exite
        if os.path.exists(dir_path+"/data/"+query):
            index = 0
            while os.path.exists(dir_path+"/data/"+query+str(index)):
                index += 1

        # Crea la carpeta
        os.mkdir(dir_path+"/data/"+query+str(index))

        zip_ref.extractall(dir_path+"/data/"+query+str(index))
        zip_ref.close()

        # Elimina el .zip
        os.remove(dir_path+"/download-data/Informes.zip")

        return dir_path+"/data/"+query+str(index)
    except:
        raise ValueError("No se han podido descomprimir los archivos descargados")