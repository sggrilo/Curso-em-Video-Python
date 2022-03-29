# MAIOR E MENOR VALORES — Faça um programa que leia dois números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

# Verificando o menor número:

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando o maior número:

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior número digitado é {}.'.format(maior))
print('O menor número digitado é {}.'.format(menor))

# Ainda vai dar erro se pelo menos 2 números forem iguais...

# Desgraça triste abaixo:

'''if n1 > n2 and n1 > n3:
    print('O maior número é {}.'.format(n1))
if n1 == n2 and n1 > n3:
    print('O maior número é {}.'.format(n1))
if n1 > n2 and n1 == n3:
    print('O maior número é {}.'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior número é {}.'.format(n2))
if n2 > n1 and n2 == n3:
    print('O maior número é {}.'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor número é {}.'.format(n1))
if n1 == n2 and n1 < n3:
    print('O menor número é {}.'.format(n1))
if n1 < n2 and n1 == n3:
    print('O menor número é {}.'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor número é {}.'.format(n2))
if n2 < n1 and n2 == n3:
    print('O menor número é {}.'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número é {}'.format(n3))

if n1 == n2 and n1 == n3:
    print('{}, {} e {} têm o mesmo valor.'.format(n1, n2, n3))'''
