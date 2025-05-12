from .ler_arquivo_csv import ler_csv
import pandas as pd

def calc_quartil():
    
    quartil = pd.DataFrame(ler_csv())
    q1 = (quartil)['vendas'].quantile(0.25)
    q2 = (quartil)['vendas'].quantile(0.50)
    q3 = (quartil)['vendas'].quantile(0.75)
    print("O primeiro quartil é: R$" + str(q1))
    print("O segundo quartil é: R$" + str(q2))
    print("O terceiro quartil é: R$" + str(q3))
    quartil1 = str(q1)
    quartil2 = str(q2)
    quartil3 = str(q3)
    return quartil1, quartil2, quartil3