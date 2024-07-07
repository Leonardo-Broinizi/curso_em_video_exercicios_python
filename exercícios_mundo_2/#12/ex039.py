idade = int(input('Digite a sua idade: '))
if idade < 18:
    print(f'Você deverá se alistar daqui a {18-idade} anos.')
elif idade == 18:
    print('Você está na idade de alistamento.')
else:
    print(f'Você deveria ter se alistado a {idade- 18} anos.')