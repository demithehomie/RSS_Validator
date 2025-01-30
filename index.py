import requests
import xml.etree.ElementTree as ET

def is_valid_rss(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}  # Alguns sites bloqueiam requests sem um User-Agent
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        
        root = ET.fromstring(response.content)  # Tenta parsear o conteúdo como XML
        
        # Verifica se o XML é um feed RSS válido
        if root.tag in ('rss', 'feed', '{http://www.w3.org/2005/Atom}feed'):
            return True
        else:
            return False
    except (requests.RequestException, ET.ParseError):
        return False

# Lista de URLs RSS para validar
rss_urls = [
   // PLACE YOUR XML LINKS HERE
]

# Validando cada URL RSS
for url in rss_urls:
    if is_valid_rss(url):
        print(f"{url} é um RSS válido.")
    else:
        print(f"{url} não é um RSS válido ou não pôde ser acessado.")
