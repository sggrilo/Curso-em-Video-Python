# PINTANDO PAREDE — Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m²

l = float(input('Qual é a largura em metros da parede a ser pintada? '))
h = float(input('E qual é a altura dela? '))

a = l * h
t = a / 2

print('Para pintar uma parede de {} m de largura e {} m de altura, '.format(l, h), end='')
print('cuja área equivale a {} m², serão necessários aproximadamente {:.2f} L de tinta.'.format(a, t))
