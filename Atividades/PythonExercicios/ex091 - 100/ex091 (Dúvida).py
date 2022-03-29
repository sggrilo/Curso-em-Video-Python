# JOGO DE DADOS EM PYTHON — Crie um programa em que 4 jogadores rolem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque
# esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = dict()
print('Valores sorteados:')
sleep(0.5)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\nRanking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'  ・ {i+1}º lugar: {v[0]} - resultado {v[1]}.')
    sleep(0.5)

"""from random import randint
from time import sleep

jogo = []
jogador = {}

for i in range(1, 5):
    nome = input(f'Digite seu nome, jogador {i}: ')
    jogador['nome'] = nome.strip().title()
    jogador['dado'] = randint(1, 6)
    jogo.append(jogador.copy())

sleep(1)
print('\nValores sorteados: ')
sleep(1)
for a in jogo:
    print(f'  ・ {a["nome"]} tirou {a["dado"]}.')
    sleep(0.75)

sleep(1)
print('\nRanking dos jogadores: ')
sleep(1)
for r in range(0, 4):
    print(f'  ・ {r + 1}º lugar: NOME - resultado DADO')
    sleep(0.75)"""
