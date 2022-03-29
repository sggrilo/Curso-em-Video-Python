# TRATANDO VÁRIOS VALORES V1.0 — Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar 999, sendo a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999).

num = 0
cont = 0
soma = 0
num = int(input('Digite um número inteiro [Digite 999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro [Digite 999 para parar]: '))
print('Você digitou {} números e a soma entre eles equivale a {}.'.format(cont, soma))
