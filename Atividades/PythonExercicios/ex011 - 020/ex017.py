# CATETOS E HIPOTENUSA — Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt
co = float(input('Digite o comprimento de um dos catetos de um triângulo retângulo: '))
ca = float(input('Digite o comprimento de outro cateto desse triângulo: '))
hip2 = co ** 2 + ca ** 2
hip = sqrt(hip2)
print('O comprimento da hipotenusa desse triângulo, cujos catetos equivalem a {} e {}, é de {}.'.format(co, ca, hip))
