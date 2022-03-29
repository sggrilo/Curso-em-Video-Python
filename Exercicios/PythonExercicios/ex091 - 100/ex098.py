# FUNÇÃO DE CONTADOR — Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize a contagem.
#
# Seu programa tem que realizar três contagens através da função criada:
#
# A) De 1 até 10, de 1 em 1.
# B) De 10 até 0, de 2 em 2.
# C) Uma contagem personalizada.

from time import sleep


def linha():
    print('-=-' * 10)


def contador(inicio, fim, passo):
    linha()
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} a {fim}, de {abs(passo)} em {abs(passo)}:')
    sleep(1)
    if inicio > fim:
        for i in range(inicio, fim - 1, abs(passo) * -1):
            sleep(0.25)
            print(f'{i} ', end='', flush=True)
    elif inicio < fim:
        for i in range(inicio, fim + 1, passo):
            sleep(0.25)
            print(f'{i} ', end='', flush=True)
    sleep(0.25)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
linha()
