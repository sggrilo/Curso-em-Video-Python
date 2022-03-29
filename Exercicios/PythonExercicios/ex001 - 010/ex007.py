# MÉDIA ARITMÉTICA — Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

m = (n1 + n2) / 2

print('\nA média desse aluno equivale a {:.1f}.'.format(m), end='')
