def escreva(frase):
    t = int(len(frase) / 2) + 4
    print('<>' * t)
    print(f'   {frase}' if len(frase) // 2 == 1 else f'    {frase}')
    print('<>' * t)
while True:
    frase = str(input('Digite a mensagem central ou SAIR: ')).strip()
    if frase == 'SAIR':
        print('Até mais!')
    else:
        escreva(frase)