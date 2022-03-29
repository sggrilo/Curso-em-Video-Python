# PROCURANDO UMA STRING DENTRO DE OUTRA — Crie um programa que
# leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome: '))
print('Seu nome contém \'Silva\'?')
nome = nome.title()
print('Silva' in nome)
