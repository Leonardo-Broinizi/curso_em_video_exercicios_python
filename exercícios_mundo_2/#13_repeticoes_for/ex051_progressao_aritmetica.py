PA = int(input('Digite o primeiro termo para a Progressão Aritmética: '))
razão = int(input('Digite a razão dessa PA: '))
for c in range(1,10):
    print(f'{PA} -> ',end='')
    PA += razão
print(PA)
