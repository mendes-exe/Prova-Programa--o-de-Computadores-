from .ler_arquivo_csv import ler_csv
import pandas as pd

def calc_media():
    media = (ler_csv())['vendas'].mean()
    print("A média é: R$" + str(media))
    return media

# calc_media()