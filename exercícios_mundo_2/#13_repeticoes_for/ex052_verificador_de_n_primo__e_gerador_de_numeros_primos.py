'''p = 0
n = int(input('Digite um número inteiro para saber se é ou não primo: '))
for c in range(n-2): # Fiz um código confuso.
    if (n)%(c+2) == 0:
        p += 1
        print(c+2)
if n < 2 or p > 0:
    print(f'O número {n} não é primo.')
else:
    print(f'O número {n} é primo.')'''

# Exercício refeito após ver o funcionamento do programa do professor Guanabara, mas antes de ver seu código:

d = 0
n = int(input('\033[1mDigite um número inteiro para saber se é ou não primo: '))
for c in range(1, n+1):
    if n%c != 0 and c < n:
        print(f'\033[1;31m{c}\033[m, ',end='')
    elif n%c == 0 and c < n:
        d += 1
        print(f'\033[1;33m{c}\033[m, ',end='')
    else:
        d += 1
        print(f'\033[1;33m{c}\033[m.')
if d != 2:
    print(f'\033[1mO número {n} é divisível {d} vezes, por isso ele não é primo.')
else:
    print(f'\033[1mO número {n} é divisível {d} vezes, por isso ele é primo.')


# Gerador de números primos:
'''print('\033[1;31mTabela de números primos (de 0 até 1000): ')
n = 0
for c in range(1001):
    p = 0
    n += 1
    for i in range(n+1):
        if (n)%(i+1) == 0:
            p += 1
    if p == 2:
        print(f'{n}, ',end='')'''
