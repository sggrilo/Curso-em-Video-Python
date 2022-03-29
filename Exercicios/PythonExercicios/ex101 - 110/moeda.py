# EXERCÍCIO 107

def aumentar(preco=0, taxa=0, formato=False):
    """
     → Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço a ser reajustado.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


# EXERCÍCIO 108

def moeda(preco=0, currency='R$'):
    return f'{currency}{preco:.2f}'.replace('.', ',')


# EXERCÍCIO 110

def resumo(preco=0, taxaa=10, taxar=5):
    print(f'-=-' * 11)
    print('RESUMO DO VALOR'.center(33))
    print(f'-=-' * 11)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print(f'-=-' * 11)
