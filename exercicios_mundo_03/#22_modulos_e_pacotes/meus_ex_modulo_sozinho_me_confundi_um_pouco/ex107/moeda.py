def aumentar(num, porc=1):
    num += num / 100 * porc
    return num

def diminuir(num, porc=1):
    num -= num / 100 * porc
    return num

def dobro(num):
    num *= 2
    return num

def metade(num):
    num /= 2
    return num
