# Primeira versão (na raça):
'''import random
cont = 'S'
print('Vamos jogar Jokenpô!')
while cont != 'N':
    esc = input('Escolha \033[35mPEDRA\033[m, \033[32mPAPEL\033[m ou \033[33mTESOURA\033[m: ').strip().upper()
    sort = ['PEDRA', 'PAPEL', 'TESOURA']
    sort = sort[random.randrange(len(sort))]
    if esc == sort and esc == 'PEDRA':
        print(f'Você escolheu \033[35m{esc}\033[m e eu escolhi \033[35m{sort}\033[m.')
        print('\033[4;1mIsso foi um \033[37mEMPATE\033[m\033[4;1m!\033[m')
    elif esc == sort and esc == 'PAPEL':
        print(f'Você escolheu \033[32m{esc}\033[m e eu escolhi \033[32m{sort}\033[m.')
        print('\033[4;1mIsso foi um \033[37mEMPATE\033[m\033[4;1m!\033[m')
    elif esc == sort and esc == 'TESOURA':
        print(f'Você escolheu \033[33m{esc}\033[m e eu escolhi \033[33m{sort}\033[m.')
        print('\033[4;1mIsso foi um \033[37mEMPATE\033[m\033[4;1m!\033[m')
    elif esc == 'PEDRA' and sort == 'PAPEL':
        print(f'Você escolheu \033[35m{esc}\033[m e eu escolhi \033[32m{sort}\033[m.')
        print('\033[4;1mVocê \033[31mPERDEU\033[m\033[4;1m essa!\033[m')
    elif esc == 'PEDRA' and sort == 'TESOURA':
        print(f'Você escolheu \033[35m{esc}\033[m e eu escolhi \033[33m{sort}\033[m.')
        print('\033[4;1mParabéns, você \033[34mVENCEU\033[m\033[4;1m essa!\033[m')
    elif esc == 'TESOURA' and sort == 'PEDRA':
        print(f'Você escolheu \033[33m{esc}\033[m e eu escolhi \033[35m{sort}\033[m.')
        print('\033[4;1mVocê \033[31mPERDEU\033[m\033[4;1m essa!\033[m')
    elif esc == 'TESOURA' and sort == 'PAPEL':
        print(f'Você escolheu \033[33m{esc}\033[m e eu escolhi \033[32m{sort}\033[m.')
        print('\033[4;1mParabéns, você \033[34mVENCEU\033[m\033[4;1m essa!\033[m')
    elif esc == 'PAPEL' and sort == 'TESOURA':
        print(f'Você escolheu \033[32m{esc}\033[m e eu escolhi \033[33m{sort}\033[m.')
        print('\033[4;1mVocê \033[31mPERDEU\033[m\033[4;1m essa!\033[m')
    elif esc == 'PAPEL' and sort == 'PEDRA':
        print(f'Você escolheu \033[32m{esc}\033[m e eu escolhi \033[35m{sort}\033[m.')
        print('\033[4;1mParabéns, você \033[34mVENCEU\033[m\033[4;1m essa!\033[m')
    else:
        print('\033[4;1mCOMANDO INVÁLIDO!\033[m ')
    cont = input('Quer jogar novamente? [S/N]').strip().upper()
print('Fim de jogo.')


sort = ['\033[31mPEDRA\033[m', '\033[32mPAPEL\033[m', '\033[33mTESOURA\033[m']'''

# Segunda versão, após ver o funcionamento do código do professor (sem ver o código):

from random import randint
from time import sleep
itens = {1:'\033[1;37mPedra\033[m\033[1m',
         2:'\033[1;32mPapel\033[m\033[1m',
         3:'\033[1;33mTesoura\033[m\033[1m'}
print(f'\033[1mVamos jogar Jo Ken Poo!\n')
cont = 'S'
while True:
    print('Suas opções: ')
    print(f'[1] {itens[1]} \n[2] {itens[2]} \n[3] {itens[3]}')
    escolha = int(input('\033[1mQual é sua jogada? '))
    if escolha > 0 and escolha < 4:
        esccomp = randint(1,3)
        print('Vamos lá: ')
        sleep(0.5)
        print('Jo')
        sleep(1)
        print('Ken')
        sleep(1)
        print('Po!!!')
        sleep(0.5)
        print('\033[1;31m=\033[1;34m-'*12+'\033[1;31m=\033[m\033[1m')
        sleep(0.3)
        print(f'Você jogou: {itens[escolha]}')
        sleep(0.5),
        print(f'Computador jogou: {itens[esccomp]}')
        sleep(0.5)
        if escolha == esccomp:
            print('Deu \033[1;36mEMPATE!\033[m\033[1m')
        elif escolha == 1 and esccomp == 2 or escolha == 2 and esccomp == 3 or escolha == 3 and esccomp == 1:
            print('Você \033[1;31mPERDEU!\033[1m')
        elif escolha == 1 and esccomp == 3 or escolha == 2 and esccomp == 1 or escolha == 3 and esccomp == 2:
            print('Você \033[1;34mVENCEU!\033[1m')
        print('\033[1;31m=\033[1;34m-'*12+'\033[1;31m=\033[m\033[1m')
        cont = input('Quer jogar novamente? [S/N]: ').upper().strip()
    else:
        print('Jogada inválida!')
    if cont == 'N':
        break

