a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a < b+c and b < a+c and c < a+b:
    print('Estas retas podem formar um triângulo.')
else:
    print('Estas retas não podem formar um triângulo.')
