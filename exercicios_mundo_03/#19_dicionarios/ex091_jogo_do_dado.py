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



from random import randint
from time import sleep
jogo = {}
basev = c = 0
print('Valores sorteados: ')
for j in range(1,5):
    jogo[f'jogador {j}'] = randint(1,6)
    print(f'O jogador {j} tirou {jogo[f'jogador {j}']}')
print('Ranking dos jogadores: ')


print(f'jogo[jogador 4]:{jogo['jogador 4']}')
for i in range(1, 5):
    menor = True
    for v in jogo.values():
        c += 1
        if c == 1:
            basev = v
        if basev < jogo[f'jogador 4']:
            menor = False
    if menor:
        jogo[f'jogador {c}'] = jogo.pop(f'jogador {c}')
    c = 0
for j, n in jogo.items():
    c += 1
    print(f'{c}º lugar: {j} com {n}')

