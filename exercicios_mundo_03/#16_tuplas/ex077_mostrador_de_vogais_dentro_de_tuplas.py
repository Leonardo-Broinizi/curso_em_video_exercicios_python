#   Também gostei bastante desse código. Cumpriu bem com o enunciado da questão, de maneira econômica.
#   Minha resolução:

nomes = ('Nathanael','Rosimeiry','Juliana','Leonardo', 'Henrique')
for palavra in nomes:
    print(f'\nA palavra {palavra:<9} possui as seguintes vogais: ',end='')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(letra.lower(), end=' ')
