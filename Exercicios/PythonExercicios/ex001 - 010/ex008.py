# CONVERSOR DE MEDIDAS — Escreva um programa que leia um valor
# em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros: '))

km = m * 1000
hm = m * 100
dam = m * 10
dm = m / 10
cm = m / 100
mm = m / 1000

print('O valor de {} em quilômetros equivale a {}.\n'.format(m, km), end='')
print('O seu valor em hectômetros equivale a {}.'.format(hm))
print('O seu valor em decâmetros equivale a {}.'.format(dam))
print('O seu valor em decímetros equivale a {}.'.format(dm))
print('O seu valor em centímetros equivale a {}.'.format(cm))
print('O seu valor em milímetros equivale a {}.'.format(mm))
