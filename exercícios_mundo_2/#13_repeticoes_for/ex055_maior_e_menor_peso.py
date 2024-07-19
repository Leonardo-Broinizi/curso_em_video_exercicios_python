maior = menor = base = 0
for c in range(5):
    peso = float(input(f'Digite o peso da {c+1}° pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor or c == 0:
        menor = peso
print(f'O maior peso digitado foi {maior:.2f} e o menor foi {menor:.2f}')
