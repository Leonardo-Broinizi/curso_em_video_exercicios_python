#   O meu código está bem parecido com o do professor Guanabara, então não coloquei o dele.
# Só achei estranho o método sort() não estar funcionando bem para números com mais de uma casa decimal.
# Nesses casos, a ordenação fica apenas pelos números da última casa decimal de cada, com a penúltima servindo
# como critério de desempate, e a antepenúltima, caso a pelúltima também esteja empatade, e assim sucessivamente.
# Nesse caso, 1900 vêm antes de 2 e  19 vêm antes de 2000, por exemplo. Tentei descobrir o motivo mas não encontrei.

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