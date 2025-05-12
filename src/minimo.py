from .ler_arquivo_csv import ler_csv
import pandas as pd

def calc_minimo():
    minimo = (ler_csv())['vendas'].min()
    print("O minimo é é: R$" + str(minimo))
    return minimo