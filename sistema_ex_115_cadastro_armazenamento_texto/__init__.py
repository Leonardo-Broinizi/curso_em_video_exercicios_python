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
            cadastradas(cad)
        elif opção == 2:
            cad = cadastrar_novos(cad)
        elif opção == 3:
            break
        else:
            print('\033[31mERRO! Por favor, digite uma opção válida.\033[m\033[1m')
    return {'OIA':2}

def cadastradas(cad_mostrar):
    cabeçalho('PESSOAS CADASTRADAS')
    if type(cad_mostrar) != dict:
        print('Ainda não há pessoas cadastradas!')
    else:
        for chave, valor in cad_mostrar.items():
            if valor > 1:
                print(f'{chave:<50} {valor:>3} anos')
            else:
                print(f'{chave:<50} {valor:>3}  ano')

def cadastrar_novos(cad_novos):
    cabeçalho('NOVO CADASTRO')
    while True:
        nome = str(input('Nome: ')).strip()
        if len(nome) == 0:
            print(f'\033[31mERRO: digite seu nome.\033[m\033[1m')
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print(f'\033[31mERRO: digite sua idade.\033[m\033[1m')
            continue
        break
    cad_novos[nome] = idade
    return cad_novos

