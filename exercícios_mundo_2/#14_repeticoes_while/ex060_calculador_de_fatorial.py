f = n = c = int(input('Digite um número para saber seu fatorial: '))
while c > 2:
    c -= 1
    f *= c
print(f'O fatorial de {n} é {f}!')