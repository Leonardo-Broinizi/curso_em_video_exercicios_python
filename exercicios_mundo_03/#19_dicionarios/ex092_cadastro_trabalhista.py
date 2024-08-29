#    Meu código está relativamente parecido com o do professor. O dele está melhor no tratamento com
# o datetime, por isso preciso aprender cada vez mais a sintaxe da linguagem para conhecer as possibilidades.
#    Meu código:

'''from datetime import date
data = date.today()
ano = int('{}'.format(data.year))
cadastro = {}
cadastro['nome'] = str(input('\033[1mNome: ')).strip()
cadastro['idade'] = ano - int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] > 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + (35 - (ano - cadastro['contratação']))
    print('-=' * 40 + '-')
    print(f'Nome tem o valor {cadastro['nome']}')
    print(f'Idade tem o valor {cadastro['idade']}')
    print(f'CTPS tem o valor {cadastro['ctps']}')
    print(f'Contratação tem o valor {cadastro['contratação']}')
    print(f'Salário tem o valor R${cadastro['salário']:.2f}')
    print(f'Aposentadoria tem o valor {cadastro['aposentadoria']}')
else:
    print('-=' * 40 + '-')
    print(f'Nome tem o valor {cadastro['nome']}')
    print(f'Idade tem o valor {cadastro['idade']}')
    print(f'Você ainda não tem registro em carteira de trabalho.')
# print(f'DICIONÁRIO COMPLETO:   {cadastro}')'''

#    Código do professor Guanabara:

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')

