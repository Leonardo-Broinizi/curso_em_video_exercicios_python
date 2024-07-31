n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
cores = {'amarelo':'\033[33m',
         'azul':'\033[34m',
         'limpa':'\033[m',
         'verde':'\033[32m'}
result = n1 + n2
print(f'A soma entre {cores['amarelo']} {n1} {cores['limpa']}e{cores['verde']} {cores['azul']} {n2} {cores['limpa']}é{cores['verde']} {result} {cores['limpa']}.')