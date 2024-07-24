r = s = c = 0
while r != 999:
    s += r
    c += 1
    r = int(input('Digite o número: '))
print(f'Você digitou {c-1} números, a soma entre eles é {s}.')

