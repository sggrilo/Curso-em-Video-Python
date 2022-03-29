# SORTEANDO UM ITEM NA LISTA — Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que o ajude, lendo o nome dos alunos e escrevendo o nome de um aluno escolhido.

from random import choice

a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('O aluno escolhido foi {}.'.format(escolhido))
