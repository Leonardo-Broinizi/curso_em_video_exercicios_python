'''n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
média = (n1 + n2) / 2
if média <5.0:
    print(f'Sua média foi de {média:.2} e você está \033[31mREPROVADO!')
elif média >= 5.0 and média < 7.0:
    print(f'Sua média foi de {média:.2} e você está em \033[33mRECUPERAÇÃO!')
else:
    print(f'Sua média foi de {média:.2} e você está \033[34mAPROVADO!')'''

'''Solução pelo professor Guanabara com uma maneira interessante de realizar a verificação de se a média é menor que 'X' e maior que 'Y': '''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')

