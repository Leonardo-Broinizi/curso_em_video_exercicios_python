#   Novamente o código do professor foi bem mais econômico do que o meu. Preciso me empenhar
# ainda mais em encontrar soluções mais simples para resolver os problemas.

#   Minha resolução:

'''print('=' * 31)
print('\033[1mC A I X A   E L E T R Ô N I C O\033[m')
print('=' * 31)
print()
n50 = n20 = n10 = n1 = 0
saque = int(input('\033[1mDigite o valor do saque: '))
while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    elif saque >= 20:
        saque -= 20
        n20 += 1
    elif saque >= 10:
        saque -= 10
        n10 += 1
    elif saque >= 1:
        saque -= 1
        n1 += 1
    else:
        break
if n50 > 0:
    print(f'Total de {n50} notas de R$50')
if n20 > 0:
    print(f'Total de {n20} notas de R$20')
if n10 > 0:
    print(f'Total de {n10} notas de R$10')
if n1 > 0:
    print(f'Total de {n1} notas de R$1')
print('\033[m')
print('=' * 31)
print('\033[1mOPERAÇÃO FINALIZADA COM SUCESSO!\nVOLTE SEMPRE.\033[m')
print('=' * 31)'''


#   Resolução do professor Guanabara:

print('=' * 30)
print('{:^30}'.format(' BANCO CEV '))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
