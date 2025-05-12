from .ler_arquivo_csv import ler_csv
import pandas as pd

def calc_minimo():
    min_valor = (ler_csv())['vendas'].min()
    mes_min = ler_csv()[ler_csv()['vendas'] == min_valor].iloc[0]['mes']
    # print("O minimo é é: R$" + str(min_valor) + "no mes de: " + str(mes_min))
    minimo = (f"O minimo é: R$ {str(min_valor)} no mes de: + {str(mes_min)}")
    print(minimo)
    return minimo

