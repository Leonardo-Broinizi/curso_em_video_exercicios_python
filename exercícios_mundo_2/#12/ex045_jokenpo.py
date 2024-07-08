import random
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


sort = ['\033[31mPEDRA\033[m', '\033[32mPAPEL\033[m', '\033[33mTESOURA\033[m']