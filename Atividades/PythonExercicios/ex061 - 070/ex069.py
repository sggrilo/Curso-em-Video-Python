# ANÁLISE DE DADOS DO GRUPO — Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar ao usuário se ele quer ou não continuar. No final, mostre:
#
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

maior = homens = fmenor = idade = 0
cont = 'S'
a = True
sexo = 'Jabuti'
while a:
    print('')
    print('-=-' * 7)
    print('{: ^21}'.format('Cadastre uma Pessoa'))
    print('-=-' * 7)
    idade = int(input('\nDigite a idade de uma pessoa: '))
    if idade > 18:
        maior += 1
    sexo = input('Digite o sexo dessa pessoa. [M/F]: ').strip()[0]
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        fmenor += 1
    while sexo not in 'MmFf':
        print('\n\033[1;31mResposta inválida. Tente novamente.\033[m\n')
        sexo = input('Digite o sexo dessa pessoa [M/F]: ')
    cont = input('\nDeseja continuar? [S/N]: ').strip()[0]
    if cont in 'Nn':
        a = False
    while cont not in 'SsNn':
        print('\n\033[1;31mResposta inválida. Tente novamente.\033[m\n')
        cont = input('Deseja continuar? [S/N]: ')
print('''\nAo todo, {} pessoas têm mais de 18 anos.
Há {} homens no total.
Também há {} mulheres com menos de 20 anos.'''.format(maior, homens, fmenor))
