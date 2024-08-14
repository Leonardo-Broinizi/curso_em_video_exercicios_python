#    Gostei tanto da minha resolução quanto a do professor, que foram um pouco diferentes.

#    Minha resolução:

lista = str(input('Digite: '))
aberto = fechado = 0
for c in lista:
    if c == '(':
        aberto += 1
    elif c == ')':
        fechado += 1
    if aberto == 0 and fechado > 0 or aberto - fechado < 0:
        break
if aberto == fechado:
    print('Você fechou corretamente seus parênteses.')
else:
    print('Você não fechou corretamente seus parênteses.')

#   Resolução do professor Guanabara:

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão não está válida!')
