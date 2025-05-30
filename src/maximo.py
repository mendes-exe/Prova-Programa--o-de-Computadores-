from .ler_arquivo_csv import ler_csv
import pandas as pd

def calc_max():
    max = (ler_csv())['vendas'].max()
    print("O máximo é: R$" + str(max))
    return max