#    ERROS são os de sintaxe, quando a sintaxe está correta e ocorre um problema, como uma variável
# que não existe sendo chamada por print, o nome que se dá é EXCEÇÃO.

#    COMANDO "TRY" (tente): O comando try irá tentar efetuar o trecho de código que estiver nele e,
# caso encontre um erro ou exceção, irá reproduzir o código que estiver em EXCEPT. Em uma única estrutura
# de podemos ter vários EXCEPT para tipos de erros diferentes, que identificaremos ao especificar com
# o nome após o comando EXCEPT, por exemplo: except TypeError: (bloco para quando houver erro de tipo);
# except VallueError: (bloco para quando houver erro de valor); e assim por diante. Caso o comando não
# apresente problemas, ainda pode-se colocar um código em ELSE, abaixo de EXCEPT, com o código que
# queríamos que rodasse caso o programa estivesse funcionando. Também podemos colocar a cláusula
# FINALLY, que executará um código independente de haver tido falha ou não. As clausulas ELSE e
# FINALLY são opcionais na estrutura (TRY e EXCEPT são obrigatórias).

#    Exemplo de estrutura "TRY":  "EXCEPT": "ELSE": "FINALLY":

'''try:
    num = int(input('Digite um número: '))
except Exception as erro: # com "Exception as" eu estou colocando na classe "erro" o nome do erro/exceção encontrado.
    print(f'O erro encontrado foi \"{erro.__class__}\"') # na variável que possui o erro podemos escolher, com atributos, qual instancia do erro  iremos mostrar.
else:
    print(num)
finally:
    print('Volte sempre!')'''

#    Segundo exemplo:

'''try:
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
'''