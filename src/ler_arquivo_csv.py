import pandas as pd #Pandas: biblioteca para leitura da fonte de dados que iremos precisar para usar em nossos dataframes. Com ela também podemos realizar calculos estatisticos.
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def ler_csv(): # Função base para a leitura do csv que contem nossos dados
    try: #Será o codigo em que iremos rodar, que pode vir a ocorrer um erro
        df = pd.read_csv('data\\dados_vendas.csv') #DF é o dataframe que ficará armazenado os valores que iremos usar
        return df #Retornará um valor com o data frame que será usados nos calculos estatisticos
    except ValueError as e: # O except será usado para quando ocorrer erros ou exceção, retornando um mensagem
        logging.warning(f'Arquivo não encontrado - erro: {e}')
        return None
ler_csv()
