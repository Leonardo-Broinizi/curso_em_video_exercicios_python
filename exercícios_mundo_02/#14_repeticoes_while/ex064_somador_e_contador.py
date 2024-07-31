#   O professor Guanabara ressaltou mais uma vez que não é bom usar 'gambiarras' nos códigos, e eu tento ao máximo evitar.
# Ele também disse que entende que, como os poucos recursos que nós, alunos iniciantes, temos até o momento, algumas gambiarras são inevitáveis.
# Porém, fico feliz de ver, ao longo das aulas, que tenho conseguido antever o mau uso de gambiarras evitáveis e achado soluções criativas, às vezes não dadas nem pelo professor (obviamente não sou um programador experiente, longe disso, mas fico feliz em estar evoluindo aos poucos).

# Minha resolução:

r = s = c = 0
while r != 999:
    s += r
    c += 1
    r = int(input('Digite o número: '))
print(f'Você digitou {c-1} números, a soma entre eles é {s}.')

# Resolução do professor Guanabara:

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
