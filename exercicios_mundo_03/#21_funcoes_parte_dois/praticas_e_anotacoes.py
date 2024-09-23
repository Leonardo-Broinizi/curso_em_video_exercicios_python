#    Rascunho:

#    Minha primeira tentativa antes de ver o programa do professor funcionando:

#    Meu código após ver o funcionamento do programa do professor Guanabara:

#    Código do professor Guanabara:

#    <<< INTERACTIVE HELP >>>
'''help() é uma função interna que serve para usarmos a ajuda interativa no Python. Ao chamar essa função,
 o terminal do python entrará no modo help, onde poderemos escrever o nome de alguma função da linguagem
 e ele nos mostrará o manual da função.'''
# ex:
# help()                # Aqui o help é chamado para o nosso terminal, para perguntarmos sobre qualquer função.
# help(print)           # Aqui o help é chamado especificamente para nos informar sobre uma função (nesse exemplo, print)
# print(input.__doc__)  # Aqui é chamada uma outra parte de help que traz informações diferentes sobre uma função. Por isso é interessante usar esse modo junto com algum dos anteriormente citados.

#    <<< DOCSTRINGS >>>
'''São justamente as documentações internas do Python, como as que acabamos de requisitar nos exemplos acima.
As funções podem ser criadas por qualquer usuário de Python, e desse modo, também podemos criar docstrings para 
descrevermos ela para outros possíveis usuários de nossas funções colaborativas (futuramente eu devo aprender 
como deixo uma função própria na biblioteca pública do Python).
Para criarmos docstrings nas nossas funções, precisamos abrir três áspas (se forem áspas duplas é melhor, 
pois já será criado uma estrutura base para fazer esse 'manual' da sua função) logo abaixo do nome da nossa função,
como no exemplo abaixo:'''

#   Exemplo:
'''def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2)

help(contador)'''

#   <<< PARÂMETROS OPCIONAIS >>>
'''    Em Python, caso o número de parâmetros reais (os que contém os valores, que são apresentados na
 chamada da função/subprograma) seja diferente do número de parâmetros formais (os que vão no cabeçalho 
do subprograma/função), ocorrerá um erro no programa, a menos que se declarem os parâmetros opcionais,
 da seguinte maneira: ao declarar os parâmetros reais, coloca-se um sinal de atribuição (=) junto com 
 o valor que será considerado caso o subprograma/rotina/função não seja declarado na chamada da função.'''

# Exemplo:

'''def somar(a=0, b=0, c=0): # Aqui foram passados os valores 0 como alternativos à falta de valores na chamada da função
    s = a + b + c
    print(f'A soma vale {s}')

somar(8, 4)
somar()'''

# Exemplo 2:

'''def cadastro(nome='Não declarado!', profissão='Não declarada!', idade=0): # Testando agora com string.
    print(f'Nome: {nome}\nProfissão: {profissão}\nIdade: {idade}')


n = str(input('Digite seu nome: ')).strip()
p = str(input('Digite sua profissão: ')).strip()
i = int(input('Digite sua idade: '))
if n == '' and p != '':     # Aqui eu fiz essa validação para declarar quais parâmetros serão passados, já que se o usuário apenas não digitar o nome, o valor vazio será passado e não o nosso valor opcional.
    cadastro(profissão=p, idade=i)
elif n != '' and p == '':
    cadastro(nome=n, idade=i)
elif n == '' and p == '':
    cadastro(idade=i)
else:
    cadastro(profissão=p, nome=n, idade=i)'''


#   <<< ESCOPO DE VARIÁVEIS >>>

''' O escopo de variáveis é o local onde essas variáveis se encontram. Uma variável global pode ser acessada 
em qualquer parte do código. Já uma variável local, só poderá ser acessada no local onde ela se encontra.
Se ele foi criada em uma subrotina/função, por exemplo, ela só poderá ser acessada nessa função. 
É importante se atentar a isso para o código não dar errado. Se eu tentar acessar uma variável fora de seu 
escopo, o código vai apresentar um erro, pois a variável não será encontrada.'''

# Observação importante sobre escopo de variáveis:

''' Quando tentei, em um programa de exercício próprio, alterar uma variável de escopo global dentro 
de uma função, não obtive o resultado desejado e agora o professor Guanabara está explicando o motivo: 
em Python, uma variável global pode ser acessada dentro de uma função somente para exibição em print, 
mas não não para acessar ou alterar seu valor. Caso seja escrito o nome dessa variável para recever 
algum valor, será criada uma nova variável local. Caso se tente usar a variável global (sem declarar 
uma nova variável local de mesmo nome) para incrementar algum valor ou coisa do tipo, ocorrerá um erro.
<<< GLOBAL >>>
Isso que foi dito ocorrerá a menos que eu use o comando 'global' antes da variável dentro da função, onde estarei
pedindo para que a função use a variável global ao invés de criar uma nova local.'''

# Exemplo 1:

'''def teste_ex111():
    x = 8 # variável local, só pode ser acessada nessa função
    n = 5 # esse n não é o mesmo que o da variável global, declarado no programa principal, e sim uma nova variável de escopo local.
    print(f'Na função teste_ex111, n vale {n}')
    print(f'Na função teste_ex111, x vale {x}')

# Programa Principal
n = 2 # variável global, vale em qualquer parte do código.
print(f'No programa principal, n vale {n}')
teste_ex111()
print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}') # se essa linha for executada, o código dará erro, pois essa variável não existe fora da função em que foi criada.'''

# Exemplo 2:

'''def teste_ex111():
    x = 8
    global n # Essa alteração fez com que o código se comportasse de maneira diferente do anterior, pois agora a variável 'n' é a global, mesmo aqui, dentro da função.
    n = 3 
    print(f'Na função teste_ex111, n vale {n}')
    print(f'Na função teste_ex111, x vale {x}')

# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste_ex111()
print(f'No programa principal, n vale {n}')
'''

#    <<< RETURN >>>

''' Esse comando fará com que um ou mais valores sejam passadas da função para uma variável.'''



# Práticas:

# FATORIAL
# Meu código:
'''def fatorial(n):
    fat = n
    n -= 1
    for c in range(n, 1, -1):
        fat *= n
        n -= 1
    return fat

num = int(input('Digite um número para descobrir seu fatorial: '))
f = fatorial(num)
print(f'O fatorial de {num} é {f}')'''

# Código do professor:

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
'''

