n1 = float(input('\033[2;33m Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if (n1 + n2) / 2 >= 6:
    cores = '\033[34m'
else:
    cores = '\033[31m'
print(f'A média do aluno é: {cores}{(n1 + n2)/ 2}.')