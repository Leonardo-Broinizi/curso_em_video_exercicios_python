#    Meu código:

'''cadastro = {}
cadastro['Nome'] = str(input('Nome: ')).strip()
cadastro['Média'] = float(input(f'Média de {cadastro['Nome']}: '))
print(f'Nome é igual a {cadastro['Nome']}\nMédia é igual a {cadastro['Média']}')
if cadastro['Média'] >= 7:
    cadastro['Situação'] = 'Aprovado'
elif cadastro['Média'] >= 5:
    cadastro['Situação'] = 'Recuperação'
else:
    cadastro['Situação'] = 'Reprovado'
print(f'Situação é igual a {cadastro['Situação']}')'''

#    Código do professor Guanabara:
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')

