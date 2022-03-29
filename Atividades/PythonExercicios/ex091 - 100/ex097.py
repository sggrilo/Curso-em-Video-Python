# UM PRINT ESPECIAL — Faça um programa que tenha uma função chamada escreva(), que receba
# um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#
# Ex.:
#
# escreva('Olá, mundo!')
#
# Saída:
#
# ~~~~~~~~~~~
# Olá, mundo!
# ~~~~~~~~~~~

def escreva(txt):
    print('')
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))


while True:
    print('')
    escreva(input('Digite algo: '))
