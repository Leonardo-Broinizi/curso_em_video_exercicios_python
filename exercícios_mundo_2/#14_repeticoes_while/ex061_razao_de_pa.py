PA = int(input('Digite o primeiro termo para a Progressão Aritmética: '))
razão = int(input('Digite a razão dessa PA: '))
c = 1
while c < 10:
    print(f'{PA} -> ',end='')
    PA += razão
    c += 1
print(PA)
