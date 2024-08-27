jogador = {}
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
    print(f'{p:>2} {cad['nome']:15} {cad['gols']} {cad['total']:>12}')
while True:
    print('-' * 49)
    while True:
        res = int(input('  Mostrar dados de qual jogador? [999 para SAIR]: '))
        if res >= len(jogadores) and res != 999:
            print('VALOR INCORRETO! Tente novamente.')
        else:
            break
    if res == 999:
        print('<< VOLTE SEMPRE >>')
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[res]['nome']}:')
        for p, g in enumerate(jogadores[res]['gols']):
            print(f'No jogo {p} fez {g} gols.')
