# FUNÇÃO QUE DESCOBRE O MAIOR — Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep

n = 0
num = []


def linha():
    print('-=-' * 10)


def maior():
    num.sort()


while True:
    linha()
    n = abs(int(input('Analisar quantos valores? ')))
    if n == 0:
        print('\nNenhum valor foi analisado.')
        print('Logo, não existe um valor maior.')
    else:
        for i in range(0, n):
            num.append(randint(0, 9))
        for i in num:
            sleep(0.25)
            print(i, end='   ')
        sleep(0.25)
        print('')
        print(f'Foram analisados {len(num)} valores ao todo.')
        maior()
        mai = num[-1]
        print(f'O maior valor entre eles é {mai}.')
        num.clear()
    linha()
    escolha = input('Quer continuar? [S/N] ').upper()[0]
    while escolha not in 'SN':
        print('Resposta inválida. Por favor, digite apenas S ou N.')
    if escolha in 'N':
        break

"""from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=-' * 10)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()"""
