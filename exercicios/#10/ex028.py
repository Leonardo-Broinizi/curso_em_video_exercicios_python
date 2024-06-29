'''from random import randint
s = 0
r = 1
while r != s:
    s = randint(0,5)
    r = int(input('Entre 0 e 5, tente adivinhar qual foi o número sorteado pelo computador: '))
    print('Parabéns, você acertou o número!' if r==s else 'Que pena, não foi dessa vez.')
    print(f'O número sorteado foi: {s}.')'''


'''Solução do professor Guanabara:'''

from random import randint
from time import sleep # O sleep faz com que o programa dê uma pausa pelo tempo que quisermos.
computador = randint(0,5) # Faz o computador 'Pensar'
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta advinhar.
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no número {jogador}.')


