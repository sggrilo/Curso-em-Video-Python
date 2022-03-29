# SOMA DOS PARES — Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('=-' * 12)
print('{: ^24}'.format('Soma dos Números Pares'))
print('=-' * 12, '\n')

s = 0
cont = 1
for i in range(1, 7):
    num = int(input('Digite o {}º número: '.format(cont)))
    if num % 2 == 0:
        s += num
        cont += 1
print('\nA soma dos {} números pares equivale a {}.'.format(cont, s))
