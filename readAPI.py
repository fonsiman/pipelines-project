from difflib import SequenceMatcher
import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

if not "ALPHAVANTAGE_KEY" in os.environ:
    raise ValueError("Necesitas una API key de alphavantage: https://www.alphavantage.co/support/#api-key")

key = os.environ["ALPHAVANTAGE_KEY"]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def findticker(query):
    dicticker = {
        "ACCIONA" : "ANA.MC",
        "ACERINOX" : "ACX.MC",
        "GRUPO ACS" : "ACS.MC",
        "AENA" : "AENA.MC",
        "AMADEUS IT GROUP" : "AMS.MC",
        "ARCELORMITTAL" : "MTS.MC",
        "BANCO SABADELL" : "SAB.MC",
        "BANCO SANTANDER" : "SAN.MC",
        "BANKIA" :"BKIA.MC",
        "BANKINTER" : "BKT.MC",
        "BBVA BANCO BILBAO VIZCAYA ARGENTARIA" : "BBVA.MC",
        "CAIXABANK" : "CABX.MC",
        "CELLNEX TELECOM" : "CLNX.MC",
        "CIE AUTOMOTIVE" : "CIE.MC",
        "ENAGAS": "ENG.MC",
        "ENCE": "ENC.MC",
        "ENDESA": "ELE.MC",
        "FERROVIAL" : "FER.MC",
        "GRIFOLS" : "GRF.MC",
        "IAG" : "IAG.MC",
        "IBERDROLA" : "IBE.MC",
        "INDITEX" : "ITX.MC",
        "INDRA SISTEMAS" : "IDR.MC",
        "INMOBILIARIA COLONIAL" : "COL.MC",
        "MAPFRE" : "MAP.MC",
        "MASMOVIL IBERCOM": "MAS.MC",
        "MEDIASET ESPAÑA COMUNICACIÓN": "TL5.MC",
        "MELIA HOTELS INTERNATIONAL": "MEL.MC",
        "MERLIN PROPERTIES" : "MRL.MC",
        "NATURGY" : "NTGY.MC",
        "RED ELECTRICA CORPORACION" : "REE.MC",
        "REPSOL" : "REP.MC",
        "SIEMENS GAMESA" : "SGRE.MC",
        "TELEFONICA" : "TEF.MC",
        "VISCOFAN" : "VIS.MC"
    }
    
    list_similar = [[similar(query, e), dicticker[e]] for e in dicticker.keys()]
    list_similar.sort(reverse = True)

    return list_similar[0][1]


def read_api(query):
    res = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=full&apikey={}'.format(findticker(query),key))
    data_api = res.json()

    cotdic = []

    for e in data_api["Time Series (Daily)"]:

        dicaux = {
            "fecha": e,
            "precio": data_api["Time Series (Daily)"][e]["4. close"]
        }

        cotdic.append(dicaux)

    df = pd.DataFrame(cotdic)
    df['fecha'] =pd.to_datetime(df.fecha)
    df['precio'] = df['precio'].apply(float)
    df.sort_values(by=["fecha"], inplace=True)
    # df.reset_index(inplace=True)

    # Aprovechamos y guardamos los datos en csv
    df.to_csv("cotizacion.csv",index=False)
    return df