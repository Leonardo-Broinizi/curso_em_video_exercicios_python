#    Meu código após ver o funcionamento do programa do professor Guanabara:

'''def manual(e):
    if e.upper() not in 'FIM':
        print(f'\033[44m' + '~' * 45)
        print(f"{f"Acessando o manual do comando '{e}'":^45}")
        print(f'\033[44m' + '~' * 45, '\n\033[m\033[7m')
        help(e)
        print(f'\033[m\033[42m' + '~' * 25)
        print(f'{'SISTEMA DE AJUDA PyHELP':^25}')
        print(f'\033[42m' + '~' * 25)

    return e

print('\033[42;1m' + '~' * 40)
print(f'{'SISTEMA DE AJUDA PyHELP':^40}')
print('\033[42;1m' + '~' * 40)
while True:
    esc = manual(str(input('\033[m\033[1mFunção ou Biblioteca > ')).strip())
    if esc.upper() == 'FIM':
        print('\033[41;1m' + '~' * 20)
        print(f'{'ATÉ LOGO!':^20}')
        print('\033[41;1m' + '~' * 20)
        break'''


#    Código do professor Guanabara:

from time import sleep
c = ('\033[m', # 0 - sem cores      # OBS.: tirei os '30' dos códigos porque só assim a cor aparecia para mim igual à do vídeo do professor.
     '\033[0;41m', # 1 - vermelho
     '\033[0;42m', # 2 - verde
     '\033[0;43m', # 3 - amarelo
     '\033[0;44m', # 4 - azul
     '\033[0;45m', # 5 - roxo
     '\033[7m', # 6 - branco
     );

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4) # Importante lembrar: para fazer com que aspas possam aparecer para o usuário é preciso usar essas barras invertidas \' \'.
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(2)

# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)