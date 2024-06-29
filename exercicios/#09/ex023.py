'''Tentativa 1:'''

'''n = input('Digite um número entre 0 e 9999: ')
if n[3] != :
    print(f'Unidade: {n[3]}.')
    print(f'Dezena: {n[2]}.')
    print(f'Centena: {n[1]}.')
    print(f'Milhar: {n[0]}.')
elif n[2] != '':
    print(f'Unidade: {n[2]}.')
    print(f'Dezena: {n[1]}.')
    print(f'Centena: {n[0]}.')
elif n[1] != '':
    print(f'Unidade: {n[1]}.')
    print(f'Dezena: {n[0]}.')
else:
    print(f'Unidade: {n[0]}.'''

'''Tentativa 2: '''

'''n = input('Digite um número entre 0 e 9999: ')
print(f'Unidade: {n[3]}.')
if n[1] != 0 or n[2] != 0 or n[3] != 0:
    print(f'Dezena: {n[2]}.')
if n[2] != 0 or n[3] != 0:
    print(f'Centena: {n[1]}.')
if n[3] != 0:
    print(f'Milhar: {n[0]}.')'''


'''Exercício corrigido pelo Guanabra:'''

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}.')
print(f'Unidade: {u}.')
print(f'Dezena: {d}.')
print(f'Centena: {c}.')
print(f'Milhar: {m}.')