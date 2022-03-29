# CRIANDO UM MENU DE OPÇÕES — Crie um programa que leia dois valores e mostre um menu na tela:
#
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

menu = 0

num1 = float(input('\nDigite um número: '))
num2 = float(input('Digite outro número: '))

soma = 0

produto = 0

maior = 0
menor = 0

while menu != 5:
    print('\nO que você deseja fazer com os números {} e {}?'.format(num1, num2))
    print('''\n[1] — Somá-los
[2] — Multiplicá-los
[3] — Verificar qual deles é o maior
[4] — Escolher outros números
[5] — Sair do programa''')
    menu = int(input('\nDigite aqui a sua escolha: '))
    sleep(1)
    if menu == 1:
        soma = num1 + num2
        print('\nA soma entre {} e {} equivale a {}.'.format(num1, num2, soma))
        sleep(1.5)
    elif menu == 2:
        produto = num1 * num2
        print('\nO produto entre {} e {} equivale a {}.'.format(num1, num2, soma))
        sleep(1.5)
    elif menu == 3:
        if num1 > num2:
            maior = num1
            menor = num2
            print('\nEntre esses dois números, {} é o maior e {} é o menor.'.format(maior, menor))
            sleep(2)
        elif num2 > num1:
            maior = num2
            menor = num1
            print('\nEntre esses dois números, {} é o maior e {} é o menor.'.format(maior, menor))
            sleep(1.5)
        else:
            print('\nNão há número maior entre os dois números digitados. Ambos equivalem a {}.'.format(num1))
            sleep(1.5)
    elif menu == 4:
        num1 = float(input('\nDigite um número: '))
        num2 = float(input('Digite outro número: '))
        sleep(1.5)
    elif menu > 5:
        print('\nComando inválido. Tente novamente.')
        sleep(1.5)
sleep(0.5)
print('\nPrograma desligado.')
sleep(1.5)
