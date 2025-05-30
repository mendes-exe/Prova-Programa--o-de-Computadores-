from .ler_arquivo_csv import ler_csv
import pandas as pd

def calc_desv_pad():
    desv_pad = (ler_csv())['vendas'].std()
    print("O desvio padrão é: R$" + str(desv_pad))
    return desv_pad