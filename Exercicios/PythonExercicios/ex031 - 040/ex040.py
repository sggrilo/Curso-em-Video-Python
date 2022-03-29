# AQUELE CLÁSSICO DA MÉDIA — Crie um programa que leia duas notas de um aluno e calcule
# a sua média, mostrando uma mensagem no final, conforme a média atingida.
#
# — Média abaixo de 5,0: REPROVADO
# — Média entre 5,0 e 6,9: RECUPERAÇÃO
# — Média 7,0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('\nO aluno, cuja média é de \033[1m{:.1f}\033[m, está \033[1mREPROVADO\033[m.'.format(m))
elif 5.0 <= m < 7.0:
    print('\nO aluno, cuja média é de \033[1m{:.1f}\033[m, está em \033[1mRECUPERAÇÃO\033[m.'.format(m))
elif m >= 7.0:
    print('\nO aluno, cuja média é de \033[1m{:.1f}\033[m, está \033[1mAPROVADO\033[m.'.format(m))
