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
n = int(input('Em que ano você nasceu? '))
print(voto(ano, n))'''


#   Código do professor Guanabara:

