from random import randint
jogo = {}
c = mai = base = 0
print('Valores sorteados: ')
for j in range(1,5):
    jogo[f'jogador {j}'] = randint(1,6)
    print(f'O jogador {j} tirou {jogo[f'jogador {j}']}')
print('Ranking dos jogadores: ')
while True:
    trocou = False
    for v in jogo.values():
        c += 1
        if c == 1:
            mai = v
        if v > mai:
            trocou = True
            base = v
            jogo[f'jogador {c}'] = mai
            jogo[f'jogador {c-1}'] = base
    if not trocou:
        print(f'C:{c}')
        c = 0
        break
    c = 0
for j, n in jogo.items():
    c += 1
    print(f'{c}º lugar: {j} com {n}')
