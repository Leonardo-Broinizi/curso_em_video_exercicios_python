#   Minha resolução:

continuar = ' '
ne = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um número entre 0 e 20:  '))
    if n < 0 or n > 20:
        print('Número inválido!')
    else:
        print(f'Você digitou o número {n}, que escrito por extenso é {ne[n]}.')
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    else:
        continuar = ' '
