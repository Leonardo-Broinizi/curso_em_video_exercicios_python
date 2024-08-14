b = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° número: '))
    if n%2 == 0:
        b += n
print(f'A soma entre os números pares que foram digitados é: {b}.')
