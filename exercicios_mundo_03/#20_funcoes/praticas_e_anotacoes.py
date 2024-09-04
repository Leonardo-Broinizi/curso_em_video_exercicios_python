'''def saudacao(nome): # Essa linha define a função chamada 'saudacao'
    print(f"Olá, {nome}!")
def tabuada():
    for i in range(1, 11): # Percorre os números de 1 a 10.
        print(f"  {i} x 1 = {i * 1}")
        print(f"  {i} x 2 = {i * 2}")
        print(f"  {i} x 3 = {i * 3}")
        print(f"  {i} x 4 = {i * 4}")
        print(f"  {i} x 5 = {i * 5}")
        print(f"  {i} x 6 = {i * 6}")
        print(f"  {i} x 7 = {i * 7}")
        print(f"  {i} x 8 = {i * 8}")
        print(f"  {i} x 9 = {i * 9}")
        print(f"  {i} x 10 = {i * 10}\n")

nome = str(input('Qual é o seu nome? ')).strip()
saudacao(nome)  # Aqui usamos a função com o argumento "Bentinho", que será usado como entrada
tabuada()  # Chama a função para mostrar a tabuada.
'''

'''def letreiro(texto_central):
    n = len(texto_central) / 3
    print('\033[1;31m' + '-=-' * int(n))
    print(f'\033[33m{texto_central}')
    print('\033[1;31m' + '-=-' * int(n))
while True:
    texto_central = str(input('\033[34mDigite o texto central ou SAIR: ')).upper().strip()
    if texto_central == 'SAIR':
        print('Até logo!')
        break
    else:
        letreiro(texto_central)'''



