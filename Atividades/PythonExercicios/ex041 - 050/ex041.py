# CLASSIFICANDO ATLETAS — A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, conforme a sua idade.
#
# — Até 9 anos: Mirim
# — Até 14 anos: Infantil
# — Até 19 anos: Júnior
# — Até 20 anos: Sênior
# — Acima: Master

from datetime import date
nas = int(input('Digite o ano de nascimento do(a) atleta: '))
idade = date.today().year - nas
if idade <= 9:
    print('\nO(a) atleta, cuja idade é de {} anos, pertence à categoria Mirim'.format(idade))
elif idade <= 14:
    print('\nO(a) atleta, cuja idade é de {} anos, pertence à categoria Infantil'.format(idade))
elif idade <= 19:
    print('\nO(a) atleta, cuja idade é de {} anos, pertence à categoria Júnior'.format(idade))
elif idade <= 20:
    print('\nO(a) atleta, cuja idade é de {} anos, pertence à categoria Sênior'.format(idade))
elif idade <= 14:
    print('\nO(a) atleta, cuja idade é de {} anos, pertence à categoria Master'.format(idade))