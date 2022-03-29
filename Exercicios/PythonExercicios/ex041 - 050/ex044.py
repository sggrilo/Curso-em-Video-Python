# GERENCIADOR DE PAGAMENTOS — Elabore um programa que calcule o valor a ser pago
# por um produto, considerando seu preço normal e sua condição de pagamento:
#
# — À vista com dinheiro/cheque: 10% de desconto
# — À vista no cartão: 5% de desconto
# — Em até 2x no cartão: preço normal
# — 3x ou mais no cartão: 20% de juros

preco = float(input('Qual é o preço do produto? R$'))
forma = int(input('\nQual é a forma de pagamento?\nDigite 1 para pagar com dinheiro.\nDigite 2 para pagar com '
                  'cheque.\nDigite 3 para pagar com cartão.\n'))
cond = int(input('\nQual é a condição de pagamento?\nDigite 1 para pagar à vista.\nDigite 2 para pagar a prazo.\n'))
if cond == 2:
    parcelas = int(input('\nEm quantas parcelas será pago o produto? \n'))
if forma == 1 or forma == 2:
    if cond == 1:
        print('\nO produto terá 10% de desconto, assumindo um novo preço de R${:.2f}.'.format(0.9 * preco))
    else:
        print('\nO produto terá seu preço normal.')
elif forma == 3:
    if cond == 1:
        print('\nO produto terá 5% de desconto, assumindo um novo preço de R${:.2f}.'.format(0.95 * preco))
    else:
        if parcelas <= 2:
            print('\nO produto terá seu preço normal.')
        else:
            print('\nO produto terá 20% de juros, assumindo um novo preço de R${:.2f}'.format(1.2 * preco))
else:
    print('\nOpção inválida de pagamento. Por favor, tente novamente.')