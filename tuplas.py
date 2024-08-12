primeira_tupla = (1, 2, 3, 4, "Olá tupla")
print(primeira_tupla)
print(primeira_tupla.index(4))
x = 0
y = 0
for i in primeira_tupla:
    if(i == 3):
        print("Tem o número 3 nessa tupla!")
        x = 1

if(x == 0):
    print("Não tem o número 3 nessa tupla :(")

for i in primeira_tupla:
    if(i == 33):
        print("Tem o número 33 nessa tupla!")
        y = 1

if(y == 0):
    print("Não tem o número 33 nessa tupla :(")