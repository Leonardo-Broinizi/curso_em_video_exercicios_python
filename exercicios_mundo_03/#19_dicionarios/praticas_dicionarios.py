'''filme = {} # Declarando um dicionário
filme['título'] = 'Star Wars' # Adicionando uma chave 'título' com um valor 'Star Wars'
filme['ano'] = 1982 # Adicionando uma chave 'ano' com um valor 1982
filme['ano'] = 1983 # Alterando o valor da chave 'ano' para 1983
print(filme)
del filme['ano'] # Deletando a chave 'ano'
print(filme)'''

'''filme = {'título':'Star Wars',
        'ano':1977,
         'diretor':'George Lucas'
} # Declarando vários elementos de uma vez
print(filme.keys()) # Gerará um dicionário somente com as chaves
print(filme.values()) # Gerará um dicionário somente com os valores
print(filme.items()) # Gerará um dicionário com todos os ítens (ou seja, chaves e valores)
print(filme) # Imprimirá todos os ítens (ou seja, chaves e valores)

for k, v in filme.items(): # Com essa declaração um dicionário será gerado e a primeira variável temporária do no laço,
                           # que aqui está nomeada como 'k', mostrará a chave do laço, e a segunda 'v' o valor:
    print(f'O {k} é {v}')

locadora = ['Star Wars', filme, 'Matrix', 132]
print(locadora)'''

'''pessoas = {'nome':'Leonardo', 'sexo':'masculino','idade':'32'}
pessoas['peso'] = 98.5
for k in pessoas.keys():
    print(k, end=', ')
print()
for v in pessoas.values():
    print(v, end=', ')
print()
for i in pessoas.items():
    print(i, end=', ')'''

'''estado = dict()
Brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    Brasil.append(estado.copy())   # Método para copiar os dados de um dicionário sem criar uma ligação entre eles.
for estado in Brasil:
    for key, value in estado.items():
        print(f'O campo {key} tem o valor {value}')
print()
for estado in Brasil:
    print(f'UF: {estado['uf']}. Sigla: {estado['sigla']}.')'''


notas = {'Léo': 10, 'João': 8, 'Maria': 9, 'Aline': 7}
notas['Maria'] = notas.pop('Maria')
print(notas)