# DIVIDINDO VALORES EM VÁRIAS LISTAS — Crie um programa que leia vários números e coloque-os em uma lista.
#
# Depois disso, crie duas listas extras que contenham apenas os valores
# pares e os valores ímpares digitados, respectivamente.
#
# Ao final, mostre o conteúdo das três listas geradas.

num = list()

while True:
    num.append(int(input('Digite um número inteiro: ')))
    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while resp not in 'SN':
        print('Resposta inválida. Tente novamente.')
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp in 'N':
        break
par = []
impar = []
for c in num:
    if c % 2 == 0:
        par.append(c)
    elif c % 2 == 1:
        impar.append(c)
print(f'Lista:   {num}')
print(f'Pares:   {par}')
print(f'Ímpares: {impar}')
