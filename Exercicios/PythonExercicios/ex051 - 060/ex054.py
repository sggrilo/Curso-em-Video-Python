# GRUPO DA MAIORIDADE — Crie um programa que leia o ano de nascimento de sete pessoas. No
# final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores.

from datetime import date
a = 0
b = 0
print('')
for i in range(0, 7):
    nas = int(input('Digite o ano de nascimento de uma pessoa: '))
    ano = date.today().year - nas
    a += 1
    if ano >= 18:
        b += 1
print('\nDessas {} pessoas, {} atingiram a maioridade.'.format(a, b))
print('{} delas ainda são menores de idade.'.format(a - b))
