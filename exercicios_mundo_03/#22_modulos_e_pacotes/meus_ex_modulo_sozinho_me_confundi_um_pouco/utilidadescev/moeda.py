
def aumentar(num, porc=1, converter=False):
    num += num / 100 * porc
    num = str(f'{num:.2f}')
    if converter:
        num = moeda(num)
    return num

def diminuir(num, porc=1, converter=False):
    num -= num / 100 * porc
    num = str(f'{num:.2f}')
    if converter:
        num = moeda(num)
    return num

def dobro(num, converter=False):
    num *= 2
    if converter:
        num = moeda(num)
    return num

def metade(num, converter=False):
    num /= 2
    if converter:
        num = moeda(num)
    return num

def moeda(brl):
    brl = str(brl).replace('.', ',')
    if brl[-2] == ',':
        brl = brl + '0'
    return brl

def resumo(preço, porc_mais=0, porc_menos=0):
    print('\033[1m' + '-' * 40)
    print(f'{'RESUMO DO VALOR':^40}')
    print('-' * 40)
    print(f'Preço analisado:             R${moeda(preço)}')
    print(f'Dobro do preço:              R${dobro(preço, True)}')
    print(f'Metade do preço:             R${metade(preço, True)}')
    print(f'{porc_mais}% de aumento:              R${aumentar(preço, porc_mais, True)}')
    print(f'{porc_menos}% de redução:              R${diminuir(preço, porc_menos, True)}')
    print('-' * 40)