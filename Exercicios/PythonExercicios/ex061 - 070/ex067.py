# TABUADA V3.0 — Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
# valor digitado pelo usuário. O programa será interrompido quando o valor solicitado for negativo.

num = 0
while num >= 0:
    num = int(input('\nDigite um número inteiro não negativo para ver sua tabuada: '))
    if num < 0:
        break
    print('')
    print('-=-' * 6)
    print(f'A tabuada de {num} é:\n')
    for i in range(1, 11):
        print(f'{num} * {i} = {num * i}')
    print('-=-' * 6)
print('Desligando...')
