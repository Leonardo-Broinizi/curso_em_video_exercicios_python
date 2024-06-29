from random import randint, choice
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
s = randint(1,4)
if s == 1:
    print('O aluno sorteado foi o ', (a1), '.')
elif s == 2:
    print('O aluno sorteado foi o ', (a2), '.')
elif s == 3:
    print('O aluno sorteado foi o ', (a3), '.')
elif s == 4:
    print('O aluno sorteado foi o ', (a4), '.')

print('\n\n')
'''Outro modo de fazer: '''

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print(f'O aluno escolhido foi: {escolhido}.')
