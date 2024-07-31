'''n1 = int(input('Digite um número: '))
res = int(input('Escolha a base de conversão: 1 para BINÁRIO, 2 para OCTAL e 3 para HEXADECIMAL: '))
c = 1
if res == 1:
    binário = 1
    while n1 > 1:
        c += 1
        n1 = n1 // 2
        print(f'n1 {n1}\nmódulo {n1%2}')
        if n1 % 2 < 1.0 or n1 == 1:
            binário = binário * 10
        else:
            binário = binário * 10 + 1
        if n1 == 1:
            binário = binário + 1
print(f'Binário: {binário}.')'''

'''Resolvido pelo professor Guanabara: '''
finish = 'S'
while finish == 'S':
    num = int(input('\033[1mDigite um número \033[4minteiro\033[m: '))
    print('''\033[1mEscolha uma das bases para conversão:
    \033[1m[ 1 ] Converter para \033[1;32mBINÁRIO\033[m
    \033[1m[ 2 ] Converter para \033[1;33mOCTAL\033[m
    \033[1m[ 3 ] Converter para \033[1;34mHEXADECIMAL\033[m''')
    opção = int(input('\033[1mSua opção: '))
    if opção == 1:
        print(f'\033[1;32m{num}\033[m\033[1m convertido para BINÁRIO é igual a: \033[1;32m{bin(num)[2:]}.\033[m\033[1m')
        finish = str(input('Deseja continuar [S/N]:')).upper().strip()
    elif opção == 2:
        print(f'\033[1;33m{num}\033[m\033[1m convertido para OCTAL é igual a: \033[1;33m{oct(num)[2:]}.\033[m\033[1m')
        finish = str(input('Deseja continuar [S/N]:')).upper().strip()
    elif opção == 3:
        print(f'\033[1;34m{num}\033[m\033[1m convertido para HEXADECIMAL é igual a:\033[1;34m {hex(num)[2:]}\033[m\033[1m.')
        finish = str(input('Deseja continuar [S/N]:')).upper().strip()
    else:
        print('\033[1mNúmero inválido! Tente novamente: ')
