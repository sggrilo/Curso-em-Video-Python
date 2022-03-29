# ENTRADA DE DADOS MONETÁRIOS — No pacote utilidadesCeV que foi criado no desafio 111, há um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que funcione como a função input(), mas com
# uma validação de dados para aceitar apenas valores que sejam monetários.

from utilidadesCeV import moeda, dado
p = dado.leiadinheiro("Digite o preço: R$")
moeda.resumo(p, 80, 35)
