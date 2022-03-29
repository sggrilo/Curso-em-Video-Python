# CALCULANDO DESCONTOS — Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

n1 = float(input('Qual é o preço original do produto, em reais? '))

n2 = 0.95 * n1

print('O preço desse produto com 5% de desconto equivale a R${:.2f}.'.format(n2), end='\n')
