# LISTA ORDENADA SEM REPETIÇÕES — Crie um programa em que o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#
# No final, mostre a lista ordenada na tela.

a = maior = menor = 0

num = []
for c in range(0, 5):
    n = int(input('Digite um número inteiro: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Número adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Número adicionado à {pos + 1}ª posição da lista.')
                break
            pos += 1
print(f'Os números digitados em ordem crescente foram {num}')
