'''d = float(input('Digite a distância da sua viagem em km: '))
if d <= 200:
    print(f'Sua passagem custará R$ {d*0.5:.2f}.')
else:
    print(f'Sua passagem custará R$ {d * 0.45:.2f}.')'''

'''Maneira simplificada do professor Guanabara: '''

distância = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}km.')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}.')