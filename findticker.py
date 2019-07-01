from difflib import SequenceMatcher

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