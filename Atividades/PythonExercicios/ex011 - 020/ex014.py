# CONVERSOR DE TEMPERATURAS — Escreva um programa que leia uma temperatura digitada em °C e a converta para °F.

tc = float(input('Digite a temperatura em °C a ser convertida para °F: '))
tf = (18 * tc + 320) / 10
print('A temperatura de {}°C equivale a {}°F'.format(tc, tf))
