jogador = {}
jogador_cópia = {}
partidas = []
jogadores = []
while True:
    print(f'\033[1m{'-' * 30}')
    res = ' '
    tot = 0
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    npartidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(npartidas):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
        tot += partidas[c]
    jogador['gols'] = partidas
    jogador['total'] = tot
    jogador_cópia = jogador.copy()
    jogador.clear()
    jogadores.append(jogador_cópia)
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break

print(f'\033[1m{'-' * 30}')
print('cod nome            gols       total\n',f'{'-' * 30}')
for p, cad in enumerate(jogadores):
    print(f'{p} {cad[p]['nome']} {cad[p]['gols']} {cad[p]['total']}')



'''print('-=' * 40 + '-')
print(f'O campo nome tem o valor {jogador['nome']}.')
print(f'O campo gols tem o valor {jogador['gols']}.')
print(f'O campo total tem o valor {jogador['total']}.')
print('-=' * 40 + '-')
print(f'O jogador {jogador['nome']} jogou {npartidas} partidas.')
for c in range(npartidas):
    print(f'    => Na partida {c}, fez {jogador['gols'][c]} gols.')
print(f'Foi um total de {jogador['total']} gols.')'''




