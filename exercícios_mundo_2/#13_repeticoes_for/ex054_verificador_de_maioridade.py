from datetime import date
data_atual = date.today()
ano = int('{}'.format(data_atual.year)) # É importante decorar essa e outras formas de manipular os dados vindos de datetime (e de outros módulos, se for possível).
m = 0
for i in range(7):
    a = int(input(f'Digite o ano de nascimento da {i+1}° pessoa: '))
    if ano - a > 21:
        m += 1
if m == 0:
    print('Nenhuma das sete pessoas é maior de idade.')
elif m == 1:
    print(f'Das 7 pessoas, {m} é maior de idade e {7-m} não.')
elif 1 < m < 7:
    print(f'Das 7 pessoas, {m} são maiores de idade e {7-m} não.')
else:
    print('Todas as sete pessoas são maiores de idade.')