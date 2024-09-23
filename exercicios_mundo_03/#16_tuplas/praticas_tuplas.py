#   Tuplas são IMUTÁVEIS!!!
#   Tuplas aceitam dado de tipos diferentes (int, float, str).
#   Tuplas podem ser deletadas com o método 'del'.

#   As tuplas são imutáveis quando o código está rodando. Só podem ser editadas, obviamente, enquanto  estamos formando o código.

#   Existem 3 maneiras de utilizarmos o 'for' para percorrer tuplas, cada uma servindo melhor para determinada finalidade:

'''lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche: # 1ª maneira: Usando de for para percorrer tuplas (e acho que listas também) dessa maneira ele devolverá a variável de controle já com o valor encontrado dentro do índice referente. Para obter apenas a posição precisamos fazer igual ao exemplo seguinte.
    print(comida, end=', ')
print()
print()
for cont in range(0, len(lanche)): # 2ª maneira: Dessa forma a variável de controle retornará apenas a posição que cada laço está percorrendo.
    print(lanche[cont], cont,end=', ')
print()
print()
for posição, comida in enumerate(lanche): # 3ª maneira: Enumerate retorna duas variáveis de controle: a primeira com a posição e a segunda com o ítem daquela posição.
    print(comida, posição, end=', ')


#   Método SORTED:

lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) # O método 'sorted' mostrará uma lista contendo os ítens da referida tupla em ordem alfabética (lembrando que isso não altera a tupla, que é imutável).
print(lanche)'''

'''
#   Somando tuplas de um jeito simples:
a = ('2', 5, 4)
b = (5, 8, 1, '2')
c = a + b # Aqui, 'c' virará uma tupla com os elementos de a somados aos de b. Nesse caso, a ordem dos elementos seguirá a ordem das tuplas declaradas na soma, portanto, 'a + b' gerará uma tupla com os elementos dispostos diferentemente da que 'b + a' geraria.
print(c)

#   Método COUNT:
print(c.count(5)) # O método 'count()' retornará quantas vezes o valor declarado entre parêntesis aparece dentro da tupla.

#   Propriedade INDEX
print(c.index('2',1)) # A propriedade 'index' retornará o índice da posição do elemento em questão. Ela retornará apenas a posição do primeiro valor encontrado. Caso um número seja colocado após a vírgula, ele começará a procurar o elemento a partir daquele ponto no índice.


a = ('Jose',  'Maria' , 'João')
b = a + ('Francisco', 'Ricardo', 'Lucas')  # Concatenação de tuplas.
print(b)'''
