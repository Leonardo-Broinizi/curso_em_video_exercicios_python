#    Meu código após ver o funcionamento do programa do professor Guanabara:
def manual(e):
    if e.upper() not in 'FIM':
        print(f'\033[44m' + '~' * 45)
        print(f"{f"Acessando o manual do comando '{e}'":^45}")
        print(f'\033[44m' + '~' * 45, '\n\033[m\033[7m')
        help(e)
        print(f'\033[m\033[42m' + '~' * 25)
        print(f'{'SISTEMA DE AJUDA PyHELP':^25}')
        print(f'\033[42m' + '~' * 25)

    return e

print('\033[42;1m' + '~' * 40)
print(f'{'SISTEMA DE AJUDA PyHELP':^40}')
print('\033[42;1m' + '~' * 40)
while True:
    esc = manual(str(input('\033[m\033[1mFunção ou Biblioteca > ')).strip())
    if esc.upper() == 'FIM':
        print('\033[41;1m' + '~' * 20)
        print(f'{'ATÉ LOGO!':^20}')
        print('\033[41;1m' + '~' * 20)
        break


#    Código do professor Guanabara: