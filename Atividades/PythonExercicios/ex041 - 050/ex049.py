# TABUADA V2.0 — Refaça o Desafio 009, mostrando a tabuada de um número
# que o usuário escolher, mas utilizando um laço for.

num = int(input('Digite um número inteiro para ver sua tabuada: '))
print('-=-' * 5)
for i in range(1, 11):
    tab = num * i
    print('{} * {} = {}'.format(num, i, tab))
print('-=-' * 5)
