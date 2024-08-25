lista_cadastros = []
cadastro = {}
cópia = {}
média = 0
print('\033[1m','-=' * 35 + '-')
while True:
    cont = ' '
    cadastro['nome'] = str(input('Nome: ')).strip()
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    cadastro['idade'] = int(input('Idade: '))
    cópia = cadastro.copy()
    lista_cadastros.append(cópia)
    cadastro.clear()
    média += cópia['idade']
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
média /= len(lista_cadastros)
print('-=' * 35 + '-')
print(f'Foram cadastradas {len(lista_cadastros)} pessoas.')
print(f'A média de idade do grupo cadastrado é {média:.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for c in lista_cadastros:
    if c['sexo'] == 'F':
        print(c['nome'], end=' - ')
print('\nAs pessoas com idade acima da média são: ', end=' ')
for c in lista_cadastros:
    if c['idade'] > média:
        print(f'Nome = {c['nome']}; sexo = {c['sexo']}; idade = {c['idade']};')
print(f'{'<< ENCERRADO >>':^33}')