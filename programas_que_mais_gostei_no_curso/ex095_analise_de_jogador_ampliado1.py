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
print('-=' * 28 + '-')
print('cod  nome               gols                        total')
print(f'{'-' * 57}')
for p, cad in enumerate(jogadores):
    print(f'{p+1:>3}  {cad['nome']:<18} {str(cad['gols']):<20} {cad['total']:>12}') # Atualizei essa formatação com a solução que vi no código do professor.
while True:
    print('-' * 57)
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
            print(f'No {p+1}º jogo fez {g} gols.')'''


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
print('-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='') # Aqui está a maneira que o professor usou para fazer a formatação que eu não consegui! hehe. Transformou em string e fez a formatação. Vou aplicar essa ideia.
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'[ERRO] Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')'''


