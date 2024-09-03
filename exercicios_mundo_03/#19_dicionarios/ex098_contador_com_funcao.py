from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 15 + '-')
    sleep(.5)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    if inicio > fim:
        passo = - passo
        f = -1
    else:
        f = 1
    for c in range(inicio, fim+f, passo):
        sleep(.5)
        print(c, end=' ')
    sleep(.5)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)