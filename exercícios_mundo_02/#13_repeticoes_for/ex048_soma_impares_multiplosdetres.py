contador = 0
acumulador = 0
for c in range(1,501):
    if c%2 == 1:
        if c%3 == 0:
            acumulador += c
            contador += 1
            #print(c, end=',')
print(f'A soma entre todos os números ímpares que são múltiplos de três que se encontram no intervalo de 1 a 500 é: {acumulador}. Foram encontrados {contador} números nesses critérios.')
 # Ou:
contador = acumulador = 0
for c in range(1,501,2):
    if c%3 == 0:
        #print(f'\033[34;1m{c}',end=',')
        acumulador +=c
        contador += 1
print(f'\033[1;31mA soma entre todos os números ímpares que são múltiplos de três que se encontram no intervalo de 1 a 500 é: {acumulador}.\nForam encontrados {contador} números nesses critérios.')
