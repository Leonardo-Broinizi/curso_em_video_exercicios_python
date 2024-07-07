from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
print(ano - nascimento)
if ano - nascimento < 9:
    print('Sua categoria é a MIRIM!')
elif ano - nascimento <= 14:
    print('Sua categoria é a INFANTIL!')
elif ano - nascimento <= 19:
    print('Sua categoria é a JUNIOR!')
elif ano - nascimento <= 20:
    print('Sua categoria é a SÊNIOR!')
else:
    print('Sua categoria é a MASTER!')