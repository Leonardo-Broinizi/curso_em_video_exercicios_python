#   Sem querer apaguei o primeiro código que fiz quando abri esse arquivo para assistir
# a resolução do professor Guanabara, e ainda não tinha commitado ele!
#   Tenho que tomar mais cuidado quando seleciono o código com o mouse. O lado bom é que
# esse exercício ficará mais gravado na minha memória rsrs (obs. pós refazer o código:
# foi bem rápido! Ainda bem que estava fresco na mente. Já vou lá commitar rsrsrs).

#   Refazendo o código:

lista = [[],[],[]]
for c in range(len(lista)):
    for l in range(len(lista)):
        lista[c].append(int(input(f'Digite um número para a posição [{c}, {l}]: ')))
for c in range(len(lista)):
    for l in range(len(lista)):
        print(f'[ {lista[c][l]:^3} ]', end='')
    print()