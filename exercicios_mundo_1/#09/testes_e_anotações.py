frase = '   Curso em Vídeo Python   '
print(frase[9::3])
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('leo'))
print('Curso' in frase)
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
print('*'.join(frase))

'''Aqui o professor está passando conceitos de fatiamento de string's. Vale anotar algumas coisas:

--- ANÁLISE ---
 
Os colchetes [] fazem com que a string seja vista como uma lista (colchetes servem para criar listas em Python). Usando corretamente o número inicial, dois pontos, e final das casas a serem analisadas (lembrando que os caracteres das strings são armazenados em espaços dentro da variável que vão de 0 até o número de caracteres contidos nela). Há algumas variações interessantes, como não informar o primeiro número, o que fará com que o aparecimento comece do início, ou não informar o número final. também podemos colocar mais dois pontos para indicar de quantas em quantas 'casas' a exebição irá se dar.
len() conta o tamanho da string. 
frase.count('o') (neste caso, variável, ponto, count, parêntesis, aspas, caractere): fará com que se conte quantas vezes o caractere especificado aparece naquela string (lembrando que letras maiúsculas e minúsculas são diferenciadas.
print(frase.count('o',0,13)) : fará a contagem com o fatiamento, ou seja, a partir do número especificado até o número especificado.
frase.find('deo'): mostrará em que momento começa a sequência de caracteres selecionada (se ela estiver nesta ordem na string, pois, se ela não for encontrada, será retornado o valor -1).
print('Curso' in frase): mostrará se a ordem de caracteres selecionada existe na variável, mostrando não sua posição, mas apenas a resposta lógica True ou False.

--- TRANSFORMAÇÃO ----

frase.replace('Python','Android'): Trocará a sequência de caracteres descrita pela outra.
frase.upper() : fará com que todos os caracteres fiquem maiúsculos.
frase.lower() : fará com que todos os caracteres fiquem minúsculos.
frase.capitalize() : fará com que o primeiro caractere fique maiúsculo e os demais minúsculos.
frase.title() : fará com que todos os caracteres iniciais fiquem em maiúsculos. Com iniciais me refiro ao primeiro e a todos precedidos por espaço.
frase.strip() : removerá todos os espaços em branco que houverem antes do primeiro caractere e após o último da variável.
frase.rstrip() : adicionando este r de right apenas os espaços em branco da direita serão removidos. (muitas funções do Python que tratam strings tem a variação r para tratar a direita).
frase.lstrip() : o mesmo do que o descrito anteriormente, mas para o lado left (esquerdo).

--- DIVISÃO ---

frase.split() : dividirá a string em várias, de acordo com os espaços que estiverem separando caracteres. Formará uma lista, com cada elemento recebendo um nova numeração interna de zero em diante.
 
--- JUNÇÃO --- 

'-'.join(frase) : juntará as palavras da string com o ícone que estiver entre aspas (no caso do exemplo, o sinal -).

'''

'''Outra dica: as três aspas, como as que estou usando nestes textos, se estiverem em 'print', irão exibir o texto com suas quebras de linha e linhas em branco, o que pode ser muito útil, principalmente para exibir textos grandes.'''