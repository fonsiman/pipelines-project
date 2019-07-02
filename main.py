import os
from getQuery import getQuery
from downloadDataset import PageGetter
from unzip import unzip
from cleanDataset import clean
from readAPI import read_api
from drawPlot import drawPlot
from createPDF import createPDF
from sendMail import sendMail

import warnings
warnings.filterwarnings("ignore")

def main():
    # Pedimos por terminal el nombre de la empresa
    query, data_plot = getQuery()

    # Descargamos el dataset. El wifi de Ironhack es un poco lento y suele tardar...
    pg = PageGetter('firefox')
    soup = pg.getPage("https://www.cnmv.es/ipps/default.aspx", query)
    pg.close()

    # Descomprimimos los archivos descargados
    path = unzip(query)
    f_data = sorted(os.listdir(path))

    # Limpieza de datos. Obtenemos los datos que nos interesan de los xblr descargados
    df_fund = clean(f_data, path)

    # Obtén datos de cotización de la API
    df = read_api(query)

    # Crea los gráficos
    img_file = drawPlot(df, df_fund, query, data_plot)

    # Crea los gráficos
    pdf_file = createPDF(img_file)

    # Enviamos un correo electrónico
    sendMail(pdf_file)

if __name__ == "__main__":
    main()