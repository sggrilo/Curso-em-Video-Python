# VALIDANDO ENTRADA DE DADOS EM PYTHON — Crie um programa que tenha a função leiaint(), que funcione de forma
# semelhante à função input() do Python, mas fazendo a validação para aceitar apenas um valor numérico.
#
# Ex.:
# n = leiaint('Digite um n')


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')

"""def leiaint(c):
    input(c)
    b = c.isnumeric()
    while not b:
        print('\033[1;31mErro! Por favor, digite apenas um número inteiro.\033[m')
        input(c)
    return c


n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')"""
