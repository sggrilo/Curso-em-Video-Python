# REAJUSTE SALARIAL — Faça um algoritmo que leia o salário de um
# funcionário e mostre seu novo salário, com 15% de aumento.

i = float(input('Qual era o salário original do funcionário, em reais? '))

f = 1.15 * i

print('O novo salário desse funcionário, com 15% de aumento, equivale a R${:.2f}.'.format(f))
