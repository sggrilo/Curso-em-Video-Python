# UNINDO DICIONÁRIOS E LISTAS — Crie um programa que leia o nome, a idade e o sexo de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

galera = []
mulheres = []
pessoa = {}
media = 0
while True:
    pessoa['Nome'] = input('Digite o nome: ').strip().title()
    pessoa['Sexo'] = input('Digite o sexo [M/F]: ').strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        print('Resposta inválida. Por favor, digite apenas M ou F.')
        pessoa['Sexo'] = input('Digite o sexo [M/F]: ').strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
    pessoa['Idade'] = int(input('Digite a idade: '))
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'].strip().title())
    galera.append(pessoa.copy())
    escolha = input('Quer continuar? [S/N] ').strip().title()[0]
    while escolha not in 'SN':
        print('Resposta inválida. Por favor, digite apenas S ou N.')
        escolha = input('Quer continuar? [S/N] ').strip().title()[0]
    if escolha in 'N':
        break
print('-=-' * 20)
for i in galera:
    media += i['Idade']
media /= len(galera)
print(f'— O grupo tem {len(galera)} pessoas.')
print(f'— A média de idade é de {media:.2f} anos.')
print(f'— As mulheres cadastradas foram: {mulheres}')
print(f'— Lista das pessoas com idade acima da média:')
for i in galera:
    if i['Idade'] > media:
        print(f'  ・ Nome: {i["Nome"]}; Idade: {i["Idade"]}; Sexo: {i["Sexo"]}')
