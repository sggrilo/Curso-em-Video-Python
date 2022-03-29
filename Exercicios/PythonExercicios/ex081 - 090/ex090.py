# DICIONÁRIO EM PYTHON — Faça um programa que leia o nome e a média de um aluno, guardando também
# a sua situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = input('Nome do aluno: ')
aluno['Nome'] = aluno['Nome'].strip().title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado(a)'
elif 5.0 <= aluno['Média'] < 7.0:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'
print('')
for k, v in aluno.items():
    print(f'{k}: {v}')
