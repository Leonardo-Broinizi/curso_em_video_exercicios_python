#   Minha primeira tentativa antes de ver o programa do professor funcionando:

'''def ficha(jogador='o jogador', gols=0):
    print(f'{jogador} marcou {gols} gols.')

jogador = str(input('Digite o nome do jogador: ')).strip()
gols = int(input(f'Digite quantos gols {jogador} marcou: '))
ficha(jogador, gols)'''

# Meu código após ver o funcionamento do programa do professor Guanabara:

def ficha(jogador='<desconhecido>', gols=0):
    return f'O jogador {jogador} fez {gols} gols(s) no campeonato.'

print('-' * 33)
nome = str(input('Digite o nome do jogador: ')).strip()
num = str(input('Número de gols: '))

if len(nome) == 0 == len(num):
    print(ficha())
elif len(nome) == 0:
    print(ficha(gols=num))
elif len(num) == 0:
    print(ficha(jogador=nome))
else:
    print(ficha(nome,num))

#    Código do professor Guanabara:


