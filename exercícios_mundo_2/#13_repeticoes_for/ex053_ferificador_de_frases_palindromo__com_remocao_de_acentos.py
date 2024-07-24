# minha resolução (após ver o funcionamento do programa do professor, coloquei a visualização do nome invertido).

'''from unicodedata import normalize # Peguei esse código na internet para remover acentos, mas ainda não sei bem como utilizar. Funcionou aqui, mas preciso pesquisar melhor sobre.
frase = input('Escreva uma frase para saber se ela é um palíndromo: ').upper().replace(' ','').replace('-','') # Vendo a resolução do professor percebí que eu também poderia ter juntado todas as palavras tranformando a variável 'frase' em uma lista, chamando-a, por exemplo, de 'fraselista', depois juntanto os elementos da lista com ''.join(fraselista) (obs.: se colocar algo entre as aspas de join, ele unirá os elementos da lista com isso).
frase = target = normalize('NFKD', frase).encode('ASCII','ignore').decode('ASCII')
p = 0
t = c = len(frase)
print(f'O contrário de {frase} é: ', end='')
for i in range( t):
    if frase[i] == frase[t-1]:
        p += 1
    t -= 1
    print(frase[t], end='')
print()
if p >= c:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')


# Minha resolução após ver o parte da resposta do professor Guanabara:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
palíndromo = True
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
   # print(f'junto[len(inverso)-1] {junto[len(inverso)-1]}  inverso[len(inverso)-1] {inverso[len(inverso)-1]}')
    if inverso[len(inverso)-1] != junto[len(inverso)-1]:
        palíndromo = False
print(inverso)
if palíndromo:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')'''



# Resolução do professor:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]  # Macete muito útil!
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto: # Isso foi bem mais simples do que a minha ideia!
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')