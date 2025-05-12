import csv
import pandas as pd

def ler_csv():
    try:
        # with open('data\\dados_vendas.csv', newline='') as csvfile:
        #     spamreader = csv.reader(csvfile, delimiter=',', quotechar="|")
        #     for row in spamreader:
        #         print(', '.join(row))
        df = pd.read_csv('data\\dados_vendas.csv')
        # print( df.head() ) 
        return df
    except:
        print("arquivo não encontrado")
    else:
        print("Arquivo aberto com sucesso!!")