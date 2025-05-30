from .ler_arquivo_csv import ler_csv
import pandas as pd

def calc_minimo():
    min = (ler_csv())['vendas'].min()
    print("O minímo é: R$" + str(min))
    return min

