from leitor_planilhas.planilha import Planilha
import bd.aluno 

dia = 'FIXO SEGUNDA'
caminho = 'C:/Users/Usuario/Documents/Erich/GitHub/proforco/leitor_planilhas/PAINEL DE AULAS.xlsx'
# caminho = 'C:/Users/erich/Downloads/PAINEL DE AULAS.xlsx'
teste = Planilha(caminho)
dados = teste.get_alunos(dia)

nao_adds = []
json = {}

for d in dados:
    if bd.aluno.buscar(nome=d[0]):
        aluno = bd.aluno.Aluno(d[0])
        json[aluno.nome] = {
            'hora': d[1],
            'telefone_aluno': aluno.telefone_aluno,
            'telefone_responsavel': aluno.telefone_responsavel}
    else:
        nao_adds.append(d[0])


print(len(nao_adds), 'não cadastrados.')
if input('Iniciar cadastro? ') == '':
    for nome in nao_adds:
        print(nome)
        telefone_aluno = input('TELEFONE ALUNO: ')
        telefone_responsavel = input('TELEFONE RESPONSÁVEL: ')
        bd.aluno.registrar(nome, telefone_aluno, telefone_responsavel)


print(json)