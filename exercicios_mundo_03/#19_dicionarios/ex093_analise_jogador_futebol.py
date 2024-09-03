#    Obs.: Pensei que meu código estaria muito parecido com o do professor, por isso não anotei o dele,
# mas percebí que o código do professor estava sensívelmente melhor que o meu e fui anotando as diferenças.

'''jogador = {}
partidas = []
jogador['nome'] = str(input('\033[1mNome do jogador: ')).strip()
npartidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(npartidas):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:] # Eu me lembrei, vendo o vídeo do professor, de colocar [:] para não gerar uma ligação entre as listas. Embora nos meus testes a lista de dentro do dicionário não tenha ficado com a ligação com a de fora, é bom não me esquecer disso!
jogador['total'] = sum(partidas) # Eu tinha feito uma variável variável acumuladora chamada 'tot' para calcular o total de gols mas ví, pelo código do professor, que com o método 'sum' fica bem mais prático.
print('-=' * 40 + '-') # Aqui o professor fez um for, economizando várias linhas, da seguinte maneira: for k, v in jogador.items(): (e na linha de baixo:  print(f'O campo {k} tem o valor {v}')
print(f'Jogador:  {jogador}')
print('-=' * 40 + '-')
print(f'O campo nome tem o valor {jogador['nome']}.')
print(f'O campo gols tem o valor {jogador['gols']}.')
print(f'O campo total tem o valor {jogador['total']}.')
print('-=' * 40 + '-')
print(f'O jogador {jogador['nome']} jogou {npartidas} partidas.')
for c in range(npartidas):
    print(f'    => Na partida {c+1}, fez {jogador['gols'][c]} gols.')
print(f'Foi um total de {jogador['total']} gols.')'''


#    Meu código (não consegui formatar a variável da lista de gols feitos para ocuparem todas o
# mesmo número de colunas):

'''jogador = {}
partidas = []
jogadores = []
while True:
    print(f'\033[1m{'-' * 30}')
    res = ' '
    tot = 0
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    npartidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(npartidas):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
        tot += partidas[c]
    jogador['gols'] = partidas.copy()
    jogador['total'] = tot
    jogadores.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print('-=' * 20 + '-')
print('cod nome            gols            total\n',f'{'-' * 40}')
for p, cad in enumerate(jogadores):
    print(f'{p+1:>2} {cad['nome']:15} {cad['gols']} {cad['total']:>12}')
while True:
    print('-' * 49)
    while True:
        res = int(input('  Mostrar dados de qual jogador? [999 para SAIR]: '))
        if res > len(jogadores) and res != 999 or res == 0:
            print('\nVALOR INCORRETO! Tente novamente.\n')
        else:
            break
    if res == 999:
        print('<< VOLTE SEMPRE >>')
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[res-1]['nome']}:')
        for p, g in enumerate(jogadores[res-1]['gols']):
            print(f'No jogo {p+1} fez {g} gols.')'''


#    Finalmente deixei de preguiça e copiei o código do professor rs:
#    Código do professor Guanabara:

jogador = {}
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

