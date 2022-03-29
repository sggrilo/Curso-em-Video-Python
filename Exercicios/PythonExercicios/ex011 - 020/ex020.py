# SORTEANDO UMA ORDEM NA LISTA — O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem selecionada.

from random import shuffle

a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')

lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem sorteada foi {}.'.format(lista))
