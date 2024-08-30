#    Meu código:

'''lista_cadastros = []
cadastro = {}
cópia = {}
média = 0
print('\033[1m','-=' * 35 + '-')
while True:
    cont = ' '
    cadastro['nome'] = str(input('Nome: ')).strip()
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, responda apenas S ou M.')
    cadastro['idade'] = int(input('Idade: '))
    cópia = cadastro.copy()
    lista_cadastros.append(cópia)
    cadastro.clear()
    média += cópia['idade']
    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if cont not in 'SN':
            print('ERRO! Por favor, responda apenas S ou N.')
        else:
            break
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
print('\nAs pessoas com idade acima da média são: ')
for c in lista_cadastros:
    if c['idade'] > média:
        print(f'    Nome = {c['nome']}; sexo = {c['sexo']}; idade = {c['idade']};')
print(f'{'<< ENCERRADO >>':^33}')'''

#    Código do professor Guanabara:

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.') # Interessante notar que, nessa iteração, o uso de 'else' é desnecessário, já que, caso o if não seja satisfeito, a próxima linha será execultada, e, caso seja satisfeito, o break impedirá sua execussão.
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end=' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<< ENCERRADO >>')
