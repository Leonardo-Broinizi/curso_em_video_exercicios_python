#    Meu código após ver o funcionamento do programa do professor Guanabara:

'''def notas(*r, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param r: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    boletim = dict()
    maior = menor = r[0]
    tot = 0
    total = len(r)
    for c, n in enumerate(r):
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        tot += n
    média = tot / total
    boletim['total'] = total
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['média'] = média
    if sit:
        if média <= 4:
            situação = 'RUIM'
        elif média <= 7:
            situação = 'RAZOÁVEL'
        elif média <= 8:
            situação = 'BOA'
        elif média <= 10:
            situação = 'ÓTIMA'
    boletim['situação'] = situação


    return boletim

#Programa principal:
resp = notas(5.5, 9.5, 8, 7, sit=True)
print(resp)'''

#    O código do proferssor Guanabara ficou (novamente rs) mais econômico e lógico que o meu.
# Preciso lembrar de usar as funções que já existem no Python ao invés de criar todas as estruturas que
# preciso do 'zero'.
#    Código do professor Guanabara:

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param r: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa principal:
resp = notas( 5.5, 2.5, 5, sit=True)
print(resp)
