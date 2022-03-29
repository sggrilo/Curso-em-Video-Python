# VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO — Crie um programa que leia
# o nome de uma cidade e diga se ela começa o não com o nome "SANTO".

# cidade = str(input('Digite o nome de uma cidade: '))
# print('O nome dessa cidade começa com \'Santo\'?')
# cidade = cidade.title()
# cidade = cidade.split()
# print(cidade[0] == 'Santo')"""

# O código acima funciona apenas com cidades que começam com Santo e mais um espaço entre as palavras.
# 'Santorini', por exemplo, não funcionaria.

cidade = str(input('Digite o nome de uma cidade: '))
print('O nome dessa cidade começa com \'Santo\'?')
cidade = cidade.title()
print(cidade[0:5] == 'Santo')
