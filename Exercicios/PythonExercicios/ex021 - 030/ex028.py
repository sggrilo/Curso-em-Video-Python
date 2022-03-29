# JOGO DA ADIVINHAÇÃO V1.0 — Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
num = randint(0, 5)  # Faz o computador "pensar".
print('-=-' * 10)
print('Estou pensando em um número de 0 a 5... Tente adivinhá-lo!')
print('-=-' * 10)
num1 = int(input('Em que número eu pensei? '))  # O jogador tenta adivinhar o número.
print('\nProcessando...')
sleep(2.5)
if num == num1:
    print('\nParabéns! Você acertou!')
else:
    print('\nQue pena! Você errou!')
print('O número em que eu estava pensando era {}.'.format(num))
