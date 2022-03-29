# PALPITES PARA A MEGA SENA — Faça um programa que ajude um jogador da Mega Sena a criar
# palpites. O programa vai perguntar quantos jogos serão sorteados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = []
jogos = []
print('-=-' * 11)
print('{: ^33}'.format('MEGA SENA'))
print('-=-' * 11)
quant = int(input('\nQuantos jogos serão sorteados? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('')
print('-=-' * 2, f' SORTEANDO {quant} JOGOS ', '-=-' * 2)
print('')
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {l}')
print('')
print('-=-' * 3, f'  BOA SORTE! ', '-=-' * 3)

"""from random import randint
b = 0
jogo = list()
print('-=-' * 10)
print('{: ^30}'.format('JOGA NA MEGA SENA'))
print('-=-' * 10)
num = int(input('\nQuantos jogos serão sorteados? '))
while num < 1:
    print('\nResposta inválida. Tente novamente.')
    num = int(input('\nQuantos jogos serão sorteados? '))
print('')
print('{:-^30}'.format(f' SORTEANDO {num} JOGOS '))
for i in range(0, num*6):
    jogo.append(randint(1, 60))
for a in range(0, num):
    b = a + 1
    print(f'Jogo {a+1}: ', end='')
    pao = jogo[a*6:b*6]
    print(sorted(pao))
print('')
print('{:-^30}'.format(' BOA SORTE! '))"""
