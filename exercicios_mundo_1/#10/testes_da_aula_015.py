'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo.')
else:
    print('Seu carro é velho.')
print('Fim.')'''

'''A seguir teremos um exemplo de uma simplificação, como uma shorthand, da estrutura condicional 'if/else': '''

'''tempo = int(input('Quantos anos tem seu carro? '))
print('Seu carro é novo.'if tempo<=3 else 'Seu carro é velho.')
print('Fim.')

resp = input('Você quer continuar? [S/N]')
print('Então vamos lá!' if resp=='s'or resp=='S' else 'Ok, até mais.')

# from datetime import date  # datetime é um módulo para datas.

# date.today().year # Fará com que apenas o ano atual seja recebido.

nome = str(input('Qual é o seu nome? ')).upper().strip()
if nome == 'LEONARDO':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal.')
print(f'Bom dia, {nome}.'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A média é: {m:.2}.')
if m >= 6.0:
    print('Sua média é boa, parabéns!')
else:
    print('Sua média é insatisfatória, estude mais.')