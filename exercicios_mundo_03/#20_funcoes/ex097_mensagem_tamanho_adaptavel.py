#    Meu código:

'''def escreva(frase):
    t = int(len(frase) / 2) + 4
    print('<>' * t)
    print(f'   {frase}' if len(frase) // 2 == 1 else f'    {frase}')
    print('<>' * t)
while True:
    frase = str(input('Digite a mensagem central ou SAIR: ')).strip().upper()
    if frase == 'SAIR':
        print('Até mais!')
        break
    else:
        escreva(frase)'''

#    Código do professor Guanabara (basicamente igual ao meu):

'''def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    

# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')'''