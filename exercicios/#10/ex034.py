'''sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    print(f'O aumento será de R${sal*0.1:.2f}. O salário ficará em R${sal+(sal*0.1):.2f}.')
else:
    print(f'O aumento será de R${sal/100*15:.2f}. O salário ficará em R${sal+(sal/100*15):.2f}.')
    # Os valores decimais não estão sendo calculados corretamente!'''

'''Exercício resolvido pelo professor Guanabara: '''

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 15 / 100)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f}.')