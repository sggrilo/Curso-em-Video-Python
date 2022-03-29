# COMPARANDO NÚMEROS — Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela:
#
# — O primeiro valor é maior
# — O segundo valor é maior
# — Não existe valor maior. Os dois são iguais.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print('')
if num1 > num2:
    print('{}, o primeiro valor, é o maior deles.'.format(num1))
elif num1 < num2:
    print('{}, o segundo valor, é o maior deles.'.format(num2))
elif num1 == num2:
    print('Não existe um valor maior. Os dois valores são iguais')
