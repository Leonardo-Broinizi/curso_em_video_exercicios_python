# As resoluções foram parecidas.

# Minha resolução:

'''PA = int(input('Digite o primeiro termo para a Progressão Aritmética: '))
razão = int(input('Digite a razão dessa PA: '))
c = 1
while c < 10:
    print(f'{PA} -> ',end='')
    PA += razão
    c += 1
print(PA)'''

# Resolução do professor Guanabara:

print('Gerador de PA')
print('-=' * 10 + '-')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end='')
    print(' -> ' if cont < 10 else '.', end='')
    termo += razão
    cont += 1
