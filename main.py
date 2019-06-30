from bs4 import BeautifulSoup
import os
import pandas as pd
from matplotlib import pyplot as plt
import math
import requests
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
f_data = sorted(os.listdir(dir_path+"/data/ence-2"))

lstdic = []

for files in range(len(f_data)):
    fil = dir_path+"/data/ence-2/"+f_data[files]
    with open(fil, 'r', encoding="utf8") as f:
        data = f.read()
        with open(dir_path+"/clean-data/ence/"+f_data[files][:-4]+"txt", 'w') as output:
            output.write(data)

f_data = sorted(os.listdir(dir_path+"/clean-data/ence"))

lstdic = []

for files in range(len(f_data)):
    fil = dir_path+"/clean-data/ence/"+f_data[files]
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

'''
print(startdate, enddate)
for item in periodo:
    print(item.text)

'''
f_dataset = sorted(os.listdir(dir_path+"/dataset"))

'''df = pd.DataFrame()

res = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=0K96.ILN&outputsize=full&apikey=RPY2EPG6JMND2R3M')
data_api = res.json()

for e in range(len(f_dataset)):
    dfaux = pd.read_csv(dir_path+"/dataset/"+f_dataset[e])
    df = pd.concat([df, dfaux], ignore_index=True)
'''

res = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=0K96.ILN&outputsize=full&apikey=RPY2EPG6JMND2R3M')
data_api = res.json()

cotdic = []

for e in data_api["Time Series (Daily)"]:

    dicaux = {
        "fecha": e,
        "precio": data_api["Time Series (Daily)"][e]["4. close"]
    }

    cotdic.append(dicaux)

df = pd.DataFrame(cotdic)
'''
df['FECHA'] =pd.to_datetime(df.FECHA)
df.sort_values(by=["FECHA"], inplace=True)
df.reset_index(inplace=True)
df.to_csv("cotizacion.csv",index=False)
'''

df['fecha'] =pd.to_datetime(df.fecha)
df['precio'] = df['precio'].apply(float)
df.sort_values(by=["fecha"], inplace=True)
# df.reset_index(inplace=True)
df.to_csv("cotizacion.csv",index=False)

df_fund = pd.DataFrame(lstdic)
df_fund['startdate'] =pd.to_datetime(df_fund.startdate)
df_fund['enddate'] =pd.to_datetime(df_fund.enddate)
df_fund['mediumdate'] =((df_fund.enddate-df_fund.startdate)/2 + pd.to_datetime(df_fund.enddate))

print(df_fund['mediumdate'] )
# GRÁFICOS



fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.bar(df_fund["mediumdate"], df_fund["resultado_consolidado"], width = 80, color=(190/255,190/255,190/255,0.7), label='Resultado consolidado')
ax2.plot(df["fecha"], df["precio"], color='b', label='Cotización')
ax.set_xticklabels(df["fecha"])
plt.title("Cotización ENCE",size=12,fontweight='bold')
plt.yticks(np.arange(df["precio"].min(), df["precio"].max(), 0.30))
plt.show()

plt.savefig('foo.png')
'''  
colors = ["b"]

precios = df

for i, e in enumerate(f_df_order[f_col]):
    if i >= n_plots:
        break
    else:
        if ic >= len(colors) :
            ic = 0
        plt.subplot(math.ceil(n_plots/2),2,i+1)
        ataque=f_df_aux[e]
        ataque.plot(kind='bar', color=colors[ic])
        plt.title(e + "Shark",size=12,fontweight='bold')
        plt.ylabel('Number of attacks',size=10) 
        plt.xlabel('Sizes',size=10)
'''