# CADASTRO DE JOGADOR DE FUTEBOL — Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
# vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []

nome = input('Digite o nome do jogador: ')
jogador['nome'] = nome.strip().title()

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida nº {i + 1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=-' * 20)
print(jogador)
print('-=-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  ・ Na partida nº {i + 1}, ele fez {v} gols.')
print(f'  ・ Total: {jogador["total"]} gols.')
