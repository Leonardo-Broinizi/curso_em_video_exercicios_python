#    Os códigos ficaram um pouco diferentes, mas gostei das soluções que eu encontrei.
#    Meu código:

from time import sleep
def contador(inicio, fim, passo):
    print('-=' * 15 + '-')
    sleep(.5)
    if passo < 0:
        passo = - passo
    elif passo == 0:
        passo = 1
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
print('-=' * 15 + '-')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

#    Código do professor Guanabara:

'''from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)'''
