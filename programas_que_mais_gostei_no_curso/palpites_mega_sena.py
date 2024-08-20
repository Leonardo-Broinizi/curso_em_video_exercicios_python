#    Obs.: Nesse caso eu gostei mais...

#    Meu código:

'''from random import randint
from time import sleep
lista = []
print('\033[1m','-'*33)
print(f'{'JOGA NA MEGA SENA':^33}')
print('\033[1m','-'*33)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f' SORTEANDO {jogos} JOGOS ':-^33}')
for j in range(0, jogos):
    lista.append([])
    for sorteio in range(0, 6):
        while True:
            sorteio = randint(1, 60)
            if sorteio not in lista[-1]:
                lista[-1].append(sorteio)
                break
    lista[-1].sort()
    sleep(1)
    print(f'Jogo {j+1}: {lista[-1]}')
sleep(1)
print(f'{f' < BOA SORTE! > ':-^33}')'''

#    Código do professor:
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3) # Aqui está a formatação que não consegui fazer no meu, tentando de outra maneira hehe
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

