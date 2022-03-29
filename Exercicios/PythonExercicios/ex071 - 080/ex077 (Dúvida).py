# CONTANDO VOGAIS COM TUPLA — Crie um programa que tenha uma tupla com várias palavras
# (não use acentos). Depois disso, mostre, para cada palavra, quais são suas vogais.

palavras = ('Frango', 'Lyndis', 'Brito', 'Agua', 'Chinelo')

for cont in palavras:
    print(f'\nNa palavra {cont}, há as vogais ', end='')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
print('')

"""    if 'A' in cont:
        print(f'{cont}'.count('A') * 'A ', end='')
    if 'E' in cont:
        print(f'{cont}'.count('E') * 'E ', end='')
    if 'I' in cont:
        print(f'{cont}'.count('I') * 'I ', end='')
    if 'O' in cont:
        print(f'{cont}'.count('O') * 'O ', end='')
    if 'U' in cont:
        print(f'{cont}'.count('U') * 'U ', end='')
    print('')"""
