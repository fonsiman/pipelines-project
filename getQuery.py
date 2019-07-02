# Este archivo declara un argparse para que el usuario elija una opción.
# Por un lado, el elemento -company o -c recoge el nombre de una empresa del IBEX 35, del que verá su cotización.
# Por otro, el elemento -data o -d recoge al que quieres comparar la cotización. Se puede escoger entre'resultado ', 'bpa', 'activos' o 'plantilla'

import argparse

def getQuery():
    parser = argparse.ArgumentParser(description='Introduce el nombre de una empresa del IBEX 35 que no sea un banco')

    parser.add_argument('-company', dest='el1', default="", type=str,
    help='Nombre o CIF de una empresa del IBEX 35')

    parser.add_argument('-c', dest='el1', default="", type=str,
    help='Nombre o CIF de una empresa del IBEX 35')

    parser.add_argument('-data', dest='el2', default="resultado", type=str,
    help="Información a comparar. Elige entre: 'resultado', 'bpa', 'activos' o 'plantilla'")

    parser.add_argument('-d', dest='el2', default="resultado", type=str,
    help="Información a comparar. Elige entre: 'resultado', 'bpa', 'activos' o 'plantilla'")

    query = parser.parse_args().el1.upper()
    data_plot = parser.parse_args().el2.lower()

    if query == "" :
        raise ValueError("Introduce el nombre o CIF de una compañía del IBEX 35 para realizar el análisis. El programa no analiza bancos.")

    if (data_plot != 'resultado') and (data_plot != 'bpa') and (data_plot != 'activos') and (data_plot != 'plantilla'):
        raise ValueError("Introduce un dato a comprar correcto. Elige entre: 'resultado', 'bpa', 'activos' o 'plantilla'")

    return query, data_plot