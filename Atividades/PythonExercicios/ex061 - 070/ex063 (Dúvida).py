# SEQUÊNCIA DE FIBONACCI V1.0 — Escreva um programa que leia um número inteiro 'N'
# qualquer e mostre na tela os 'N' primeiros elementos da Sequência de Fibonacci.

num = int(input('Digite um número inteiro: '))

t1 = 0
t2 = 1

print(t1)
print(t2)

contador = 3
while contador <= num:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    contador += 1
print('Fim.')

