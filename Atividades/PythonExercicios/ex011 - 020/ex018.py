# SENO, COSSENO E TANGENTE — Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = float(input('Digite o valor de um ângulo, em graus: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print('O seno de {} equivale a aproximadamente {:.2f}.'.format(ang, sen))
print('O cosseno de {} equivale a aproximadamente {:.2f}.'.format(ang, cos))
print('A tangente de {} equivale a aproximadamente {:.2f}.'.format(ang, tg))
