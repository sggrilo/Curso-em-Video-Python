# GAME: PEDRA, PAPEL E TESOURA — Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
print('-=-' * 8)
print('{: ^24}'.format('\033[32mPedra, Papel e Tesoura\033[m'))
print('-=-' * 8, end='\n')

escolha = str(input('Escolha um dos três:\n— Pedra\n— Papel\n— Tesoura\n\nDigite aqui a sua escolha: '))
escolha = escolha.title()

gen = randint(1, 3)
if gen == 1:
    comp = 'Pedra'
elif gen == 2:
    comp = 'Papel'
else:
    comp = 'Tesoura'
print('')
print('-=-' * 24)
if (escolha == 'Pedra' and comp == 'Tesoura') or (escolha == 'Papel' and comp == 'Pedra') or (escolha == 'Tesoura' and comp == 'Papel'):
    print('Você escolheu \033[32m{}\033[m e eu escolhi \033[32m{}\033[m. Você venceu! Parabéns!'.format(escolha, comp))

elif (escolha == 'Pedra' and comp == 'Papel') or (escolha == 'Papel' and comp == 'Tesoura') or (escolha == 'Tesoura' and comp == 'Pedra'):
    print('Você escolheu \033[32m{}\033[m e eu escolhi \033[32m{}\033[m. Eu venci! Boa sorte na próxima!'.format(escolha, comp))
elif escolha == comp:
    print('Ambos escolhemos \033[32m{}\033[m! Deu empate!'.format(escolha))
else:
    print('\033[31mEscolha inválida! Tente novamente!\033[m')
print('-=-' * 24)
