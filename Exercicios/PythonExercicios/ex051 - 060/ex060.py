# CÁLCULO DO FATORIAL — Faça um programa que leia um número qualquer e mostre o seu fatorial.

from time import sleep

num = int(input('Digite um número natural: '))
num1 = num
while num < 1:
    print('\nErro. Tente novamente.\n')
    sleep(0.5)
    num = int(input('Digite um número natural: '))
    num1 = num
fat = num - 1
while fat > 1:
    num *= fat
    fat -= 1
print('{}! equivale a {}.'.format(num1, num))