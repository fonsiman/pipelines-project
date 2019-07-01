from bs4 import BeautifulSoup
import os
import pandas as pd
from matplotlib import pyplot as plt
import math
import requests
import numpy as np
import downloadDataset as dd
import unzip
import findticker
import cleanDataset
import readAPI
import drawPlot
import argparse

# Pedimos por terminal el nombre de la empresa
parser = argparse.ArgumentParser(description='Introduce el nombre de una empresa del IBEX 35')

parser.add_argument('-company', dest='el1', default="", type=str,
help='Nombre o CIF de una empresa del IBEX 35')

query = parser.parse_args().el1.upper()

if(query == ""):
    raise ValueError("Introduce el nombre o CIF de una compañía del IBEX 35 para realizar el análisis.")

# Descargamos el dataset. El wifi de Ironhack es un poco lento y suele tardar...
pg = dd.PageGetter('firefox')
soup = pg.getPage("https://www.cnmv.es/ipps/default.aspx", query)
pg.close()

# Descomprimimos los archivos descargados
path = unzip.unzip(query)
f_data = sorted(os.listdir(path))

# Limpieza de datos. Obtenemos los datos que nos interesan de los xblr descargados
df_fund = cleanDataset.clean(f_data, path)

# Obtén datos de cotización de la API
df = readAPI.read_api(query)

# Crea los gráficos
drawPlot.drawPlot(df, df_fund)
