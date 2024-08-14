#    Nessa primeira tentativa eu ainda não tinha terminado de ouvir o enúnciado para entender
# que eu deveria criar duas listas dentro de outra. Por isso refiz o exercício.

#    Obs. pós resposta: Meu código ficou praticamente idêntico ao do professor,
# com a diferença de que ele declarou a variável simples, que recebia o valor antes de
# jogá-lo na lista correta, fora do laço 'for', e eu, dentro. Ainda tenho alguma dúvida
# a respeito da necessidade (caso haja) de declarar certas variáveis fora da estrutura de repetição.
# Nesse caso, meu código não apresentou problema.

#    Primeira tentativa:

'''n = []
for i in range(0, 7):
    n.append(int(input(f'Digite o {i+1}º valor: ')))
n.sort()
print('Os valores pares digitados foram: ', end='')
for pares in n:
    if pares % 2 == 0:
        print(pares, end=' - ')
print('\nOs valores ímpares foram: ', end='')
for ímpares in n:
    if ímpares % 2 == 1:
        print(ímpares, end=' - ')'''

# Segunda tentativa:

'''nl = [[],[]]
for i in range(0, 7):
    n = int(input(f'Digite o {i+1}º número: '))
    if n % 2 == 0:
        nl[0].append(n)
    else:
        nl[1].append(n)
nl[0].sort() # Aqui tive que realizar o método sort em cada uma das listas dentro da lista principal, já que se eu tentasse o sort na lista principal apenas os índices dela seriam ordenados.
nl[1].sort() # Vale ressaltar também que, quando tendo realizar o sort dentro das máscaras de substituição (as chaves {}) o valor retornado é 'None'.
print(f'Os valores pares digitados foram: {nl[0]}')
print(f'Os valores ímpares digitados foram: {nl[1]}')'''

#   Código do professor:

núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')


