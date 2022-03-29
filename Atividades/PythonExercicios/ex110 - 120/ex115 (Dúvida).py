# CRIANDO UM MENU / ARQUIVOS COM PYTHON / FINALIZANDO O PROJETO — Crie um pequeno sistema modularizado
# que permita cadastrar pessoas por seu nome e por sua idade em um arquivo de texto simples.
#
# O sistema só vai ter 2 opções: cadastrar uma pessoa nova e listar todas as pessoas cadastradas.

from utilidadesCeV.interface import *
from utilidadesCeV.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # O usuário digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
