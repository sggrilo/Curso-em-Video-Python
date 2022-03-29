# ANALISANDO TRIÂNGULO V1.0 — Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 10)
print('{: ^30}'.format('Analisador de Triângulos'))
print('-=-' * 10)
n1 = float(input('Digite o comprimento do 1º segmento de reta: '))
n2 = float(input('Digite o comprimento do 2º segmento de reta: '))
n3 = float(input('Digite o comprimento do 3º segmento de reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('É possível formar um triângulo de lados {}, {} e {} com esses segmentos de reta.'.format(n1, n2, n3))
else:
    print('É impossível formar um triângulo com esses segmentos de reta.')
