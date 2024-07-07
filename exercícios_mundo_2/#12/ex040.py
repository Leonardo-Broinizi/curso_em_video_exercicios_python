n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
média = (n1 + n2) / 2
if média <5.0:
    print(f'Sua média foi de {média} e você está REPROVADO!')
elif média >= 5.0 and média < 7.0:
    print(f'Sua média foi de {média} e você está em RECUPERAÇÃO!')
else:
    print(f'Sua média foi de {média} e você está APROVADO!')