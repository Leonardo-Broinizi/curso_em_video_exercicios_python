def aumentar(preço, taxa=10, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)
def diminuir(preço, taxa=20, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)
def dobro(preço, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)
def metade(preço, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

