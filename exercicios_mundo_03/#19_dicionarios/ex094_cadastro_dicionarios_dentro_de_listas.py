cadastro = []
nome = {}
while True:
    nome = str(input('Nome: ')).strip()
    cadastro.append(nome)
    break
print(type(cadastro[0]))
