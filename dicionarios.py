# Criação do dicionário com pares chave/valor
meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}

# Impressão do conteúdo do dicionário
print("Conteudo do dicionario:", meu_dicionario)

# Impressão do tipo de dados do dicionário
print("Tipo de dados do dicionario:", type(meu_dicionario))

# Impressão do valor da chave 'linguagem' usando o método get
# Nota: Aqui estamos apenas exemplificando o uso do método get em uma chave que não existe diretamente.
# Para exibir a linguagem associada a cada código, usamos o dicionário diretamente.
for codigo in meu_dicionario:
    print(f"Linguagem com codigo {codigo}:", meu_dicionario.get(codigo))

# Impressão do tamanho do dicionário
print("Tamanho do dicionario:", len(meu_dicionario))

# Criação de um novo dicionário aninhado
dicionario_frutas = dict({
    1: {"nome": "limao", "tipo": "acida"},
    2: {"nome": "laranja", "tipo": "acida"},
    3: {"nome": "manga", "tipo": "semiacida"},
    4: {"nome": "maca", "tipo": "semiacida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamao", "tipo": "doce"}
})

# Impressão dos valores das chaves 'nome' e 'tipo' da chave 1
fruta_1 = dicionario_frutas[1]
print("Fruta da chave 1 - Nome:", fruta_1["nome"], "Tipo:", fruta_1["tipo"])

# Impressão dos valores das chaves 'nome' e 'tipo' da chave 2
fruta_2 = dicionario_frutas[2]
print("Fruta da chave 2 - Nome:", fruta_2["nome"], "Tipo:", fruta_2["tipo"])

# Iterando sobre o dicionário e imprimindo os valores das chaves 'nome' e 'tipo'
print("Valores de todas as frutas:")
for chave, fruta in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {fruta['nome']}, Tipo: {fruta['tipo']}")


