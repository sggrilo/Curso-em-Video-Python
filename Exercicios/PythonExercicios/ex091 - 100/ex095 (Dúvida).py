# APRIMORANDO OS DICIONÁRIOS — Aprimore o Desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    nome = input('Digite o nome do jogador: ')
    jogador['nome'] = nome.strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['partidas'] = partidas
    gols.clear()
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida nº {i + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    escolha = input('Quer continuar? [S/N] ').strip().title()[0]
    while escolha not in 'SN':
        print('Resposta inválida. Por favor, digite apenas S ou N.')
        escolha = input('Quer continuar? [S/N] ').strip().title()[0]
    if escolha in 'N':
        break
print('-=-' * 20)
print(f'{"Nº":<4}{"NOME":<15}{"GOLS":<15}TOTAL')
print('-' * 39)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print('')
print('-=-' * 20)
while True:
    indice = int(input('\nMostrar dados de qual jogador? [Digite seu número na lista para selecioná-lo. Digite 999 '
                       'para interromper o programa.'))
    if indice == 999:
        break
    elif indice >= len(time):
        print('\nResposta inválida. Por favor, digite um número existente na lista.')
    else:
        print(f'\nLevantamento do jogador {time[indice]["nome"]}:')
        print('-' * 39)
        print(f'O jogador {time[indice]["nome"]} jogou {time[indice]["partidas"]} partidas.')
        for i, v in enumerate(time[indice]['gols']):
            print(f'  ・ Na partida nº {i + 1}, ele fez {v} gols.')
        print(f'  ・ Total: {time[indice]["total"]} gols.')
