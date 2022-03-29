# PROGRESSÃO ARITMÉTICA V2.0 — Refaça o Desafio 051, lendo o primeiro termo e a razão
# de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão dessa PA: '))
an = a1 + (10 - 1) * r
print('')

"""while a1 <= an:
    print(a1)
    a1 += r
print('\nFim')'"""

termo = a1
contador = 1
while contador <= 10:
    print(termo)
    termo += r
    contador += 1
print('\nFim')
