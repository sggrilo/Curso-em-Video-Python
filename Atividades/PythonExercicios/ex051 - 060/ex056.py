# ANALISADOR COMPLETO — Desenvolva um programa que leia o nome,
# a idade e o sexo de 4 pessoas. No final do programa, mostre:
#
# — A média de idade do grupo.
# — Qual é o nome do homem mais velho.
# — Quantas mulheres têm menos de 20 anos.

velho = 0
soma = 0
soma1 = 0
nome1 = ''
for i in range(1, 5):
    print('')
    print('-=-' * 10)
    nome = input('Digite o nome de uma pessoa: ')
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = input('Digite M se essa pessoa for do sexo Masculino. Digite F se essa pessoa for de sexo feminino. ')
    print('-=-' * 10)
    sexo = sexo.strip()
    sexo = sexo.upper()
    soma += idade
    if sexo == 'M' and idade > velho:
        velho = idade
        nome1 = nome
    if sexo == 'F':
        if idade < 20:
            soma1 += 1
print('\nA média de idade do grupo é de {} anos.'.format(soma / 4))
if nome1 == '':
    print('', end='')
else:
    print('O homem mais velho do grupo é {}.'.format(nome1))
print('{} mulheres têm menos de 20 anos.'.format(soma1))
