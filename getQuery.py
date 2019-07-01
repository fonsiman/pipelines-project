import argparse

def getQuery():
    parser = argparse.ArgumentParser(description='Introduce el nombre de una empresa del IBEX 35')

    parser.add_argument('-company', dest='el1', default="", type=str,
    help='Nombre o CIF de una empresa del IBEX 35')

    query = parser.parse_args().el1.upper()