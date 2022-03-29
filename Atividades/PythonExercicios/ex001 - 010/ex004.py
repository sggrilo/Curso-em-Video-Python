# DISSECANDO UMA VARIÁVEL — Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input("\033[1mDigite algo:\033[m ")
print(f'O tipo primitivo desse valor é {type(a)}')
print('')
print('\033[1mSó tem espaços?\033[m', a.isspace())
print('\033[1mÉ um número?\033[m', a.isnumeric())
print('\033[1mÉ alfabético?\033[m', a.isalpha())
print('\033[1mÉ alfanumérico?\033[m', a.isalnum())
print('\033[1mEstá em maiúsculas?\033[m', a.isupper())
print('\033[1mEstá em minúsculas?\033[m', a.islower())
print('\033[1mEstá capitalizado?\033[m', a.istitle())
