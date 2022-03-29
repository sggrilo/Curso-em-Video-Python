# LISTAS COM PARES E ÍMPARES — Crie um programa em que o usuário possa digitar sete valores
# numéricos e que os cadastre em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º número inteiro: '))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
print('-=-' * 10)
num[0].sort()
num[1].sort()
print(f'Os números pares digitados foram: {num[0]}.')
print(f'Os números ímpares digitados foram: {num[1]}.')
