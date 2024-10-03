with open('email.txt', 'r') as arquivo:
    email = arquivo.read()
print(email)

with open('mensagem.txt', 'r', encoding='utf-8') as arquivo:
    mensagem = arquivo.readlines()

for linha in mensagem:
    print(linha.strip())

with open('senha.txt', 'r') as arquivo:
    senha = arquivo.read()
print(senha)

with open('nova_senha.txt', 'w') as arquivo:
    arquivo.write('nova_senha_mais_forte')

with open('nova_senha.txt', 'r') as arquivo:
    nova_senha = arquivo.read()

print(nova_senha)

with open('email.txt', 'a') as arquivo:
    arquivo.write('\npythonimpressionador2@gmail.com')

print(email)

