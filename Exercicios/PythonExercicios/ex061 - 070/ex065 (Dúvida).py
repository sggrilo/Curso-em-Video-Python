# MAIOR E MENOR VALORES — Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e quais foram o maior e o menor valores lidos. O
# programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
num = soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('\nDigite um número inteiro: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SsNn':
        print('\nResposta inválida. Tente novamente.')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('\nA média entre todos os {} números digitados equivale a {}.'.format(quant, media))
if maior != menor:
    print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
else:
    print('Não foi digitado um número maior ou menor. Todos eles equivalem a {}.'.format(num))
