novo_dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

novo_dicionario.update({
    2: {'nome': 'Jose', 'idade': 40, 'nacionalidade': 'espanhol'},
    3: {'nome': 'James', 'idade': 3, 'nacionalidade': 'americano'}
})

print(novo_dicionario)

dicionario_final = novo_dicionario.copy()
novo_dicionario.pop(2)
novo_dicionario.popitem()
print(novo_dicionario)
novo_dicionario.clear()
dicionario_final.clear()

x = ('a', 'b', 'c')
y = 1

dict = dict.fromkeys(x, y)
print(dict.items())
print(dict.keys())
print(dict.values())
