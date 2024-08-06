#   Quebrei a cabeça e, mesmo assim, minha resolução desse exercício está deixando muito a desejar.
# Em breve compararei com o código do professor Guanabara para entender o que deixei escapar por aqui.

#   Minha resolução:
'''
from random import randint
c = ''
t = ()
menor = maior = 0
for cont in range(1,6):
    n = randint(1,10)
    if cont == 1 or n < menor:
        menor = n
    if n > maior:
        maior = n
    c += str(n)
t = tuple(c)
print(f'Os valores sorteados foram: {t}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''


#   Resolução do professor Guanabara:

from random import randint
números = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)) # Então é assim! Podemos incluir vários números sorteados de uma vez em uma tupla.
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}')  # O método max pode ser usado em outros lugares e também nas tuplas.
print(f'O menor valor sorteado foi: {min(números)}')  # O método min também.