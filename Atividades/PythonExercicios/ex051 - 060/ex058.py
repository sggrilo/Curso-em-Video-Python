# JOGO DA ADIVINHAÇÃO V2.0 — Melhore o jogo do Desafio 028 em que o computador vai "pensar" em um número entre 0 e 10,
# mas agora o jogador vai tentar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
num = randint(0, 10)
resposta = 11
palpites = 0
print('-=-' * 22)
print('{: ^66}'.format('\033[1;36mEstou pensando em um número entre 0 e 10... Tente adivinhá-lo!\033[m'))
print('-=-' * 22)
print('\nEm que número eu pensei?')
while resposta != num:
    resposta = int(input('Digite aqui a sua resposta: '))
    print('\n\033[1;31mErrado!\033[m Tente novamente!')
    if resposta > num:
        print('\033[1;35mO número em que eu estou pensando é menor...\n\033[m')
    elif resposta < num:
        print('\033[1;35mO número em que eu estou pensando é maior...\n\033[m')
    palpites += 1
print('\n\033[1;32mCorreto!\033[m O número em que eu estava pensando era \033[1;33m{}\033[m.'.format(num))
print('Foram necessários \033[1;34m{}\033[m palpites para adivinhar esse número.'.format(palpites))
