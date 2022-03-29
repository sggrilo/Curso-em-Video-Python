# FUNÇÃO QUE CALCULA ÁREA — Faça um programa que tenha uma função chamada área(), que receba
# as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def titulo():
    print('-=-' * 10)
    print(f'{"ÁREA DE UM TERRENO":^30}')
    print('-=-' * 10)


def area(lar, com):
    are = lar * com
    print(f'\n{lar} m² * {com} m² = {are} m²')


titulo()
l = float(input('Digite a largura do terreno retangular, em m²: '))
c = float(input('Digite o comprimento do terreno retangular, em m²: '))
area(l, c)
