# FUNÇÕES PARA VOTAÇÃO — Crie um programa que tenha uma função chamada voto(), que receba
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.

def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    if 16 <= idade < 18 or 65 <= idade:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


# Programa principal:
while True:
    nasc = int(input('\nEm que ano você nasceu? '))
    print(voto(nasc))
