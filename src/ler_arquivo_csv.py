import pandas as pd

def ler_csv():
    try:
        df = pd.read_csv('data\\dados_vendas.csv')
        return df
    except:
        print("arquivo não encontrado")
    else:
        print("Arquivo aberto com sucesso!!")