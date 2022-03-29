# ALUGUEL DE CARROS — Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e
# R$0.15 para cada km rodado.

km = float(input('Quantos quilômetros o carro percorreu? '))
d = float(input('Por quantos dias o carro foi alugado? '))

p = 60 * d + 0.15 * km

print('O preço a se pagar pelo aluguel desse carro é de R${:.2f}.'.format(p))
