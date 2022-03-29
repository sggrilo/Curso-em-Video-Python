# ESTATÍSTICAS EM PRODUTOS — Crie um produto que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000,00.
# C) Qual é o nome do produto mais barato.

nome = 'Nome'
nomeb = 'Nome'
preco = num = total = caros = barato = qtd = 0
cont = True
conf = 'S'
while cont:
    nome = input('\nDigite o nome do produto: ').strip().title()
    preco = float(input('Digite o seu preço, em reais: R$'))
    while preco < 0:
        print('\n\033[1;31mResposta inválida. Tente novamente.\033[m\n')
        preco = float(input('Digite o seu preço, em reais: R$'))
    total += preco
    num += 1
    if preco > 1000:
        caros += 1
    if num == 1 or preco < barato:
        barato = preco
        nomeb = nome
    conf = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if conf in 'S':
        print('', end='')
    elif conf in 'N':
        cont = False
    else:
        while conf not in 'SN':
            print('\n\033[1;31mResposta inválida. Tente novamente.\033[m\n')
            conf = input('Deseja continuar? [S/N]: ').strip().upper()[0]
print('''\nO total gasto na compra de todos os {} produtos será de R${:.2f}.
Há {} produtos que custam mais de R$1000.00 nessa lista de compras.
O produto mais barato dela é {}, que custa R${:.2f}.'''.format(num, total, caros, nomeb, barato))
