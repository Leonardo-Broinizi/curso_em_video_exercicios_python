#    Meu código:

'''a = 0
def área(l, c):
    a = l * c
    print(f'A área do terreno de {l}x{c} é de {a:.2f}m².')


print('+'* 40)
print(f'{'CALCULADORA DE ÁREA':^40}')
print('+'* 40)
l = float(input('Digite a largura do terreno em metros: '))
c = float(input('Digite o comprimento do terreno em metros: '))
área(l, c)'''


#    Código do professor Guanabara (foi basicamente igual ao meu):

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')

print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
