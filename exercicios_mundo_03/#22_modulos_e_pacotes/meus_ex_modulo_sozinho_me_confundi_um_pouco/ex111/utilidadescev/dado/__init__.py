def leiaDinheiro(dim):
    print('\033[1;31m')
    if dim == '':
        print(f'ERRO: \"{dim}\" não é um preço válido!')

    return float(dim)

