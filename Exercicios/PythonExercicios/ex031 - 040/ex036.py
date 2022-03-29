# APROVANDO EMPRÉSTIMO — Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#
# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será cancelado.

casa = float(input('\033[1mQual é o valor da casa a ser comprada, em reais?\033[m R$'))
sal = float(input('\033[1mQual é o valor do seu salário mensal, em reais?\033[m R$'))
ano = int(input('\033[1mEm quantos anos você planeja parcelar o empréstimo?\033[m '))
pres = casa / (ano * 12)
if pres > (0.3 * sal):
    print('\n\033[1;31mEmpréstimo negado!\033[m')
else:
    print('\n\033[1;32mEmpréstimo concedido!\033[m')
