média = v = m_menos20 = 0
for c in range(5):
    nome = input(f'Digite o nome da {c+1}ª pessoa: ').strip()
    idade = float(input(f'Digite a idade de {nome}: '))
    sexo = input(f'Digite o sexo de {nome} [M ou F]: ').strip().upper()
    média += idade
    if sexo == 'M' and idade > v:
        h_velho = nome
        v = idade
    if sexo == 'F' and idade < 20:
        m_menos20 += 1
print(f'A média de idade do grupo é {média/5}.\nO homem mais velho é {h_velho}.\n{m_menos20} mulheres têm menos de 20 anos.')