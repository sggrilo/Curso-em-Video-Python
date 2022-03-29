# MAIS SOBRE MATRIZ EM PYTHON — Aprimore o desafio anterior, mostrando no final:
#
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l + 1}],[{c + 1}]: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print('-=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')
print('-=-' * 20)
print(f'A soma dos números pares equivale a {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos números da 3ª coluna equivale a {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior número da segunda linha é {mai}.')

"""maior = somacol = somapar = 0
num = list()
for i in range(1, 10):
    n = int(input('Digite um número inteiro de 0 a 9: '))
    while n < 0 or n > 9:
        print('Resposta Inválida. Por favor, tente novamente.')
        n = int(input('Digite um número inteiro de 0 a 9: '))
    num.append(n)
    if i == 3:
        somacol = num[i-1]
    elif i % 3 == 0:
        somacol = somacol + num[i-1]
    if i == 4:
        maior = num[i-1]
    elif 4 < i < 7:
        if num[i-1] > maior:
            maior = num[i-1]
    if num[i-1] % 2 == 0:
        somapar += num[i-1]
print('')
print('-=-' * 10)
for i in range(0, 3):
    print('[{: ^5}'.format(num[i]), end='] ')
print('')
for i in range(3, 6):
    print('[{: ^5}'.format(num[i]), end='] ')
print('')
for i in range(6, 9):
    print('[{: ^5}'.format(num[i]), end='] ')
print('')
print('-=-' * 10)
print(f'\nA soma de todos os números pares equivale a {somapar}.')
print(f'A soma dos números da 3ª coluna equivale a {somacol}.')
print(f'O maior número da segunda linha é {maior}.')"""
