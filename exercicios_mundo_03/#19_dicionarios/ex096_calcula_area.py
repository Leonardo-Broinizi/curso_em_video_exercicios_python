a = 0
def área(l, c):
    a = l * c
    print(f'A área do terreno de {l}x{c} é de {a:.2f}m².')


print('+'* 40)
print(f'{'CALCULADORA DE ÁREA':^40}')
print('+'* 40)
l = float(input('Digite a largura do terreno em metros: '))
c = float(input('Digite o comprimento do terreno em metros: '))
área(l, c)
