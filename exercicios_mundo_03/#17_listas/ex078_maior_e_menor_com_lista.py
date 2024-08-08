#   Cumpri com o solicitado no enunciado mas duvido que tenha feito de uma maneira muito eficaz.
# Acho que me faltou o conhecimento de mais métodos para fazer o que precisaca com menos "força bruta".

#   Meu código:

menor = maior = 0
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
        print(f'{posição}...',end=' ')

#   Considerações após ver o professor resolvendo:

#   Código do professor Guanabara:

