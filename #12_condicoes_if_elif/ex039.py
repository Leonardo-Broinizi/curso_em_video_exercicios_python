from datetime import date
print('Alistamento Militar Obrigatório')
sexo = input('Digite seu sexo [MASCULINO/FEMININO]: ').strip().upper()
if sexo == 'MASCULINO':
    ano_nasc = int(input('Digite o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')
    if idade < 18:
        print(f'\033[32mVocê deverá se alistar daqui a {18 - idade} anos.')
        print(f'Seu alistamento será no ano {ano_atual + 18 - idade}.')
    elif idade == 18:
        print('\033[33mVocê deve se alistar nesse ano.')
    else:
        print(f'\033[31mVocê deveria ter se alistado há {idade - 18} anos.')
        print(f'Seu alistamento deveria ter sido no ano {ano_atual - idade + 18}.')
else:
    print('Você não precisa realizar o alistamento miliar obrigatório.')