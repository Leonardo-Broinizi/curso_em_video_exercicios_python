#   Sem querer apaguei o primeiro código que fiz quando abri esse arquivo para assistir
# a resolução do professor Guanabara, e ainda não tinha commitado ele!
#   Tenho que tomar mais cuidado quando seleciono o código com o mouse. O lado bom é que
# esse exercício ficará mais gravado na minha memória rsrs (obs. pós refazer o código:
# foi bem rápido! Ainda bem que estava fresco na mente. Já vou lá commitar rsrsrs).

#   Refazendo o código:

lista = [[],[],[]]
for l in range(len(lista)):
    for c in range(len(lista)):
        lista[l].append(int(input(f'Digite um número para a posição [{l}, {c}]: ')))
for c in range(len(lista)):
    for l in range(len(lista)):
        print(f'[ {lista[c][l]:^3} ]', end='')
    print()

#   Código do professor Guanabara (acredito que será igual ao meu):
#   Obs.: após assistir a aula de resolução: ví que eu tinha invertído linha e coluna no meu código,
# tenho que me atentar a isso. E o professor preferiu usar uma estratégia para não usar o método
# .append. Tirando isso, lógica igual.

'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): 
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()'''
