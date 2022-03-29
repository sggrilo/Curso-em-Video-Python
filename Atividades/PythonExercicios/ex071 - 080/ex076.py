# LISTA DE PREÇOS COM TUPLA — Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos preços, na sequência.
#
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

prod = ('Pão', 1, 'Leite', 3.5, 'Frango', 10.9, 'Batata', 4.75, 'Peixe', 7.89)

print('—' * 24)
print('{: ^24}'.format('LISTAGEM DE PREÇOS'))
print('—' * 24)

"""print('{:.<16}R$  {:.2f}'.format(prod[0], prod[1]))
print('{:.<16}R$  {:.2f}'.format(prod[2], prod[3]))
print('{:.<16}R$ {:.2f}'.format(prod[4], prod[5]))
print('—' * 24)"""

for pos in range(0, len(prod)):
    if pos % 2 == 0:
        print(f'{prod[pos]:.<16}', end='')
    elif pos % 2 == 1:
        print(f'R${prod[pos]:>6.2f}')
print('—' * 24)