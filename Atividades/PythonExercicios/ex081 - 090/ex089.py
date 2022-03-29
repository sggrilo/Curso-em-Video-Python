# BOLETIM COM LISTAS COMPOSTAS — Crie um programa que leia o nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = []
while True:
    nome = input('\nNome: ').capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    if len(ficha) >= 998:
        print('\nMuitos alunos. Interrompendo cadastros posteriores...')
        break
    resp = input('\nQuer continuar? [S/N]: ').strip().upper()[0]
    while resp not in 'SN':
        print('\nResposta inválida. Tente novamente.')
        resp = input('\nQuer continuar? [S/N]: ').strip().upper()[0]
    if resp in 'N':
        break
print('')
print('-=-' * 8)
print(f'{"Nº ":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-' * 24)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>10.1f}')
print('')
while True:
    print('-=-' * 8)
    print('')
    opc = int(input('Mostrar notas de qual aluno? [Digite seu Nº na lista de alunos para selecioná-lo. Digite 999 para'
                    ' interromper]: '))
    while opc > len(ficha) - 1:
        print('\nResposta inválida. Tente novamente.')
        opc = int(input(
            '\nMostrar notas de qual aluno? [Digite seu Nº na lista de alunos para selecioná-lo. Digite 999 para'
            ' interromper]: '))
    if opc == 999:
        print('')
        print('-=-' * 8)
        print('Finalizando...')
        break
    if opc <= len(ficha):
        print(f'\nAs notas de {ficha[opc][0]} são {ficha[opc][1]}\n')
print('-=-' * 8)


"""classe = list()
nomes = list()
notas = list()
opt = 'Among Us'
medias = list()
med = i = a = 0
while True:
    if len(nomes) == 998:
        print('Muitos alunos. Interrompendo...')
        break
    nomes.append(input('Nome: ').capitalize())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    classe.append(nomes[:])
    classe.append(notas[:])
    med = (notas[2 * i] + notas[2 * i + 1]) / 2
    medias.append(med)
    i += 1
    opt = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while opt not in 'SN':
        print('Resposta inválida. Tente novamente.')
        opt = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if opt in 'N':
        break
print('-=-' * 8)
print('Nº  NOME           MÉDIA')
print('-' * 24)
for c in nomes:
    print(f'{a: <4}', end='')
    print(f'{c: <15}', end='')
    print(f'{medias[a]:.1f}')
    a += 1
print('-' * 24)
while True:
    b = int(input('Mostrar notas de qual aluno? [Digite seu Nº na lista de alunos para selecioná-lo. Digite 999 para '
                  'interromper]: '))
    if b == 999:
        print('-' * 24)
        print('Finalizando...')
        break
    print(f'As notas de {nomes[b]} são {notas[2*b:2*b+2]}')
    print('-' * 24)"""
