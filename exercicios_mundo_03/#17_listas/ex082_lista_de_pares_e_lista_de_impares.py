#   Fiz dois códigos pois, após terminar o primeiro, ouvi o professor pedir pra fazer esse
# exercício de maneira um pouco diferente do que eu havia feito.

#   Meu primeiro código:

'''lista = []
pares = []
ímpares = []
while True:
    r = ' '
    num = int(input('\033[1;32mDigite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
    while r not in 'NS':
        r = str(input('\033[33mQuer continuar? [\033[34mS\033[33m/\033[31mN\033[33m] ')).strip().upper()[0]
    if r in 'N':
        break
print('\033[32mVocê digitou os valores: \033[33m', end='')
for p, n in enumerate(lista):
    print(n, end=', ')
    if p == len(lista)-2:
        break
print(f'{lista[-1]}.')
if len(pares) > 1:
    print('\033[34mOs números pares digitados foram: \033[33m', end='')
    for p, n in enumerate(pares):
        print(n, end=', ')
        if p == len(pares)- 2:
            break
    print(f'{pares[-1]}.')
elif len(pares) == 1:
    print(f'\033[34mO único número par digitado foi: \033[33m{pares[0]}.')
else:
    print('\033[34mNenhum número par foi digitado.')
if len(ímpares) > 1:
    print('\033[31mOs números ímpares digitados foram: \033[33m',end='')
    for p, n in enumerate(ímpares):
        print(n,end=', ')
        if p == len(ímpares) - 2:
            break
    print(f'{ímpares[-1]}.')
elif len(ímpares) == 1:
    print(f'\033[31mO único número ímpar digitado foi: \033[33m{ímpares[-1]}.')
else:
    print('\033[31mNão foram digitados números ímpares.')

#   Meu segundo código:

lista = []
pares = []
ímpares = []
while True:
    r = ' '
    lista.append(int(input('\033[1;32mDigite um valor: ')))
    while r not in 'NS':
        r = str(input('\033[33mQuer continuar? [\033[34mS\033[33m/\033[31mN\033[33m] ')).strip().upper()[0]
    if r in 'N':
        break
for p, n in enumerate(lista):
    if n % 2 == 0:
        pares.append(lista[p])
    else:
        ímpares.append(lista[p])
print('\033[32m','-='*34+'-')
print(f'\033[33mA lista completa é {lista}')
print(f'\033[34mA lista de pares é {pares}')
print(f'\033[31mA lista de ímpares é {ímpares}')'''

