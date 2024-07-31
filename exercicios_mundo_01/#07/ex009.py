t = int(input('Digite um número inteiro: '))
c = 0
r = t
print('-'*13)
while c < 10:
    c += 1
    r = t * c
    print(f'{t:2} x {c:2} = {r:>3}')
    print('-'*13)