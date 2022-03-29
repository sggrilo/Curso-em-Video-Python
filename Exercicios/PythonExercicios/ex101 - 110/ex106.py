# INTERACTIVE HELPING SYSTEM EM PYTHON — Faça um mini-sistema que utilize o Interactive
# Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o
# usuário digitar a palavra 'FIM', o programa se encerrará.
#
# OBS.: Use cores.

from time import sleep
c = ('\033[m',          # 0 — Sem cores
     '\033[1;41m',      # 1 — Vermelho
     '\033[1;42m',      # 2 — Verde
     '\033[1;43m',      # 3 — Amarelo
     '\033[1;44m',      # 4 — Azul
     '\033[1;45m',      # 5 — Magenta
     '\033[7m',      # 6 — Branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'...', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)

"""def ajuda():
    while True:
        from time import sleep
        print('\033[1;42m~' * 27)
        print('  SISTEMA DE AJUDA PYHELP  ')
        print('~' * 27)
        sleep(1)
        a = input('\033[mFunção ou biblioteca: ')
        sleep(1)
        if a.strip().lower() == 'fim':
            print('\033[1;41m~' * 13)
            print('  ATÉ LOGO!  ')
            print('~' * 13)
            sleep(1)
            break
        print('\033[1;44m~' * (len(f'Acessando o manual do comando \'{a}\'') + 4))
        print(f'  Acessando o manual do comando \'{a}\'')
        print('~' * (len(f'Acessando o manual do comando \'{a}\'\033[m') + 4))
        sleep(1)
        print('\033[m', end='')
        print('\033[1m', end='')
        print('\033[7m', end='')
        help(a)
        print('\033[m', end='')
        sleep(1)


ajuda()"""
