preço = float(input('Digite o preço do produto: '))
forma = int(input('''Escolha a forma de pagamento: 
[1] para pagamento à vista no dinheiro ou cheque, com 10% de desconto.
[2] para pagamento à vista no cartão de crédito, com 5% de desconto.
[3] para pagamento no cartão em duas vezes sem juros.
[4] para pagamento no cartão em 3 ou mais parcelas, com 20% de juros.
'''))
if forma == 1:
    print(f'A forma escolhida foi\033[32;1m à vista no dinheiro ou cheque\033[m e o valor a sar pago será \033[32;1mR${preço-(preço/100 * 10):.2f}\033[m.')
elif forma == 2:
    print(f'A forma escolhida foi\033[32;1m \033[m e o valor a sar pago será \033[32;1mR${preço-(preço/100 * 5):.2f}\033[m.')
elif forma == 3:
    print(f'A forma escolhida foi\033[32;1m \033[m e o valor a sar pago será \033[32;1mR${preço:.2f}\033[m.')
elif forma == 4:
    print(f'A forma escolhida foi\033[32;1m \033[m e o valor a sar pago será \033[32;1mR${preço+(preço/100 * 20):.2f}\033[m.')
else:
    print('Forma de pagamento inválida!')