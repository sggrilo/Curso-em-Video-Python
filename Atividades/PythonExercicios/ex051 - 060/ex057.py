# VALIDAÇÃO DE DADOS — Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 'QWERTYUIOPASDFGHJKLZXCVBNM'
print('')
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo (M/F): ').title().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Erro. Tente novamente.\n')
print('Sexo {} registrado com sucesso.'.format(sexo))
