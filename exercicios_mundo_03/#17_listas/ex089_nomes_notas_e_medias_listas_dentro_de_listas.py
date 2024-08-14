#    Minha primeira tentativa (antes de ver o programa do professor funcionando e,
# pra falar a verdade, sem ter compreendido plenamente o enunciado):

'''boletim = [[],[],[]]
while True:
    r = ' '
    boletim[-3].append(str(input('Digite o nome: ')).strip())
    boletim[-2].append(float(input('Digite a 1ª nota: ')))
    boletim[-1].append(float(input('Digite a 2ª nota: ')))
    while r not in 'NS':
        r = str(input('Quer continuar cadastrando? ')).upper().strip()[0]
    if r == 'N':
        break
print('As médias dos alunos foram: ')
for p, nomes in enumerate(boletim[0]):
    print(f'A média do aluno {nomes} é: {(boletim[1][p] + boletim[2][p]) / 2:.2f}')'''

#   Segunda tentativa:

boletim = []
while True:
    r = ' '
    boletim.append([str(input('Nome: '))])
    boletim[-1].append([float(input('Nota 1: '))])
    boletim[-1][-1].append(float(input('Nota 2: ')))
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 35)
print('Nº  NOME             MÉDIA')
print('-' * 27)
for n in range(len(boletim)):
    print(f'{n}   {boletim[n][0]:15}   {(boletim[n][1][0] + boletim[n][1][1]) / 2:.2f}')
print('-' * 35)
while True:
    esc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if esc == 999:
        print('FINALIAZANDO...\n<<< VOLTE SEMPRE >>>')
        break
    elif esc < len(boletim):
        print(f'As notas de {boletim[esc][0]} são {boletim[esc][1]}')
    else:
        print('Número não encontrado! Por favor, tente novamente.')
    print('-' * 35)