cadastramento = []
while True:
    num = str(input('Digite um valor: '))
    if num not in cadastramento:
        cadastramento.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print(f'O valor {num} já foi adicionado anteriormente, então não pode mais ser cadastrado.')
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar o cadastramento? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
cadastramento.sort()
print(f'Os valores adicionados foram: {cadastramento}.')