# VALIDANDO EXPRESSÕES MATEMÁTICAS — Crie um programa em que o usuário digite uma expressão matemática qualquer que use
# parênteses. Seu programa deve analisar se o programa está com os parênteses abertos e fechados na ordem correta.

expr = input('Digite uma expressão matemática: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está formatada corretamente.')
else:
    print('Sua expressão não está formatada corretamente.')
