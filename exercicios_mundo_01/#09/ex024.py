cidade = input('Digite o nome da cidade: ').strip()
cidade = cidade.upper()
if cidade.find('SANTO ') == 0:
    print('Esta cidade começa com o nome: Santo.')
else:
    print('Esta cidade não começa com o nome: Santo')


'''Solução Guanabara: '''

cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')

