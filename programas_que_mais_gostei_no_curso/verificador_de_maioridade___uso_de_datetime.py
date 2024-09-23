''' # Primeira tentativa:
from datetime import date
data_atual = date.today()
ano = int('{}'.format(data_atual.year)) # É importante decorar essa e outras formas de manipular os dado vindos de datetime (e de outros módulos, se for possível).
m = 0
for i in range(7):
    a = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))
    if ano - a > 21:
        m += 1
if m == 0:
    print('Nenhuma das sete pessoas é maior de idade.')
elif m == 1:
    print(f'Das 7 pessoas, {m} é maior de idade e {7-m} não.')
elif 1 < m < 7:
    print(f'Das 7 pessoas, {m} são maiores de idade e {7-m} não.')
else:
    print('Todas as sete pessoas são maiores de idade.')'''

# Resolução do professor Guanabara:

from datetime import date
atual = date.today().year
totmaior = totmenor = 0
for pess in range(1,8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade ')
print(f'E também tivemos {totmenor} pessoas menores de idade.')