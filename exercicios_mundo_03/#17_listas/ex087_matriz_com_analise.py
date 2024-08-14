#    Fiz esse exercício e o anterior bem rapidamente, sem muita dificuldade, graças a
# já ter feito exercícios parecidos no curso de lógica da programação do próprio Curso em Vídeo.
#    Realmente a lógica é a base, e a síntaxe é o que varia. Na época, fiz esse exercício no Visualg.

matriz = [[],[],[]]
soma_par = soma_ter = maior_seg =  0
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
print(f'O maior valor digitado na segunda linha foi: {maior_seg}.')
