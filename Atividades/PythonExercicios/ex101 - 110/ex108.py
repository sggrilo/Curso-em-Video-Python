# FORMATANDO MOEDAS EM PYTHON — Adapte o código do Desafio 107, criando uma função adicional
# chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

from moeda import moeda, metade, dobro, aumentar, diminuir
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando em 10%, temos {moeda(aumentar(p, 10))}')
print(f'Reduzindo em 13%, temos {moeda(diminuir(p, 13))}')
