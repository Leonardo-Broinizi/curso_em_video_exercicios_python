#    Minha primeira tentativa antes de ver o programa do professor funcionando:

'''def leiaInt():
    num = False
    while True:
        n = str(input('Digite um número: '))
        for l in n:
            if l not in '0123456789':
                print('ERRO! Você não digitou um número. Tente novamente.')
                num = False
                break
            num = True
        if num:
            print(f'Você digitou o número {n}.')
            break


leiaInt()'''

#    Meu código após ver o funcionamento do programa do professor Guanabara (esse não ficou tão diferente do anterior):

def leiaInt(entrada):
    print('-' * 30)
    while True:
        não = False
        res = str(input(f'\033[m{entrada} '))
        for l in res:
            if l not in '0123456789':
                não = True
                break
        if não or len(res) < 1:
            print('\033[31mERRO! Digite um número válido.')
        else:
            break
    return res


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

#    Código do professor Guanabara: