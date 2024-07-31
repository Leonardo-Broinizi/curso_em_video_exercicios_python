from math import radians, cos, tan, sin
ang = float(input('Digite o ângulo: '))
rad = radians(ang)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print(f'O seno de {ang} é: {seno}.\nO cosseno é {cosseno}.\nA Tangente é {tangente}.\n\n')

'''Outra maneira de fazer: '''

ang= float(input('Digite o ângulo: '))
rad = radians(ang)
print(f'O ângulo de {ang} tem o seno de {sin(rad):.2f}, o cosseno de {cos(rad):.2f} e a tangente de {tan(rad):.2f}.')
