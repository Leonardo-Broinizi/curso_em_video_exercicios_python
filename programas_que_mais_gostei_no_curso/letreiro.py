def letreiro(texto_central):
    n = len(texto_central) / 3
    print('\033[1;31m' + '-=-' * int(n))
    print(f'\033[33m{texto_central}')
    print('\033[1;31m' + '-=-' * int(n))
while True:
    texto_central = str(input('\033[34mDigite o texto central ou SAIR: ')).upper().strip()
    if texto_central == 'SAIR':
        print('Até logo!')
        break
    else:
        letreiro(texto_central)