# JOGO DO PAR OU ÍMPAR — Faça um programa que jogue par ou ímpar com o usuário. O jogo só será interrompido
# quando o usuário perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('-=-' * 4)
print('\033[1;34mPar ou Ímpar\033[m')
print('-=-' * 4, end='\n\n')

com = randint(0, 10)
ganhou = True
streak = resultado = soma = 0

while ganhou:
    confirm = input('Digite [Par] ou [Ímpar] para escolher uma opção: ').strip().title()
    while confirm not in 'ParÍmparImpar':
        print('Entrada inválida. Tente novamente.\n')
        confirm = input('Digite [Par] ou [Ímpar] para escolher uma opção: ').strip().title()
    p1 = int(input('Digite um número de 0 a 10 para jogar: '))
    while p1 < 0 or p1 > 10:
        print('Entrada inválida. Tente novamente.\n')
        p1 = int(input('Digite um número de 0 a 10 para jogar: '))
    print(f'\nVocê escolheu o número {p1}. O computador escolheu o número {com}.\n')
    soma = p1 + com
    if p1 % 2 == 0 and com % 2 == 0 and confirm == 'Par':
        print(f'{p1} + {com} = {soma}, um número Par.')
        print('\033[1;32mParabéns! Você venceu!\033[m\n')
        com = randint(0, 10)
        streak += 1
    elif p1 % 2 != 0 and com % 2 != 0 and confirm == 'Par':
        print(f'{p1} + {com} = {soma}, um número Par.')
        print('\033[1;32mParabéns! Você venceu!\033[m\n')
        com = randint(0, 10)
        streak += 1
    elif p1 % 2 == 0 and com % 2 != 0 and confirm == 'Ímpar':
        print(f'{p1} + {com} = {soma}, um número Ímpar.')
        print('\033[1;32mParabéns! Você venceu!\033[m\n')
        com = randint(0, 10)
        streak += 1
    elif p1 % 2 != 0 and com % 2 == 0 and confirm == 'Ímpar':
        print(f'{p1} + {com} = {soma}, um número Ímpar.')
        print('\033[1;32mParabéns! Você venceu!\033[m\n')
        com = randint(0, 10)
        streak += 1
    else:
        if p1 % 2 == 0:
            print(f'{p1} + {com} = {soma}, um número Ímpar.')
            print('\033[1;31mQue pena! Você perdeu!\033[m')
            break
        else:
            print(f'{p1} + {com} = {soma}, um número Par.')
            print('\033[1;31mQue pena! Você perdeu!\033[m')
            break
    print('\033[1;33mVamos jogar novamente!\033[m\n')
print(f'\n\033[1;35mFim de Jogo!\033[m\nVocê conseguiu {streak} vitórias consecutivas! Parabéns!')

"""from random import randint

jogador = computador = total = v = 0
tipo = ''

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}. ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')"""
