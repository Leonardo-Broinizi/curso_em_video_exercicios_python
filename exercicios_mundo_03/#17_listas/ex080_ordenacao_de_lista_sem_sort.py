#    Quebrei bastante a cabeça e demorei muito mais do que vinha demorando nos exercícios,
# mas consegui, embora não seja da maneira mais econômica, imagino. Quando ver o código do
# professor eu confirmo.

#   Considerações após ver o código do professor:
#   Realmente o código do professor é um pouco mais econômico do que o meu, já que ele confere
# de uma vez se o número é o primeiro a ser digitado ou maior que o último da fila, já que ele garantirá
# que o último da fila será o maior (e eu não tive essa sacada). Mas fiquei satisfeito com meu resultado,
# que seguiu lógica parecida com a do professor. Demorei mais que o normal mas resolvi mais esse quebra-cabeças.

#    Minha resolução:

'''lista = []
for i in range(0,5):
    num = int(input('Digite um valor: '))
    if i == 0:
        lista.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        for c in range(0,len(lista):
            if num <= lista[c]:
                lista.insert(c,num)
                print(f'Valor adicionado na posição {c} da lista...')
                break
            elif c == len(lista)-1:
                lista.append(num)
                print('Valor adicionado ao final da lista...')
print('-=' * 25 + '-')
print(f'Os valores digitados em ordem foram {lista}')'''

#    Resolução do professor:

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: ' ))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')


