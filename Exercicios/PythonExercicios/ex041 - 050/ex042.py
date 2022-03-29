# ANALISANDO TRIÂNGULOS V2.0 — Refaça o Desafio 35 dos triângulos, acrescentando
# o recurso de mostrar que categoria de triângulo será formado:
#
# — Equilátero: Todos os lados congruentes
# — Isósceles: Dois lados congruentes
# — Escaleno: Todos os lados diferentes

n1 = float(input('Digite o comprimento do 1º segmento de reta: '))
n2 = float(input('Digite o comprimento do 2º segmento de reta: '))
n3 = float(input('Digite o comprimento do 3º segmento de reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('\nEsses segmentos de reta podem formar um triângulo.')
    if n1 == n2 == n3:
        print('O triângulo formado será um triângulo equilátero.')
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('O triângulo formado será um triângulo isósceles.')
    else:
        print('O triângulo formado será um triângulo escaleno.')
else:
    print('\nEsses segmentos de reta não podem formar um triângulo.')
