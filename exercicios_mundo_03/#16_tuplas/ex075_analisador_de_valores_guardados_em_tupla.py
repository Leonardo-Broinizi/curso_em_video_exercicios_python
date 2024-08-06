#   Não consegui fazer esse exercício nem o anterior de maneira satisfatória.

#   Minha gambiarra:
'''nstr = pares = ''
n9 = n3 = 0
tupla = ('')
for c in range(1,5):
    n = int(input(f'Digite o {c}º valor: '))
    nstr += str(n)
    if n == 9:
        n9 += 1
    elif n == 3 and n3 == 0:
        n3 = c
    if n % 2 == 0 and c < 4:
        pares += str(n)
        pares += ' '
if n % 2 == 0:
    pares += str(n)
tupla = tuple(nstr)
print(f'Você digitou os valores {tupla}')
print(f'O número 9 foi digitado {n9} vezes.' if n9 > 0 else 'O número 9 não foi digitado.')
print(f'O número 3 foi digitado primeiramente na {n3}ª vez.' if n3 > 0 else 'O número 3 não foi digitado.')
print(f'Os números pares foram {pares}.'if pares != '' else 'Não foram digitados números pares.')'''

# Resolução do professor (um pouco modificada por mim, mas essencialmente a do professor Guanabara):

num = (int(input('Digite o 1º número: ')),
       int(input('Digite um 2º número: ')),
       int(input('Digite um 3º número: ')),
       int(input('Digite um 4º número: '))) # O professor faz uso de um macete parecido com o que ele ensinou no exercício passado, onde, aqui, fazemos vários valores serem digitados para entrarem todos na tupla de uma só vez, já que ela é imutável.
print(f'Você digitou os valores {num}')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
else:
    print('O número 9 não foi digitado.')
if 3 in num:
    print(f'A primeira ocorrência de 3 foi na posição {num.index(3)+1}')
else:
    print('O número 3 não foi digitado.')
print('Os números pares são: ',end='')
for número in num:
    if número % 2 == 0:
        print(número, end=' ')

