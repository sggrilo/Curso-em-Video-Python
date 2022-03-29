# CUSTO DA VIAGEM — Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço
# da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas.

dist = float(input('Qual é a distância da viagem em km? '))
if dist <= 200:
    taxa = 0.50 * dist
else:
    taxa = 0.45 * dist
print('O preço a se pagar pela passagem de uma viagem de {} km será de R${:.2f}.'.format(dist, taxa))
