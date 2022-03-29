# SUPER PROGRESSÃO ARITMÉTICA V3.0 — Melhore o Desafio 061, perguntando ao usuário se ele quer mostrar
# mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 novos termos.

a1 = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão dessa PA: '))
an = a1 + (10 - 1) * r
print('')
while a1 <= an:
    print(a1)
    a1 += r

con = 'S'

while con != 'N':
    con = input('\nVocê quer mostrar mais termos dessa PA? [S/N] ').title()

    while con != 'S' and con != 'N':
        print('Resposta inválida. Tente novamente.')
        con = input('\nVocê quer mostrar mais termos dessa PA? [S/N] ').title()

    if con == 'S':
        termos = int(input('Quantos termos você quer adicionar à PA? '))
        if termos == 0:
            con = 'N'
        else:
            an += termos
            print('')
            while a1 <= an:
                print(a1)
                a1 += r
