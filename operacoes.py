def calc_media(notas):
    soma = 0
    media = 0
    for i in range(4):
        soma = soma + notas[i]
    media = soma / 4
    return media

def reprovacao(notas):
    media = calc_media(notas)
    if(media < 6):
        return True
    return False

def reprovados(dados_alunos, matriculas_reprovados):
    lista = ""
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula)
        if aluno:
            nome = aluno['nome']
            media = calc_media(aluno['notas'])
            lista += (f'Aluno Reprovado: {nome} - Matrícula: {matricula} - Média Final: {media:.2f}\n')
    return lista
