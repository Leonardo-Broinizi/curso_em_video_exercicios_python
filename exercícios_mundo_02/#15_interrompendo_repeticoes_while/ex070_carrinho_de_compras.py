#   O código do professor está consideravelmente melhor que o meu. Ele economizou linhas com,
# por exemplo, sua solução para não aceitar comandos inválidos na linha 46 em relação à minha solução.
#
#   Meu código:

'''menor = total = maisdemil = 0
continuar = ''
while continuar != 'N':
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    if preço < menor or total == 0:
        menor = preço
        menornome = produto
    if preço > 1000:
        maisdemil += 1
    total += preço
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar not in 'SN':
            print('Comando inválido!')
        else:
            break
print(f'Você gastou R${total:.2f} no total.')
if maisdemil == 1:
    print(f'Você comprou {maisdemil} produto que custa mais de mil reais.')
elif maisdemil > 1:
    print(f'Você comprou {maisdemil} produtos que custam mais de mil reais.')
else:
    print(f'Você comprou não comprou nenhum produto que custa mais de mil reais.')
print(f'O produto mais barato que você comprou foi o(a) {menornome}, que custou R${menor:.2f}.')'''

# Resolução do professor Guanabara:

total = totmil = menor = cont = barato = 0
while True:
    produto = str(input('Nome do Produto: ' ))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra é R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de mil reais')
print(f'O produto mais barato for {barato} que custa R${menor:.2f}')
