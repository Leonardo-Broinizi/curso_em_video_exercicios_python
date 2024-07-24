PA = int(input('Digite o primeiro termo para a Progressão Aritmética: '))
razão = int(input('Digite a razão dessa PA: '))
t = 10
while t != 0:
    while t > 1:
        print(f'{PA} -> ',end='')
        PA += razão
        t -= 1
    print(PA)
    PA += razão
    t = int(input('Quer mostrar quantos termos mais? (0 para sair)'))


