# SOMANDO DOIS NÚMEROS — Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2

# Com os valores de n1 e n2:

# print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre \033[1;31m{0}\033[m e \033[1;34m{1}\033[m vale \033[1;35m{2}\033[m.'.format(n1, n2, s))
# print(f'A soma entre {n1} e {n2} vale {s}.')

# Sem os valores de n1 e n2:

# print('A soma vale, s)
# print('A soma vale {}.'.format(s))
# print(f'A soma vale {s}.')
