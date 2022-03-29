# PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA — Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip()

nome = nome.split()
nome1 = nome[0]
nome2 = len(nome) - 1
print('Primeiro nome: {}'.format(nome1))
print('Último nome: {}'.format(nome2))
