def cabeçalho(texto='MENU PRINCIPAL', opções=False):
    print('\033[1m' + '-' * 60)
    print(texto.center(60))
    print('-' * 60)
    if opções:
        print('\033[33m1\033[m\033[1m -\33[34m Ver pessoas cadastradas')
        print('\033[33m2\033[m\033[1m -\33[34m Cadastrar nova Pessoa')
        print('\033[33m3\033[m\033[1m -\33[34m Sair do Sistema\033[m\033[1m')
        print('-' * 60)

def menu_principal(cad=None):
    while True:
        cabeçalho(opções=True)
        sair = False
        while not sair:
            try:
                opção = int(input('\033[32mSua Opção: \033[m\033[1m'))
                sair = True
            except:
                print('\033[31mERRO: digite um número válido!\033[m\033[1m')
        if opção == 1:
            cadastradas()
        elif opção == 2:
            cabeçalho('NOVO CADASTRO')
            cad = cadastrar_novos()
        elif opção == 3:
            cabeçalho('SAINDO DO SISTEMA... ATÉ LOGO!')
            break
        else:
            print('\033[31mERRO! Por favor, digite uma opção válida.\033[m\033[1m')

def cadastradas():
    cabeçalho('PESSOAS CADASTRADAS')
    with open('cadastro_ex115.txt', 'r') as arquivo:
        cadastro = arquivo.read()
    if len(cadastro) < 1:
        print('Ainda não há pessoas cadastradas!')
    else:
        print(cadastro)

def cadastrar_novos():
    while True:
        nome = str(input('Nome: ')).strip()
        if len(nome) == 0:
            print(f'\033[31mERRO: digite seu nome.\033[m\033[1m')
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
            if idade < 0:
                idade = +-idade
        except:
            print(f'\033[31mERRO: digite sua idade.\033[m\033[1m')
            continue
        break

    with open('cadastro_ex115.txt', 'a') as arquivo:
        arquivo.write(f'\n{nome:<51} {idade:>3} anos')

