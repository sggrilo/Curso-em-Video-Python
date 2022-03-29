# CONVERSOR DE BASES NUMÉRICAS — Escreva um programa que leia um número
# inteiro e peça para o usuário escolher qual será a base de conversão:
#
# — 1 para binário
# — 2 para octal
# — 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('\nPara converter o número \033[31m{}\033[m para binário, digite 1.'.format(num))
print('Para convertê-lo para a base octal, digite 2.')
print('Para convertê-lo para a base hexadecimal, digite 3.')
con = int(input())
print('')
if con == 1:
    num1 = bin(num)
    print('O número \033[31m{}\033[m convertido para a base binária é \033[31m{}\033[m.'.format(num, num1[2:]))
elif con == 2:
    num1 = oct(num)
    print('O número \033[31m{}\033[m convertido para a base octal é \033[31m{}\033[m.'.format(num, num1[2:]))
elif con == 3:
    num1 = hex(num)
    print('O número \033[31m{}\033[m convertido para a base hexadecimal é \033[31m{}\033[m.'.format(num, num1[2:]))
