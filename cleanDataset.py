import os
from bs4 import BeautifulSoup
import pandas as pd

def clean(f_data, path):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    lstdic = []

    for files in range(len(f_data)):
        fil = path+"/"+f_data[files]
        with open(fil, 'r', encoding="utf8") as f:
            data = f.read()

        if int(f_data[files][:6]) > 201605:
        
            soup = BeautifulSoup(data, 'lxml')
            
            dicaux = {
                "company": soup.select("xbrli\:identifier")[0].text,
                #"segmentos": soup.select("[contextRef='Icur_SegmentoslMiembro']"),
                
                # Cuenta de resultados

                "importe_neto_cifra_negocio": soup.select("ipp_ge\:I1205")[0].text,
                "resultado_exp": soup.select("ipp_ge\:I1245")[0].text,
                "resultado_antes_imp": soup.select("ipp_ge\:I1265")[0].text,
                "resultado_consolidado": soup.select("ipp_ge\:I1288")[0].text,
                "bpa_basico": soup.select("ipp_ge\:I1290")[0].text,
                "bpa_diluido": soup.select("ipp_ge\:I1295")[0].text,

                #"dividendos": soup.select("ipp_ge\:I1258"),

                # Balance
                "activo": soup.select("ipp_ge\:I0100")[0].text,
                "activo_anterior": soup.select("ipp_ge\:I0100")[0].text,
                "pasivo": soup.select("ipp_ge\:I0195")[0].text,
                "patrimonio_neto_1": soup.select("ipp_ge\:I0120")[0].text,
                "patrimonio_neto_2": soup.select("ipp_ge\:I0130")[0].text,
                
                # Flujos de caja
                "patrimonio_neto_2": soup.select("ipp_ge\:I0130")[0].text,
                "patrimonio_neto_2": soup.select("ipp_ge\:I0130")[0].text,
                "patrimonio_neto_2": soup.select("ipp_ge\:I0130")[0].text,

                # Plantilla
                "plantilla": soup.select("ipp_ge\:I2295")[0].text,
                "hombres": soup.select("ipp_ge\:I2296")[0].text,
                "mujeres": soup.select("ipp_ge\:I2297")[0].text,

                "startdate": soup.select("xbrli\:startdate")[0].text,
                "enddate": soup.select("xbrli\:enddate")[0].text
            }

            lstdic.append(dicaux)

    df_fund = pd.DataFrame(lstdic)
    df_fund['startdate'] =pd.to_datetime(df_fund.startdate)
    df_fund['enddate'] =pd.to_datetime(df_fund.enddate)
    df_fund['mediumdate'] =((df_fund.enddate-df_fund.startdate)/2 + pd.to_datetime(df_fund.enddate))
    return df_fund