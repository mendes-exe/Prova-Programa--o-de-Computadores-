from src.ler_arquivo_csv import ler_csv
from src.media import calc_media
from src.minimo import calc_minimo
from src.maximo import calc_max
from src.desv_pad import calc_desv_pad
from src.quartil import calc_quartil
from src.salvar_txt import save_txt

# menu
ler_csv()
calc_media()
calc_minimo()
calc_max()
calc_desv_pad()
calc_quartil()
save_txt(calc_media(), calc_minimo(), calc_max(), calc_desv_pad(), calc_quartil())


