#   Esse meu código correspondeu bem ao pedido pelo professor:

tabela_brasileirão = ('Flamengo','Botafogo','Palmeiras','Fortaleza','Cruzeiro',
                      'São Paulo','Bahia','Athletico-PR','Atlético-MG',
                      'Bragantino','Vasco da Gama','Criciúma','Juventude',
                      'Internacional','Corinthians','Grêmio','EC Vitória',
                      'Cuiabá','Fluminense','Atlético-GO')

print(f'\033[1;31m','-' * 30)
print('     TABELA DO BRASILEIRÃO')
print(f'\033[1;31m', '-' * 30)
print('\033[1;32m')
for times in tabela_brasileirão:
    print(times, end=',')
print()
print('\033[1;33mOs cinco primeiros colocados são: \033[1;34m')
print(tabela_brasileirão[:5])
print('\n\033[1;33mOs clubes na zona de rebaixamento são: \033[1;31m')
print(tabela_brasileirão[-4:])
print(f'\n\033[1;33mA lista de clubes da série A do Brasileirão em ordem alfabética: ')
print(f'\033[1;32m')
print(sorted(tabela_brasileirão))
print(f'\n\033[1;33mO \033[1;36mCorinthians\033[1;33m está na', end='')
print(f'\033[1;35m {tabela_brasileirão.index('Corinthians')+1}ª\033[1;33m posição.')
