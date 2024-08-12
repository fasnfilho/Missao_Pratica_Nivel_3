lista_mesclada = [1, 2, 3, "Olá Pyhton", True, 12.6]
print(lista_mesclada)
lista_mesclada.append("Lista_aninhada")
print(lista_mesclada)
lista_mesclada.insert(4, 5)
print(lista_mesclada)
print(len(lista_mesclada))
lista_mesclada.remove(1)
print(lista_mesclada)
nova_lista_mesclada = []
for i in range(5):
    nova_lista_mesclada.append(lista_mesclada[i])
print(nova_lista_mesclada)
