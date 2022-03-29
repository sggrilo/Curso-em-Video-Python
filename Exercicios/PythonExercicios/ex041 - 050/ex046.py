# CONTAGEM REGRESSIVA — Faça um programa que mostre uma contagem regressiva na tela para o
# estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
from emoji import emojize
print('\033[1;31mFogos de Artifício\033[m\n')
sleep(1)
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('\n{0} \033[1;31m*BUM!*\033[m {0}'.format(emojize('\033[0;31m:fireworks:\033[m' * 3)))
