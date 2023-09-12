from flask_login import UserMixin

from database_inject import insert, update
from database_consult import request


def registrar(nome, telefone_aluno, telefone_responsavel):
    try:
        dados = {'nome': nome, 'telefone_aluno': telefone_aluno, 'telefone_responsavel': telefone_responsavel}
        insert('alunos', [x for x in dados if dados[x]], [dados[x] for x in dados if dados[x]])
        return True
    except Exception as e:
        if 'Duplicate entry' in str(e):
            print('Já existe uma conta com este email.')
        else:
            print(e)
        return False

def buscar(_id=None, nome=None):
    return request('*', 'alunos', f'id = {_id}' if _id else f"nome = '{nome}'", limit=1)


class Aluno(UserMixin):
    """Acessar e escrever informações sobre o aluno"""

    def __init__(self, nome, _id=None):
        dados = buscar(_id) if _id else buscar(nome=nome)
        self.dados = dados
        self.id = dados[0]
        self.nome = dados[1]
        self.telefone_aluno = dados[2]
        self.telefone_responsavel = dados[3]


    def alterar(self, attrs):
        # Exemplo de uso: aluno.alterar({'cidades': '["Nova Friburgo", "Florestal", "Ouro Preto"]'})
        update('alunos', attrs, f'id = {self.id}')


registrar('Marcos', '5522999407306', '5522996063008')
erich = Aluno('Marcos')
print(erich.dados)