# Preferí minha resolução por pouca margem (sem levar em conta a estética do resultado final).

# Minha resolução do exercício, com acréscimo após ver o exercício do professor funcionando, já que (novamente rsrs) ví uma funcionalidade do programa que não estava no enunciado:

'''from random import randint
s = c = 0
while True:
    r = -1
    s = randint(0,10)
    c = 0
    print('\033[1;33m======================================================\n\033[1;34mVou pensar em um número entre 0 e 10, tente adivinhar!\n\033[1;33m======================================================')
    while s != r:
        c += 1
        r = int(input(f'\033[1;36mFaça sua {c}ª tentativa: '))
        if r == s:
            print('\033[1;33mParabéns, você acertou!!!')
            print(f'\033[1;31mO número sorteado foi: \033[1;31m{s}.\033[1;33m\nForam necessárias {c} tentativas.')
        elif r > s:
            print('\033[1;31mErrado! Número MAIOR.\033[1;36m')
        else:
            print('\033[1;31mErrado! Número MENOR.\033[1;36m')
    cont = input('\033[1;36mQuer tentar novamente? [S/N] ').strip().upper()
    if 'N' in cont:
        break
print('\033[1;33mOk, até a proxima!')'''

# Resolução do professor Guanabara:

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas.')
