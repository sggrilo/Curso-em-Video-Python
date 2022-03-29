# LISTA COMPOSTA E ANÁLISE DE DADOS — Faça um programa que leia o nome e o
# peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [S/N] ').strip().capitalize()[0]
    while resp not in 'SN':
        print('Resposta Inválida. Por favor, tente novamente.')
        resp = input('Quer continuar? [S/N] ').strip().capitalize()[0]
    if resp in 'N':
        break
print('-=-' * 20)
print(f'Ao todo, foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso cadastrado foi de {mai} kg. Peso de: ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso cadastrado foi de {men} kg. Peso de: ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

"""pessoas = list()
dados = list()
pmaior = list()
pmenor = list()
np = pma = pme = 0
while True:
    dados.append(input('\nNome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    np += 1
    confirm = input('\nDeseja continuar? [S/N]: ')
    confirm = confirm.strip().upper()[0]
    while confirm not in 'SN':
        print('\nResposta Inválida. Por favor, tente novamente.')
        confirm = input('\nDeseja continuar? [S/N]: ')
        confirm = confirm.strip().upper()[0]
    if confirm in 'N':
        print('-=-' * 10)
        break
print(pessoas)
print(f'Ao todo, foram digitados os nomes de {np} pessoas.')
print(pmaior)
print(pmenor)"""
