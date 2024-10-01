#    Não consegui fazer. Eis minha tentativa:

'''import requests
url = "http://www.pudim.com.br"

if requests.get(url).status_code == 200:
    print("O servidor está disponível.")
else:
    print("O servidor está indisponível.")'''

#    Resolução do professor Guanabara:

'''import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro!')
else:
    print('Tudo Ok')'''

