import pandas as pd #Pandas: biblioteca para leitura da fonte de dados que iremos precisar para usar em nossos dataframes. Com ela também podemos realizar calculos estatisticos.

def ler_csv(): # Função base para a leitura do csv que contem nossos dados
    try: #Será o codigo em que iremos rodar, que pode vir a ocorrer um erro
        df = pd.read_csv('data\\dados_vendas.csv') #DF é o dataframe que ficará armazenado os valores que iremos usar
        return df #Retornará um valor com o data frame que será usados nos calculos estatisticos
    except: # O except será usado para quando ocorrer erros ou exceção, retornando um mensagem
        print("arquivo não encontrado")
    else:
        print("Arquivo aberto com sucesso!!")