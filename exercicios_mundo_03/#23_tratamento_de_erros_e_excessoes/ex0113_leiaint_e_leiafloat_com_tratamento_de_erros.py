#    Minha resolução:

'''def leiaInt(msg):
    print('-' * 30)
    while True:
        valor = str(input(msg))#.strip().replace(' ', '')
        try:
            valor = int(valor)
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
        except:
            print(f'\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return valor
            break

def leiaFloat(mgs):
    print('-' * 30)
    while True:
        valor = str(input(mgs))
        try:
            valor = float(valor)
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
        except:
            print('\033[31mERRO: por favor digite um número inteiro válido.\033[m')
        else:
            return valor

# Programa principal
inteiro = leiaInt('Digite um número INTEIRO: ')
print(f'Você acabou de digitar o número {inteiro}')

real = leiaFloat('Digite um número REAL: ')
print(f'Você acabou de digitar o número {real}')

print(f'O número inteiro foi {inteiro} e o real foi {real}')'''


#    Código do professor Guanabara:



