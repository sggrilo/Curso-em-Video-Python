# MATRIZ EM PYTHON — Crie um programa que crie uma matriz de dimensões
# 3 × 3 e a preencha com números lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}],[{c+1}]: '))
print('-=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')

"""num = list()
for i in range(1, 10):
    n = int(input('Digite um número inteiro de 0 a 9: '))
    while n < 0 or n > 9:
        print('Resposta Inválida. Por favor, tente novamente.')
        n = int(input('Digite um número inteiro de 0 a 9: '))
    num.append(n)
print('-=-' * 10)
for i in range(0, 3):
    print('[{: ^5}'.format(num[i]), end='] ')
print('')
for i in range(3, 6):
    print('[{: ^5}'.format(num[i]), end='] ')
print('')
for i in range(6, 9):
    print('[{: ^5}'.format(num[i]), end='] ')"""
