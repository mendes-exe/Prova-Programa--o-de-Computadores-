import matplotlib.pyplot as plt
from .ler_arquivo_csv import ler_csv

def gerar_graf():
    df = ler_csv()

    vendas_mensais = df.groupby('mes')['vendas'].sum()

    ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
               'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    vendas_mensais = vendas_mensais.to_frame(name='vendas')
    vendas_mensais = vendas_mensais.reindex(ordem_meses).dropna()

    vendas_mensais['media_movel_3_meses'] = vendas_mensais.rolling(window=3).mean()

    plt.figure(figsize=(15, 6))
    plt.plot(vendas_mensais.index, vendas_mensais['vendas'], marker='o', linestyle='-')
    plt.plot(vendas_mensais.index, vendas_mensais['media_movel_3_meses'], color='red', linestyle='--', label='Média móvel (3 meses)')
    plt.title('Vendas Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Total de Vendas')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Salvar o gráfico primeiro
    plt.savefig(f'output\\grafico_vendas.png')

    # Mostrar o gráfico depois de salvar
    plt.show()

# Chama a função para gerar e salvar o gráfico
# gerar_graf()
