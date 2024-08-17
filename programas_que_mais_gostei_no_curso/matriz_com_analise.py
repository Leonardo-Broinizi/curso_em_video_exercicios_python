#    Fiz esse exercício e o anterior bem rapidamente, sem muita dificuldade, graças a
# já ter feito exercícios parecidos no curso de lógica da programação do próprio Curso em Vídeo.
#    Realmente a lógica é a base, e a síntaxe é o que varia. Na época, fiz esse exercício no Visualg.
#    Minha resolução:

matriz = [[],[],[]]
soma_par = soma_ter = maior_seg = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[c].append(int(input(f'Digite um número para a posição [{l}, {c}]: ')))
        if matriz[c][-1] % 2 == 0:
            soma_par += matriz[c][-1]
        if c == 2:
            soma_ter += matriz[c][-1]
        if l == 1 and matriz[c][-1] > maior_seg:
            maior_seg = matriz[c][l]
print('-=' * 35 + '-')
for c in range(len(matriz)):
    for l in range(len(matriz)):
        print(f'[ {matriz[l][c]} ] ', end='')
    print()
print('-=' * 35 + '-')
print(f'A soma de todos os valores pares digitados é: {soma_par}.')
print(f'A soma de todos os valores digitados na terceira coluna é: {soma_ter}.')
print(f'O maior valor digitado na segunda linha foi: {maior_seg}.')

# Nesse código a variável matriz, caso fossem adicionados valores de 1 a 9 em sequência, ficaria assim: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


#   Meu código alternativo (com pequenas alterações):

'''matriz = [[],[],[]]
soma_par = soma_ter = maior_seg = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um número para a posição [{l}, {c}]: ')))
        if matriz[l][-1] % 2 == 0:
            soma_par += matriz[l][-1]
        if c == 2:
            soma_ter += matriz[l][c]
        if l == 1 and matriz[l][c] > maior_seg:
            maior_seg = matriz[l][c]
print('-=' * 35 + '-')
for l in matriz:
    for c in l:
        print(f'[ {c} ]', end='')
    print()
print(f'A soma de todos os valores pares digitados é: {soma_par}.')
print(f'A soma de todos os valores digitados na terceira coluna é: {soma_ter}.')
print(f'O maior valor digitado na segunda linha foi: {maior_seg}.')'''

# Nesse código a variável matriz, caso fossem adicionados valores de 1 a 9 em sequência, ficaria assim: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#   Resolução do professor:

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')'''
