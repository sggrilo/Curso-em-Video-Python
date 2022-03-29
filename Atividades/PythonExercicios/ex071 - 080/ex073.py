# TUPLAS COM TIMES DE FUTEBOL — Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois, mostre:
#
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Chapecoense.

times = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bull Bragantino', 'Fluminense',
         'America', 'Atlético', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico Paranaense', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
separador = '-=-' * 10

print(separador)
print(f'Lista de times do Brasileirão: {times}')
print(separador)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(separador)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(separador)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(separador)
print(f'O {times[19]} está na {times.index(times[19]) + 1}ª posição.')

