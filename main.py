from src.ler_arquivo_csv import ler_csv
from src.media import calc_media
from src.minimo import calc_minimo
from src.maximo import calc_max
from src.desv_pad import calc_desv_pad
from src.quartil import calc_quartil
from src.salvar_txt import save_txt

print("1 - Calcular média\n" \
"2 - Calcular minimo\n" \
"3 - Calcular máximo\n" \
"4 - Calcular Desvio Padrão\n" \
"5 - Calcular Quartil\n" \
"6 - Gerar arquivo TXT\n" \
"7 - Gerar Gráficos")
opcaoteste = int(input("Escolha uma opção: "))

# Menu
def menu(opcao):
    match opcao:
        case 1:
            print(f'A média é: {calc_media()}')
        case 2:
            print(f'O mínimo é: {calc_minimo()}')
        case 3:
            print(f'O máximo é: {calc_max()}')
        case 4:
            print(f'O desvio padrão é: {calc_desv_pad()}')
        case 5:
            print(f'O quartil é: {calc_quartil()}')
        case 6:
            save_txt(calc_media(), calc_minimo(), calc_max(), calc_desv_pad(), calc_quartil())
            print("Arquivo TXT gerado com sucesso!")
        case 7:
            print("Gerar gráficos...")  
        case _:
            print("Opção incorreta!")
            opcaoteste = int(input("Escolha uma opção válida: "))
            menu(opcaoteste)  

menu(opcaoteste)


