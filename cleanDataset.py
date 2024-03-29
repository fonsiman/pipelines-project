# Nuestro dataset está en formato XBRL, un formato basado en XML para intercambio de información financiera.
# Para almacenar esta información en un dataframe, hay que leerlo con BeautifulSoup.
# La información de estos archivos es enorme. Por simpleza, he cargo solo algunos que me han parecido más interesantes. Lo ideal hubiera sido poder
# tenerlos todos.
# Por otra parte, la legislación acerca del formato que deben cumplir estos XBRL, se ha modificado varias veces desde que se implantó.
# Este código recoge el último de estos formatos, por ello, solo recoge los datos desde el segundo semestre de 2016
# También cabe destacar, que algunos tipos de empresas tienen formato XBRL especial. Por ejemplo: Los bancos. En este caso, el código tampoco está
# adaptado.

import os
from bs4 import BeautifulSoup
import pandas as pd

def clean(f_data, path):
    print ("Limpiando el dataset...")
    dir_path = os.path.dirname(os.path.realpath(__file__))

    lstdic = []

    for files in range(len(f_data)):
        fil = path+"/"+f_data[files]
        with open(fil, 'r', encoding="utf8") as f:
            data = f.read()

        # Para no crear celdas vacías, solo cogemos los datos a partir de mayo de 2016
        if int(f_data[files][:6]) > 201605:
        
            soup = BeautifulSoup(data, 'lxml')
            
            dicaux = {
                "company": soup.select("xbrli\:identifier")[0].text,
                #"segmentos": soup.select("[contextRef='Icur_SegmentoslMiembro']"),
                
                # Cuenta de resultados

                #"importe_neto_cifra_negocio": soup.select("ipp_ge\:I1205")[0].text,
                "EBITDA": soup.select("ipp_ge\:I1245")[0].text,
                "EBIT": soup.select("ipp_ge\:I1265")[0].text,
                "Resultado": soup.select("ipp_ge\:I1288")[0].text,
                "BPA": soup.select("ipp_ge\:I1290")[0].text,
                "bpa_diluido": soup.select("ipp_ge\:I1295")[0].text,

                #"dividendos": soup.select("ipp_ge\:I1258"),

                # Balance
                "Activo": soup.select("ipp_ge\:I0100")[0].text,
                "Pasivo": soup.select("ipp_ge\:I0195")[0].text,
                "patrimonio_neto_1": soup.select("ipp_ge\:I0120")[0].text,
                "patrimonio_neto_2": soup.select("ipp_ge\:I0130")[0].text,
                
                # Plantilla
                "Plantilla": soup.select("ipp_ge\:I2295")[0].text,
                "Hombres": soup.select("ipp_ge\:I2296")[0].text,
                "Mujeres": soup.select("ipp_ge\:I2297")[0].text,

                "startdate": soup.select("xbrli\:startdate")[0].text,
                "enddate": soup.select("xbrli\:enddate")[0].text
            }

            lstdic.append(dicaux)

    # Creamos el dataframe
    df_fund = pd.DataFrame(lstdic)
    # Cambiamos el formato de las columnas con fechas a date
    df_fund['startdate'] =pd.to_datetime(df_fund.startdate)
    df_fund['enddate'] =pd.to_datetime(df_fund.enddate)
    # Creamos una columna mediumdate que será donde el plot representará las columnas
    df_fund['mediumdate'] =((df_fund.enddate-df_fund.startdate)/2 + pd.to_datetime(df_fund.enddate))

    # El Patrimonio Neto realmente es la suma de los dos datos recogidos
    df_fund['PN'] = df_fund['patrimonio_neto_1'] + df_fund['patrimonio_neto_2']

    # Separamos el año y los semestres en columnas separadas para poder representarlos en un groupby más adelante.
    df_fund['year'] =pd.DatetimeIndex(df_fund['startdate']).year
    df_fund['semestre'] =pd.DatetimeIndex(df_fund['startdate']).month
    df_fund['semestre'] = df_fund['semestre'].apply(lambda x: "S1" if x == 1 else "S2")

    return df_fund