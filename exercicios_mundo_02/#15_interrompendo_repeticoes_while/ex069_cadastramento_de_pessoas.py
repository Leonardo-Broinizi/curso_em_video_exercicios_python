#   Preferí o código do professor porque achei um pouco mais simples do que o meu.

#   Meu código:

'''mais18 = homens = msub20 = 0
continuar = ''
while continuar != 'N':
    idade = int(input('Digite a idade: '))
    while True:
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
        if sexo not in 'MF':
            print('Comando inválido!')
        else:
            break
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        msub20 += 1
    while True:
        continuar = str(input('Quer cadastrar mais pessoas? [S/N] ')).upper().strip()[0]
        if continuar in 'NS':
            break
print(f'Foram cadastradas {mais18} pessoas com mais de 18 anos.')
print(f'No total, {homens} homens foram cadastrados, com qualquer idade, e {msub20} mulheres com menos de 20 anos.')'''

#   Código do professor Guanabara:

tot18 = toth = totM20 = 0
while True:
    idade = int(input('Idade: ' ))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')