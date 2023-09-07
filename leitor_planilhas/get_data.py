import pandas as pd

# Delimitadores
path = 'C:/Users/Usuario/Documents/Erich/GitHub/proforco/leitor_planilhas'
planilha = pd.read_excel(path+'/PAINEL DE AULAS.xlsx', sheet_name="FIXO SEGUNDA")
colunas = list(planilha.columns)
posX = [colunas.index(x) for x in colunas if x.startswith('ERICH')][0]
colunas_usadas = colunas[posX:posX+3] 
data = planilha[colunas_usadas]
data = data.dropna()
print(data)
