#   Obs.: No meu código não fiz listas dentro de lista, o que seria útil
# e atenderia melhor ao objetivo do exercício. Tirando isso,
# meu código está com a lógica muito parecido com a lógica do código do professor Guanabara.
#   Meu código:

'''cadastro = []
pesados = []
leves = []
maior = menor = c = 0
while True:
    res = ' '
    c += 1
    cadastro.append(str(input('Nome: ')).strip())
    cadastro.append(float(input('Peso: ')))
    if c == 1 or cadastro[-1] < menor:
        menor = cadastro[-1]
    if cadastro[-1] > maior:
        maior = cadastro[-1]
    while res not in 'NS':
        res = str(input('Quer cadastrar mais alguém? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
for posição, peso in enumerate(cadastro):
    if peso == maior:
        pesados.append(cadastro[posição-1])
    if peso == menor:
        leves.append((cadastro[posição-1]))
print(f'Ao todo, você cadastrou {len(cadastro)/2:.0f} pessoas.')
print(f'O maior peso cadastrado foi de {maior}kg. Peso de ', end='')
for p, nome in enumerate(pesados):
    if p < len(pesados)-1:
        print(nome, end=', ')
print(f'{pesados[-1]}.')
print(f'O menor peso cadastrado foi de {menor}kg. Peso de ', end='')
for p, nome in enumerate(leves):
    if p < len(leves)-1:
        print(nome, end=', ')
print(f'{leves[-1]}.')'''

#    Código do professor Guanabara:

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' *30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai: # Achei interessanto que aqui, p equivale a uma lista, então pode ser trabalhado com um índice.
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

