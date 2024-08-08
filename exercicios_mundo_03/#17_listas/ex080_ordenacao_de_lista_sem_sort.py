#    Quebrei bastante a cabeça e demorei muito mais do que vinha demorando nos exercícios,
# mas consegui, embora não seja da maneira mais econômica, imagino. Quando ver o código do
# professor eu confirmo.

#    Minha resolução:

lista = []
for i in range(0,5):
    num = int(input('Digite um valor: '))
    if i == 0:
        lista.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        for c in range(0,len(lista)):
            if num <= lista[c]:
                lista.insert(c,num)
                print(f'Valor adicionado na posição {c} da lista...')
                break
            elif c == len(lista)-1:
                lista.append(num)
                print('Valor adicionado ao final da lista...')
print('-=' * 25 + '-')
print(f'Os valores digitados em ordem foram {lista}')