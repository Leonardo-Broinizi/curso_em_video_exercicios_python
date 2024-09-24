def leiaInt(msg):
    print('-' * 30)
    while True:
        valor = str(input(msg)).strip().replace(' ', '')
        try:
            valor = int(valor)
        except Exception as erro:
            print(f'O erro encontrado foi: {erro}.')
        else:
            return valor
            break

def leiaFloat(num):
    print()

# Programa principal
n = leiaInt('Digite um número INTEIRO: ')
print(f'Você acabou de digitar o número {n}')

n = leiaFloat('Digite um número REAL: ')
print(f'Você acabou de digitar o número {n}')