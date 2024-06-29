'''  n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número: '))
if n1 >= n2 and n1 >= n3:
    print(f'O maior número é {n1}.')
elif n2 >= n1 and n2 >= n3 and n2 != n1:
    print(f'O maior número é {n2}.')
else:
    print(f'O maior número é {n3}.')
if n1 <= n2 and n1 <= n3:
    print(f'O menor número é {n1}.')
elif n2 <= n1 and n2 <= n3 and n2 != n1:
    print(f'O menor número é {n2}.')
else:
    print(f'O menor número é {n3}.')  '''

'''n1 = int(input('Digite o primeiro número: '))
maior = n1
menor = n1
n2 = int(input('Digite o segundo número:'))
if n2 > n1:
    maior = n2
else:
    menor = n2
n3 = int(input('Digite o terceiro número: '))
if n3 > n2 and n3 > n1:
    maior = n3
elif n3 < n2 and n3 < n1:
    menor = n3
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')'''

'''Exercício resolvido pelo professor Guanabara: '''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor é {menor}\nO maior valor é {maior}.')