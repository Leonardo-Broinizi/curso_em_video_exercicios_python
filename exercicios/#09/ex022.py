nome = input('Digite o seu nome completo: ')
dividido = nome.split()
nome_strip = len(nome) - nome.count(' ')
print('Seu nome em letras maiúsculas é: ', nome.upper(),'\nSeu nome em letras minúsculas é: ',nome.lower(),'\nO total de letras do seu nome completo é: ', nome_strip,'\nO total de letras do seu primeiro nome é: ', len(dividido[0]))

'''Soluções enontradas na internet para a contagem de caracteres excetuando os espaços em branco: '''

'''nome = input('Digite o seu nome completo: ')
nomeTam = len(nome) - nome.count(" ")
print(nomeTam)

ncarac= len(nome.replace(" ","")) # troca espaços por "nada"
print(ncarac)  '''

'''Exercício corrigido: '''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu em maiúsculas é: {nome.upper()}.')
print(f'Seu em minúsculas é: {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.')
print(f'Seu primeiro nome tem {nome.find(' ')} letras.')