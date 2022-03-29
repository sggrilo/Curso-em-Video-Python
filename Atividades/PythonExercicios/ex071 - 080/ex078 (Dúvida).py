# MAIOR E MENOR VALORES NA LISTA — Faça um programa que leia 5 valores numéricos e guarde-os e uma lista.
# No final, mostre quais foram o menor e o maior valores digitados e suas respectivas posições na lista.

maior = menor = posmaior = posmenor = 0
num = []
for i in range(0, 5):
    num.append(int(input(f'Digite um número para a {i + 1} posição: ')))
    if i == 0:
        maior = menor = num[i]
        posmaior = posmenor = i + 1
    else:
        if num[i] > maior:
            maior = num[i]
            posmaior = i + 1
        if num[i] < menor:
            menor = num[i]
            posmenor = i + 1
print(f'O maior número entre {num} foi {maior}, encontrado nas posições ', end='')
for pos, val in enumerate(num):
    if val == maior:
        print(f'{pos} ', end='')
print(f'Já o menor número entre esses foi {menor}, encontrado nas posições ', end='')
for pos, val in enumerate(num):
    if val == menor:
        print(f'{pos} ', end='')
