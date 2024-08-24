from datetime import date
data = date.today()
ano = int('{}'.format(data.year))
cadastro = {}
cadastro['nome'] = str(input('\033[1mNome: ')).strip()
cadastro['idade'] = ano - int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
print('-=' * 40 + '-')
if cadastro['ctps'] > 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + (35 - (ano - cadastro['contratação']))
    print(f'Nome tem o valor {cadastro['nome']}')
    print(f'Idade tem o valor {cadastro['idade']}')
    print(f'CTPS tem o valor {cadastro['ctps']}')
    print(f'Contratação tem o valor {cadastro['contratação']}')
    print(f'Salário tem o valor {cadastro['salário']}')
    print(f'Aposentadoria tem o valor {cadastro['aposentadoria']}')
else:
    print(f'Nome tem o valor {cadastro['nome']}')
    print(f'Idade tem o valor {cadastro['idade']}')
    print(f'Você ainda não tem registro em carteira de trabalho.')
print(f'DICIONÁRIO COMPLETO:   {cadastro}')