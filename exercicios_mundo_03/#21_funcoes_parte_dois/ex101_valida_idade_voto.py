#   Minha primeira tentativa antes de ver o funcionamento do programa do professor Guanabara:

'''from datetime import date
def voto(natal, ano):
    situação = ''
    if ano - natal < 16:
        situação = 'Você ainda não tem idade suficiente para votar!'
    elif ano - natal < 18 or ano - natal >= 65:
        situação = 'Você não é obrigado a votar, mas pode, se quiser!'
    elif ano - natal >= 18 and ano - natal <= 65:
        situação = 'Você está na idade de votação obrigatória!'

    return situação

ano = date.today()
ano = ano.year

n = int(input('Digite o ano de seu nascimento: '))
print(voto(n, ano))'''


#   Meu segundo código, imitando o funcionamento do programa do professor, mas sem ver seu código:

'''from datetime import date

def voto(ano, natal):
    idade = ano - natal
    if idade >= 16 and idade < 18 or idade >= 65:
        situação = 'VOTO OPCIONAL'
    elif idade >= 18 and idade < 65:
        situação = 'VOTO OBRIGATÓRIO'
    elif idade < 16:
        situação = 'NÃO VOTA'
    return f'Com {idade} anos: {situação}.'

ano = date.today()
ano = ano.year
print('-' * 30)
n = int(input('Em que ano você nasceu? '))
print(voto(ano, n))'''


#   Código do professor Guanabara (ficou bem mais econômico que os meus):


def voto(ano):
    from datetime import date # O professor explicou na resolução que, deixando essa importação aqui, dentro da função, seu escopo de importação a manterá aqui, onde ela será necessária, o que economiza memória.
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))