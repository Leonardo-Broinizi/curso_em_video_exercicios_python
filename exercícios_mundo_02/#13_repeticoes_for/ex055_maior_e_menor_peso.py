 #  A partir de agora (e talvez eu faça isso em exercícios antigos também) eu vou julgar se preferí a minha solução,
 # a do professor, ou ambas me pareceram equivalentes. Nesse caso eu preferí a minha solução.

 #  O professor Guanabara até mencionou sobre a solução 'gambiarra' que geralmente se usam para resolver o problama de se encontrar o menor número em uma série,
 # que é iniciar a variável 'menor' com um número gigantesco para ser substituído pelo primeiro valor inserido na repetição, mas eu também achei essa solução não muito interessante.

 # Minha resolução:

'''maior = menor = base = 0
for c in range(5):
    peso = float(input(f'Digite o peso da {c+1}ª pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor or c == 0:
        menor = peso
print(f'O maior peso digitado foi {maior:.2f} e o menor foi {menor:.2f}')'''

# Resolução do professor Guanabara:

maior = menor = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg.')
print(f'O menor peso lido foi de {menor}kg')

