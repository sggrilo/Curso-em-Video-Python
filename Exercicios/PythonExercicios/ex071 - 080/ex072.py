# NÚMERO POR EXTENSO — Crie um programa que tenha uma tupla totalmente
# preenchida com uma contagem por extenso de zero a vinte.
#
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

"""num = int(input('\nDigite um número inteiro de 0 a 20: '))

while num < 0 or num > 20:
    print('\n\033[1;31mEntrada inválida. Tente Novamente.\033[m')
    num = int(input('\nDigite um número inteiro de 0 a 20: '))"""

while True:
    num = int(input('\nDigite um número inteiro de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('\n\033[1;31mEntrada inválida. Tente Novamente.\033[m')

print(f'\n{num} escrito por extenso é {t[num].lower()}.')
