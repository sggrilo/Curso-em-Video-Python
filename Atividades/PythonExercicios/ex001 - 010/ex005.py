# ANTECESSOR E SUCESSOR — Faça um programa que leia um número
# inteiro e mostre na tela o seu antecessor e o seu sucessor.

n = int(input('Digite um número inteiro: '))

a = n - 1
s = n + 1

print('O antecessor de \033[4;33m{}\033[m equivale a \033[4;31m{}\033[m. '.format(n, a), end='')
print('Seu sucessor equivale a \033[4;32m{}\033[m.'.format(s))
