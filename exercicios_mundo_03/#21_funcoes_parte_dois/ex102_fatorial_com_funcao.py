#   Minha primeira tentativa antes de ver o programa do professor funcionando:

'''from time import sleep
def fatorial(num, show):
    n = 1
    if show:
        print(f'{num}! = ', end='')
        for c in range(num, 0, -1):
            sleep(1)
            n *= c
            if c > 1:
                print(f'{c} x ', end='')
        print(f'1 = {n}')
    else:
        for c in range(num, 0, -1):
            n *= c
        print(f'O fatorial de {num} é {n}.')

n = int(input('Digite um número para descobrir seu fatorial: '))
while True:
    r = str(input('Se quiser ver os cálculos, digite C, se apenas quer ver a resposta, digite R: ')).strip().upper()[0]
    if r in 'C':
        c = True
        break
    elif r in 'R':
        c = False
        break
    else:
        print('ERRO! Digite apenas C ou R.')
fatorial(n, c)'''

#    Meu código após ver o funcionamento do programa do professor Guanabara:

'''def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: [opcional] Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    if show:
        for c in range(num, 0, -1):
            f *= c
            if c > 1:
                print(f'{c} x ', end='')
        print('1 = ', end='')
        return f
    else:
        for c in range(num, 0, -1):
            f *= c
        return f

help(fatorial)
print(fatorial(7, show=True))'''

#    Código do professor Guanabara:

