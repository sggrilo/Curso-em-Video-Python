# SIMULADOR DE CAIXA ELETRÔNICO — Crie um programa que simule o funcionamento de um
# caixa eletrônico. No início, pergunte ao usuário qual será o valor sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#
# OBS. Considere que o caixa possui cédulas de R$50,00; R$20,00; R$10,00 e R$1,00.

print('')
print('-=-' * 6)
print('{: ^18}'.format('Caixa Eletrônico'))
print('-=-' * 6)

saque = int(input('Quanto dinheiro você deseja sacar (insira um número inteiro)? R$'))
total = saque

"""cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0

while saque >= 50:
    cedulas50 = saque // 50
    saque -= cedulas50 * 50
while saque >= 20:
    cedulas20 = saque // 20
    saque -= cedulas20 * 20
while saque >= 10:
    cedulas10 = saque // 10
    saque -= cedulas10 * 10
while saque >= 1:
    cedulas1 = saque // 1
    saque -= cedulas1
print(f'''\nPara um saque de R${total:.2f}, são necessárias:\n
— {cedulas50} cédulas de R$50,00;
— {cedulas20} cédulas de R$20,00;
— {cedulas10} cédulas de R$10,00;
— {cedulas1} cédulas de R$1,00.''')"""

cedulas = 50
totalcedulas = 0

print(f'\nPara um saque de R${total:.2f}, são necessárias:\n')
while True:
    if total >= cedulas:
        total -= cedulas
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'— {totalcedulas} cédulas de R${cedulas:.2f}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalcedulas = 0
        if total == 0:
            break
