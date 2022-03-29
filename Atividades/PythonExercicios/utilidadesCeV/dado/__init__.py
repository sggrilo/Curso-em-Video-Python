def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO: \"{entrada}\" não é um preço válido.\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    while True:
        try:
            num1 = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num1


def leiafloat(msg):
    while True:
        try:
            num1 = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro! Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num1