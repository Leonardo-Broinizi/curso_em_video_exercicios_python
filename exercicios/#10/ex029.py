''' vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado em R${multa:.2f}.')
else:
    print('Você não foi multado.') '''

'''Problema resolvido pelo professor Guanabara:'''

velocidade = float(input('Qual é a velocidade do carro?'))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança.')