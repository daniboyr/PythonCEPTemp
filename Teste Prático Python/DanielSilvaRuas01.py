# 1) Retornar as Meta tags de uma página
# getMetas(URL)
# Ex: getMetas(“https://enttry.com.br/contato”)
# Retorna um json com um array (com nome do meta e content) de metas extraídos do código html
# da página com endereço web passada por parâmetro em URL.
# (Meta tags são elementos no html utilizados para armazenar informações técnicas
# da página)
# Import the required modules
import requests
from bs4 import BeautifulSoup

url = input('Informe uma URL: \n')

#   Puxando as informações da variavel url e criando um arquivo json com elas
def json_from_html_using_bs4(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    metas = soup.find_all('meta')

    res = []

    for meta in metas:
        print(meta.attrs)


    return res


res = json_from_html_using_bs4(url)



print("Questão finalizada.")