def save_txt(media_save, minimo_save, max_save, desv_pad_save, quartil_save):
    nome_arquivo = input("Digite o nome para salvar o arquivo: ")
    arquivo = open(f'output\{nome_arquivo}.txt', 'w')
    arquivo.write(f"A  é: {media_save} \nO valor minimo: {minimo_save} \nO valor maximo é: {max_save} \nO desvio padrão é: {desv_pad_save} \nOs quartis são:  {quartil_save}")
    print('arquivo salvo com sucesso')
    arquivo.close()