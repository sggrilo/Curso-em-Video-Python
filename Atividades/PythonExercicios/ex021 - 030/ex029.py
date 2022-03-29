# RADAR ELETRÔNICO — Escreva um programa que leia a velocidade de um carro.
# Se ela ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 para cada km acima do limite.

vel = float(input('Digite a velocidade do carro, em km/h: '))
if vel > 80:
    lim = vel - 80
    mul = lim * 7
    print('Seu carro está rodando a {} km/h acima do limite de velocidade de 80 km/h.'.format(lim))
    print('Portanto, você será multado com um valor de R${:.2f}.'.format(mul))
else:
    print('Parabéns! Seu carro está rodando a uma velocidade dentro do limite de 80 km/h')
print('Tenha um bom dia! Dirija com segurança!')