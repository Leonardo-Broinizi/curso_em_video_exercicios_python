c = m = maior = menor = 0
r = ''
while r != 'N':
    c += 1
    n = float(input(f'Digite o {c}º número: '))
    r = str(input('Quer continuar acrescentando? [S/N] ')).upper().strip()
    if c == 1 or n < menor:
        menor = n
    if n > maior:
        maior = n
    m += n
print(f'A média dos números digitados é {m/c:.2f}, o maior número foi {maior} e o menor foi {menor}.')

