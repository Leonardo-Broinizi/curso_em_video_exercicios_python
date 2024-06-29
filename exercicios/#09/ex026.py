'''frase = input('Digite uma frase: ').upper().strip()
if frase.count('A') == 0:
    print('A letra A não aparece nessa frase.')
else:
    print(f'A letra A aparece {frase.count('A')} vezes na frase. {frase.find('A')} é a primeira posição em que ela aparece, e {frase.find('A')} é a última.') '''


'''Exercício resolvido pelo professor:'''

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra A  aparece pela primeira vez na posição {frase.find('A')+1}.')
print(f'A última letra A apareceu na posição {frase.rfind('A')+1}.')