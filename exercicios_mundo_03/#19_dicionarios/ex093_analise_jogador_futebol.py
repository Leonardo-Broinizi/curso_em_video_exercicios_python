jogador = {}
partidas = []
tot = 0
jogador['nome'] = str(input('\033[1mNome do jogador: ')).strip()
npartidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(npartidas):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    tot += partidas[c]
jogador['gols'] = partidas
jogador['total'] = tot
print('-=' * 40 + '-')
print(f'Jogador:  {jogador}')
print('-=' * 40 + '-')
print(f'O campo nome tem o valor {jogador['nome']}.')
print(f'O campo gols tem o valor {jogador['gols']}.')
print(f'O campo total tem o valor {jogador['total']}.')
print('-=' * 40 + '-')
print(f'O jogador {jogador['nome']} jogou {npartidas} partidas.')
for c in range(npartidas):
    print(f'    => Na partida {c}, fez {jogador['gols'][c]} gols.')
print(f'Foi um total de {jogador['total']} gols.')




