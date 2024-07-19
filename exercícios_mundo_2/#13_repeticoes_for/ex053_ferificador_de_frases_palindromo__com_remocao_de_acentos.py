from unicodedata import normalize # Peguei esse código na internet para remover acentos, mas ainda não sei bem como utilizar. Funcionou aqui, mas preciso pesquisar melhor sobre.
frase = input('Escreva uma frase para saber se ela é um palíndromo: ').upper().replace(' ','').replace('-','')
frase = target = normalize('NFKD', frase).encode('ASCII','ignore').decode('ASCII')
p = 0
c = len(frase)//2
t = len(frase)
for i in range(c):
    if frase[i] == frase[t-1]:
        p += 1
    t -= 1
if p >= c:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')