#    Minha primeira versão:

'''def maior(num):
    m = 0
    for n in num:
        if n > m:
            m = n
    print(f'O maior valor digitado foi: {m}.')

números = []
while True:
    números.append(int(input('Digite um número: ')))
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        else:
            print('Caractere inválido! Digite apenas S ou N.')
    if res == 'N':
        break
maior(números)
'''

#    Minha segunda versão:

from time import sleep
def maior(* valores):
    print('-=' * 20 + '-')
    print('Analisando os valores passados...')
    for v in valores:
        sleep(.5)
        print(v, end=' ')
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {max(valores)}.')


maior(2, 9, 4, 5, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
a = int(input('Digite o 1º valor: '))
b = int(input('Digite o 2º valor: '))
c = int(input('Digite o 3º valor: '))
maior(a, b, c)