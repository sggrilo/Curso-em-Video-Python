# INTERROMPENDO REPETIÇÕES WHILE — Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar 999, sendo a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999).

num = soma = cont = 0
print('')
while True:
    num = int(input('Digite um número inteiro (Digite 999 para parar): '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'\nA soma entre os {cont} números digitados equivale a {soma}.')
