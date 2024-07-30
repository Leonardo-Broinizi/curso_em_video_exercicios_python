from unicodedata import normalize
from random import randint
from time import sleep
print('\033[1;31m=' * 20)
print('\033[1;34mJOGO DO \033[35mPAR\033[1;34m ou \033[36mÍMPAR?')
print('\033[1;31m=' * 20)
vitórias = 0
while True:
    computador = randint(0,99)
    jogaesc = ''
    while jogaesc != 'P' and jogaesc != 'I':
        jogaesc = input('\033[1;7;33mVocê escolhe \033[35mPAR\033[1;33m ou \033[36mÍMPAR? \033[m').strip().upper()[0]
        jogaesc = normalize('NFKD', jogaesc).encode('ASCII','ignore').decode('ASCII')
        if jogaesc != 'P' and jogaesc != 'I':
            print('\033[1;31mEscolha inválida!')
    joganum = int(input(f'\033[m\033[1;7;40mAgora escolha um número:\033[m   '))
    resultado = computador + joganum
    sleep(0.3)
    print('\033[1;31mPreparado?')
    sleep(1.2)
    print('\033[1;37mVamos ver quem ganhou em: \033[1;33m', end='')
    sleep(1)
    for i in range(3,0,-1):
        print(i,end='... ')
        sleep(1.5)
    print()
    if jogaesc == 'P' and resultado % 2 == 0:
        print(f'\033[1;32mEu joguei o número \033[1;7;37m{computador}\033[m\033[1;32m e você jogou \033[1;7;33m{joganum}\033[m\033[1;32m. ')
        sleep(1.5)
        print(f'\033[1;33mA soma é \033[1;37m{resultado}\033[1;33m, que é \033[1;35mPAR\033[1;33m, portanto você \033[1;34mVENCEU\033[1;33m essa!!!')
        sleep(1.5)
        vitórias += 1
    elif jogaesc == 'P' and resultado % 2 == 1:
        print(f'\033[1;32mEu joguei o número \033[1;7;37m{computador}\033[m\033[1;32m e você jogou \033[1;7;33m{joganum}\033[m\033[1;32m. ')
        sleep(1.5)
        print(f'\033[1;33mA soma é \033[1;37m{resultado}\033[1;33m, que é \033[1;36mÍMPAR\033[1;33m, portanto você \033[1;31mPERDEU\033[1;33m essa!!!')
        sleep(1.5)
        break
    elif jogaesc == 'I' and resultado % 2 == 1:
        print(f'\033[1;32mEu joguei o número \033[1;7;37m{computador}\033[m\033[1;32m e você jogou \033[1;7;33m{joganum}\033[m\033[1;32m. ')
        sleep(1.5)
        print(f'\033[1;33mA soma é \033[1;37m{resultado}\033[1;33m, que é \033[1;36mÍMPAR\033[1;33m, portanto você \033[1;34mVENCEU\033[1;33m essa!!!')
        sleep(1.5)
        vitórias += 1
    elif jogaesc == 'I' and resultado % 2 == 0:
        print(f'\033[1;32mEu joguei o número \033[1;7;37m{computador}\033[m\033[1;32m e você jogou \033[1;7;33m{joganum}\033[m\033[1;32m. ')
        sleep(1.5)
        print(f'\033[1;33mA soma é \033[1;37m{resultado}\033[1;33m, que é \033[1;35mPAR\033[1;33m, portanto você \033[1;31mPERDEU\033[1;33m essa!!!')
        sleep(1.5)
        break
if vitórias == 0:
    print(f'\033[1;34mVocê \033[1;31mNÃO\033[1;34m venceu hoje!')
elif vitórias == 1:
    print(f'\033[1;34mVocê só venceu \033[1;33mUMA\033[1;34m vez hoje!')
else:
    print(f'\033[1;34mVocê venceu \033[1;33m{vitórias}\033[1;34m vezes hoje!')