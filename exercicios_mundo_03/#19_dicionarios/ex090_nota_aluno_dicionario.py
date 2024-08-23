cadastro = {}
cadastro['Nome'] = str(input('Nome: ')).strip()
cadastro['Média'] = float(input(f'Média de {cadastro['Nome']}: '))
print(f'Nome é igual a {cadastro['Nome']}\nMédia é igual a {cadastro['Média']}')
if cadastro['Média'] >= 7:
    cadastro['Situação'] = 'Aprovado'
else:
    cadastro['Situação'] = 'Reprovado'
print(f'Situação é igual a {cadastro['Situação']}')

