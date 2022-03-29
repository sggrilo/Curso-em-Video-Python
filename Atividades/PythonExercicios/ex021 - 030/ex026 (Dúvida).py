# PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING — Faça um programa que leia uma frase pelo teclado e mostre:
# — Quantas vezes aparece a letra "A".
# — Em que posição ela aparece pela primeira vez.
# — Em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase: '))
frase = frase.upper()
letras = frase.count('A')
print('Nessa frase, a letra \'A\' aparece {} vezes.'.format(letras))

posi = frase.find('A') + 1
print('A letra \'A\' aparece pela primeira vez como o {}º caractere, incluindo espaços.'.format(posi))

posu = frase.rfind('A') + 1
print('A letra \'A\' aparece pela última vez como o {}º caractere, incluindo espaços.'.format(posu))
