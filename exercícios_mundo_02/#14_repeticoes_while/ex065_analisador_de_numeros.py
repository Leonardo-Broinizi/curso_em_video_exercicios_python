#

#  Minha resolução:

'''c = m = maior = menor = 0
r = ''
while r != 'N':
    c += 1
    n = float(input(f'Digite o {c}º número: '))
    r = str(input('Quer continuar acrescentando? [S/N] ')).upper().strip()
    if c == 1 or n < menor:
        menor = n
    if n > maior:
        maior = n
    m += n
print(f'A média dos números digitados é {m/c:.2f}, o maior número foi {maior} e o menor foi {menor}.')'''

# Resolução do professor Guanabara:

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'S':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')