# PROGRESSÃO ARITMÉTICA — Desenvolva um programa que leia o primeiro termo e a
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão dessa PA: '))
an = a1 + (10 - 1) * r
print('')
for i in range(a1, an + r, r):
    print(i)
