while True:
    c = 0
    n = int(input('Digite um número [um valor negativo para sair]: '))
    if n < 0:
        break
    while c < 10:
        c += 1
        print(f'{n} x {c} = {n*c}')
