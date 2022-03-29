# ANALISADOR DE TEXTOS — Crie um programa que leia o nome completo de uma pessoa e mostre:
# — O nome com todas as letras maiúsculas.
# — O nome com todas as letras minúsculas.
# — Quantas letras ao todo (sem considerar espaços).
# — Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()

upper = nome.upper()
lower = nome.lower()

print('\nO seu nome com apenas letras maiúsculas é {}'.format(upper), end='\n')
print('O seu nome com apenas letras minúsculas é {}'.format(lower), end='\n')

dividido = nome.split()
junto = ''.join(dividido)
tamanho = len(junto)

print('O seu nome completo tem {} letras ao todo.'.format(tamanho))

tamanho1 = len(dividido[0])
print('Já o seu primeiro nome, que é {}, tem {} letras.'.format(dividido[0], tamanho1))
