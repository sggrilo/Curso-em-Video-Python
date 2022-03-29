# ALISTAMENTO MILITAR — Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade:
#
# — Se ele ainda vai se alistar ao serviço militar.
# — Se é a hora de se alistar.
# — Se já passou do tempo do alistamento.
#
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nas = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nas
print('Quem nasceu no ano de {} tem {} anos de idade em {}.'.format(nas, idade, ano))
if idade < 18:
    print('Você se alistará ao serviço militar daqui a {} anos, no ano de {}.'.format(18 - idade, ano + (18 - idade)))
elif idade == 18:
    print('Já é hora de se alistar ao serviço militar.')
else:
    print('Você deveria ter se alistado ao serviço militar há {} anos, em {}.'.format(idade - 18, ano - (idade - 18)))
