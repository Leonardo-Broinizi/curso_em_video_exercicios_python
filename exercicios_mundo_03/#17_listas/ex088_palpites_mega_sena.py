from random import randint
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
print(f'{f' < BOA SORTE! > ':-^33}')
