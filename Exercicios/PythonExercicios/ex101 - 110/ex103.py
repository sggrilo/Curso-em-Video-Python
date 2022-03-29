# FICHA DO JOGADOR — Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#
# O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não
# tenha sido informado corretamente.

def ficha(jog='desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip == '':
    ficha(gol=g)
else:
    ficha(n, g)

"""def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    if gols != '':
        gols = int(gols)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


ficha(input('Nome do jogador: ').strip().title(), input('Número de gols: '))"""
