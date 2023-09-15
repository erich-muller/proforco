# RESPONSÁVEL POR PREPARAR OS DADOS
# DE ACORDO COM A NECESSIDADE

from datetime import datetime
from gerador_json import gerar_json


class Data():
    def __init__(self, caminho='C:/Users/erich/Downloads/PAINEL DE AULAS.xlsx') -> None:
        self.caminho = caminho

    def get_today(self):
        dias = ['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA']
        return  dias[datetime.today().weekday()]
    
    def get_json(self, dia):
        return gerar_json(self.caminho, dia)


x = Data()
print(x.get_json('SEGUNDA'))