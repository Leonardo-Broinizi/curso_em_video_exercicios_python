#    Meu código (não consegui formatar a variável da lista de gols feitos para ocuparem todas o
# mesmo número de colunas):

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
print('-=' * 25 + '-')
print('cod nome            gols                      total')
print(f'{'-' * 51}')
for p, cad in enumerate(jogadores):
    print(f'{p+1:>2} {cad['nome']:15} {str(cad['gols']):<16} {cad['total']:>12}') # Atualizei essa formatação com a solução que vi no código do professor.
while True:
    print('-' * 51)
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
            print(f'No jogo {p+1} fez {g} gols.')


#    Código do professor Guanabara:
'''time = list()
jogador = {}
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='') # Aqui está a maneira que o professor usou para fazer a formatação que eu não consegui! hehe
    print()
print('-' * 40)'''


