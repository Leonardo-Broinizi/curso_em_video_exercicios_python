cores = {'amarelo':'\033[33m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'limpa':'\033[m'}

nome = str(input(f'{cores['amarelo']}Qual é seu nome? {cores['limpa']}')).upper().strip()
if nome == 'LEONARDO':
    print(f'{cores['vermelho']}Seu nome é muito bonito! {cores['limpa']}.')
elif nome == 'PEDRO' or nome == 'MARIAS' or nome == 'PAULO':
    print(f'{cores['azul']}Seu nome é bem popular no Brasil.{cores['limpa']}.')
elif nome in 'ANA CLAUDIA JÉSSICA JULIANA':
    print(f'{cores['amarelo']}Belo nome feminino{cores['limpa']}.')
else:
    print(f'{cores['vermelho']}Seu nome é bem comum{cores['limpa']}.')
print(f'{cores['verde']}Tenha um bom dia, {cores['azul']}{nome.capitalize()}\033[m{cores['limpa']}.')

'''Diva interessante do professor Guanabara sobre uma maneira interessante de realizar a verificação de se determinada média é menor que 'X' e maior que 'Y'. Exemplo: 'if 7 > média >= 5:' '''
