# RESPONDENDO AO USUÁRIO — Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, \033[1;34m{}\033[m!'.format(nome))

# Versão alternativa de escrever o comando: print(f'É um prazer te conhecer, {nome}!')
