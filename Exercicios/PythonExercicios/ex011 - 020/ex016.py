# QUEBRANDO UM NÚMERO — Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.

from math import trunc
n = float(input('Digite um número: '))
i = trunc(n)
print('O número {} tem a parte inteira {}.'.format(n, i), end='\n')
