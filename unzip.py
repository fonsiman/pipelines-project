import zipfile
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def unzip(query):
    try:
        zip_ref = zipfile.ZipFile(dir_path+"/download-data/Informes.zip", 'r')

        index = ""

        if os.path.exists(dir_path+"/data/"+query):
            index = 0
            while os.path.exists(dir_path+"/data/"+query+str(index)):
                index += 1

        os.mkdir(dir_path+"/data/"+query+str(index))

        zip_ref.extractall(dir_path+"/data/"+query+str(index))
        zip_ref.close()

        os.remove(dir_path+"/download-data/Informes.zip")

        return dir_path+"/data/"+query+str(index)
    except:
        raise ValueError("No se han podido descomprimir los archivos descargados")