n = int(input('Digite a quantidade de termos da sequência de Fibonacci deseja ver: '))
f1 = 0
f2 = f = 1
print(f'\033[1;34m{f1}\033[31m -> ',end='')
while n > 1:
    print(f'\033[34m{f}\033[m \033[31m->\033[m ',end='')
    f = f1 + f2
    f1 = f2
    f2 = f
    n -= 1
print(f'\033[34m{f}\033[m')

