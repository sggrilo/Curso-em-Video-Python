# AUMENTOS MÚLTIPLOS — Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o salário do funcionário, em reais: '))
if sal > 1250:
    aum = 1.10 * sal
    porc = '10%'
else:
    aum = 1.15 * sal
    porc = '15%'
print('Com um aumento de {}, o salário, que antes era de R${:.2f}, passará a ser de R${:.2f}.'.format(porc, sal, aum))
