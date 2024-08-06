#    Gostei da minha resolução.

#    Minha resolução:

estoque = ('Cafeteira',399.90,'Microondas',439.90,'Televisor',2399.90,'Notebook',3999.90,'Celular',3000.90,'Jogo de Panelas', 299.99,'Cama', 1789.89,'Armário', 1599)
c = 0
print(f'\033[1m'+'-' * 50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print(f'-' * 50)
while c < len(estoque):
    print(f'{estoque[c]:.<40}R${estoque[c+1]:>8.2f}')
    c += 2
print(f'-' * 50)

#    Parte do código da resolução do professor, mostrando como ele optou por fazer a estrutura de repetiçõa:

'''for pos in range(0,len(estoque)):
    if pos % 2 == 0:  # O professor preferiu conferir a cada caso se a posição do índice é par ou ímpar, sabendo que os nomes dos produtos estão nos índices pares e os preços nos índices ímpares.
        print(f'{estoque[pos]:.<40}',end='R$ ')
    else:
        print(f'{estoque[pos]:.2f}')'''
