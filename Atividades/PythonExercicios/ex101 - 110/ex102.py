# FUNÇÃO PARA FATORIAL — Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a ser calculado e o segundo chamado show, que será um valor lógico
# (opcional), indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    → Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do fatorial de um número n.
    """
    print('-=-' * 10)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c}', end=' × ')
            else:
                print(f'{c}', end=' = ')
    return f


# Programa principal
print(fatorial(5, show=True))
print('-=-' * 10)
help(fatorial)
