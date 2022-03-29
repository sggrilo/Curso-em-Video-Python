# ANÁLISE DE DADOS EM UMA TUPLA — Desenvolva um programa que leia quatro
# valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os valores pares.

"""par1 = ''
par2 = ''
par3 = ''
par4 = ''

num1 = int(input('Digite um número inteiro: '))
if num1 % 2 == 0:
    par1 = num1
num2 = int(input('Digite outro número inteiro: '))
if num2 % 2 == 0:
    par2 = num2
num3 = int(input('Digite outro número inteiro: '))
if num3 % 2 == 0:
    par3 = num3
num4 = int(input('Digite outro número inteiro: '))
if num4 % 2 == 0:
    par4 = num4

num = (num1, num2, num3, num4)
if 9 in num:
    print(f'\nO número 9 foi digitado {num.count(9)} vezes.')
else:
    print('O número 9 não foi digitado.')
if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')
if par1 != '' or par2 != '' or par3 != '' or par4 != '':
    print(f'Os números pares digitados foram {par1} {par2} {par3} {par4}')
else:
    print('Nenhum número par foi digitado.')"""

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os números {num}.')
if 9 in num:
    print(f'\nO número 9 foi digitado {num.count(9)} vezes.')
else:
    print('O número 9 não foi digitado.')
if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
