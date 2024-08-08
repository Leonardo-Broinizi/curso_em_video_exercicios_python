#    Minha resolução:

lista = str(input('Digite: '))
aberto = fechado = 0
certo = True
for c in lista:
    if c == '(':
        aberto += 1
    elif c == ')':
        fechado += 1
    if aberto == 0 and fechado > 0 or aberto - fechado < 0:
        certo = False
        break
if aberto != fechado:
    certo = False
if certo:
    print('Você fechou corretamente seus parênteses.')
else:
    print('Você não fechou corretamente seus parênteses.')