tempo = float(input('Digite o tempo de uso em dias: '))
km = float(input('Digite a quantidade de quilômetros rodados: '))
print(f'O preço a pagar pelos {tempo:.0f} dias e {km:.0f}km rodados é R${(tempo*60)+(km*0.15):.2f}.')
