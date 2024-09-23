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

#   Considerações após assistir o vídeo de resposta do professor: O código do professor já leva a média calculada dentro
# da lista, coisa que não fiz. Por esse ponto ele é mais completo que o meu. Também a forma como o código do professor
# incorpora os dado na lista completa também foi mais engenhoso e eficiente que o meu, já que fazia entrar de uma vez
# uma lista com nome, outra lista com ambas as notas, e a média, por vez. Meu código vazia entrar uma lista com nome e outra lista com
# as notas.

#   Minha segunda tentativa:

'''boletim = []
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
    print('-' * 35)'''

#   Código do professor Guanabara:

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{'No.':<4}{'NOME':10}{'MÉDIA':>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('<<< VOLTE SEMPRE >>>')
