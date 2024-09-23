def leiaDinheiro(dim):
    while True:
        if not dim.replace('.','').isnumeric():
            print(f'\033[1;31mERRO: \"{dim}\" não é um preço válido!\033[m\033[1m')
            dim = str(input('Digite o preço: R$')).strip().replace(' ', '').replace(',', '.')
        else:
            dim = float(dim)
            return dim
