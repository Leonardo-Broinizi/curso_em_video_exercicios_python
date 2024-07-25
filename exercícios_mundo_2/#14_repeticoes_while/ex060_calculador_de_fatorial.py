# Gostei um pouco mais da resolução do professor Guanabara do que da minha.

# Minha primeira resolução:

'''f = n = c = int(input('Digite um número para saber seu fatorial: '))
while c > 2:
    c -= 1
    f *= c
print(f'O fatorial de {n} é {f}!')'''

# Minha resolução após ver o exercício do professor Guanabara funcionar de um jeito legal:

'''f = n = c = int(input('Digite um número para saber seu fatorial: '))
print(f'O fatorial de {n}, que é o mesmo que {n} x ',end='')
while c > 2:
    c -= 1
    f *= c
    print(c,end=' x ')
print(f'{c-1 } = {f}')'''

# Minha resolução com 'for', respondendo ao desafio do professor:

'''f = n = c = int(input('Digite um número para saber seu fatorial: '))
print(f'O fatorial de {n}, que é o mesmo que {n} x ',end='')
for c in range(f, 2, -1):
    c -= 1
    f *= c
    print(c,end=' x ')
print(f'{c-1 } = {f}')'''

# Resolução do professor Guanabara:
# Com módulo:
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')'''

# Sem módulo:

'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='') # Gostei dessa solução para fazer o 'x' ser 'printado' até o penúltimo, e o '=' no último
    f *= c
    c -= 1
print(f'{f}.')'''
