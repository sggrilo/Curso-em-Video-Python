# FORMATANDO MOEDAS EM PYTHON — Modifique as funções criadas no Desafio 107 para elas aceitarem um parâmetro a mais,
# informando se o valor retornado por elas será ou não formatado pela função moeda(), desenvolvida no desafio 108.

from moeda import moeda, metade, dobro, aumentar, diminuir
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando em 10%, temos {aumentar(p, 10, True)}')
print(f'Reduzindo em 13%, temos {diminuir(p, 13, True)}')
