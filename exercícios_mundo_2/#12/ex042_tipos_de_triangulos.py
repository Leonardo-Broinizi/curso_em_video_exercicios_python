a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a < b+c and b < a+c and c < a+b:
    if a == b and a == c:
        print('Este é um triângulo EQUILÁTERO, ou seja, todos os lados possuem o mesmo tamanho.')
    elif a == b or a == c or b == c:
        print('Este é um triângulo ISÓSCELES, ou seja, dois de seus lados são iguais.')
    else:
        print('Este é um triângulo ESCALENO, ou seja, todos os lados são diferentes.')
else:
    print('Estas retas não podem formar um triângulo.')
