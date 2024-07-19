a = float(input('\033[1;32mDigite o comprimento da primeira reta: \033[m'))
b = float(input('\033[1;31mDigite o comprimento da segunda reta: \033[m'))
c = float(input('\033[1;33mDigite o comprimento da terceira reta: \033[m'))
if a < b+c and b < a+c and c < a+b:
    if a == b and a == c: # O professor Guanabara sugeriu a seguinte forma que funciona igualmente: a == b == c
        print('\033[37mEste é um triângulo EQUILÁTERO, ou seja, todos os lados possuem o mesmo tamanho.\033[m')
    elif a == b or a == c or b == c:# Outra forma: a != b != c != a (a diferente de b, b diferente de c, c diferente de a)
        print('\033[1;34mEste é um triângulo ISÓSCELES, ou seja, dois de seus lados são iguais.\033[m')
    else:
        print('\033[1;35mEste é um triângulo ESCALENO, ou seja, todos os lados são diferentes.\033[m')
else:
    print('\033[1;36mEstas retas não podem formar um triângulo.\033[m')
