import requests
import os
from urls import urls

resultados = []

def limpa_tela():
    os.system('cls' if os.name=='nt' else 'clear')

def VerificaStatus (lista_urls):
    for url in lista_urls:
        try:
            response = requests.get(url, timeout=5)
            dados = {
                "url": url,
                "status": response.status_code,
                "online": response.ok
            }
            resultados.append(dados)
        except:
            resultados.append({
                "url": url,
                "status": "ERRO",
                "online": False
            })
    return resultados

def main ():
    limpa_tela()
    sites = VerificaStatus(urls)
    for i, site in enumerate (sites,  start=1):
        status_texto = "ONLINE" if site['online'] else "OFFLINE" 
        print (f"SERVIDOR {i} - {status_texto} ")
        i+=1
main ()