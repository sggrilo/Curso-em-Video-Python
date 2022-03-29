# FUNÇÕES PARA SORTEAR E SOMAR — Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los na lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 números para a lista: ', end='')
    for cont in range(0, 5):
        lista.append(randint(1, 10))
    for i in numeros:
        sleep(0.25)
        print(i, end='  ', flush=True)
    sleep(0.25)
    print('Fim!')
    sleep(0.25)


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma entre os números pares da lista {numeros} equivale a {soma}.')


numeros = []
sorteia(numeros)
somapar(numeros)
