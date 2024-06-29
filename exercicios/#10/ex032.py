'''ano = int(input('Digite o ano:'))
if ano%4==0:
    print('Esse é um ano bissexto.')
else:
    print('Esse não é um ano bissexto.')'''

'''Exercício resolvido pelo professor Guanabara: '''

# Definição de ano bissexto: Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400)

from datetime import date  # datetime é um módulo para datas.
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Fará com que apenas o ano atual seja recebido.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')


