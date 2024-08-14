Peso = float(input('\033[1mDigite seu peso em quilos: '))
Altura = float(input('\033[1mDigite sua altura em metros: '))
IMC = Peso / (Altura**2)
print(f'Seu IMC é: {IMC:.2f}.')
if IMC < 18.5:
    print('\033[31;1mVocê está abaixo do peso!\033[m')
elif IMC <= 25:# Dica de declaração: 18.5 <= IMC <= 25 (o Python aceita essas representações encadeadas).
    print('\033[34;1mVocê está no peso ideal!\033[m')
elif IMC <= 30:
    print('\033[33;1mVocê está com sobrepeso!\033[m')
elif IMC <= 40:
    print('\033[35;1mVocê está com obesidade!\033[m')
elif IMC > 40:
    print('\033[31;1;4mVocê está com obesidade mórbida!\033[m')
