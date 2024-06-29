Códigos prontos:

30: branco; 31: vermelho; 32: verde; 33: amarelo; 34: azul; 35: magenta; 36: ciano; 37: cinza;
cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo': '\033[33m',
         'azul':'\033[34m',
         'magenta':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[37m',

        'negrito':'\033[1m',
         'sublinhado'::'\033[4m',
         'inverter'::'\033[7m'

         'branco_sublinhado':'\033[4;30m',
         'vermelho_sublinhado':'\033[4;31m',
         'verde_sublinhado':'\033[4;32m',
         'amarelo_sublinhado: '\033[4;33m',
         'azul_sublinhado':'\033[4;34m',
         'magenta_sublinhado':'\033[4;35m',
         'ciano_sublinhado':'\033[4;36m',
         'cinza_sublinhado':'\033[4;37m',

         'branco_negrito':'\033[1;30m',
         'vermelho_negrito':'\033[1;31m',
         'verde_negrito':'\033[1;32m',
         'amarelo_negrito': '\033[1;33m',
         'azul_negrito':'\033[1;34m',
         'magenta_negrito':'\033[1;35m',
         'ciano_negrito':'\033[1;36m',
         'cinza_negrito':'\033[1;37m',

         'branco_negrito_sublinhado':'\033[1;4;30m',
         'vermelho_negrito_sublinhado':'\033[1;4;31m',
         'verde_negrito_sublinhado':'\033[1;4;32m',
         'amarelo_negrito_sublinhado': '\033[1;4;33m',
         'azul_negrito_sublinhado':'\033[1;4;34m',
         'magenta_negrito_sublinhado':'\033[1;4;35m',
         'ciano_negrito_sublinhado':'\033[1;4;36m',
         'cinza_negrito_sublinhado':'\033[1;4;37m',

'''\033[ m # Esse é um comando básico para se colocar o código da cor desejada entre o colchete e a letra M.
# É possível colocar três códigos dentro (embora não obrigatório): 1°- style (estilo da fonte); 2°- text (cor do texto); 3°- back (cor do fundo);
\033[0;33;44m # O 0 significa que não quis especificar um código para aquele valor.
# Estilo: Os códigos de estilo que melhor funcionam em Python são: 0 (none), 1 (bold), 4 (underline), 7 (negative, que altera o que foi feito para o texto com o que foi feito para o fundo).
# Text: 30: branco; 31: vermelho; 32: verde; 33: amarelo; 34: azul; 35: magenta; 36: ciano; 37: cinza;
# Back: 40: branco; 41: vermelho; 42: verde; 43: amarelo; 44: azul; 45: magenta; 46: ciano; 47: cinza; '''

print('\033[7;33;44mOlá Mundo!\033[m') # O código vazio '\033[m' (sem as aspas) desfaz, do ponto em que aparecer em diante, as configurações de estilo que fizemos anteriormente na linha do código.
a = 3
b = 5
print(f'Os valores são \033[0;32m{a}\033[m e \033[31m{b}\033[m.')
nome = 'Leonardo'
print(f'Olá! Muito prazer em te conhecer, {'\033[4:33m'}{nome}{'\033[m'}!')

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'} # Isso é um dicionário. Mais pra frente, no curso, o professor falará mais sobre esse recurso interessante.
print(f'Olá {cores['azul']}{nome}{cores['limpa']}. {cores['pretoebranco']}Hoje{cores['limpa']} é dia de {cores['amarelo']}Jiu-Jitsu{cores['limpa']}!')
''''
\033[0;30;41m
\033[4:33:44m
\033[1:35:43m
\033[30:42m
\033[m
\033[7:30m'''