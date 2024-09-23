#    AVISO IMPORTANTE SOBRE MÓDULOS: nos exercícios eu não estava conseguindo fazer as importações
# do código como o professor e descobri que, para importar uma função de um módulo a pasta com
# o código que está importando precisa estar logo abaixo da pasta principal do PyCharm (minha
# explicação não está muito adequada porque me falta conhecimento técnico no assunto). Se eu quiser
# importar no estilo 'from pasta import módulo' eu preciso colocar as pastas logo abaixo da pasta
# principal, e, como eu estava separando os módulos por pastas, com os exercícios dentro de outras
# pastas, precisei adaptar as coisas para conseguir fazer os exercícios.

#   Obs.: criei uma pasta chamada 'test_ex111' para verificar se os erros ao tentar fazer as importações
# tal qual o professor Guanabara eram por conta de estar usando pastas dentro de pastas, e realmente era,
# pois nessa pasta, que criei fora das minhas pastas de exercícios dentro das minhas pastas do mundo 3,
# as importações funcionaram corretamente.

#    Modularização é dividir o código em módulos, mais especificamente deixar as funções criadas em
# arquivos separados e acessá-las via importação como já vinhamos acessando os módulos internos do Python
# durante o curso, com a importação do módulo inteiro (ex. import time) ou de uma ou mais funções específicas
# do módulo (ex.: from time import sleep). Para isso basta o módulo estar no mesmo diretório do arquivo que o
# quer acessar, já que o Python entende que qualquer arquivo python (com extensão .py) pode ser um módulo.


from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
dob = numeros.dobro(num)
print(f'O dobro de {num} é {dob}')
tri = numeros.triplo(num)
print(f'O triplo de {num} é {tri}')

