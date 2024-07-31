#   Tuplas são IMUTÁVEIS!!!
# As tuplas são imutáveis quando o código está rodando. Só podem ser editadas, obviamente, enquanto  estamos formando o código.

#   Existem 3 maneiras de utilizarmos o 'for' para percorrer tuplas, cada uma servindo melhor para determinada finalidade:

'''lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche: # Usando de for para percorrer tuplas (e acho que listas também) dessa maneira ele devolverá a variável de controle já com o valor encontrado dentro do índice referente. Para obter apenas a posição precisamos fazer igual ao exemplo seguinte.
    print(comida, end=', ')
print()
print()
for cont in range(0, len(lanche)): # Dessa forma a variável de controle retornará apenas a posição que cada laço está percorrendo.
    print(lanche[cont], cont,end=', ')
print()
print()
for posição, comida in enumerate(lanche): # Enumerate retorna duas variáveis de controle: a primeira com a posição e a segunda com o ítem daquela posição.
    print(comida, posição, end=', ')

lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) # O método 'sorted' mostrará uma lista contendo os ítens da referida tupla em ordem alfabética (lembrando que isso não altera a tupla, que é imutável).
print(lanche)'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # Aqui, 'c' virará uma tupla com os elementos de a somados aos de b. Nesse caso, a ordem dos elementos seguirá a ordem das tuplas declaradas na soma, portanto, 'a + b' gerará uma tupla com os elementos dispostos diferentemente da que 'b + a' geraria.
print(c.count(5)) # O método 'count()' retornará quantas vezes o valor declarado entre parêntesis aparece dentro da tupla.

