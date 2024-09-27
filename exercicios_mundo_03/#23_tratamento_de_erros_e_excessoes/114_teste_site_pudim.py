pip install requests

import requests
url = "https://www.youtube.com"

if requests.get(url).status_code == 200:
    print("O servidor está disponível.")
else:
    print("O servidor está indisponível.")