# FUNÇÕES APROFUNDADAS EM PYTHON — Reescreva a função leiaInt() que foi feita no
# Desafio 104, incluindo agora a possibilidade da digitação de um tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


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


# Programa principal
n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}.')
