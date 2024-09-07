#    Meu código:

'''from random import randint
from time import sleep
def sorteio(números):
    print('Sorteando os valores: ', end='')
    for n in range(1, 6):
        números.append(randint(1, 10))
        sleep(.3)
        print(números[-1], end=' ')
    print('Pronto!')
def somaPar(números, sp):
    for n in números:
        if n % 2 == 0:
            sp += n
    print(f'A soma entre os números pares sorteados é {sp}.') # Tentei mandar a variável sp para ser tratada pela função somaPar e me retornar o valor mas sempre retornava vazia. Preciso entender o motivo.

números = []
sp = 0
sorteio(números)
somaPar(números, sp)'''

#    Código do professor Guanabara:

from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
números = list()
sorteia(números)
somaPar(números)

