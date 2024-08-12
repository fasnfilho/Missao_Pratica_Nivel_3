from operacoes import calc_media
from operacoes import reprovacao
from operacoes import reprovados

dados_alunos = {
        '26': {'nome': 'Maria', 'notas': [8, 7, 5, 9]},
        '101': {'nome': 'Ana', 'notas': [9, 9, 8, 9]},
        '13': {'nome': 'João', 'notas': [6, 5, 5, 5]},
        '37': {'nome': 'Ágatha', 'notas': [8, 6, 7.5, 9]},
        '72': {'nome': 'Joaquim', 'notas': [6, 5.5, 5, 7]},
        '5': {'nome': 'Félix', 'notas': [10, 8, 8, 8]}
    }

matriculas_reprovados = []

for matricula, dados in dados_alunos.items():
    if reprovacao(dados['notas']):
        matriculas_reprovados.append(matricula)

relatorio = reprovados(dados_alunos, matriculas_reprovados)
print(relatorio)