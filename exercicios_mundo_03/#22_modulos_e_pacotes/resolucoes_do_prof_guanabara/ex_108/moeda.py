def aumentar(preço, taxa=10):
    res = preço + (preço * taxa/100)
    return res
def diminuir(preço, taxa=20):
    res = preço - (preço * taxa/100)
    return res
def dobro(preço):
    res = preço * 2
    return res
def metade(preço):
    res = preço / 2
    return res

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

