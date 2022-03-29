# CONVERSOR DE MOEDAS — Crie um programa que mostre quanto dinheiro
# uma pessoa tem na carteira e quantos dólares ela pode comprar.
#
# Considere US$1.00 = R$ 3.27

r = float(input('Quantos reais você tem? '))

d = r / 3.27

print('Com R${:.2f}, é possível obter US${:.2f}.'.format(r, d), end='\n')
