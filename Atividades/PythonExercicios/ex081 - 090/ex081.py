# EXTRAINDO DADOS DE UMA LISTA — Crie um programa que leia vários números e coloque-os em uma lista.
# Depois disso, mostre:
# A) Quantos números forma digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o número 5 foi digitado e se está ou não na lista.

num = []

while True:
    num.append(int(input('Digite um número inteiro: ')))
    opt = input('Deseja continuar? [S/N]: ')
    print('')
    opt = opt.title()
    while opt not in 'SimNãoNao':
        print('\033[1;31mEntrada inválida. Tente novamente.\n\033[m')
        opt = input('Deseja continuar? [S/N]: ')
        opt = opt.title()
        print('')
    if opt in 'NãoNao':
        break
print(f'Na lista {num} foram digitados {len(num)} números.')
num.sort(reverse=True)
print(f'Essa lista na ordem decrescente é {num}.')
if 5 in num:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
