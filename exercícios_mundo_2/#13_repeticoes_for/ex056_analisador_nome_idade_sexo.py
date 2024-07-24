#  Nesse caso acho ambas as resoluções equivalentes (a minha é mais enxuta por conta de uns macetes que já aprendi e creio que o professor Guanabara não esteja usando para não confundir os alunos que ainda as desconhecem, e aos poucos ele vai ensinando-as).

#  Minha resolução:

média = v = m_menos20 = 0
for c in range(4):
    nome = input(f'Digite o nome da {c+1}ª pessoa: ').strip()
    idade = float(input(f'Digite a idade de {nome}: '))
    sexo = input(f'Digite o sexo de {nome} [M ou F]: ').strip().upper()
    média += idade
    if sexo == 'M' and idade > v:
        h_velho = nome
        v = int(idade)
    if sexo == 'F' and idade < 20:
        m_menos20 += 1
print(f'A média de idade do grupo é {média/4}.\nO homem mais velho é o {h_velho} com {v} anos.\n{m_menos20} mulheres têm menos de 20 anos.')


#  Resolução do professor Guanabara:

somaidade = 0
médiaidade = 0
maioridadehomem = 0
totmulher20 = 0
nomevelho = ''
for p in range(1,5):
    print(f'------- {p}ª PESSOA ---------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm': # Interessante essa configuração para fazer o operador lógico buscar qualquer dos 'm's (maiúsculo e minúsculo) dentro da variável sexo.
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
