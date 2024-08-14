#   A resolução do professor Guanabara foi melhor do que a minha porque ele usou um 'for',
# que realmente é mais prático que o 'while' quando possível de usá-lo, o que economizou linhas no código dele.

#   Minha resolução:

'''while True:
    c = 0
    n = int(input('Digite um número [um valor negativo para sair]: '))
    if n < 0:
        break
    while c < 10:
        c += 1
        print(f'{n} x {c} = {n*c}')
'''

# Resolução do professor:

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
