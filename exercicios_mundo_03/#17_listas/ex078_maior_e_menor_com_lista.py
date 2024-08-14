#   Cumpri com o solicitado no enunciado mas duvido que tenha feito de uma maneira muito eficaz.
# Acho que me faltou o conhecimento de mais métodos para fazer o que precisava com menos "força bruta".

#   Meu código:

'''menor = maior = 0
num = []
for i in range(0,5):
    num.append(int(input(f'Digite o {i+1}º número: ')))
    if i == 1 or num[i] < menor:
        menor = num[i]
    if num[i] > maior:
        maior = num[i]
print(f'Você digitou os valores {num}.')
print(f'O menor número digitado foi {menor} nas posições: ', end='')
for posição, número in enumerate(num):
    if número == menor:
        print(f'{posição}...',end=' ')
print(f'\nO maior número digitado foi {maior} nas posições: ', end='')
for posição, número in enumerate(num):
    if número == maior:
        print(f'{posição}...',end=' ')'''

#   Considerações após ver o professor resolvendo:
#   Na verdade, vendo a resolução do professor Guanabara, percebí que minha solução foi
# praticamente igual a dele, então fiz um bom trabalho nesse exercício.

#   Código do professor Guanabara:

listanum = [] # também serviria list()
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end=' ')
print()
print(f'O menor valor digitado foi {men} nas posições ', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end=' ')
print()