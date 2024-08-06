'''#   Métodos de inserção em listas:

 Há o já conhecido método append.
   O método 'insert' para listas adiciona elementos no índice selecionado, 'empurrando' os
outros elementos. '''
#   Exemplo:
lista = ['Leonardo','Broinizi','Farias']
lista.insert(2,'de')
for palavras in lista:
    print(palavras, end=' ')

'''#   Métodos de remoção: 

   Há o método del, com a sintaxe 'del nome_da_lista[(índice do elemento a ser deletado)]'.
#   Exemplo do uso de del: 
print()
del lista[2]
for i in lista:
    print(i,end=' ')
    
    Também há o método pop, com a sintaxe 'nome_da_lista.pop(índice do elemento a ser deletado)'.
    Caso se queira deletar o último elemento da lista, mesmo não sabendo sua posição no índice, basta não declarar nada dentro dos parêntesis.
    Essa função também tem a propriedade, opcional mas muitas vezes necessária, de guardar em outra variável o valor que será deletado da lista.
Para isto, basta colocar uma variável para receber antes de realizar a sintaxe do método. '''
#   Exemplos do uso de pop:
print()
a = lista.pop(0)
for i in lista:
    print(i,end=' ')
print('\nO valor guardado através do método pop, que foi removido da lista, foi:',a)
lista.pop()
print('\n O método pop, com os parêntesis vazios, excluiu o último elemento da lista: ',lista)

"""   O método remove tem a seguinte sintaxe: nome_da_lista.remove['valor_do_que_será_excluído']. 
Como vimos, essa propriedade não remove pelo índice, mas pelo valor guardado em sí. """
#   Exemplo do uso de remove:

lista.remove('Broinizi')
print('\n',lista)

""" #   Método de criação de lista numérica com a função 'list' e o método 'range':
    A função list junto ao método range gerará uma lista numérica """
lista_com_range = list(range(4,11))
print(lista_com_range)