#   Meu código:

'''lista = []
p5 = []
c = 0
while True:
    resp = ' '
    lista.append(int(input('\033[1;3;4;34mDigite um número: ')))
    if lista[c] == 5:
        p5.append(c)
    c += 1
    while resp not in 'SN':
        resp = str(input('Quer adicionar outro número? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Sua lista é: {lista}')
print(f'Ao todo foram digitados {len(lista)} números.')
print(f'A ordem decrescente da sua lista é {sorted(lista,reverse="True")}')
if 5 not in lista:
    print(f'O valor 5 não foi digitado nesta lista.')
elif len(p5) > 1:
    print(f'O valor 5 foi digitado {len(p5)} vezes, nas posições {p5}.')
else:
    print(f'O valor 5 foi digitado na posição {lista.index(5)}.')'''



