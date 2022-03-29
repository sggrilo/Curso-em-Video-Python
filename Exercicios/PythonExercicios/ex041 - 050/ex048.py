# SOMA ÍMPARES MÚLTIPLOS DE TRÊS — Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.

s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i)
        s += i
        cont += 1
print('\nA soma entre todos os \033[1;34m{}\033[m números equivale a \033[1;34m{}\033[m'.format(cont, s))
