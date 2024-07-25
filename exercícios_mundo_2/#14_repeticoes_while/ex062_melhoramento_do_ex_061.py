# Achei minha resolução um pouco mais simples e interessante.

# Minha resolução:

'''PA = int(input('Digite o primeiro termo para a Progressão Aritmética: '))
razão = int(input('Digite a razão dessa PA: '))
t = 10
tot = 0
while t != 0:
    while t > 1:
        print(f'{PA} -> ',end='')
        PA += razão
        tot += 1
        t -= 1
    tot += 1
    print(PA)
    PA += razão
    t = int(input('Quer mostrar quantos termos mais? (0 para sair)'))
print(f'Progressão finalizada com {tot} termos mostrados.')'''

# Resolução do professor:

'''print('Gerador de PA')
print('-=' * 10 + '-')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))'''