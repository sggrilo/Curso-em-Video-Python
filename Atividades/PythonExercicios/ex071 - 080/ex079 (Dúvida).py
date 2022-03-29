# VALORES ÚNICOS EM UMA LISTA — Crie um programa em que o usuário pode digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.

pos = entra = copia = 0
opt = 'Amogus'
num = []
while True:
    entra = int(input('Digite um número inteiro: '))
    if entra not in num:
        num.append(entra)
        print('\033\n[1;32mNúmero adicionado à lista.\033[m\n')
    else:
        print('\033\n[1;31mVocê digitou um número duplicado. Ele não será adicionado à lista.\033[m\n')
    opt = input('Deseja continuar? [S/N]: ')
    print('')
    opt = opt.title()
    while opt not in 'SimNãoNao':
        print('\033[1;31mEntrada inválida. Tente novamente.\n\033[m')
        opt = input('Deseja continuar? [S/N]: ')
        opt = opt.title()
        print('')
    if opt in 'NãoNao':
        break
num.sort()
print(f'Os números distintos digitados foram {num}, em ordem crescente.')
