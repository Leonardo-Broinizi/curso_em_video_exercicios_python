r = 0
while r != 5:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print()
    r = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair \n '))
    if r == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif r == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif r == 3:
        if n1 == n2:
            print('Os números são iguais!')
        elif n1 > n2:
            print(f'{n1} é maior que {n2}!')
        else:
            print(f'{n2} é maior que {n1}!')
    elif r > 5:
        print('Número inválido! Tente novamente.')
    print()
print('Fim do programa!')