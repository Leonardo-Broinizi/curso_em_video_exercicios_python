# Por pouca coisa, gostei mais da minha resolução.

# Minha resolção:

'''n = int(input('Digite a quantidade de termos da sequência de Fibonacci deseja ver: '))
f1 = 0
f2 = f = 1
print(f'\033[1;34m{f1}\033[31m -> ',end='')
while n > 1:
    print(f'\033[34m{f}\033[m \033[31m->\033[m ',end='')
    f = f1 + f2
    f1 = f2
    f2 = f
    n -= 1
print(f'\033[1;33mFIM\033[m')'''

# Resolução do professor:

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')
