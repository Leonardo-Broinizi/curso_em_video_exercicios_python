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

maior

