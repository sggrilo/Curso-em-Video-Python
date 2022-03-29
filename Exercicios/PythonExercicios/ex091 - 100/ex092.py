# CADASTRO DE TRABALHADOR EM PYTHON — Crie um programa que leia o nome, o ano de nascimento e a carteira de trabalho de
# uma pessoa e os cadastre (com a idade) em um dicionário. Se a CTPS diferir de zero, o dicionário receberá também o
# ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = {}

nome = input('Digite o seu nome: ')
dados['Nome'] = nome.strip().title()

anonas = int(input('Digite o seu ano de nascimento: '))
dados['Idade'] = date.today().year - anonas

dados['CTPS'] = int(input('Digite sua carteira de trabalho (digite 0 se não a tiver): '))
if dados['CTPS'] != 0:
    anocon = int(input('Digite o seu ano de contratação: '))
    dados['Ano de contratação'] = anocon
    dados['Salário'] = float(input('Digite o seu salário: R$'))
    idacon = anocon - anonas
    idaapo = idacon + 35
    dados['Idade da Aposentadoria'] = idaapo
print('')
for k, v in dados.items():
    print(f'{k}: {v}')
