
def aumentar(num, porc=1, converter=False):
    num += num / 100 * porc
    if converter:
        num = moeda(num)
    return num

def diminuir(num, porc=1, converter=False):
    num -= num / 100 * porc
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