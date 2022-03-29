# NÚMEROS PRIMOS — Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from math import sqrt
num = int(input('Digite um número inteiro: '))
a = 0
for i in range(1, num+1):
    if num % i == 0:
        a += 1
if a == 2:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo.'.format(num))