#  A resolução do professor Guanabara é melhor do que a minha,
# tem funcionalidades (ou macetes) que eu não sabia usar.

#  Minha resolução:

'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if sexo != 'M' and sexo != 'F' and sexo != 'S':
        print('Opção inválida! Tente novamente.')'''

# Resolução do professor Guanabara:

sexo = str(input('Informe seu sexo: ')).strip().upper()[0] # para a str 'sexo' ficar apenas com a primeira letra digitada.
while sexo not in 'MF': # interessante ver que pode-se usar o 'not in' aqui
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
