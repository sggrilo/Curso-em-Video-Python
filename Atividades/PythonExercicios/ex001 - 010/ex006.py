# DOBRO, TRIPLO, RAIZ QUADRADA — Crie um algoritmo que leia um
# número e mostre seu dobro, seu triplo e sua raiz quadrada.

n = float(input('\033[1mDigite um número:\033[m '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('\033[1mO dobro de \033[3;97m{}\033[m\033[1m equivale a \033[3;97m{}\033[m. '.format(n, d), end='\n')
print('\033[1mSeu triplo equivale a \033[3;97m{}\033[m\033[1m\n'
      'Sua raiz quadrada equivale a aproximadamente \033[3;97m{:.3f}'.format(t, r))
