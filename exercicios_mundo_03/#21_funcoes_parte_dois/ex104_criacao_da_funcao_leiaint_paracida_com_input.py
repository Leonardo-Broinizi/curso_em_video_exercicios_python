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

'''def leiaInt(entrada):
    print('-' * 30)
    while True:
        não = False
        res = str(input(f'{entrada} '))
        for l in res:
            if l not in '0123456789':
                não = True
                break
        if não or len(res) < 1:
            print('\033[31mERRO! Digite um número válido.\033[m')
        else:
            break
    return res

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''


#    O código do professor é mais enxuto que o meu, muito por causa da função isnumeric que eu não conhecia,
# mas fico feliz por ainda assim ter encontrado uma solução.
#    Código do professor Guanabara:

def leiaInt(msg):
    print('-' * 30)
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
