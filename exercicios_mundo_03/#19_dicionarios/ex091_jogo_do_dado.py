#   Nas minhas tentativas, o máximo que consegui foi ordenar os valores do dicionário.
# Não consegui ordenar chaves e valores, como o professor. Tentei bastante. Vamos ver como ele fez...
#   Minha tentativa:

'''from random import randint
from time import sleep
jogo = {}
c = basev = 0
basek = ' '
print('Valores sorteados: ')
for j in range(1,5):
    jogo[f'jogador {j}'] = randint(1,6)
    print(f'O jogador {j} tirou {jogo[f'jogador {j}']}')
    sleep(1)
print('Ranking dos jogadores: ')
while True:
    trocou = False
    for v in jogo.values():
        c += 1
        if c == 1:
            basev = v
        if v > basev:
            trocou = True
            jogo[f'jogador {c}'] = basev
            jogo[f'jogador {c-1}'] = v
        else:
            basev = v
    if not trocou:
        c = 0
        break
    c = 0
for j, n in jogo.items():
    c += 1
    print(f'{c}º lugar: {j} com {n}')
    sleep(1)'''

#    Resolução do professor:

