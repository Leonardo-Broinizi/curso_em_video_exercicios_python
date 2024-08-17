'''Obs.: O 'in' é muito útil para verificar se determinado elemento está em uma lista (entre outras coisas)
pois assim evitamos possíveis erros que viriam, por exemplo, ao usarmos o método 'remove' com um valor
que não consta dentro da lista. Para evitar isso, usaríamos uma estrutura dessa:
if 'elemento_de_exemplo' in lista:
    lista.remove(elemento_de_exemplo)
else:
    print('elemento não encontrado na lista')'''

#   Métodos de inserção em listas:

'''   Há o já conhecido método append.
   O método 'insert' para listas adiciona elementos no índice selecionado, 'empurrando' os
outros elementos. '''
#   Exemplo:
'''lista = ['Leonardo','Broinizi','Farias']
lista.insert(2,'de')
for palavras in lista:
    print(palavras, end=' ')'''

#   Métodos de remoção:

'''   Há o método del, com a sintaxe 'del nome_da_lista[(índice do elemento a ser deletado)]'.'''
#   Exemplo do uso de del: 
'''print()
del lista[2]
for i in lista:
    print(i,end=' ')'''
    
'''   Também há o método pop, com a sintaxe 'nome_da_lista.pop(índice do elemento a ser deletado)'.
    Caso se queira deletar o último elemento da lista, mesmo não sabendo sua posição no índice, basta não declarar nada dentro dos parêntesis.
    Essa função também tem a propriedade, opcional mas muitas vezes necessária, de guardar em outra variável o valor que será deletado da lista.
Para isto, basta colocar uma variável para receber antes de realizar a sintaxe do método. '''
#   Exemplos do uso de pop:
'''print()
a = lista.pop(0)
for i in lista:
    print(i,end=' ')
print('\nO valor guardado através do método pop, que foi removido da lista, foi:',a)
lista.pop()
print('\n O método pop, com os parêntesis vazios, excluiu o último elemento da lista: ',lista)'''

"""   O método 'remove' tem a seguinte sintaxe: nome_da_lista.remove['valor_do_que_será_excluído']. 
Como vimos, essa propriedade não remove pelo índice, mas pelo valor guardado em sí. 
 Atenção: esse método removerá apenas o primeiro valor correspondente que ele encontrar, 
 procurando do início dos índices em diante."""
#   Exemplo do uso de remove:

'''lista.remove('Broinizi')
print('\nO método remove com o valor Broinizi declarado removeu este nome da lista: ',lista,'\n')'''

""" #   Método de criação de lista numérica com a função 'list' e o método 'range':
    A função list junto ao método range gerará uma lista numérica. O primeiro valor declarado entre 
parêntesis é o número inicial da lista, o segundo é o número final, e o terceiro, opcional, 
é o número de casas que serão puladas entre um número e outro."""
#   Exemplo de lista com list e range(com três valores no range):
'''lista_com_range = list(range(44,11,-2))
print(lista_com_range)'''

'''#   Método sort pega uma lista numérica desordenada e a reorganiza em ordem crescente, ou decrescente,
caso se declare o parâmetro 'reverse=True' dentro de parêntesis.'''
#   Exemplo de uso do método sort():

'''n = [3,43,1,34,56,3,7,24,5,45,-2,42,22,11,15,4,8,5]
n.sort(reverse=True)
print(n,'\n')'''

'''É bom lembrar que, em Python, se eu pedir para uma lista receber outra lista do modo simples 
(listaA = listaB, por exemplo) as duas listas se entrelaçarão e o que for alterado em uma será alterado na outra '''

'''listaA = ['a','b','c','d','e']
listaB = listaA
listaA.append(1) # veja que aqui eu estou alterando a listaA, e, quanto ou printar a listaB, essa alteração aparecerá!
listaB.append(2)
print(listaB)'''
#    Se eu quiser que uma lista receba todos os elementos de outra mas sem esse entrelaçamento, ou seja,
# com ambas se mantendo independentes uma da outra, preciso usar a seguinte sintaxe: listaB = listaA[:].
#   Exemplo:
'''listaA = ['a','b','c','d','e']
listaB = listaA[:]
listaA.append(1) # veja que aqui eu estou alterando a listaA, e, quanto ou printar a listaB, essa alteração aparecerá!
listaB.append(2)
print(listaB)'''

#   Analisando índices de listas dentro de lista (dentro de listas rs):

'''dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas = list()
pessoas.append(dados[:])
pessoas = [['Pedro',25],['Maria',[9,7,5,3],19],['João',32]]
print(pessoas[2])
print(pessoas[0][0])
print(pessoas[1][1][2])'''

'''teste = list()
teste.append('Leonardo')
teste.append(32)
galera = []
galera.append(teste[:]) # É importante não esquecer que, caso se faça uma cópia de uma lista, ambas estarão ligadas,
# e o que for feito a uma será autamaticamente feiro a outra. Para evitar essa ligação, quando não for desejada,
# é que fazemos uma cópia apenas dos dados da outra lista, usando o índice desse modo [:].
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''