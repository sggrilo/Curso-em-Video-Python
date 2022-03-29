# MAIOR E MENOR DA SEQUÊNCIA — Faça um programa que leia o peso de cinco
# pessoas. No final, mostre quais foram o maior e o menor peso lidos.

maior = 0
menor = 0
print('')
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\nO maior peso foi de {} kg'.format(maior))
print('O menor peso foi de {} kg'.format(menor))
