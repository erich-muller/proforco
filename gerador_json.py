from leitor_planilhas.planilha import Planilha
import bd.aluno 


def gerar_json(path, dia):
    planilha = Planilha(path)
    dados = planilha.get_alunos(dia)

    sem_cadastro = []
    json = {}

    for d in dados:
        if bd.aluno.buscar(nome=d[0]):
            aluno = bd.aluno.Aluno(d[0])
            json[aluno.nome] = {
                'hora': d[1],
                'telefone_aluno': aluno.telefone_aluno,
                'telefone_responsavel': aluno.telefone_responsavel}
        else:
            sem_cadastro.append(d[0])

    json['sem_cadastro'] = sem_cadastro
    return(json)