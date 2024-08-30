#    Obs.: Pensei que meu código estaria muito parecido com o do professor, por isso não anotei o dele,
# mas percebí que o código do professor estava sensívelmente melhor que o meu e fui anotando as diferenças.

jogador = {}
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
print(f'Foi um total de {jogador['total']} gols.')