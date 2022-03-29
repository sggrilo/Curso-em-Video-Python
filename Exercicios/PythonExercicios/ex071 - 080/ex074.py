# MAIOR E MENOR VALORES EM TUPLA — Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#
# Depois disso, mostre a listagem de números gerados e indique o maior e o menor valores que estão na tupla.

from random import randint

"""num1 = randint(1, 10)

maior = num1
menor = num1

num2 = randint(1, 10)

if num2 > maior:
    maior = num2
elif num2 < menor:
    menor = num2

num3 = randint(1, 10)

if num3 > maior:
    maior = num3
elif num3 < menor:
    menor = num3

num4 = randint(1, 10)

if num4 > maior:
    maior = num4
elif num4 < menor:
    menor = num4

num5 = randint(1, 10)

if num5 > maior:
    maior = num5
elif num5 < menor:
    menor = num5

num = (num1, num2, num3, num4, num5)"""

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# print(f'\nOs números sorteados foram: {num}')

print('Os números sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
print(f'\nO maior número sorteado foi {max(num)}.')
print(f'O menor número sorteado foi {min(num)}.')
