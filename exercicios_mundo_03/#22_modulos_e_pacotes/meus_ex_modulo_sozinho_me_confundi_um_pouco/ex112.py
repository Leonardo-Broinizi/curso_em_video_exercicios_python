from utilidadescev import dado, moeda

p = dado.leiaDinheiro(str(input('\033[1mDigite o preço: R$')).strip().replace(' ', '').replace(',', '.'))
moeda.resumo(p, 25, 22)

