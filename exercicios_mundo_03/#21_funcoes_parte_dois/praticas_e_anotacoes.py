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

def contador(i,f,p):
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

help(contador)

<<<<< PAREI O VÍDEO DA AULA NO MINUTO 15 !!!>>>>


