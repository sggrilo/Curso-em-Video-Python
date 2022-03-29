# DETECTOR DE PALÍNDROMO — Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
"""for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]"""
print('\"{}\" ao contrário é \"{}\".'.format(junto.title(), inverso.lower()))
if inverso == junto:
    print('Logo, \"{}\" é um palíndromo.'.format(frase.lower()))
else:
    print('Logo, \"{}\" não é um palíndromo.'.format(frase.lower()))