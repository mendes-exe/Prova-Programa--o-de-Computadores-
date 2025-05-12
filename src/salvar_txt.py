def save_txt(media_save, minimo_save, max_save, desv_pad_save, quartil_save):
    #  Salvar em txt
    # media_save = str(calc_media())
    # minimo_save = str(calc_minimo())
    # max_save = str(calc_max)
    # desv_pad_save = str(calc_desv_pad())
    # quartil_save = str(calc_quartil())
    nome_arquivo = input("Digite o nome para salvar o arquivo: ")
    arquivo = open(f'output\{nome_arquivo}.txt', 'w')
    arquivo.write(f"A  é: {media_save} \nO valor minimo: {minimo_save} \nO valor maximo é: {max_save} \nO desvio padrão é: {desv_pad_save} \nOs quartis são:  {quartil_save}")
    print('arquivo salvo com sucesso')
    arquivo.close()