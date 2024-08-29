#   Nas minhas tentativas, antes de pesquisar na internet, o máximo que consegui foi ordenar os valores do dicionário.
# Não consegui ordenar chaves e valores, como o professor. Tentei bastante. Vamos ver como ele fez...
#   Resultado das minhas primeiras tentativas:

from random import randint
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
    sleep(1)


#    Minha segunda tentativa, após pesquisar na internet:
'''# (primeiro, um exemplo de ordenação pego na internet):
d = {'cachorro':2, 'gato':3, 'elefante':1 }
for i in sorted(d, key = d.get):
    print(i, d[i]) # ficará: elefante 1; cachorro 2; gato 3;
'''

from random import randint
from time import sleep
print('\033[1mValores sorteados:')
jog = {}
for i in range(1, 5):
    sleep(1)
    jog[f'Jogador{i}'] = randint(1,6)
    print(f'O jogador {i} tirou {jog[f'Jogador{i}']}')
sleep(1)
print('\nRanking dos jogadores:')
for n, i in enumerate(sorted(jog, key = jog.get, reverse=True)): # ainda não compreendo plenamente essa linha.
    sleep(1)
    print(f'{n+1}º lugar: {i} com {jog[i]}')
print(f'Conteúdo do dicionário jog: {jog}')
#    Agora sim, acho que resolvi o problema. (Correção: o método que apliquei não reordenou o dicionário realmente,
# apenas o fez na exibição. O código do professor Guanabara consegue gerar um dicionário realmente ordenado com base em outro)


#    Resolução do professor:

from random import randint
from time import sleep
from operator import itemgetter #
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # ainda não compreendo plenamente essa linha também.
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
