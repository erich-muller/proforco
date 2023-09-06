import pandas as pd
from datetime import datetime

# path = 'C:/Users/Usuario/Documents/Erich/GitHub/proforco/leitor_planilhas'
# planilha = pd.read_excel(path+'/PAINEL DE AULAS.xlsx', sheet_name="FIXO SEGUNDA", usecols='AU,AW', nrows=29)
# headers = list(planilha.columns)
# print(headers)
# alunos = [x.strip() for x in planilha[headers[0]] if type(x) == str]
# print(alunos, type(alunos[0]))

# Delimitadores
path = 'C:/Users/Usuario/Documents/Erich/GitHub/proforco/leitor_planilhas'
planilha = pd.read_excel(path+'/PAINEL DE AULAS.xlsx', sheet_name="FIXO SEGUNDA")
headers = list(planilha.columns)
posX = [headers.index(x) for x in headers if x.startswith('ERICH')][0]
used_headers = headers[posX:posX+3] 
data = planilha[used_headers]
# planilha[posY:posY+3]
print(data[data.notnull()])
