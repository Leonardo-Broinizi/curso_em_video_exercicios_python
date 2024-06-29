from random import choice, shuffle
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
participantes = [a1,a2,a3,a4]
for i in range(1,5):
    sorteado = choice(participantes)
    participantes.remove(sorteado)
    print(f'O {i}° sortado foi: {sorteado}.')
print('Fim.')

'''Outra maneira de fazer: '''

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
participantes = [a1,a2,a3,a4]
shuffle(participantes)
print(f'A ordem dos alunos será: {participantes}.')
